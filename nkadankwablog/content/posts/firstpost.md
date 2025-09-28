+++
date = '2025-07-07T14:53:16+08:00'
categories = ['Homelab']
image = '/images/false_start.jpg'
tags = ['syncthing', 'WSL2']
title = '🚧 The False Start to My Homelab Journey (Before I Knew What It Was)'
+++

I did not begin with a plan to build a homelab. I began with a smaller frustration: I wanted my files to be available on every device I used, without turning file transfers into a daily chore.

That question led me through Syncthing, Joplin, WSL2, Docker, Nextcloud, Tailscale, forums, tutorials, and plenty of moments where I was not yet sure what I was trying to build. Looking back, this was the beginning of the journey—not because the setup worked, but because it gave me a reason to learn what sits behind the tools I use.

## Where it actually started

I wanted a way to access, manage, and move files across devices running different operating systems. Syncthing was useful for syncing folders, but it did not feel like the whole answer. Joplin was useful for notes. Telegram saved messages became a temporary place for links and files. I also looked at Obsidian and Evernote, hoping to find one central space for everything.

Eventually, “self-hosted Nextcloud” kept appearing in the research. I did not fully understand the infrastructure behind it, but the idea of running my own cloud sounded close to the independence I wanted.

## The first private-cloud attempt

I installed WSL2, installed Docker, and tried to bring up a Nextcloud container. My reasoning was simple: if I could make a setup work now, perhaps I could move it to future hardware later.

It did not go smoothly. Docker was installed and reinstalled more than once. I experimented with storage on an external drive, including an ext4 partition that I hoped would behave well with Linux. Nextcloud failed to start, Tailscale was unreliable, and VPN conflicts made downloading updates and images more difficult than expected.

## What the failure taught me

- A setup that works on one operating system does not automatically translate to another.
- Documentation matters. AI and tutorials can be useful, but they need checking against reliable, current sources.
- It is easier to grow a small, stable system than rescue an ambitious one that I do not yet understand.

## The resources that shaped the attempt

- YouTube tutorials for Docker and WSL2
- GitHub repositories with Nextcloud and Tailscale Compose examples
- Stack Overflow, forums, and niche technical blogs
- Reddit threads and AI tools for discovery—followed by documentation to validate the details

## What comes next

Eventually I realised I was trying to build infrastructure before I understood the infrastructure. That realisation led me toward a home server and, later, a homelab. This was a false start, but not a wasted one. It gave me the curiosity that made the rest of this blog possible.
