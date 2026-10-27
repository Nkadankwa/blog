+++
title = "Part 8 — Building the KVM and Docker Hybrid"
date = "2026-02-17T00:00:00+08:00"
recorded_period = "February 15–17, 2026; later network evidence on March 20"
weight = 9
description = "KVM installation, a working storage pool and a separate agent VM."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Giving different experiments their own space

The idea behind the KVM and Docker hybrid was to keep the flexibility of containers while giving an application such as OpenClaw a separate virtual machine. The February 15 plan used distinct credentials and limits on what the agent could reach, with additional ideas for handling untrusted web content. At that point, those were design choices being considered rather than a completed installation.

Before proceeding on February 17, I corrected the assumed starting point: Docker was not yet running on that Ubuntu machine, and libvirt had not already crashed during use. The installation targeted the replacement Ubuntu mini PC. The installation plan needed to match the actual host and its condition.

A freeCodeCamp guide on turning Ubuntu into a KVM hypervisor was one of the resources selected after the routing work. It provided a reference for the next stage, although the network and access requirements still needed to fit my own machine.

## Checking virtualization and building the bridge

The initial checks showed hardware virtualization support and loaded KVM modules. The package-install stage then used the following command:

```bash
sudo apt install -y \
  qemu-kvm \
  libvirt-daemon-system \
  libvirt-daemon-config-network \
  libvirt-clients \
  bridge-utils \
  virt-manager \
  virtinst \
  ovmf \
  cpu-checker
```

The surrounding setup did not match every filename and interface definition assumed by the instructions. A backup command pointed at `/etc/netplan/00-installer-config.yaml`, which was absent, and the first bridge configuration failed twice because its member interface had not been defined correctly:

```text
Error in network definition: br0: interface 'enp1s0' is not defined
```

Later interface output showed `enp1s0` attached to `br0`, but the bridge still needed attention. Its default route had a high metric, and activation included a “master waiting for slaves” state; bringing up the bridge and its slave profile did not immediately demonstrate a stable campus connection.

This attempted bridge was one part of the installation process. It should stay distinct from the dedicated libvirt network described later, since I had not confirmed that `br0` became a permanently working campus-network arrangement.

### Checking CPU support and loaded modules

The virtualization checks used processor flags and loaded KVM modules. A nonzero match count shows exposed virtualization flags; it should not be read as a physical core count.

For a repeat check, these commands expose the same layers:

```bash
grep -Ec '(vmx|svm)' /proc/cpuinfo
lsmod | grep kvm
ls -l /dev/kvm
```

CPU flags show exposed virtualization support, modules show that the kernel driver is loaded, and `/dev/kvm` shows the device and its permissions. Package installation alone cannot establish that a user can start a hardware-accelerated guest.

## Creating the storage pool and starting a test VM

The next obstacle was simpler to identify: `virsh pool-list --all` returned an empty list. A libvirt storage pool tells the virtualization tools where managed storage can live, so a directory-backed pool was created under `/var/lib/libvirt/images`:

```bash
sudo virsh pool-define-as default dir --target /var/lib/libvirt/images
sudo virsh pool-autostart default
sudo virsh pool-start default
sudo virsh pool-list --all
```

This time the output gave a clear result, showing the `default` pool as active with autostart enabled. A later VM listing showed `test-alpine` running, establishing that the setup had progressed beyond package installation to starting a guest.

The networking test was less conclusive. `virsh domifaddr` returned no guest address, and the literal placeholder in `ssh root@<vm-ip>` caused a shell syntax error. Although a ping succeeded afterward, the surrounding prompt still belonged to the host and no successful guest login was shown, so that ping did not establish internet access from inside the VM.

### Pool creation and guest state

After the pool commands above, libvirt returned:

```text
Pool default defined
Pool default marked as autostarted
Pool default started

 Name      State    Autostart
-------------------------------
 default   active   yes
```

The later guest listing showed:

```bash
sudo virsh list --all
```

```text
 Id   Name          State
-----------------------------
 1    test-alpine   running
```

The next address lookup returned no address rows:

```bash
sudo virsh domifaddr test-alpine
```

```text
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
```

A running domain did not prove its network was configured. An empty address table also did not establish that the guest had no address: the result depends on the address source available to libvirt. The later `ssh root@<vm-ip>` attempt failed because the angle-bracket placeholder was pasted literally, so there was no successful guest login at that point.

### Additional checks for the isolated network

These inspections would compare the saved guest definition, virtual network and recovery snapshot without changing them:

```bash
sudo virsh domiflist test-alpine
sudo virsh net-list --all
sudo virsh net-dumpxml openclaw-net
sudo virsh snapshot-list agent-vm
```

`agent-vm` is a placeholder for the agent guest's actual domain name. `openclaw-net` was the named network in the setup. The XML should be inspected for its bridge, address range and forwarding mode; a network name alone does not establish isolation. Snapshot presence must also be followed by a restore test on a suitable test guest before treating it as a recovery procedure. [libvirt command reference](https://libvirt.org/manpages/virsh.html).

