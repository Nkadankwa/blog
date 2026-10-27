+++
title = "Part 5 — Hardware Failure and Moving to a Mini PC"
date = "2025-11-11T00:00:00+08:00"
recorded_period = "September 10–November 11, 2025; principal storage incidents October 31–November 8"
weight = 6
description = "Power faults, storage errors and the move from a laptop to a mini PC."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## When the original laptop stopped being a usable host

The original laptop had given the project a dedicated machine to work toward, but on September 10 it stopped responding to power. There was no charging light, fan noise, or drive activity, even though the charger appeared to work; putting in a fully charged battery did not restore operation either. The only later sign of activity was a sound described as two clicks when trying to start it.

The discussion considered faults in the power path, firmware, and motherboard, but component-level testing was not available. By September 18, I was describing it as a motherboard problem and questioning whether repair was worthwhile, which shifted the practical decision toward finding a replacement. There was no repair report confirming a particular failed component, so the diagnosis remained broader than some of the suggestions made during troubleshooting.

## Choosing a replacement around the parts and budget available

The replacement needed to suit Ubuntu, leave room for future services, and work without a permanent monitor. Reusing existing storage and memory was part of the plan.

I compared several small computers before choosing a replacement mini PC. Compatibility with Ubuntu, storage connections and available memory slots were more useful selection criteria than the product name.

The quoted prices and seller statements helped with that purchase decision at the time. They should be read as historical details, since neither a listing nor a seller's assurance was the same as testing the machine after it arrived.

## The old SSD would not behave normally in the mini PC

On October 31, the Ubuntu SSD was installed in the mini PC, but the cable did not sit securely and kept moving during the first attempt. Moving the drive back to Windows as external storage brought a more concerning result: **No Media, 0 MB**. That established a problem with the storage as connected, but did not isolate the drive from its adapter or cabling.

An HDD and Ubuntu flash drive were then used for another boot attempt, which froze at the loading screen. Removing the HDD allowed Ubuntu to start, providing a useful change to investigate without proving that every other component in the used mini PC was healthy.

CrystalDiskInfo also showed yellow warnings on HDDs, including a message referring to “reallocated sectors count yellow 100.” The complete attribute and raw-value table was not included, so that number cannot safely be interpreted as 100 damaged sectors. The warning still belonged in the storage investigation, but its exact meaning needed the missing detail.

## A new NVMe was visible in BIOS but failed during installation

By November 7, the next problem involved a new NVMe drive and the Ubuntu 24.04.3 LTS live environment. BIOS could detect it, yet Disks reported no media and `lsblk` showed `nvme0n1` with a capacity of **0 B**. Initial checks were slowed by a missing `nvme` command and permission restrictions on reading the kernel log.

The elevated kernel output was more informative, showing a critical medium error, read timeouts, and AMD-Vi page faults. The seller's explanation was that the drive needed initialization and formatting, so Windows tools were tried as well; those attempts returned formatting failures and installer error **0x80070057**, while a later `clean all` attempt also failed.

Its short and extended BIOS tests had reportedly passed, and later Ubuntu could see it with a SMART result showing `PASSED`, but those results sat alongside repeated installation and write failures. A passing headline health result therefore did not settle whether the drive could reliably do the work required of it.

## Separating device detection from usable storage

The useful distinction was whether the firmware could identify the controller, whether Linux could expose a usable namespace, and whether the drive could complete reads and writes. BIOS detection answered only the first of those questions.

The kernel output included:

```text
nvme0: Device not ready; aborting reset, CSTS=0x1
Buffer I/0 error on dev nvme0n1, logical block 112, async page read
```

The copied output contained incomplete lines, but the failure to reset and the read error were enough to justify further storage checks. The separate Windows installation attempt returned:

```text
Windows could not format a partition on disk 0.
Error code: 0x80070057
```

### Additional read-only checks

