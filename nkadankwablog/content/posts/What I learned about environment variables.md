+++
date = '2026-02-05T09:00:00+08:00'
image = '/images/environment-variables-cover.png'
title = 'What I learned about environment variables'
categories = ['Journal']
tags = ['Environment Variables', 'Docker', 'Learning']
+++

Environment variables were one of those terms I saw everywhere before I properly understood them. Tutorials would tell me to copy values into a `.env` file, Docker Compose examples were full of `${NAMES_LIKE_THIS}`, and a missing variable could stop an entire stack from starting.

At first, they felt like another layer hiding the real configuration. Eventually, I understood that the separation was the point.

## The idea that made them click

An application needs information that may change depending on where it runs: a port number, a database address, a feature flag, an API key, or a password. Hard-coding those values means changing the source whenever the environment changes and creates an easy way to publish a secret by accident.

Environment variables let the application ask its surroundings for those values instead. The code can stay the same while my laptop, a container, and a production server each provide different configuration.

I began to see this clearly while working with Docker Compose. A database container might have a stable service name inside the Docker network but a different address from the host machine. The variable was not random decoration; it described which environment the application expected to find.

## The mistakes that taught me the most

Small errors caused surprisingly large problems: a misspelled variable name, quotation marks becoming part of a value, a `.env` file in the wrong directory, or a container that had not been recreated after the configuration changed. “Variable not set” stopped being a mysterious message once I learned to check which process was reading the value and when it was loaded.

The more important lesson was about secrets. A `.env` file is convenient, but it is not automatically secure. If I commit it to Git, print it in a log, share a screenshot, or leave it readable in the wrong place, the separation from the code has not protected anything.

## The habit I use now

I keep real secrets out of version control and add the relevant `.env` file to `.gitignore`. I include an `.env.example` with the required names and harmless placeholders so the next setup—including my own setup months later—has instructions. I also document which values are required and which have safe defaults.

Environment variables have not removed configuration problems from my projects. They have given those problems a clearer home. What once looked like extra complexity now feels like a boundary between the application I am building and the place where I choose to run it.
