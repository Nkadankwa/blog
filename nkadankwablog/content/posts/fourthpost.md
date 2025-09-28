+++
date = '2025-07-28T14:53:16+08:00'
image = '/images/os-options.jpg'
categories = ['Homelab']
tags = ['Linux', 'Proxmox', 'Ubuntu']
title = 'From Proxmox Dreams to Ubuntu Reality'
+++

With the hardware chosen, I reached one of the first decisions that would shape everything that followed: the operating system.

I was excited about this part. Linux is often described as the place where a homelab becomes truly flexible, but I also knew that choosing a tool is different from making it work in the environment I actually have.

The question was simple:

> “Which OS should I use?”

I’d seen one of my mentors using Kali Linux, and he told me it was one
of the best choices for his field—Cybersecurity. I liked its look and
feel, but I knew it wasn't the best choice for a general-purpose home
lab.

So I turned to the usual sources: YouTube, Discord, Reddit, and general
research. Surprisingly, this time the decision didn’t take long—Proxmox
VE kept coming up as the go-to OS for home labs.

That settled it. I downloaded Proxmox, made a bootable USB drive, and
began the installation. Everything worked smoothly, especially since I
had already bought an Ethernet cable ahead of time. But then came the
real issue.

### The Wi-Fi Login Problem

Where I live, the internet requires logging in through a captive portal
(web page) before it actually connects. While Ethernet worked fine
during the install, Proxmox didn’t support VPNs or the driver setup I
needed to connect through the portal afterward.

And before you ask—yes, I could’ve tried Wi-Fi, but that brought its own
complications. The drivers weren’t preinstalled, and without internet, I
couldn’t install them. Catch-22.

I thought I had a solution: download everything on another machine,
transfer it to an external drive, and install it manually. I even set up
a Debian virtual machine, installed the required drivers, gathered all
the files, and moved everything onto an external drive.

And as you might’ve guessed…

It didn’t work.

I checked multiple platforms, forums, and tutorials. After trying
everything I could think of, I had to make the tough decision to let go
of Proxmox for now.

### The Switch to Ubuntu

Since I needed something more beginner-friendly (and less
network-dependent), I chose Ubuntu Linux. It’s widely supported, simple
to use, and still a solid foundation for a home lab.

I created a bootable Ubuntu USB and installed it on my laptop’s hard
drive.

But instead of rushing to install services right away, I’ve decided to
pause and focus on learning Linux properly. I could follow YouTube
tutorials and AI prompts, sure—but I want to understand what I’m doing.

That’s where things stand now.

### 🧠 Lessons Learned

### 

- Don’t get too attached to a specific tool—sometimes, practicality has to come first.

- Not everything needs to be perfect at the start. Your setup will evolve with time and learning.

- Captive portals and driver issues are real obstacles—and should be factored into planning.

### 📚 Resources Used

- Proxmox VE Official Documentation

- Ubuntu Linux Downloads

- YouTube channels: Techno Tim, LearnLinuxTV, NetworkChuck

- Reddit: r/homelab, r/linux4noobs

- Discord communities around Linux and Homelab setups

### 🔜 What’s Next?

- My next step is to spend some time learning:

- Basic Linux commands and file structure

- SSH setup and remote access

- Package management with APT

- Installing essential tools like Docker, Portainer, and others

- Once I feel confident enough, I’ll begin deploying my first services and document that in the next blog post.

### 💭 Final Thoughts

Setting up a home lab isn’t just about choosing hardware and
software—it’s also about adapting when things don’t go your way. And
while Proxmox didn’t work out this time, the journey still taught me a
lot. Ubuntu might not have been Plan A, but it’s turned out to be the
best next step for where I am now.

Let’s see where this goes!
