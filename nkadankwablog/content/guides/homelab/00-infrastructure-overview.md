+++
title = "Infrastructure Overview and Evolution"
date = "2026-04-02T00:00:00+08:00"
recorded_period = "February 2025–April 2026"
weight = 1
description = "The machines, services and network connections behind the homelab."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## How the project developed

My homelab started with a fairly ordinary problem: moving files between devices that ran different operating systems. Windows, Linux, macOS, Android, and iOS all needed to fit into the same workflow, and because my living arrangements could change, portability mattered almost as much as the software itself. Local AI, automation, cybersecurity, and home automation became part of the longer-term plan as the project developed.

YouTube, Reddit, Discord, general research, and AI assistance all contributed along the way. Tutorials provided starting points, while the actual setup exposed differences in storage, networking, hardware, and software versions that needed more investigation. This series follows those decisions and experiments, including the attempts that only partly worked.

## From portable storage to a dedicated host

The earliest experiments used a Windows laptop, Docker Desktop, WSL, and external storage. The idea was to put the services and their data somewhere that could move with me, although getting Nextcloud to run turned out to be a different problem from getting it to store data on the intended drive.

By April 2025, a spare laptop had become the planned server. Proxmox was the first choice, but campus network restrictions complicated the installation, so Ubuntu LTS became the more practical starting point.

Hardware trouble interrupted that plan in September. A replacement mini PC became the Ubuntu host for the later networking and virtualization work.

| Period | Main environment | What was happening |
|---|---|---|
| March 2025 | Windows, Docker Desktop/WSL, external storage | Portable Nextcloud and cross-platform sharing experiments. |
| April–July 2025 | original laptop and Ubuntu LTS | Move away from Proxmox, service planning, and connectivity troubleshooting. |
| May–September 2025 | Separate Windows/local-AI environment | NVIDIA-backed Docker experiments alongside the Ubuntu work. |
| September–November 2025 | original laptop failure and mini-PC replacement | Purchase research, drive problems, and Ubuntu installation attempts. |
| November 2025–March 2026 | Ubuntu host | Remote desktop access, hotspot management, campus Ethernet, and KVM work. |
| April 2026 | Windows development environment | Ollama and Continue integration. |

The Windows and Ubuntu environments need to stay distinct when reading the later parts. GPU-runtime settings and PowerShell paths belonged to the Windows stack work; they should not be copied to the Ubuntu host without checking compatibility.

## How the network fitted together

Remote access became especially important because the mini PC did not have a permanent monitor. The arrangement used campus Ethernet for network access and a phone hotspot to keep the Ubuntu desktop reachable from the management laptop, with XFCE and a viewer providing the working interface. That made network changes unusually sensitive: losing Wi-Fi could also mean losing the screen used to repair Ethernet.

The addresses below describe different stages of the project. They changed during troubleshooting and should be read alongside the dates in the individual parts.

| Component | Address or network | Where it appears |
|---|---|---|
| Campus Ethernet | Host `192.0.2.6/23`, gateway `192.0.2.1` | January and March routing output. |
| Management hotspot | Host `198.51.100.10/28`, gateway `198.51.100.1` | January configuration; November attempts initially retained a dynamic address. |
| Campus portal | `portal.example.com` resolving to `10.80.190.200` | March portal troubleshooting. |
| Docker bridge | `docker0`, `10.80.0.0/16` | March routes, where this range overlapped the portal address. |
| Default libvirt network | `virbr0`, `10.91.0.0/24` | VM network and route output. |
| OpenClaw network | `openclaw-net`, `virbr1`, `10.90.0.0/24` | February's implementation summary and later March routes. |



```text
Windows management laptop
        |
        | remote desktop / VNC over reachable network
        v
Ubuntu host
  |-- wlo1: hotspot / management access
  |-- enp1s0: campus Ethernet / captive portal
  |-- libvirt networks -> test VM and reported OpenClaw VM
  `-- docker0: container bridge present by March

Separate Windows stack work:
Docker Desktop -> n8n / Ollama / Baserow / Caddy / supporting services
```

The diagram brings together the dated configurations described in this series. It is a guide to how the environments related to one another, rather than a live inventory of everything currently running.

## Reading the service and network layers

The Windows container stack and the Ubuntu virtualization host were separate systems. A container address such as `http://ollama:11434` belonged to a Docker network; it was not automatically an address the Windows browser could use.

| Layer | Configuration or tool | What it controls |
|---|---|---|
| Ubuntu interfaces | Netplan and NetworkManager | Host addresses, gateways and route preferences. |
| Container services | Docker Compose | Images, mounts, published ports and dependencies. |
| Virtual machines | libvirt and KVM | Guest definitions, storage pools and virtual networks. |
| Application access | URLs, reverse proxy and credentials | How a caller reaches and authenticates to a service. |

### Additional inventory checks

On the Ubuntu host, these read-only commands would capture the network and VM layers before another change:

```bash
ip -brief address
ip route
nmcli connection show --active
sudo virsh list --all
sudo virsh net-list --all
sudo virsh pool-list --all
```

On the machine running Docker, inspect containers separately:

```bash
docker ps --all
docker network ls
docker volume ls
```

These are checks to repeat, rather than a claim that everything listed is currently running. An interface address, a running guest and a healthy application answer different questions.

For each service, the useful inventory fields are its host, image version, container port, published port, data mount and dependencies. In this stack, port `11434` served Ollama, port `5678` served n8n, and Open WebUI used a `3000:8080` mapping. Those values belonged to the Windows experiments; the Ubuntu host needs its own inventory.

## What had worked, and what still needed checking

Progress came in stages. Nextcloud reached application setup, but its intended external storage remained troublesome; the n8n, Baserow, and Ollama stack also reached partial startup while individual connections continued to fail. Later, libvirt output showed an active storage pool and a running test VM, followed by my own verification summary for the OpenClaw isolation setup.

One correction is particularly important to the chronology: on February 17, Docker was not yet in use on the Ubuntu machine, and the earlier claim that libvirtd had already crashed was wrong. Docker bridges appearing in March therefore belong to a later configuration, not the starting point for February's installation.

Several checks remained unfinished: confirming the retained replacement NVMe, testing the Windows stacks over time, restarting Docker after the March failure and opening the portal after the subnet change. Each part explains what worked and what still needed testing.
