+++
date = '2026-03-30T09:00:00+08:00'
image = '/images/java-spring-editorial.png'
title = 'What I am learning about logs and debugging'
categories = ['Journal']
tags = ['Debugging', 'Java', 'Learning']
+++

I am still at the beginning of learning logs and debugging. My first instinct has usually been to print something to the console: the value of a variable, a message showing that a branch ran, or a marker proving that the program reached a particular line.

That method is simple, and it has helped me. It becomes messy quickly, though. Temporary messages mix with real output, important details disappear in the noise, and I sometimes remove the very line that would have explained a later problem.

## What the debugger changes

A debugger lets me pause the program, inspect its current state, and move through execution without adding a new print statement for every question. A breakpoint near the place where behaviour becomes unexpected can show whether the wrong value arrived from somewhere else or was changed locally.

I am trying to become more deliberate about this. Instead of placing breakpoints everywhere, I begin near the boundary where good data becomes bad. I check the call stack and the inputs, then move outward. Debugging is more about tracing how the program reached it than about staring at the failing line.

## Moving from console messages to useful logs

I have also been reading about Java logging and Lombok's logging annotations. The part I want to understand is not just how to replace `System.out.println`. Proper logs have levels, context, and a consistent format. They can record useful events without making everthing seem as equally urgent.

The caution is that logs can create problems too. Passwords, tokens, and personal data do not belong in them, and a loop that logs constantly can hide the message that matters.

My current approach is still a mixture: console output for quick experiments, a debugger for following state, and structured logging as the habit I am working towards. I do not yet consider myself good at it, but I am beginning to ask a new question “What evidence would explain this failure?” not “Where can I print this value?”
