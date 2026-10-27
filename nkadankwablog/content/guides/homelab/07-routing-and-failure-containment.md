+++
title = "Part 7 — Fixing Routing and Containing Failures"
date = "2026-03-20T00:00:00+08:00"
recorded_period = "January 9–March 20, 2026"
weight = 8
description = "Ethernet route priorities, a Docker subnet conflict and a failed daemon restart."
technical = true
aliases = ["/posts/ubuntu-campus-portal-docker-routing/"]
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Keeping the management connection while fixing Ethernet

The Ubuntu host was now being managed through XFCE and a viewer, with a phone hotspot keeping the desktop reachable while campus Ethernet handled a different network connection. Both interfaces needed to coexist, because a global network restart could also remove the screen being used to make the repair. This was Ubuntu 24.04.3 LTS, and the active interfaces were `enp1s0` for Ethernet and `wlo1` for Wi-Fi.

## Why changing a metric did not fix the default route

On January 9, requests to the campus portal at `10.80.190.200` failed with `No route to host`. The route table showed Wi-Fi's default at metric **600**, ahead of Ethernet's default at **20100**, even though the local Ethernet subnet route had metric **100**. Lower values generally give comparable routes preference, but the local subnet route and the default route were different entries; changing one did not necessarily change the other.

Several attempts adjusted the connection profiles, removed a guessed portal route, changed Netplan settings, and reconnected the hotspot profile. The default preference kept returning in the output, including one attempt where Ethernet's local route reached metric **10** while its default remained **20010**. That made the actual route table more useful than the setting I had intended to apply.

At **22:47**, I reported that the connection worked after applying a solution from Claude. It replaced the Ethernet default route directly and added a manual default to the NetworkManager profile, using these commands as part of the solution:

```bash
sudo ip route del default via 192.0.2.1 dev enp1s0
sudo ip route add default via 192.0.2.1 dev enp1s0 metric 100
sudo nmcli connection modify CampusEth +ipv4.routes "0.0.0.0/0 192.0.2.1 100"
sudo nmcli connection modify CampusEth ipv4.route-metric 100
```

That got the connection working at the time. A reboot test was still needed to check whether the saved settings would keep working. The explanation accompanying the solution blamed DHCP Option 121; the route output showed the unwanted preference, but without a DHCP capture or lease-option details, that particular explanation remained unconfirmed.

### Reading the route fields

The comparison involved two kinds of entry:

```text
default via 192.0.2.1 dev enp1s0 metric 20100
192.0.2.0/23 dev enp1s0 proto kernel scope link src 192.0.2.6 metric 100
```

The `/23` entry describes the directly connected subnet. Its metric of `100` did not mean the default route also had metric `100`. For comparable default routes, the lower metric is preferred; a matching destination subnet is a separate decision based on a more specific prefix.

The commands above changed the live kernel route and then the NetworkManager profile. Those are separate layers: an immediate `ip route` change can disappear when a connection is reactivated, while a saved profile can recreate a route later.

These additional inspections would compare them before another change:

```bash
ip route show default
ip route get 8.8.8.8
nmcli connection show CampusEth
```

`CampusEth` is the example connection name. Its saved `ipv4.routes`, `ipv4.route-metric` and `ipv4.ignore-auto-routes` values need to be compared with the live table, rather than assuming the last command entered describes the active state.

## Thinking about how to limit the effect of mistakes

A few days later, a video about another creator's homelab raised a related concern. One mistake had taken down their services, and the creator planned to separate services into groups so that a future failure would affect a smaller part of the setup. That prompted questions about using KVM, Docker, or a hybrid arrangement to give my own experiments clearer boundaries. It was their outage that motivated the discussion, rather than an outage of my own being described.

The resulting virtualization work is covered in [Part 8]({{< relref "/guides/homelab/08-kvm-docker-hybrid.md" >}}), but the network problem returned in March as the host's configuration became more complicated.

## Duplicate defaults made the next failure harder to follow

On March 20, the route table contained multiple Ethernet and Wi-Fi defaults, Docker's bridge, and two libvirt networks. Routing information also appeared in both Netplan files and NetworkManager profiles, with older generated files still present. A manual change could therefore produce the desired result briefly without showing which configuration would recreate the routes later.

