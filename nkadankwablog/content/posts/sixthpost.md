 +++
date = '2025-08-11T14:53:16+08:00'
image = '/images/clouderror.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Nextcloud', 'Docker', 'SSD']
title = 'The Portable Cloud Experiment – A Failed Attempt'
+++

I wanted a setup that felt consistent across all my devices. Nextcloud would handle structured storage and productivity, Syncthing would keep files in sync, and Tailscale would provide secure remote access. In theory, putting that environment on an external SSD would let me plug into any machine, start Docker, and carry the same private cloud with me.

It was an appealing idea because I move between Windows and Linux machines often. It was also the kind of idea that only reveals its hidden assumptions when you try to make it real.

But as the project stretched on, I realized the weakest part of the
setup wasn’t the tools themselves. It was the assumption that I could
force these tools to operate reliably from a portable storage device
that behaved differently on every operating system. Syncthing and
Tailscale ran without trouble. The only failure was **Nextcloud**, and
that one failure was enough to collapse the whole concept of a fully
portable cloud ecosystem on an external SSD.

## **The Ambition**

The plan was ambitious, even though it sounded simple at first. I wanted
a single SSD to act as the central system, carrying not only files but
also the full stack that powered my productivity. Nextcloud would handle
structured files, previews, calendar data, contacts, and anything that
needed an application layer. Syncthing would manage raw file syncing
across devices. Tailscale would give me secure access from anywhere.

This wasn’t supposed to replace everything I used, but it was meant to
make my workflow independent of the machine itself. Since my main
machine ran Windows, I wanted the SSD to behave consistently whenever I
plugged it in—whether I was in WSL, a Linux live environment, or a
remote machine. I knew it wouldn’t be perfect, but I hoped that a
dual-partition structure would allow the tools to coexist: exFAT for
portability, ext4 for database stability.

The idea made sense in theory, and that made the failure even more
noticeable as I went deeper.

## **Challenges**

### **Mounting issues across systems**

The first major issue appeared early. Windows and Linux treated the SSD
differently, and this changed how Docker could access the partitions.
exFAT didn’t support the permission structures that Nextcloud expected.
NTFS had similar problems. The ext4 partition worked well in Linux, but
Windows couldn’t interact with it without extra software, and that broke
consistency.

When the mount point changed—which happened often on Windows—the entire
Nextcloud setup broke. Permissions shifted, paths changed, and the
containers sometimes failed silently. Even when I managed to bring the
stack up again, the environment felt unstable.

### **Nextcloud’s requirements didn’t align with portability**

Nextcloud wasn’t designed to run from a device that might appear under a
new path each time it was connected. It relied on a database and a
strict internal structure, and it expected predictable storage with
consistent permissions. If anything in the chain changed, Nextcloud
showed errors or corrupted the database.

In contrast, Syncthing didn’t complain. It synced files without caring
about mount points, as long as the folder existed. Tailscale was even
simpler—once installed on Windows, it just worked, without expecting
anything from the SSD.

Only Nextcloud collapsed, but because it was a core part of the plan,
that collapse took the original concept with it.

### **Docker’s behavior on Windows**

Because the host machine was Windows, I depended heavily on WSL and
Docker Desktop. Docker treated the SSD differently depending on how it
was mounted. Sometimes volumes fell back to internal storage. Other
times containers refused to start because they couldn’t write to the
SSD. These inconsistencies made the setup fragile.

## **The Decision to Halt**

After repeating the same cycle multiple times—mount, configure, break,
rebuild—I accepted that the portable-cloud concept didn’t work with
Nextcloud in the middle of it. The SSD could act as storage, but not as
the system. The host machine had to carry the workload.

## **Final Thoughts**

This experiment wasn’t a complete failure, but it was a clear reminder
that some tools have boundaries that portability can’t stretch.
Syncthing and Tailscale handled the portable SSD without difficulty.
Nextcloud didn’t. And when a system depends on everything working
together, one weak link is enough to break the entire approach.

If someone wants to try a similar setup, the idea itself isn’t
unrealistic—but the assumptions about portability need to be adjusted.
Nextcloud demands a stable home. Syncthing doesn’t. Tailscale doesn’t.
Understanding that difference is what saved the project from going in
circles.
