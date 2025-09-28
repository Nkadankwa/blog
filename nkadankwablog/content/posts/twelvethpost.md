 +++
date = '2025-09-22T14:53:16+08:00'
image = '/images/storagebattle.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Docker', 'Baserow', 'Supabase']
title = 'Why I Chose Baserow Over Airtable and Others'
+++


I needed a data layer for the automation setup, and the choice came down to Airtable, Notion, Supabase, and Baserow. I was not looking for the most fashionable option. I wanted something local, predictable, and comfortable to automate.

After comparing the tools, watching more tutorials than I expected, and testing what the workflows would actually require, I settled on Baserow.

### **Main Journey**

I started by comparing what each tool actually gives you. Airtable was
the obvious first pick because everyone uses it in automation tutorials.
It has a clean UI, lots of templates, and the videos online make
everything look simple. But the more I researched, the more I realised
it wasn’t going to work for what I want long-term.

My plans depend on local-first systems. I want everything running on my
own hardware, without depending on external API limits or outages.
Airtable immediately fell off the list because it’s not self-hosted.
Notion had the same issue. As soon as the automation load increases,
you’re stuck with rate limits you can’t bypass.

Supabase was the next option. The backend is strong, but the UX wasn’t
what I wanted. The table interface feels like a developer tool, not
something I can plug into fast workflows. I needed a database that
behaves like a spreadsheet and still gives me a structured API.

This is where Baserow started to look better. Every YouTube tutorial on
Baserow shows the exact style I work well with:
> Docker-based setup

> Simple workspace layout

> Spreadsheet-style tables
> Clear API 

> Easy schema edits
> Good integration with automation tools

Most of the Airtable tutorials felt like they were meant for no-code
dashboards, not backend-heavy automation. The Baserow videos focused on
local hosting, API usage, and real workflows. That matched what I
needed.

When I saw creators actually building self-hosted systems—running
Baserow locally, pairing it with n8n, pushing data, pulling rows, and
doing file uploads—I realised the teaching style made the decision for
me. The Baserow tutorials were slower, more technical, and focused on
things that matter to builders: endpoints, tokens, field IDs,
networking. That was exactly what I wanted.

I test-installed everything in Docker, explored the UI, checked the API
responses, and tried a few manual calls. Baserow just felt right.

### **Challenges**

Even though Baserow won the comparison, the setup wasn’t perfect.  
> Airtable had the smoothest tutorials but no local hosting.

> Notion had the nicest UI but the worst automation flexibility.

> Supabase had strong infrastructure but a mismatched workflow style.

> Baserow had the workflow I wanted but needed proper configuration to behave well in Docker.


The main challenges were around understanding which tutorials applied to
my use case. Airtable videos focus on drag-and-drop workflows, Notion
videos focus on templates, and Supabase videos assume you want to build
an app. Baserow videos assume you want a self-hosted data engine. That
difference added extra learning in the beginning.

I also had to get used to the structured IDs, the API rules, and the way
Baserow handles uploads. Nothing major, but definitely different from
Airtable’s UI-only workflow.

### **Lessons**
A few things became clear during the decision phase:
> Tutorials shape the learning curve more than the documentation.

> Airtable is great for simple public workflows but bad for long-term scalability.

> Notion isn’t built for automation-heavy setups.

> Supabase is powerful but overkill for this type of content system.

> Baserow gives you control if you’re willing to handle the backend.

> Local-first tools narrow your options, but the trade-off gives you full ownership.

Most importantly, I realised that choosing a platform isn’t just about
features. It’s about how well the community and tutorials align with the
way you learn.

### **Resources**
The main things that helped me decide:
> YouTube tutorials focused on self-hosting
> Baserow’s API docs for automation examples

> A few Reddit threads comparing Baserow and Airtable
> Docker setup guides
> Random GitHub issues that explained the structure of Baserow’s backend

These were more practical than the official comparison charts.

### **What’s Next**
Now that I’ve settled on Baserow, the next steps are:
> Setting up the full Docker stack

> Connecting n8n to Baserow

> Creating tables for content, media files, and workflow status

> Testing uploads and row creation

> Building the first automated posting pipeline 

The goal is to get a complete automation loop running end-to-end.

### **Final Thoughts**

Choosing Baserow wasn’t about it being perfect. It was about it being
the best fit for my workflow style and my long-term plan. Airtable and
Notion are great tools, but their ecosystems don’t match the local-first
automation setup I’m building. Baserow gives me control, room to grow,
and the exact type of tutorials that help me move faster.
