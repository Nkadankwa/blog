+++
title = "Part 6 — Making Ubuntu Usable Without a Monitor"
date = "2025-11-16T00:00:00+08:00"
recorded_period = "October 23–November 16, 2025"
weight = 7
description = "Remote desktop access, proxy problems and keeping Ubuntu reachable."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## A desktop I could reach without keeping a monitor attached

The mini PC needed to be usable from my Windows laptop because buying a permanent monitor was not part of the plan. A borrowed display could help with installation, while Ubuntu's graphical desktop, a phone hotspot, and possible Tailscale access offered ways to manage it afterward. Campus authentication was already complicating installation, so maintaining a separate management connection seemed useful.

October's discussion was mainly preparation for that arrangement. The practical remote-access work appears in November, alongside an effort to get the proxy application working on Ubuntu.

## Installing the proxy was only the first step

On November 14, the package log showed v2rayN **7.12.3** being installed successfully. A notice about `_apt` being unable to access the downloaded file appeared after setup, but the application itself opened; the remaining complaint was that the VPN did not work. Installation and usable proxy access had therefore become separate things to check.

Finding the executable and getting the core to run introduced more detours. `sudo v2rayn` returned command-not-found, while `dpkg -L v2rayn` showed where the package had placed its files. Later output reported that the core could not load `geoip.dat`, even as another check showed a local listener on `127.0.0.1:10808`. The `curl --proxy` tests still failed, so a listening port alone did not demonstrate a working path through the proxy.

A stopped `apt install curl` job also left the package manager waiting for a lock during a later attempt. That was another local problem to resolve, rather than a result from the VPN server. The proxy files appeared to be present, but the failure continued; a later remote-desktop message suggested the VPN could remain enabled without dropping that connection, but did not confirm a permanent fix for every earlier core problem.

## xrdp connected, but the desktop behaviour was confusing

On November 16, xrdp connected from Windows, which was the first clear remote-access milestone. The next issue was that opening Firefox from the remote session caused it to appear on Ubuntu's local display instead of the screen being viewed remotely. For the way I intended to use the machine, seeing the actual Ubuntu desktop was more useful than having an isolated session that behaved differently.

That led to sharing display `:0` with x11vnc and viewing it through TigerVNC. Connection attempts initially failed, including a Windows socket timeout **10060**, even though the process and socket checks showed x11vnc and a listener on port **5900**. The server process being present was useful information, but reachability from the viewer still needed checking.

Later questions concerned TigerVNC's scrollbars and how to fit the desktop into the viewer. Those questions suggest the desktop was being displayed by that stage, although there was no explicit test showing that the arrangement survived a cold boot with the monitor removed.

### Separating the remote-desktop process from its socket

Two of the checks during the VNC attempt were:

```bash
ps aux | grep x11vnc
ss -tlnp | grep 5900
```

The socket output included this listener, with the process details omitted here:

```text
LISTEN 0 32 0.0.0.0:5900 0.0.0.0:*
```

The service was accepting IPv4 connections on port `5900`, but the Windows viewer still returned timeout `10060`. A local listener does not establish a path from Windows through the hotspot, the host firewall and the server socket.

These additional checks would separate that path without changing the server:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 5900
```

```bash
ip -brief address show wlo1
sudo ufw status verbose
```

The PowerShell result's `TcpTestSucceeded` field tests the connection from the Windows caller. The Ubuntu address must match the one the viewer uses. The address above is a documentation-only placeholder, not a real VNC endpoint. A wildcard listener also makes the firewall and interface exposure worth checking before allowing access beyond the management network.

## The static address did not take effect straight away

Keeping the host reachable also meant dealing with its address. A Netplan configuration requested `198.51.100.10/28`, but after applying it, the interface output still showed the dynamic address `198.51.100.2/28`. Repeated checks returned the same mismatch, so saving the requested address in a file was not yet the same as having it active on the interface.

Some of the supporting commands failed too:

```text
sudo cp /etc/netplan/*.yaml ~/netplan-backup.yaml
cp: target '/home/labuser/netplan-backup.yaml': No such file or directory

sudo dhclient -r wlo1
sudo: dhclient: command not found
```

The backup command's error needed the wildcard expansion and destination to be checked; it did not show that the Netplan directory contained no configuration. Likewise, `dhclient` could not release a lease in that attempt because the utility was missing.

The desired `198.51.100.10/28` address does appear in January's interface output, giving a later point at which that configuration was in use. It would be misleading to move that success back into the November session, where the dynamic address was still being shown.

### The attempted static Wi-Fi configuration

The Netplan file requested a static hotspot address. This excerpt replaces the hotspot name and password with dummy values:

```yaml
network:
  version: 2
  renderer: NetworkManager
  wifis:
    wlo1:
      dhcp4: false
      dhcp6: false
      access-points:
        "LAB-HOTSPOT":
          password: "EXAMPLE_WIFI_PASSWORD"
      addresses:
        - 198.51.100.10/28
      routes:
        - to: default
          via: 198.51.100.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
```

Applying it and inspecting the interface produced a different address:

```bash
sudo netplan apply
ip a show wlo1
```

```text
inet 198.51.100.2/28 brd 198.51.100.15 scope global dynamic noprefixroute wlo1
```

The file requested `.10`, while the active interface still held a dynamic `.2` address. Editing the YAML had not established that the intended connection profile was active. With NetworkManager as the renderer, generated and manually saved profiles needed to be checked together.

For a repeat investigation, these additional commands would check parsing and the active profile before another application attempt:

```bash
sudo netplan generate
nmcli connection show --active
nmcli device show wlo1
```

Generating the configuration checks it without bringing the connection down. Applying it can interrupt remote access, so a local console or another working management path needs to be available. [Netplan configuration reference](https://netplan.readthedocs.io/en/stable/netplan-yaml/).

## What still needed a proper end-to-end test

Display sizing remained part of the final questions. `xrandr` showed a **1920×1080** desktop with HDMI connected, while the viewer's auto-scaling option was not available as described. That left an important gap between reaching a desktop during setup and proving that the machine would boot unattended, create a usable display, and reconnect after network changes.

The experience separated three checks that had initially felt like one task: reaching Ubuntu over the network, connecting to its remote-desktop service, and seeing the graphical session I actually wanted. Once that viewer became the main way to work on the host, preserving its network path became part of every routing change, as [Part 7]({{< relref "/guides/homelab/07-routing-and-failure-containment.md" >}}) describes.