The investigation tried replacing Ethernet's default, simplifying Netplan, moving route management into NetworkManager, and reconnecting profiles. One sequence encountered an unknown-connection error before the profile appeared again, while later output alternated between the intended defaults and a table showing only Wi-Fi's default. That was progress to investigate, but not a reason to call the routing permanently fixed.

## General internet access worked while the campus portal still failed

By **11:48**, `ip route get 8.8.8.8` selected Ethernet, and an HTTP request to `1.1.1.1` returned `200 OK` shortly afterward. The campus hostname also resolved to `10.80.190.200`, yet ping returned `Destination Host Unreachable` from `10.80.0.1`. These results narrowed the problem: an external request could work while the portal request still took an unsuitable path.

Docker's `10.80.0.0/16` bridge network covered the portal's address, making a subnet overlap the likely explanation for that path. Traffic for the portal could be directed toward Docker's bridge instead of the campus connection. Moving the bridge to a non-overlapping range was suggested, with `172.30.0.1/16` used in the example, but the change was not followed by a successful portal test in the work.

### Comparing the destination with the bridge prefix

The external route lookup selected Ethernet:

```bash
ip route get 8.8.8.8
```

```text
8.8.8.8 via 192.0.2.1 dev enp1s0 src 192.0.2.6 uid 1000
    cache
```

The conflicting bridge entry and portal failure were:

```text
10.80.0.0/16 dev docker0 proto kernel scope link src 10.80.0.1 linkdown
```

```bash
ping portal.example.com
```

```text
PING portal.example.com (10.80.190.200) 56(84) bytes of data.
From lab-node (10.80.0.1) icmp_seq=1 Destination Host Unreachable
```

`10.80.190.200` falls inside `10.80.0.0/16`, making the bridge a likely route conflict. The additional check to confirm the selected destination route would be:

```bash
ip route get 10.80.190.200
docker network inspect bridge
```

Those final two checks are follow-up diagnostics. A bridge match would explain why changing only the Ethernet default metric could leave the portal unreachable. A replacement bridge range must avoid all networks the host needs to reach.

## Docker's restart introduced a configuration error

Stopping Docker repeatedly produced a warning that `docker.socket` remained active. After both the service and socket were stopped, the status output showed Docker inactive, which established that part of the procedure had completed. Restarting it brought a new, more specific error:

```text
unable to configure the Docker daemon with file /etc/docker/daemon.json:
invalid character '"' after object key:value pair
docker.service: Main process exited, code=exited, status=1/FAILURE
```

The daemon could not read the edited JSON configuration, so the next task had become correcting the file before testing the network change. A corrected example was supplied afterward, but there was no successful restart or portal request before this attempt ended.

### Checking the daemon file before another restart

The stop and restart sequence included:

```bash
sudo systemctl stop docker.socket
sudo systemctl stop docker.service
systemctl status docker
sudo systemctl start docker
```

Stopping the units succeeded, but starting Docker failed on the JSON error above. Before another restart, these additional validation commands would check the syntax and Docker's accepted configuration:

```bash
sudo python3 -m json.tool /etc/docker/daemon.json >/dev/null
sudo dockerd --validate --config-file=/etc/docker/daemon.json
```

