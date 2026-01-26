+++
date = '2025-07-07T14:53:16+08:00'
categories = ['Homelab']
image = '/images/false_start.jpg'
tags = ['syncthing', 'WSL2']
title = '🚧 The False Start to My Homelab Journey (Before I Knew What It Was)'
+++

Taking the first step in anything tech-related can feel like opening a puzzle box—especially when you don’t know what picture you’re even trying to build. At the time, I wasn’t planning to build a home lab. In fact, I didn’t even know what a home lab was.

But I did know one thing:
> I wanted seamless access to my files, no matter what device I was on.

And that seemingly simple goal? It sent me on a spiral of trial, error, and stubborn persistence.

## 🔍 Where It _Actually_ Started
The issue was clear: I needed a way to access, manage, and transfer files across all my devices—devices that ran on different operating systems.

The solution? Much murkier.

At first, I tried basic apps like Syncthing, which is great for syncing folders but felt too limited for what I had in mind. Joplin came next for notes, and before that, I was (and still am) using Telegram’s saved messages to toss files and links between devices.

I also researched apps like Obsidian and Evernote, hoping to find a flexible, central space for notes and file access—but none of them quite solved the root problem.

That’s when I stumbled upon the idea of setting up my own cloud. I didn’t fully understand what that entailed at the time, but the phrase “self-hosted Nextcloud” kept popping up in forums and videos, and it sounded exactly like what I needed.

## 🐣 First Attempt at a Private Cloud
I decided to give it a go. I installed WSL2 on my Windows laptop, installed Docker (after way too many Compose errors), and attempted to spin up a Nextcloud container. 
My thinking was:
>“If I can get this working now, I can just move the setup to whatever system I build later.”

But spoiler alert—it didn’t go smoothly.

I deleted and reinstalled Docker multiple times, moved files to an external drive, and tried setting up persistent storage using a partition formatted as ext4 (which, in theory, would play nice with Linux systems). But mounting it properly was a challenge of its own. I _think_ I got it right… eventually.

Every time I thought I had it working, something broke. Nextcloud would fail to start. Tailscale would refuse to connect. And VPN conflicts meant even downloading updates or getting Docker images became a mess.

## 📌 Lessons Learned (the Hard Way)
Looking back, it’s easy to laugh at how chaotic this phase was. But I picked up some important lessons along the way:
- __Just because something works on one OS doesn’t mean it’ll translate easily__.
- __Reading the docs matters.__ AI tools helped, but they often gave me outdated or just plain wrong steps.
- __Don’t rush to scale.__ I was trying to build a “transferable setup” before I even had a stable one.

## 📔 Resources I Went Through
While most things didn’t go to plan, these resources played a role in nudging me forward:
- YouTube tutorials on setting up Docker and WSL2
- GitHub repos for Nextcloud and Tailscale Compose files
- Stack Overflow (a lot)
- Free AI tools like ChatGPT and Gemini (until I ran out of free usage )
- Reddit threads and niche tech blogs

## What’s Next?
After hitting roadblock after roadblock, I eventually realized I was going about things backward.
I was trying to build infrastructure without understanding what I was building.
That’s when the idea of a home server came up—and then a home lab.
But that’s a story for the next post.

## ✨ Final Thoughts
This wasn’t the start I expected, but maybe that’s the point. Sometimes, you have to stumble into the right path. My “false start” ended up teaching me more than any successful first attempt ever could have.
So if you’re feeling stuck or confused right now—don’t worry. You might just be in the first chapter of your own tech journey.
And trust me… it gets better.



