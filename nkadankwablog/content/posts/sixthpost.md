+++
date = '2025-08-11T14:53:16+08:00'
image = '/images/clouderror.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Nextcloud', 'Docker', 'SSD']
title = 'The Portable Cloud Experiment – A Failed Attempt'
+++

I wanted a cloud I could carry: an external SSD with Nextcloud, Syncthing, and Tailscale ready to run whenever I moved between machines. The idea was appealing—plug it in, start Docker, and keep the same environment everywhere.

Syncthing and Tailscale behaved well. Nextcloud did not. Its database, permissions, and storage expectations need a stable home. Windows, WSL, and Linux mounted the SSD differently; paths changed, permissions changed, and Docker volumes became unpredictable.

## The boundary I found

The tools were not the problem. The assumption was. A portable drive can be great storage, but it cannot always be the system itself.

After enough mount–configure–break–rebuild cycles, I stopped forcing it. The experiment clarified the difference between files that can travel and services that need a stable host. That was disappointing in the moment, but it saved me from spending more time trying to make an unstable design feel normal.
