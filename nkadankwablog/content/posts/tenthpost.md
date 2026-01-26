+++
date = '2025-09-08T14:53:16+08:00'
image = '/images/N8n.png'
categories = ['Preparatory Homelab hiatus']
tags = ['n8n', 'Docker']
title = 'My First n8n & Ollama Experiment (and the Telegram Bot Mess)'
+++

My first n8n experiment was meant to be simple: connect a local Ollama model, build a small workflow, then let a Telegram bot talk to it.

The first part worked. Docker Desktop ran both containers, n8n connected to Ollama, and I could send prompts through a workflow. It was slow without GPU acceleration, but it was real progress.

## Where the plan met the network

Telegram needs a public, secure URL for its trigger. My temporary Windows and Docker setup did not have one. I had no router access for port forwarding, no stable external address, and no sensible reason to force a reverse proxy into a network I did not control.

The bot did not happen, but the failure was specific and useful. Local automation can work well inside the lab. Integrations that receive traffic from the internet need stable networking and a deliberate exposure strategy.

For now, I am keeping the experiments local and saving the public-facing ideas for infrastructure that can support them properly.
