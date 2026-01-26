+++
date = '2025-07-07T14:53:16+08:00'
categories = ['Homelab']
image = '/images/false_start.jpg'
tags = ['syncthing', 'WSL2']
title = '🚧 The False Start to My Homelab Journey (Before I Knew What It Was)'
+++

I did not set out to build a homelab. I just wanted my files to follow me between devices without becoming another thing to manage.

That small problem sent me through Syncthing, Joplin, WSL2, Docker, Nextcloud, and Tailscale. Each tool solved part of the problem, but I was trying to assemble a complete system before I understood the pieces.

## The first attempt

I tried to turn Docker and WSL2 into a private cloud, with Nextcloud at the centre. It sounded sensible: build something portable now, then move it to future hardware later. In practice, containers failed to start, storage paths became confusing, and VPN conflicts made even basic setup work harder than it should have been.

The project did not become the cloud I imagined. It did give me a better question: *what am I actually trying to build, and why?*

## What stayed with me

- A setup that works on one operating system may not translate neatly to another.
- Documentation matters more than a confident-looking command from a tutorial or AI prompt.
- It is easier to grow a small, stable system than rescue an ambitious, fragile one.

This was a false start, but not a wasted one. It was the point where “I need my files everywhere” became “I want to understand the infrastructure behind that.”
