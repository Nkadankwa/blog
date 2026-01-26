 +++
date = '2025-08-25T14:53:16+08:00'
image = '/images/mind-graph.png'
categories = ['Preparatory Homelab hiatus']
tags = ['Joplin', 'Notetaking']
title = 'Going Down the Self-Hosted Notes Rabbit Hole'
+++

My focus was on finding a note-taking app that supports mind-mapping and
offers seamless syncing. After researching, I narrowed down my options
to Simplenote, Obsidian, Evernote, Joplin, Notion, and Zoho Notebook.

## The Research phase 

The research process involved evaluating each app based on key criteria:
free access, cross-platform support, syncing capabilities, privacy, and
long-term viability.To get started with the journey I had to do more
research into the options I had for this project. I searched for app for
my note taking and I especially wanted a note taker where you can make a
mind storm with the notes. After some research I narrowed my search down
to simplenote,obsidian,evernote,joplin,notion and zoho

and so I stated to do the pros and cons that I found which I will
probably put the table down below(this is just want I found at the time
and may have changed so I urge you to do your own research) Here’s a
breakdown of my findings:

|                          |                                 |                                         |                               |                                           |                                                  |                     |
|---------------|----------|---------|---------|----------|-----------|---------|
| Feature                  | Simplenote                      | Obsidian                                | Evernote                      | Joplin                                    | Notion                                           | Zoho Notebook       |
| Completely Free          | ✅ Yes                          | ✅ Yes                                  | ❌ No (Limited free plan)     | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| Cross-Platform           | ✅ Yes                          | ✅ Yes                                  | ✅ Yes                        | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| Cloud Sync               | ✅ Yes (via Simplenote servers) | ❌ No (Sync requires third-party cloud) | ✅ Yes (Evernote cloud)       | ✅ Yes (via OneDrive, Dropbox, Nextcloud) | ✅ Yes (Notion Cloud)                            | ✅ Yes (Zoho Cloud) |
| Offline Access           | ✅ Yes                          | ✅ Yes                                  | ✅ Yes (Limited in free plan) | ✅ Yes                                    | ❌ No (Requires internet for full functionality) | ✅ Yes              |
| Multimedia Support       | ❌ No (Text-only)               | ✅ Yes (via plugins)                    | ✅ Yes                        | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| File & Folder Management | ❌ No                           | ✅ Yes (Vault structure)                | ✫ Yes                         | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| Search & Tagging         | ✅ Yes                          | ✅ Yes                                  | ✅ Yes                        | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| Markdown Support         | ✅ Yes                          | ✅ Yes                                  | ❌ No                         | ✅ Yes                                    | ❌ No                                            | ❌ No               |
| Collaboration            | ❌ No                           | ❌ No                                   | ✅ Yes (Free plan limited)    | ✅ Yes (via Nextcloud)                    | ✅ Yes                                           | ✅ Yes              |
| Encryption               | ✅ Yes (Server-side)            | ❌ No (Local only)                      | ❌ No                         | ✅ Yes (End-to-end)                       | ❌ No                                            | ❌ No               |
| Customization            | ❌ No                           | ✅ Yes                                  | ❌ No                         | ✅ Yes                                    | ✅ Yes                                           | ❌ No               |
| Best for Privacy         | ✅ Yes                          | ✅ Yes                                  | ❌ No                         | ✅ Yes                                    | ❌ No                                            | ❌ No               |
| Best for Rich Notes      | ❌ No                           | ✅ Yes                                  | ✅ Yes                        | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |
| Best for Collaboration   | ❌ No                           | ❌ No                                   | ✅ Yes                        | ✅ Yes                                    | ✅ Yes                                           | ✅ Yes              |

After evaluating these apps, I eliminated Zoho, Simplenote, and
Evernote. The primary reason was plugins—I prioritized apps with active
communities and long-term sustainability. For example, Notion was ruled
out because it’s not self-hostable or open source, while Obsidian
(though not open source) and Joplin (open source, self-hostable) were
the final contenders. Joplin won due to its open-source nature,
self-hostability, and built-in mind-mapping via plugins, which aligns
with my goal of long-term reliability and flexibility.

###  Challenges 

\- Plugin Dependency: While Joplin’s mind-mapping feature is available
via plugins, it requires some setup and learning.

\- Learning Curve: Joplin’s interface and plugin ecosystem took time to
master, especially for advanced workflows.

###  Lessons 

\- Open Source Matters: Apps with active communities and self-hosting
capabilities are more sustainable for long-term use.

\- Plugins Are a Double-Edged Sword: While they add flexibility, they
also introduce dependencies and potential instability.

\- Privacy vs. Convenience: Balancing ease of use with control over data
(e.g., self-hosting vs. third-party sync) is critical.

###  Resources 

\- Joplin: \[https://joplinapp.org\](https://joplinapp.org) (Official
site, documentation, and community forums)

\- Obsidian: \[https://obsidian.md\](https://obsidian.md) (For
comparison, though not open source)

\- Markdown Cheatsheet:
\[https://www.markdownguide.org/cheat-sheet\](https://www.markdownguide.org/cheat-sheet)
(For advanced note-taking)

###  What’s Next 

Now that I’ve narrowed down the tools, the next step is to set up Joplin
on my home lab. This includes:

1\. Installing Joplin and configuring it with a self-hosted sync backend
(e.g., Nextcloud).

2\. Exploring plugins for mind-mapping and multimedia support.

3\. Testing cross-platform compatibility and backup strategies.

4\. Planning for future expansion (e.g., integrating with other home lab
tools).

###  Final Thoughts 

This journey has reinforced the importance of self-hosted solutions for
privacy, control, and long-term reliability. While the process was
challenging, the reward of a tailored, secure system is worth the
effort. For readers, I encourage you to evaluate your own needs—whether
it’s simplicity, collaboration, or advanced features—and choose tools
that align with your goals. The rabbit hole is deep, but the clarity it
brings is invaluable. 🧭
