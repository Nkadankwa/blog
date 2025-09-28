 +++
date = '2025-09-01T14:53:16+08:00'
image = '/images/local-ai.png'
categories = ['Preparatory Homelab hiatus']
tags = ['Ollama', 'Local Ai', 'Open WebUI']
title = 'Hosting My First Local AI: The Ollama Experiment'
+++

Docker Desktop had become my temporary lab while I waited for my main machine. Once the basics were working, I wanted to try something more ambitious: hosting an AI model locally.

The long-term idea is a private assistant that can fit into my workflow, help organise ideas, and run without depending entirely on a cloud service. Before I could build toward that, I needed to understand the local-model options and the trade-offs behind them.

## 🔍 The Research Phase ##

After spending a few days going down the rabbit hole, I narrowed my
options down to three main tools:

Ollama – known for its simplicity and efficient local AI model
management.

Hugging Face – massive library, great for experimentation, but heavier
to set up locally.

LM Studio – desktop-based and beginner-friendly, but more limited for
integration and Docker use.

Each had its pros and cons, but after comparing them carefully, I ended
up choosing—drumroll please—Ollama.

The deciding factor was flexibility. Ollama supports a wide range of
open-source models, integrates nicely with Docker, and runs well even on
mid-tier GPUs. For someone like me, who’s still early in their home lab
and AI journey, it felt like the best balance between accessibility and
control.

## 🧠 Setting Up Ollama ##

After making my decision, I started looking for the Docker command to
pull and run Ollama. Since I wanted to use my GPU for faster inference,
I made sure to use the GPU-enabled version of the Docker image. The
process went smoothly—it pulled the image, spun up the container, and
just like that, Ollama was up and running.

There was only one catch: Ollama runs entirely from the terminal.

Now, I don’t mind using the terminal—especially while learning Linux—but
it still felt a little inconvenient for managing multiple models or
having conversations. I wanted something with a GUI (Graphical User
Interface), so I started searching again.

That’s when I discovered Open WebUI.

## 💻 Adding a GUI with Open WebUI ##

From what I found, Open WebUI is a sleek, browser-based interface that
connects to your local Ollama instance. It gives you a proper chat-style
environment, lets you switch between models, and even saves your
previous sessions—all while running entirely on your machine.

Excited by the discovery, I pulled it using Docker and linked it to
Ollama. The setup was surprisingly simple. Within minutes, I had a
functional local AI chat environment that looked almost like ChatGPT—but
completely offline and under my control.

## 🧩 Choosing the Right AI Model

Once everything was running, the next question was: which model should I
use?

I started by testing Mistral, a popular lightweight model known for its
speed and efficiency. It worked well for casual tasks, but I later came
across Qwen 3, which was said to be more balanced—smarter responses
without a big performance hit.

Curious, I pulled Qwen 3 using Ollama and immediately noticed a
difference. The model handled context better and felt more “aware” of
what I was asking. Since then, Qwen 3 has become my go-to model for most
tasks.

## ⚙️ What’s New in Docker AI

Recently, I came across something interesting: Docker has introduced a
new AI integration that allows users to pull and use models directly
within Docker itself—no separate setups needed. This could make running
local AI models much more seamless.

While I haven’t tried this feature yet, I can see how it would simplify
things for many people, especially beginners. Personally, though, I
prefer the flexibility that comes with running Ollama separately—it
gives me more control over system prompts, configurations, and model
behavior.

## 🧩 Lessons Learned

Research matters. Even if it takes time, understanding your options
saves you from frustration later.

Simplicity wins. Ollama’s clean setup helped me focus on experimenting
instead of troubleshooting.

Documentation \> Guesswork. I learned to trust official docs and
reliable community posts instead of random snippets online.

## 📘 Helpful Resources

If you’re thinking about trying this yourself, here are some resources
that helped me:

-Ollama Official Website – Setup and model downloads.

-Open WebUI on GitHub – Instructions for installation and customization.

-Docker Docs – For understanding container setup basics.

-Qwen 3 Model Card – Model details and usage guide.

## ⏭️ What’s Next

My next step will be to integrate Ollama with n8n, so I can automate
some workflows using local AI. I also plan to experiment with adding
some voice interaction down the road.

## ✨ Final Thoughts

This phase of my journey taught me that building something powerful
doesn’t always require expensive tools or cloud services. With the right
setup and patience, you can create something incredible right from your
own machine.

It might have started as just a curiosity—but now it feels like the
beginning of something much bigger.
