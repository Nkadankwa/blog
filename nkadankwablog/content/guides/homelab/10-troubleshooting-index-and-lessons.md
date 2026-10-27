+++
title = "Part 10 — Troubleshooting Index, Recovery Checks, and Lessons Learned"
date = "2026-04-02T00:00:00+08:00"
recorded_period = "February 2025–April 2026; cross-reference document"
weight = 11
description = "A symptom index, recovery checks and lessons carried into later work."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Finding the useful part of an old failure

The same few symptoms appeared throughout this project, but they did not always mean the same thing. A page that would not load could come from a missing route, a container-only hostname, the wrong port, or an application that had failed to start. This index brings those attempts together so that the next investigation can begin with the relevant detail instead of repeating every earlier change.

The results column shows how far each attempt got at the time. An unfinished test stays open until it is repeated. Follow each link for the explanation, commands and output.

## Troubleshooting index

| Date | Symptom / incident | Where | Recorded outcome |
|---|---|---|---|
| March 12, 2025 | Compose project name empty; image pull EOF — P1-01 | [Part 1]({{< relref "/guides/homelab/01-cross-platform-and-portable-cloud.md" >}}) | Later reached application setup; complete portability not established. |
| March 12–13 | Port 8080 allocated; untrusted domain; config not writable — P1-01/02 | [Part 1]({{< relref "/guides/homelab/01-cross-platform-and-portable-cloud.md" >}}) | Multiple distinct failures; final external persistence unresolved. |
| March 13–23 | Drive interruptions and WSL visibility — P1-03 | [Part 1]({{< relref "/guides/homelab/01-cross-platform-and-portable-cloud.md" >}}) | Reseating/cable change reportedly stopped clicking; Compose still not writing to SSD. |
| April 13 | Proxmox web interface unreachable — P2-01 | [Part 2]({{< relref "/guides/homelab/02-proxmox-to-ubuntu.md" >}}) | Port listener shown; working remote management not established. |
| April 13 | DNS failure and offline package dependencies — P2-02 | [Part 2]({{< relref "/guides/homelab/02-proxmox-to-ubuntu.md" >}}) | No final package repair shown; Ubuntu chosen later. |
| May 29 | Ollama unhealthy; n8n ECONNREFUSED — P3-01 | [Part 3]({{< relref "/guides/homelab/03-ubuntu-services-and-first-automation.md" >}}) | Containers started; credential connection still failed. |
| May 29 | Telegram HTTPS webhook error and HTTP 404 — P3-02 | [Part 3]({{< relref "/guides/homelab/03-ubuntu-services-and-first-automation.md" >}}) | Unresolved in troubleshooting session. |
| July 1 | Windows/Python context and missing model.chat method — P3-03 | [Part 3]({{< relref "/guides/homelab/03-ubuntu-services-and-first-automation.md" >}}) | Object constructed; inference test failed. |
| July 26 | Docker Hub timeout — P3-04 | [Part 3]({{< relref "/guides/homelab/03-ubuntu-services-and-first-automation.md" >}}) | Alternative registry pull reportedly worked; Hub remained unreachable. |
| August 14–15 | Baserow UI/API mismatch; 401/404/refused ports — P4-01 | [Part 4]({{< relref "/guides/homelab/04-automation-stack-and-integrations.md" >}}) | Partial reachability; no complete workflow success shown. |
| August 15 | SQL column does not exist — P4-01 | [Part 4]({{< relref "/guides/homelab/04-automation-stack-and-integrations.md" >}}) | Attempt failed against actual schema. |
| August 17–18 | Caddy redirect and credential failures — P4-02 | [Part 4]({{< relref "/guides/homelab/04-automation-stack-and-integrations.md" >}}) | Redirect/ping observed; Baserow options still failed. |
| September 21–26 | OAuth callback rejected; Ngrok config/script errors — P4-03 | [Part 4]({{< relref "/guides/homelab/04-automation-stack-and-integrations.md" >}}) | Successful callback/tunnel recovery absent. |
| September 10 | original laptop no power — P5-01 | [Part 5]({{< relref "/guides/homelab/05-hardware-failure-and-mini-pc.md" >}}) | Taken out of service; exact component diagnosis unverified. |
| October 31 | SATA drive No Media/0 MB and live-boot freeze — P5-02 | [Part 5]({{< relref "/guides/homelab/05-hardware-failure-and-mini-pc.md" >}}) | Boot reportedly worked after HDD removal; drive cause not conclusively isolated. |
| November 7 | NVMe 0 B, medium errors, Windows 0x80070057 — P5-03 | [Part 5]({{< relref "/guides/homelab/05-hardware-failure-and-mini-pc.md" >}}) | Return/replacement considered; completed resolution absent. |
| November 14–16 | v2rayN core/data-file failure — P6-01 | [Part 6]({{< relref "/guides/homelab/06-headless-ubuntu-access.md" >}}) | Package installed; Final working proxy test still needed. |
| November 16 | xrdp session mismatch; VNC 10060 — P6-02 | [Part 6]({{< relref "/guides/homelab/06-headless-ubuntu-access.md" >}}) | xrdp connected; later VNC display use inferred from scaling questions. |
| November 16 | Static Wi-Fi request still shows dynamic address — P6-03 | [Part 6]({{< relref "/guides/homelab/06-headless-ubuntu-access.md" >}}) | Desired address observed in January, not immediately demonstrated in November. |
| January 9, 2026 | Ethernet default loses to hotspot — P7-01 | [Part 7]({{< relref "/guides/homelab/07-routing-and-failure-containment.md" >}}) | I explicitly reported Claude's route solution worked. |
| February 17 | Undefined bridge member and activation issues — P8-01 | [Part 8]({{< relref "/guides/homelab/08-kvm-docker-hybrid.md" >}}) | Bridge appeared; long-term campus bridging not established. |
| February 17 | No libvirt storage pool — P8-02 | [Part 8]({{< relref "/guides/homelab/08-kvm-docker-hybrid.md" >}}) | Pool active/autostart and test VM running observed. |
| February 17 | OpenClaw guest isolation checks | [Part 8]({{< relref "/guides/homelab/08-kvm-docker-hybrid.md" >}}) | Verification reported by me; full independent test logs absent. |
| February 23 | PostgreSQL 18+ layout / unhealthy dependency — P9-01 | [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}) | Later healthy startup; preservation of old data unverified. |
| February 23 | Ollama has no health check; browser cannot resolve n8n — P9-02 | [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}) | n8n process started; browser path still needed work. |
| February 23 | Baserow connection reset/refused upstream — P9-03 | [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}) | Unresolved in final test. |
| March 20 | Duplicate default routes and portal subnet overlap — P7-02/03 | [Part 7]({{< relref "/guides/homelab/07-routing-and-failure-containment.md" >}}) | Ethernet selection observed; portal/Docker recovery unfinished. |
| March 20 | docker.socket warning; invalid daemon.json — P7-04 | [Part 7]({{< relref "/guides/homelab/07-routing-and-failure-containment.md" >}}) | Both units stopped; restart failed on JSON syntax. |
| April 2 | Continue 79 KB file limit and repository-context trouble — P9-04 | [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}) | Full-codebase retrieval unresolved. |