## Developing the OpenClaw isolation setup

During the afternoon, the security configuration developed through several inventories and revisions. One outbound-firewall change was followed by a request for reversal commands, which is a reason to preserve the sequence rather than combine every earlier rule into an assumed final policy. The later inventory described a dedicated network and a different host-management address.

| Area | Setup described in the later inventory |
|---|---|
| Guest and account | Ubuntu 24.04 Server with a non-root `agentuser` user. |
| Management | Key-only SSH restricted to host address `10.90.0.1`. |
| Virtual network | `openclaw-net`, using `virbr1` and `10.90.0.0/24`. |
| Traffic restrictions | Limited outbound services and private-network blocking. |
| Guest controls | Filesystem mount restrictions, kernel settings, AppArmor, and audit-related controls. |
| Recovery | A `hardened-base` snapshot was included in the inventories. |



By **18:15**, my checks covered network isolation, LAN blocking, filesystem hardening, audit logging, time sync and internet access. I still needed to keep the individual test outputs and repeat the checks after a restart to make the setup easier to verify.

## What this stage established

The clearest direct results were the available virtualization support, active storage pool, and running test VM. The OpenClaw inventory adds a more developed account of the guest controls and the checks I reported, while a later March route table also shows `virbr1` and `10.90.0.0/24` on the host. A `linkdown` entry in that table does not, by itself, show that libvirt had crashed.

Effective firewall behaviour, guest-side test results, and a demonstrated snapshot restore would make the documentation stronger. Until those details are available, the configuration can be described without turning it into a claim that every security risk had been eliminated. The separate application and AI work continued in [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}).

## Inspecting the VM's actual resource and network settings

The domain definition provides a more precise check than the VM's display name. These additional commands would inspect its resources, disk attachments and network interfaces without changing them; `agent-vm` is an example domain name:

```bash
virsh dominfo agent-vm
virsh domblklist agent-vm --details
virsh domiflist agent-vm
virsh dumpxml agent-vm
```

In the XML, `<memory>` and `<vcpu>` describe the assigned resources, disk source entries identify the backing storage, and interface source entries show which bridge or libvirt network the guest uses. A network interface alone does not establish isolation: the host's forwarding rules, the network's forwarding mode and services reachable from the guest still determine what it can access.

Before treating the VM as a recovery boundary, the disk files and any required configuration would also need a backup and a tested restore. A listed snapshot or a running domain does not demonstrate that recovery has been tested.

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
labuser@lab-node:~$ sudo netplan apply
/etc/netplan/01-network-manager-all.yaml:21:20: Error in network definition: br0: interface 'enp1s0' is not defined
      interfaces: [enp1s0]
                   ^
```

```text
ana@lab-node:~$ sudo virsh net-list --all
 Name      State    Autostart   Persistent
--------------------------------------------
 default   active   yes         yes

labuser@lab-node:~$ sudo virsh pool-list --all
 Name   State   Autostart
---------------------------

labuser@lab-node:~$ sudo virsh pool-define-as default dir --target /var/lib/libvirt/images
sudo virsh pool-autostart default
sudo virsh pool-start default
sudo virsh pool-list --all
Pool default defined

Pool default marked as autostarted

Pool default started

 Name      State    Autostart
-------------------------------
 default   active   yes

labuser@lab-node:~$ # Download a tiny Alpine Linux ISO (~200MB, fast)
cd /var/lib/libvirt/images
sudo wget https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso
--2026-02-17 14:37:59--  https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-standard-3.19.1-x86_64.iso
Resolving dl-cdn.alpinelinux.org (dl-cdn.alpinelinux.org)... 2a04:4e42:1a::644, 146.75.114.132
Connecting to dl-cdn.alpinelinux.org (dl-cdn.alpinelinux.org)|2a04:4e42:1a::644|:443... connected.
```

```text
labuser@lab-node:/var/lib/libvirt/images$ sudo virsh list --all
 Id   Name          State
-----------------------------
 1    test-alpine   running

labuser@lab-node:/var/lib/libvirt/images$ # Get the VM's IP
sudo virsh domifaddr test-alpine

# SSH into it once it's booted (Alpine default: root, no password)
ssh root@<vm-ip>

# Inside the VM
ping 8.8.8.8
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------

bash: syntax error near unexpected token `newline'
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=105 time=190 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=105 time=188 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=105 time=189 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=105 time=194 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=105 time=196 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=105 time=188 ms
64 bytes from 8.8.8.8: icmp_seq=7 ttl=105 time=188 ms
64 bytes from 8.8.8.8: icmp_seq=8 ttl=105 time=190 ms
64 bytes from 8.8.8.8: icmp_seq=9 ttl=105 time=188 ms
64 bytes from 8.8.8.8: icmp_seq=10 ttl=105 time=195 ms
^Z
[2]+  Stopped                 ping 8.8.8.8
labuser@lab-node:/var/lib/libvirt/images$
```

{{< /details >}}