For another investigation, I would collect these Linux checks before another formatting attempt. `nvme-cli` and `smartmontools` must be installed for their commands to be available; the device name must match `lsblk`.

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL
sudo journalctl -k -b --no-pager
sudo nvme list
sudo nvme smart-log /dev/nvme0
sudo smartctl -a /dev/nvme0n1
```

`/dev/nvme0` names the controller, while `/dev/nvme0n1` names a namespace exposed as a block device. The capacity and namespace details should agree with the purchased drive. A missing utility or permission error must be resolved before its absence is treated as evidence of a hardware fault.

The later SMART output included:

```text
SMART overall-health self-assessment test result: PASSED
Read Self-test Log failed: Invalid Field in Command (0x2002)
```

The first line did not cancel out the installation failures. The second showed that one requested log could not be read; it did not, by itself, identify the failing component. The next useful comparison would be the same drive in a known-good compatible host or adapter, alongside a known-good drive in the mini PC. That comparison was still needed to separate the drive from the connection and host.

Formatting and `clean all` were attempted earlier, but they erase data and did not resolve this failure. They are not part of this read-only diagnostic sequence.

## Where the hardware investigation ended

I began collecting the Ubuntu and Windows failures for a return and compared replacement SSDs the following day. I did not confirm the completed refund, which replacement was ultimately retained, or a controlled test that isolated the NVMe from the host as the sole cause.

The important lesson was to keep these storage incidents separate. An older SATA drive reporting no media, an HDD affecting live boot, and a new NVMe failing installation were different observations, even though they happened around the same mini PC. BIOS detection, capacity, SMART output, and actual read/write behaviour each added useful information, but none of them replaced the others.

The erase and formatting attempts were part of investigating a newly purchased drive that I intended to return, rather than a general recovery method for storage containing files worth keeping. With the host still needing a workable management setup, the next part follows the effort to use Ubuntu without a permanent monitor: [Part 6]({{< relref "/guides/homelab/06-headless-ubuntu-access.md" >}}).

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
13.662242]
nvme0n1: I/0 Cmd(0x2) @ LBA 776, 248 blocks, I/0 Error (sct 0x2 / sc 0x81) MORE
13.919377]
critical medium error, dev nmeni, sector 776 op 0x0: (READ) flags 0x80700 phys_seg 3 prio class 0 nvne
13.919407] nvme
0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x000e address=0x6e200 flags=0x0020]
13.919427] nvme
0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x000e address=0x6e800 flags=0x0020]
13.919445] nvme
0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x000e address=0x6ee00 flags=0x0020]
[
[
44. 082551]
nvme
0000:03:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x000e address=0x6f000 flags=0x0020]
74.290554]
nvme0: 1/0 tag 513 (0201) opcode 0x2 (I/0 Cmd) QID 1 timeout, aborting req_op: READ(0) size: 4096
264.234739]
nome nvme0: 1/0 tag 513 (0201) opcode 0x2 (I/0 Cmd) QID 1 timeout, reset controller nme nvme0: Device not ready; aborting reset, CSTS=0x1
264.244922]
392.252504]
nme nme®: Abort status: 0x371
nome nvme0: Device not ready; aborting reset, CSTS=0x1
392.252782]
nome nume: Disabling device after reset failure: -19
392.262396]
408.017685]
Buffer I/0 error on dev nvme0n1, logical block 112, async page read nume nme: using unchecked data buffer
408.040077]
nyme nme®: Identify namespace failed (-5)
469.510314]
```

```text
Windows Setup
Windows could not format a partition on disk 0. The error occurred while preparing the partition selected or installation. Error code: 0x80070057
```

```text
Supported Power States
Supported LBA Sizes (NSID 0x1)
=== START OF SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
Error Information (NVMe Log 0x01, 8 of 8 entries)
No Errors Logged
Read Self-test Log failed: Invalid Field in Command (0x2002)
St Op
Max
Active
Idle
RL RT WL WT
Ent_Lat
Ex_Lat
0 +
6.00W


0
000
0
0
1 +
4.60W


1
1
0
0
2 +
3.60W


2
2
2
0
SMART/Health Information (NVMe Log 0x02)
Critical Warning:
0x00
Temperature:
33 Celsius
Available Spare:
44%
Available Spare Threshold:
10%
Percentage Used:
0%
Data Units Read:
2,450 1.25 08J
Data Units Written:
2,624 [1.34 GB]
Host Read Commands:
43,436
Host Write Commands:
133,302
Controller Busy Time:

Power Cycles:
14
Power On Hours:

Unsafe Shutdowns:
13
Media and Data Integrity Errors:
0
Error Information Log Entries:
1
,483
Warning Comp. Temperature Time:
0
Critical Comp. Temperature Time:
0
```

{{< /details >}}
