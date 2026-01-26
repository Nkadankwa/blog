+++
date = '2026-01-26T09:00:00+08:00'
image = '/images/learning-websites-editorial.png'
title = 'What makes a good tutorial'
categories = ['Posts']
tags = ['Learning', 'Tutorials', 'Documentation']
+++

I have followed tutorials that produced a working result and still left me unable to explain what I had built. The screen matched the instructor’s, the commands completed successfully, and yet one small difference on my own machine was enough to send me back to the beginning.

That experience changed what I call a good tutorial.

## A result is not the same as understanding

A good tutorial does more than tell me where to click or what to paste. It explains the important decisions: what a command changes, why a service needs a particular setting, and which parts are specific to the instructor’s environment.

This became obvious while I was learning Docker and self-hosting. Many videos showed the happy path on Linux, while I was working through Windows-specific paths, ports, networking, and permission problems. Copying the same configuration was not enough. The tutorials that helped were the ones that explained the structure, because structure survives when versions and interfaces change.

## The details that keep me watching

I value a tutorial that states its assumptions near the beginning. Which operating system and software version is being used? What should already be installed? Is the example suitable for a test environment, or is it meant to be secure enough for real use?

I also appreciate comparisons. If an instructor explains why they chose a bind mount instead of a named volume, or why one database fits the example better than another, I learn how to make a decision rather than how to reproduce one decision.

The best tutorials include a little troubleshooting. They show how to read a log, verify that a service is running, or undo a step safely. Watching someone recover from a mistake is often more useful than watching a perfect installation.

## What I do differently now

I try not to follow a long tutorial without pausing. I stop after a meaningful step, check what changed, and write down the part I would otherwise forget. If the tutorial provides a configuration file, I read it before running it. If it makes a claim that affects security or compatibility, I compare it with the official documentation.

A tutorial has done its job when I can adapt the lesson to a slightly different problem. A working screen is satisfying, but the real test is whether I know what to investigate when that screen does not appear.
