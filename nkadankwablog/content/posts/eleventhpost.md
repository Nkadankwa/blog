 +++
date = '2025-09-15T14:53:16+08:00'
image = '/images/n8n-baserow.png'
categories = ['Preparatory Homelab hiatus']
tags = ['baserow', 'n8n', 'Ollama']
title = 'Setting Up My First Baserow Stack With YouTube and AI'
+++

I wanted a content-automation system that could run locally, so building the stack behind it became the next major step. The plan looked simple on paper: Baserow for data, MinIO for media, n8n for automation, and local AI tools where they made sense.

In practice, the setup became a mix of tutorials, AI-assisted questions, experiments, and the slower work of understanding how every service connects to the next.

### **Main Journey**

Once I decided to go with Baserow, the next phase was building the
backend stack that would support my automation. I knew I needed a few
things: a database layer, storage for media files, and an automation
engine. The plan was straightforward—Baserow + MinIO + n8n + my local AI
tools.

I started like most people do: searching for “self-host baserow docker”
on YouTube. There were a few tutorials, and most of them followed the
same pattern—pull the images, run docker-compose, and access the web UI.
What helped me most was how these videos showed the structure: the
backend, the web frontend, Redis, and PostgreSQL all running behind the
scenes. I finally understood that Baserow wasn’t just a single container
but a whole set of services.

YouTube got me through the basic setup, but I wanted to customise things
for my use case. That’s where I brought AI into the mix. Whenever I hit
a point the video didn’t explain—like environment variables, networking,
internal URLs, or API behaviour—I used AI to get direct explanations
instead of digging through documentation.

The first real milestone was getting everything running together in one
Docker compose file. I grouped the containers under the same network so
they could talk to each other. Then I added MinIO for media file storage
and n8n for workflow automation. I spent a lot of time adjusting ports,
rewriting variables, and testing how each service responded.

At one point, I rebuilt the entire compose twice because I didn’t like
how the folders were structured. But it helped me understand what each
container actually does. The backend handled the API, the frontend
handled the UI, Redis handled caching, and PostgreSQL kept everything
stored. Seeing these pieces connect made the system feel less
“mysterious” and more like a real setup I could control.

The final step was connecting n8n to the Baserow API. The tutorials gave
the basics, but I had to figure out the details myself—auth, file
uploads, field IDs, and the internal URLs needed for
container-to-container communication. This was my first time seeing how
many small details go into automation when everything is self-hosted.

### **Challenges**

This setup phase had more roadblocks than I expected.

- > Most YouTube tutorials assume you’re running things on Linux, so> following them on Windows introduced extra steps.
- > Some videos show older versions of Baserow, which made the UI slightly different.

- > The examples used public URLs, but my system relies on internal Docker networking.

- > Storage handling wasn’t explained clearly in tutorials, so connecting MinIO took experimentation.

- > I had to rewrite some of the compose file multiple times because certain environment variables didn’t behave as expected.

- > The AI-generated suggestions were helpful but needed testing because small mistakes in networking or volume paths break the whole system.
   

Another issue: YouTube creators often focus on showing the working demo
rather than explaining what each part actually does. It took a mix of
experimenting and asking targeted questions to AI before everything
finally clicked.

### **Lessons**

A few key lessons became obvious once the stack started working:

- > Self-hosted stacks aren’t “plug and play.” You need to understand how each service connects.

- > Docker networking is the backbone of this whole setup.

- >Local URLs behave differently from public URLs, and tutorials rarely cover that.

- > YouTube is good for conceptual understanding, not for real debugging.

- > AI shines when filling gaps the videos skip.

- > A working compose file is worth more than any documentation.

- > Testing endpoints manually teaches more than watching someone else do it.
  

This phase also showed me the difference between learning by watching
and learning by building. Following the tutorial isn’t the same as
understanding what you’re doing. The long debugging sessions were
annoying, but they helped me understand the system in a more practical
way.

### **Resources**

The things that actually helped:
> YouTube tutorials on self-hosting Baserow and MinIO

> GitHub repositories with working compose files

> AI-generated explanations for environment variables

> Docker and network troubleshooting commands

> Postgres and Redis quick guides

> Baserow API docs for internal calls


These resources gave me enough flexibility to customise the system
instead of copying someone else’s setup.

### **What’s Next**

With the stack running, the next steps are:
> Connecting file uploads to the right tables

> Testing row creation from n8n

> Building the content generation workflow

> Automating caption storage

> Integrating TTS, video editing, and posting pipelines 

> Optimising the compose file for stability


The goal now is to turn this stack into a fully automated content
machine.

### **Final Thoughts**

Setting up the stack wasn’t smooth, and the tutorials didn’t cover
everything. But working through the problems gave me a better
understanding of the system than just following the videos. Mixing
YouTube and AI ended up being a good balance—videos for structure, AI
for the specifics. This setup is far from perfect, but it’s finally
stable enough to build on.