## Start by keeping a way back into the host

The routing incidents made remote access part of the repair itself. With Ubuntu managed through a viewer over the hotspot, a network change could disconnect the very session needed to finish the work, which made it useful to inspect the active state before changing anything.

These diagnostic commands appeared during the investigation:

```bash
nmcli connection show
ip addr
ip route
ip route get 8.8.8.8
```

Together, they helped show the active profiles, interface addresses, route entries, and the route chosen for a particular destination. That last check became important when external connectivity worked while the campus portal remained unreachable, since a successful request elsewhere could not explain the portal's path on its own. The addresses and profile names in [Part 7]({{< relref "/guides/homelab/07-routing-and-failure-containment.md" >}}) belong to that dated environment and need checking before reuse.

For future changes, keeping a copy of the working configuration and a local way back into the host would make recovery easier. Those recovery steps still needed testing.

## Follow a request from where it actually starts

The n8n and Baserow work repeatedly showed why the source of a request matters. A browser on Windows, a shell on Ubuntu, and a process inside a container can see different names and addresses, even when they ultimately need to reach the same application. The host-published port and the container's listening port also serve different parts of that path.

A useful order for the next investigation is:

1. Identify the caller and record the URL it is actually using.
2. Check whether the name resolves and whether the target port accepts the connection.
3. Inspect container state, published ports, and the affected service's logs.
4. Separate HTTP responses such as 401 or 404 from DNS and connection failures.
5. After changing one part, repeat the request that failed before adjusting another.

This order comes from looking back across the attempts, rather than a claim that every original session followed it. In particular, an HTTP 404 from the health path showed that an HTTP server had answered, while an upload's HTTP 401 shifted attention toward the authentication accepted by that request. Treating both as a general network failure would have lost that useful distinction.

## Check the configuration before repeating the restart

Docker's final March error was clear: the daemon could not parse `daemon.json`. The socket warning encountered earlier was a separate part of stopping the service, and the two issues needed different responses. A corrected example was supplied, but a successful restart was not confirmed afterward, so that remains a follow-up to confirm.

