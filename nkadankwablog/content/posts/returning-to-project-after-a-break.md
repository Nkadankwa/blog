+++
date = '2026-09-10T09:00:00+08:00'
image = '/images/project-reflection-cover.png'
title = 'What returning to a project after a break reveals'
categories = ['Journal']
tags = ['Software Design', 'Java', 'Documentation']
+++

Returning to a project after a break shows whether its organisation can support my memory. Code that felt obvious while I was writing it can become difficult to navigate once the details are no longer fresh.

When I was newer to structuring applications, I placed every controller in one controller package. I understood the code, and the layout looked organised at first. As the project grew, finding code for a specific function became annoying. Related controllers, DTOs, entities, and services were separated by technical type, so following one feature meant jumping across several large folders.

## I started organising around functions

I changed the structure so each function or feature had its own area containing the controller, DTOs, entities, and other relevant pieces. Creating that structure can take more time during development, and every project does not require the same level of separation.

For me, the cost is justified when I return later. The path tells me which code belongs together. Someone else opening the project also has a clearer place to begin when they want to understand a feature.

## Distance is a useful test

A break exposes unclear names, hidden assumptions, and setup knowledge that never reached the README. If I have to reconstruct every decision from memory, the project depended too heavily on the person I was while writing it.

I now see organisation as part of maintaining the code. Folder structure cannot repair a confused design, and excessive nesting can create its own friction. The useful structure is the one that helps me trace a feature and make a change without first rebuilding the entire project in my head.

Returning after time away gives me a perspective close to that of a new contributor. The questions I ask during that return show me where the code and documentation need to communicate more clearly.