The first command checks JSON syntax; the second asks Docker to validate its options. Both need to exit successfully before a restart is worth testing. Neither proves that the chosen subnet is reachable or conflict-free. The existing file must be corrected in place so unrelated settings are not lost. [Docker daemon troubleshooting](https://docs.docker.com/engine/daemon/troubleshoot/).

## What the two routing incidents showed

January's working solution and March's failures belonged to different configurations, even though they involved the same host and campus portal. Route priorities mattered in the first investigation; duplicate configuration and a Docker subnet overlap complicated the later one, followed by a separate JSON error during recovery.

The most useful check became the route selected for the destination that actually failed, combined with a clear way to preserve management access. A successful request elsewhere on the internet could narrow the investigation, but could not stand in for testing the portal itself.

## Checking policy routing before changing another metric

The main routing table is only part of Linux's routing decision when policy rules are present. These additional read-only checks would show the rules, all populated tables and the selected path for each destination:

```bash
ip -4 rule show
ip -4 route show table all
ip -4 route get 8.8.8.8
ip -4 route get 10.80.190.200
```

Read the `dev`, `via` and `src` fields together. They identify the outgoing interface, next-hop gateway and chosen source address. A connected Docker subnet can take the portal traffic even when the internet default route is correct, because its matching prefix is more specific. Changing a default-route metric would not remove that overlap.

A useful verification compares both destinations before and after a change, then checks again after reactivating the relevant connection. Only a later reboot check can establish whether the saved configuration recreates the intended routes. None of these proposed checks establishes persistence by itself.

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
labuser@lab-node:~$ ip route get 8.8.8.8
8.8.8.8 via 192.0.2.1 dev enp1s0 src 192.0.2.6 uid 1000 
    cache
```

```text
labuser@lab-node:~$ curl -I http://1.1.1.1
HTTP/1.1 200 OK
Content-Length: 963
Content-Type: text/html
Last-Modified: Tue, 03 Dec 2024 04:32:30 GMT
Accept-Ranges: bytes
ETag: "37a5a15d3c45db1:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *
Date: Fri, 20 Mar 2026 03:48:56 GMT

labuser@lab-node:~$ ping portal.example.com
PING portal.example.com (10.80.190.200) 56(84) bytes of data.
From lab-node (10.80.0.1) icmp_seq=1 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=2 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=3 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=4 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=5 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=6 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=7 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=8 Destination Host Unreachable
From lab-node (10.80.0.1) icmp_seq=9 Destination Host Unreachable
```

```text
Stopping 'docker.service', but its triggering units are still active:
docker.socket
labuser@lab-node:~$ sudo systemctl stop docker.socket
labuser@lab-node:~$ sudo systemctl stop docker.service
labuser@lab-node:~$ systemctl status docker
○ docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: e>
    Drop-In: /etc/systemd/system/docker.service.d
             └─proxy.conf
     Active: inactive (dead) since Fri 2026-03-20 11:52:19 CST; 9min ago
   Duration: 4h 10min 37.827s
TriggeredBy: ○ docker.socket
       Docs: https://docs.docker.com
    Process: 2456 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/contain>
   Main PID: 2456 (code=exited, status=0/SUCCESS)
        CPU: 1.784s

Mar 20 07:41:41 lab-node dockerd[2456]: time="2026-03-20T07:41:41.901181503+08:>
Mar 20 07:41:41 lab-node dockerd[2456]: time="2026-03-20T07:41:41.906924706+08:>
Mar 20 07:41:41 lab-node dockerd[2456]: time="2026-03-20T07:41:41.906974970+08:>
Mar 20 07:41:41 lab-node systemd[1]: Started docker.service - Docker Applicatio>
Mar 20 11:52:19 lab-node systemd[1]: Stopping docker.service - Docker Applicati>
Mar 20 11:52:19 lab-node dockerd[2456]: time="2026-03-20T11:52:19.735019406+08:>
Mar 20 11:52:19 lab-node dockerd[2456]: time="2026-03-20T11:52:19.736413580+08:>
Mar 20 11:52:19 lab-node systemd[1]: docker.service: Deactivated successfully.
Mar 20 11:52:19 lab-node systemd[1]: Stopped docker.service - Docker Applicatio>
```

```text
Mar 20 12:16:20 lab-node dockerd[28454]: unable to configure the Docker daemon with file /etc/docker/daemon.json: invalid character '"' after object key:value pair
Mar 20 12:16:20 lab-node systemd[1]: docker.service: Main process exited, code=exited, status=1/FAILURE
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ An ExecStart= process belonging to unit docker.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Mar 20 12:16:20 lab-node systemd[1]: docker.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ The unit docker.service has entered the 'failed' state with result 'exit-code'.
Mar 20 12:16:20 lab-node systemd[1]: Failed to start docker.service - Docker Application Container Engine.
░░ Subject: A start job for unit docker.service has failed
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A start job for unit docker.service has finished with a failure.
░░ 
░░ The job identifier is 16200 and the job result is failed.
Mar 20 12:16:22 lab-node systemd[1]: docker.service: Scheduled restart job, restart counter is at 3.
░░ Subject: Automatic restarting of a unit has been scheduled
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░
```

{{< /details >}}
