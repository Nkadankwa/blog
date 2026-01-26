+++
date = '2025-09-01T14:53:16+08:00'
image = '/images/local-ai.png'
categories = ['Preparatory Homelab hiatus']
tags = ['Ollama', 'Local Ai', 'Open WebUI']
title = 'Hosting My First Local AI: The Ollama Experiment'
+++

With Docker already running on my temporary setup, I wanted to try something more ambitious: hosting an AI model locally. The long-term idea is a private assistant that can fit into my own workflow without depending entirely on a cloud service.

I compared Ollama, Hugging Face, and LM Studio. Ollama won because it felt approachable while still fitting the Docker-based environment I was learning.

## From terminal to a usable workspace

Ollama came up quickly in a container. The next improvement was Open WebUI, which gave me a browser-based chat interface for managing models and conversations locally. It made the experiment feel less like a command-line test and more like something I could use.

I tried Mistral and later Qwen3. The difference was a useful reminder that “local AI” is not one thing: model choice affects speed, context, hardware needs, and how helpful the system feels.

The setup is still an experiment, not a finished assistant. But it proved that a private, local model is within reach—and gave me a real foundation for exploring n8n and automation next.
