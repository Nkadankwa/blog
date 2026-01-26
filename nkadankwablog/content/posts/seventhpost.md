+++
date = '2025-08-18T14:53:16+08:00'
image = '/images/cloudfix.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Nextcloud', 'Docker', 'SSD']
title = 'Fixing Mounting Issues – A Deeper Dive Into the Solution'
+++

When the portable-cloud idea failed, I stopped treating the SSD as the problem and started looking at the roles I had given everything. The drive was being asked to behave like portable storage, a Docker volume, and the home for a database-backed service at the same time.

Windows, WSL, and Linux all mounted it differently. That meant changing paths, inconsistent permissions, and containers that could not reliably find the data they needed. Nextcloud needed stability; the SSD was built to move.

## A simpler split

The solution was less clever than the original idea. The host machine runs the services. The SSD stores data. Docker stays local to the host, while the drive remains portable storage rather than the compute layer.

Syncthing fits that model well because it watches and syncs files. Tailscale does too because it solves networking. Nextcloud is the exception: it needs a predictable place for its database and internal files.

This was a useful design lesson. Portability does not mean every part of a system must move. It means being deliberate about what can travel and what needs a stable home.
