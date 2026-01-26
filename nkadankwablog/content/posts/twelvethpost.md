+++
date = '2025-09-22T14:53:16+08:00'
image = '/images/storagebattle.jpg'
categories = ['Preparatory Homelab hiatus']
tags = ['Docker', 'Baserow', 'Supabase']
title = 'Why I Chose Baserow Over Airtable and Others'
+++

For my automation project, I needed a data layer that felt local, predictable, and easy to connect to workflows. The shortlist was Airtable, Notion, Supabase, and Baserow.

Airtable was tempting because it appears in almost every automation tutorial. Notion looked friendly too. But both rely on hosted services, and that does not fit a local-first system where I want control over availability, limits, and data.

## Why Baserow fit

Supabase is powerful, but it felt like more infrastructure than I needed for this particular workflow. Baserow landed in the middle: a spreadsheet-style interface, a clear API, Docker-friendly self-hosting, and a model that makes sense alongside n8n.

It was not only a feature decision. It was a learning decision. The Baserow material I found focused on networking, tokens, endpoints, file uploads, and real self-hosted workflows—the parts I wanted to understand.

Baserow is not perfect, and it needs proper configuration. It is simply the best fit for the system I am building now. The next step is to connect it to n8n, create the tables that matter, and test a complete automation loop from start to finish.
