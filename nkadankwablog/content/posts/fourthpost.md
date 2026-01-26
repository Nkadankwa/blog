+++
date = '2025-07-28T14:53:16+08:00'
image = '/images/os-options.jpg'
categories = ['Homelab']
tags = ['Linux', 'Proxmox', 'Ubuntu']
title = 'From Proxmox Dreams to Ubuntu Reality'
+++

With hardware sorted, I reached the next big choice: the operating system. Proxmox kept appearing in homelab guides, and I understood why. It is capable, popular, and built for the virtualised setup I hoped to grow into.

The installation itself went smoothly. The problem appeared afterwards. My internet connection relies on a captive portal, and the combination of missing Wi-Fi drivers, no easy way to authenticate, and limited access to the packages I needed turned a simple install into a loop.

## Changing course

I tried preparing drivers on another machine and moving them over manually. It did not solve the problem. Eventually I chose Ubuntu instead—not because Proxmox is a bad tool, but because Ubuntu fit the reality of my network and my current experience better.

That decision gave me a clearer plan: learn the terminal, filesystem, package management, SSH, and Docker before layering more infrastructure on top.

Good tools still need the right environment. Letting go of Plan A was not failure; it was choosing a foundation I could actually understand and maintain.