Storage changes need a similar distinction between making something start and keeping its previous contents. Formatting, `clean all`, volume deletion, and the guessed Baserow SQL update all appeared during troubleshooting, but their consequences were different. PostgreSQL later becoming healthy with newly created volumes did not show that an old database had been migrated intact.

For that reason, these steps belong to their particular incidents rather than a default list of repairs to repeat whenever an application fails.

## A technical check sequence for the next failure

The following is an additional diagnostic sequence, not a claim that every earlier attempt followed it. Choose the shell belonging to the machine being tested, and replace container names where needed.

### Ubuntu: capture addresses and destination routes

```bash
ip -brief address
ip route
nmcli connection show --active
ip route get 8.8.8.8
ip route get 10.80.190.200
```

Compare the interface selected for the failing destination with the one selected for an external address. The portal address is a dummy value preserving the documented Docker overlap. A general internet test cannot substitute for that destination check.

### Docker: check configuration, state and mounts

Run these from the stack's Compose directory:

```bash
docker compose config --quiet
docker compose ps --all
docker logs --tail 80 n8n
docker inspect baserow --format '{{json .NetworkSettings.Ports}}'
docker inspect baserow --format '{{json .Mounts}}'
```

The first command validates configuration without starting the stack. The remaining commands separate startup state, application errors, host-port bindings and storage attachment. Output can include private paths or application data, so use the same dummy-value substitutions before publishing it.

### Ubuntu: validate Docker's daemon configuration

```bash
sudo python3 -m json.tool /etc/docker/daemon.json >/dev/null
sudo dockerd --validate --config-file=/etc/docker/daemon.json
systemctl status docker.service docker.socket --no-pager
sudo journalctl -u docker.service -b -n 80 --no-pager
```

Fix syntax or option errors before another restart. A JSON parser validates syntax; it does not establish that the network range or service behaviour is correct.

### libvirt: check the host and guest separately

```bash
sudo virsh pool-list --all
sudo virsh net-list --all
sudo virsh list --all
sudo virsh domifaddr test-alpine
```

An active pool, an active network and a running guest are separate results. Complete the test inside the guest before claiming guest connectivity or effective isolation.

References: [Compose configuration](https://docs.docker.com/reference/cli/docker/compose/config/), [container inspection](https://docs.docker.com/reference/cli/docker/inspect/), [libvirt commands](https://libvirt.org/manpages/virsh.html).

## The lessons that kept coming back

**A visible application does not prove its storage is right.** Nextcloud could keep running while the external drive was disconnected, even though portability was the reason for the setup. The useful test was where its files were being written, not just whether the browser could open it.

**Instructions have to fit the actual environment.** Missing shell tools, a PowerShell syntax difference, and absent polling or credential fields all interrupted the work. The next command became easier to assess once the host shell, container image, node, and version were clear.

**The inventory needs to change when the project changes.** Earlier assumptions about the hardware, Docker's installation, and a supposed libvirt crash needed correcting before the next plan made sense. A dated description of the machine is more useful than carrying every older configuration forward as though it still applies.

**A passing test answers a particular question.** BIOS and SMART results did not erase the NVMe's installation failures, just as a running VM did not prove that the following ping had come from inside the guest. Recording what the test actually exercised helps keep the next conclusion proportionate to the result.

**The source of a useful idea belongs in the account.** The January route solution came from Claude, and the Baserow stack began with a YouTube tutorial alongside AI assistance. Those resources were part of the work, while applying the ideas, checking results, and deciding what to try next remained part of my own troubleshooting.

**Recovery needs attention before the next failure.** A creator's outage prompted the isolation discussion, followed later by a dedicated VM network and a reported hardened-base snapshot. The next useful step would be to demonstrate that those recovery arrangements work, rather than stopping at the configuration or snapshot name.

## Follow-up checks still worth recording

These checks would help confirm the remaining results and make the setup easier to rebuild.

| Priority | Follow-up | What it would settle |
|---|---|---|
| 1 | Restart Docker, record its bridge prefix, and repeat the campus portal request after the March changes. | Whether the final configuration and subnet repair worked. |
| 2 | Test a reboot and Ethernet/hotspot failover with the intended profiles. | Whether remote access persists beyond one working session. |
| 3 | Test Baserow's browser access, internal API, authentication, and one complete workflow against the same stack revision. | Which configuration works from end to end. |
| 4 | Record the retained NVMe, installation/read-write results, and any completed return. | How the hardware replacement ended. |
| 5 | Keep guest-side connectivity and isolation output, then test restoring the snapshot. | Whether the reported VM boundaries and recovery work as expected. |
| 6 | Record a successful OAuth callback, Telegram execution, and scheduled run. | Whether the configured automation completes its intended task. |
| 7 | Test Continue indexing with a cross-file question and inspect the retrieved material. | Whether repository context is working in practice. |
