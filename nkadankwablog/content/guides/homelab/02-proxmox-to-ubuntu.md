+++
title = "Part 2 — The Proxmox Attempt and the Switch to Ubuntu"
date = "2025-04-21T00:00:00+08:00"
recorded_period = "April 3–21, 2025; Proxmox incident on April 13"
weight = 3
description = "An unreachable Proxmox interface and the decision to start with Ubuntu."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Choosing a foundation for the homelab

I originally chose Proxmox because it seemed like a useful foundation for the homelab I wanted to build, with room for virtual machines and different services as the project grew. YouTube, Reddit, Discord, and general research helped shape that choice, but getting it working on the campus network turned out to be more complicated than expected.

The planned host was an original laptop, with remote access to files across different operating systems among the first goals. Campus Ethernet required a login, there was no travel router available, and the setup did not have a domain. Those conditions mattered as much as the choice of operating system once installation began.

## The console worked, but the web interface would not load

On April 13, the Proxmox console was accessible directly on the machine, but its management page would not open from my laptop. Checks using `ss -tulu | grep 8006` and `ip a` showed a listener on port 8006, while the interface output showed the physical interfaces down and a private address on the bridge.

That helped separate two questions: whether the management service was running, and whether another device had a working network path to it. A listening port answered the first question without solving the second, particularly when the campus connection still needed its browser login. At that point, connecting Proxmox to a phone hotspot was another possible route, but one I had not managed to set up.

### Separating the listener from the network path

The service check used during this attempt was:

```bash
ss -tulu | grep 8006
ip a
```

Port `8006` had a listener, but the physical interfaces were down. That left the management service running without a usable path from the laptop.

For a repeat investigation, these additional checks would separate the service, interface and routing layers:

```bash
systemctl status pveproxy --no-pager
ss -ltnp | grep ':8006'
ip -brief address
ip route
cat /etc/resolv.conf
```

`pveproxy` is the management web service. A listener on `0.0.0.0:8006` or an IPv6 wildcard shows that a process accepts connections on that port; it does not show that the laptop can reach it. The address and route checks come next, followed by testing the management URL from the laptop.

## Trying to bring the network packages in by USB

Package installation quickly became part of the same problem. Running the update command produced a name-resolution failure instead of usable repository access:

```text
apt-get update
Temporary failure resolving for all five
```

With the machine unable to retrieve what it needed directly, I tried downloading packages elsewhere and transferring them on a USB drive. The instructions being followed used this command sequence, with `sda1` standing in for the actual USB device:

```bash
mkdir /mnt/usb && mount /dev/sda1 /mnt/usb
dpkg -i /mnt/usb/*.deb
```

The installation returned dependency problems, so having the package files on the drive was not enough. NetworkManager, firmware, and the supplicant were among the items being investigated, with Ubuntu under Windows used as a way to obtain files for the offline machine.

Another concern appeared when archive processing failed: some files had been downloaded through Ubuntu even though the target machine was running Proxmox. My final question in that sequence was whether this difference could itself be causing problems. Resolving dependencies in a matching Debian/Proxmox environment was suggested, but there was no successful package repair or working web-interface test before switching approaches.

### Checking package compatibility before another offline install

The failed update returned:

```text
Temporary failure resolving for all five
```

That pointed to name resolution during repository access. Copying package files onto USB bypassed the download problem, but it did not resolve package dependencies or make Ubuntu packages suitable for the Proxmox installation.

These additional commands would identify the target and inspect a package before attempting installation:

```bash
cat /etc/os-release
dpkg --print-architecture
dpkg --audit
dpkg-deb --field /mnt/usb/example-package.deb Package Version Architecture Depends
```

`example-package.deb` is a placeholder. The dependency list must be resolved against the target distribution and release. The earlier `dpkg -i /mnt/usb/*.deb` attempt installed everything matching that path; it did not fetch missing dependencies. A matching package environment would be the next step before repeating that approach.

## Why Ubuntu became the more practical option

By April 17, I had decided to switch to Ubuntu LTS. The aim was still to explore virtualization and self-hosted services, but the immediate priority was getting a usable system running on the network available to me. Proxmox had reached the installation and troubleshooting stage without becoming the working platform for the homelab.

Cross-platform file sharing was likely to be the first service on the laptop. Ubuntu offered a different starting point for that work, while virtualization and additional management tools remained possibilities to add later. Their appearance in the plan did not mean they had all been installed already.

Understanding the choices was part of the work. On April 18, I asked for learning resources because simply following a set of steps would not help much when the next variation or failure appeared.

## What carried into the next attempt

This phase ended with a platform change rather than a completed Proxmox repair. The network-login difficulty and the complete set of missing dependencies were never fully resolved in the work, so the experience does not establish that Proxmox itself was faulty.

What it did show was how easily several problems could become tangled together: a service listening locally, an unreachable management page, unavailable repositories, and packages gathered in a different operating-system environment. Establishing connectivity and matching packages to the target system became useful checks to carry into the Ubuntu work in [Part 3]({{< relref "/guides/homelab/03-ubuntu-services-and-first-automation.md" >}}).

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
Error processing achieve won’t the fact that it downloaded Ubuntu files when I needed peoxmox files cause issues
```

{{< /details >}}
