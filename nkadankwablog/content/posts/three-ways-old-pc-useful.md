+++
date = '2026-03-16T09:00:00+08:00'
image = '/images/sbc_vs_mini_pc.jpg'
title = 'Three practical ways to give an old PC a second life'
categories = ['Posts']
tags = ['Linux', 'Hardware', 'Homelab']
+++

An old PC does not become useless the moment it stops feeling fast as a daily computer. I have not tried every reuse idea myself, but starting a homelab has made me look at older hardware as a collection of possible services rather than a failed desktop.

## 1. Install Linux and give it one job

A lightweight Linux installation can remove some of the overhead that made the machine frustrating. The important part is choosing a job that matches the hardware. It could become a place to practise Linux, run a small service, store non-critical files, or test something I would rather not break on my main laptop.

## 2. Turn it into a media server

Plex and Jellyfin can organise a personal media library and stream it to other devices. This is not free performance: video transcoding can be demanding, storage drives still fail, and a machine left on all day uses electricity. Direct playback of compatible files is much easier on older hardware than converting several high-resolution streams at once.

## 3. Use it for networking or a homelab

An old PC can run a VPN service for remote access or become part of a router/firewall setup, although placing it in charge of the network requires careful research and suitable network interfaces. A gentler starting point is a homelab. That is the direction I have begun exploring: using hardware I already have to learn containers, networking, backups, and self-hosted applications.

Before reusing any machine, I would check its drive health, clean out dust, consider its power consumption, and avoid trusting it with the only copy of important data. The best second life is the useful job the old PC can perform reliably without costing more than the problem it solves.
