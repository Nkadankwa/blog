 +++
date = '2025-08-18T14:53:16+08:00'
image = '/images/cloudfix.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Nextcloud', 'Docker', 'SSD']
title = 'Fixing Mounting Issues – A Deeper Dive Into the Solution'
+++

When the portable cloud idea collapsed, I knew the root cause wasn’t the
tools I used but the way the SSD behaved across different systems. The
mounting issues became the biggest obstacle, and the only way forward
was to understand why the environment broke every time I tried to move
it between Windows, Linux, and WSL. What looked like a simple mismatch
turned out to be a chain of conflicts involving file systems,
permissions, Docker volume behavior, and how each platform interacted
with removable storage. The more I examined the entire setup, the more
research made me think that the entire strategy needed to change

## **Mounting Issues – The Core Problem**

The SSD didn’t behave the same on every system, and that inconsistency
made the entire environment unreliable. Windows mounted the disk in one
style, WSL added another layer on top, and Linux handled it in a way
that clashed with both. Even something as simple as a drive letter could
break the containers because Nextcloud expected stable paths that didn’t
change between sessions.

The portable SSD acted like it was being asked to do more than it was
intended to do. exFAT didn’t support the permissions or metadata that
Nextcloud needed. NTFS offered more structure, but it still lacked the
reliability required for Docker’s storage backend. And while the ext4
partition worked well under Linux, it wasn’t directly visible on Windows
without extra tools, which meant Docker on Windows couldn’t interact
with it cleanly.

This mismatch caused the setup to break repeatedly. Sometimes Docker
silently wrote to internal storage instead of the SSD. Other times the
mount point changed and Nextcloud refused to start because the data
directory wasn’t where it expected. The more I tried to force the SSD
into acting like a system root, the worse the experience became.

## **Rethinking the SSD’s Role**

Once I understood why each attempt failed, I had to rethink the entire
approach. The SSD shouldn’t act as the compute layer. It should only
store data. It needed to be a predictable, portable storage device, not
a machine pretending to host a system.

That shift changed everything.

Instead of trying to run Nextcloud from the SSD, I moved the application
to the host machine—Windows in this case—where storage paths remained
consistent. The SSD became the location for persistent data, but it
didn’t carry the responsibility of running services. That separation
removed the fragility that had made the original setup so unstable.

With this change, the architecture became simpler:

> The **host machine** ran the services
>
> The **SSD acted as storage**
>
> Linux-specific data lived on ext4
>
> Portable data stayed on exFAT/NTFS
>
> Docker stayed local to the host

This stopped the constant volume errors and path conflicts that made the
first attempt unmanageable.

## **Syncthing, Nextcloud, and Tailscale Under the New Approach**

Syncthing adapted well under the new structure. It didn’t need a fixed
system path or special permissions. As long as the folder existed on the
SSD, Syncthing synced it. It didn’t rely on databases or complex
hierarchies. It simply watched the directory and synced changes across
devices.

Tailscale also worked better once it ran directly on Windows instead of
being tied to the SSD. With a consistent network configuration and a
stable identity, Tailscale turned into the secure access layer I
originally wanted without conflicting with Docker or storage.

Nextcloud became the only component that required a stable host
environment. Once I moved it off the SSD and let the host system manage
the database and internal structure, it stopped breaking. The SSD became
an optional storage backend instead of the core dependency. That
separation removed the mount-point instability and prevented the data
corruption that used to happen when the disk appeared under a different
path.

## **Lessons Learned**

This second attempt taught me that portability wasn’t the
problem—misplaced responsibility was. The SSD could move around easily,
but it shouldn’t be treated as the compute environment. Nextcloud wasn’t
designed to run off a device that might mount differently on every boot.
Docker didn’t like relying on exFAT or NTFS for critical volumes.
Windows mount points changed too often for container paths.

On the other hand, Syncthing thrived because it avoided databases. It
simply synced files without caring about how the underlying file system
behaved. Tailscale thrived because it focused on networking rather than
storage. These tools didn’t collapse under the same conditions that
destroyed the Nextcloud setup, which made the contrast even clearer.

I learned that designing a portable system doesn’t mean placing
everything on the portable storage. It means deciding which pieces can
move and which pieces must stay fixed. Nextcloud needed a home. The SSD
didn’t need that burden.

## **Resources**

Linux mounting guides

Nextcloud storage documentation

Tailscale quick-start material, file system comparisons, and Syncthing
documentation.

## **What’s Next**

I’m now working on a modular ecosystem that uses the SSD as a reliable
portable storage layer while running all services from the host machine
or, in the future, a compact SBC. This structure opens the door for
tools like OnlyOffice, Home Assistant, and local AI models without
dealing with the fragility of cross-platform mounts.

## **Final Thought**

Fixing the mounting issues wasn’t just a technical step; it was a shift
in understanding. The SSD had to return to what it actually was—a
storage device—and the host machine had to take responsibility for
running the environment. Once I separated those roles, everything became
more manageable. This version of the setup is far more stable, and it
gives me a better foundation for future experimentation without forcing
storage to behave like compute.
