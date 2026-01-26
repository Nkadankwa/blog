 +++
date = '2025-09-08T14:53:16+08:00'
image = '/images/N8n.png'
categories = ['Preparatory Homelab hiatus']
tags = ['n8n', 'Docker']
title = 'My First n8n & Ollama Experiment (and the Telegram Bot Mess)'
+++


As I said in my last post I have gotten my first local Ai and as such
this post covers my first attempt to link n8n with Ollama on Windows
using Docker Desktop. I wanted a simple setup that could move me closer
to a full homelab, but the whole thing ended badly. Still, it pushed my
learning forward.

### The Main Setup

Since I don’t have my main homelab yet, I tested everything on Windows
with Docker Desktop. My plan was simple:

> Run Ollama in Docker
>
> Run n8n in Docker
>
> Connect the two
>
> Build a workflow
>
> Add a Telegram bot on top

Docker Desktop made the installation part easy. Both containers came up
without trouble, and I could open n8n in the browser. I added an Ollama
credential in n8n and connected it to the Ollama container. That part
worked. I also pulled a couple of models—first Mistral, then Qwen3—so I
could test responses inside n8n.

Once everything connected, I built a tiny workflow: a trigger and a
prompt node. It ran, and the model replied, although slowly, since there
was no GPU acceleration. But technically, it worked. That small win was
enough motivation to move to the next idea.

### The Telegram Bot Attempt

This is where everything went downhill.

I created a Telegram bot and tried linking it to n8n so I could message
it and get responses from my local model. The plan was simple:

> Telegram sends a message
>
> n8n receives it
>
> n8n passes it to Ollama
>
> Ollama replies

The problem was the trigger. Telegram doesn’t accept local URLs. It
needs a public, secure URL. And since I was running everything on
Windows inside Docker, there was no reliable way to expose it safely. I
couldn’t give Telegram a stable address. Every workaround I tried
eventually hit the same wall.

Trying to expose n8n properly wasn’t an option because:

> No access to router port forwarding
>
> Windows network was logged in through a controlled network
>
> No stable external IP
>
> Reverse proxy on Windows made no sense in my situation

So all routes that use a domain + reverse proxy + cert were off the
table.

After hours of back and forth, I accepted the truth:  
**The Telegram bot wasn’t going to work in this setup.**

The experiment ended there.

### Lessons Learned

Here’s what this whole failed attempt taught me:

> **You need stable networking for bot integrations.** Local setups
> won’t cut it.
>
> **CPU-only models are painfully slow.** You can run them, but don’t
> expect snappy replies.
>
> **Docker Desktop on Windows is fine for testing.** But it’s limited
> for anything that needs incoming traffic.
>
> **Trying and failing still teaches you something.** Even if the
> project collapses, you walk away knowing more than when you started.

### What’s Next

Since I can’t run proper external integrations on this temporary Windows
setup, my next steps are simple:

> Keep running local models and workflows inside n8n
>
> Practice building automations without external triggers
>
> Save the bigger ideas for when the real homelab returns
>
> Plan a proper setup that supports secure access, private LLMs, and
> long-term workflows

### Final Thoughts

This experiment didn’t work, but it wasn’t a waste. It pushed me to
think more about infrastructure, networking, and how different parts
need to connect. The Telegram bot might have failed, but the learning
didn’t. When the full homelab comes back, I’ll pick this project up
again with better hardware, better networking, and fewer limitations.

For now, the Windows test phase continues, and every failed attempt
prepares me for when the real setup arrives.
