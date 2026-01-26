+++
date = '2025-09-15T14:53:16+08:00'
image = '/images/n8n-baserow.png'
categories = ['Preparatory Homelab hiatus']
tags = ['baserow', 'n8n', 'Ollama']
title = 'Setting Up My First Baserow Stack With YouTube and AI'
+++

I wanted a local foundation for content automation: a place to store data, files, and workflow state without handing the whole system to a hosted platform. The stack became Baserow, MinIO, n8n, and local AI tools.

YouTube tutorials helped me see the broad shape of Baserow, but the useful learning started when I had to make the pieces talk to each other. Docker networks, environment variables, internal URLs, ports, Redis, PostgreSQL, storage, and API credentials all became less abstract once I had to troubleshoot them.

## Learning beyond the tutorial

I rebuilt the Compose setup more than once while organising folders and testing assumptions. That was frustrating, but it made the architecture clearer: the frontend presents the UI, the backend serves the API, PostgreSQL holds the data, Redis supports the application, and the network connects the whole system.

AI was helpful for filling gaps, but every suggestion still needed testing. Videos gave me structure; hands-on debugging gave me understanding.

The stack is now stable enough to build on. Next comes connecting n8n to Baserow properly, testing uploads and row creation, and turning the individual services into a useful workflow.
