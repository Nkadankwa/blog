+++
date = '2026-10-19T00:00:00+08:00'
title = 'After PhotoCraft, reverse engineering could become routine'
description = 'REA connects coding agents to software-analysis tools. After the PhotoCraft controversy, it suggests a deeper shift in how alternatives might be built.'
image = '/images/reverse-engineering-shift-editorial.png'
categories = ['My Two Cents']
tags = ['AI', 'Open Source', 'Software', 'Self-Hosting']
+++

For years, a useful feature in somebody else's application could remain out of reach even when its purpose was obvious. A developer might understand the result they wanted and still spend weeks working out the details that made it behave properly. Buying the application was often cheaper than investigating it, rebuilding the relevant part and maintaining the result.

That practical calculation helped protect software businesses. Customers paid for expertise, reliability and support, but they also paid because reproducing even a small part of a product was difficult.

The PhotoCraft controversy made the possibility of changing that calculation unusually visible. Now a GitHub project called [REA, or Reverse Engineer Anything](https://github.com/morluto/rea), makes me wonder whether the more lasting change will arrive through the tools used to investigate software in the first place.

I have not used REA or tested PhotoCraft. This is an editorial about what their documented approaches could mean, rather than a claim that either has already delivered on every ambition attached to it.

## PhotoCraft made the scale of the ambition visible

The [announcement behind PhotoCraft and its sibling projects](https://www.reddit.com/r/vibecoding/comments/1wvz4ua/100_open_source_clean_room_implementations_of_7/) presented open-source implementations aimed at seven Adobe applications. It invited an argument about how much software one developer could now attempt, and about the origins of the work being produced.

There is a significant gap between attempting that scope and replacing the tools professionals depend on. PhotoCraft's own README still describes an early alpha and says it is not yet a Photoshop replacement for daily professional work. [PhotoCraft repository](https://github.com/storytold/photocraft).

That qualification matters. A feature list cannot tell someone whether an important file will survive a round trip or whether a familiar operation behaves correctly in a difficult case. The work of making a dependable application continues long after an impressive screenshot.

Even so, I think dismissing the whole episode because the product is unfinished misses the interesting question. An incomplete project can still reveal that people are prepared to attempt something they previously considered impractical.

In [my earlier editorial on PhotoCraft]({{< relref "/posts/photocraft-adobe-and-the-right-to-compete.md" >}}), I argued that falling development costs should not automatically become a reason to expand ownership over software functions. REA brings another part of that calculation into view: the cost of understanding what already exists.

## REA brings investigation into the coding session

According to its documentation, REA connects agents to tools including Ghidra, Hopper and IDA for inspecting native software, with other workflows for JavaScript, Electron and additional targets. The agent can use findings and supporting evidence to explain behaviour and develop an implementation. [REA README](https://github.com/morluto/rea).

The important possibility is a shorter distance between asking how something works and having enough evidence to build an alternative. The analysis tools existed before this repository. Bringing them into an agent's workflow could make their capabilities accessible to people who would otherwise struggle to coordinate them.

There is no basis here for saying REA produced PhotoCraft. I see them as separate examples of pressures that could reinforce each other: cheaper implementation and more accessible investigation.

The project's published examples are narrower than the phrase “anything” might suggest. They include tracing Notion's clipboard handling and reconstructing a sound-position calculation from DX-Ball. Those are the project's demonstrations, not independent tests I have repeated. [REA case studies](https://rea.tools/).

Their narrowness makes the argument more interesting to me. A reusable way to investigate one stubborn feature could matter to far more developers than a promise to reproduce an entire suite.

## The first shift may be much smaller than an Adobe replacement

Imagine a small organisation that uses an expensive application mainly to transform files into one particular format. Or a developer who needs an abandoned utility to keep working with a newer system. The value they want may occupy a tiny corner of a much larger product.

If investigation and implementation become affordable enough, building a limited alternative becomes a more plausible choice. It would not need to persuade every customer to leave the original. It would need to satisfy one well-defined requirement reliably.

This is where I would expect an early shift: more modest replacements, compatibility tools and components designed around a particular user's work. That is a prediction about incentives, not evidence that REA has already made those projects economical.

The effect could still reach large vendors. A customer with a credible alternative has a different conversation about price, export and access. A company may discover that some customers were paying for a broad suite because a small essential capability was difficult to obtain anywhere else.

There are limits. Inspecting a desktop application cannot reproduce a remote service's private data or the people operating it. Distribution, trusted updates, collaboration and support remain substantial work. Easier analysis would change one obstacle among several.

## Small developers would feel this too

The comfortable version of this story has expensive holders facing energetic newcomers. The less comfortable version has a small developer spending years discovering a useful interaction, then facing a competitor who can study the successful result and follow quickly.

The follower benefits from knowing which experiment worked. The original developer paid for that discovery, including the attempts customers never saw. Faster reconstruction could widen that imbalance.

I do not think the answer is to pretend the original work had no value. I would expect businesses to put more weight on the parts of their service customers continue to need: dependable operation, thoughtful improvements, support and the confidence that someone will fix a serious problem.

That transition could be painful even for good businesses. Being exposed to stronger competition does not mean a developer was previously doing something wrong. It means a practical advantage they relied on may be weakening.

## Evidence will matter more as the process gets easier

One distinction deserves particular care after PhotoCraft. Observing what an application does and examining its implementation involve different source material. A project claiming an independent reconstruction needs an account of what its contributors actually examined and reused.

REA's disclaimer presents it as a tool for lawful research, education, interoperability, preservation and authorised analysis. It does not grant permission to use somebody else's software or materials however a user wishes. [REA's stated scope](https://github.com/morluto/rea/blob/main/DISCLAIMER.md).

For me, the useful response is to make provenance easier to examine. What was inspected? Which findings were observations, and which were guesses? Where did the distributed code and assets come from? What tests support claims about matching behaviour?

A record of investigation could help answer those questions, although the existence of a record would not settle every dispute. The point is to give reviewers something more substantial than a familiar interface or an assurance that AI wrote the code.

The most consequential outcome would be a change in ordinary development habits. A developer encounters an unfamiliar feature, investigates it through an agent, checks the evidence and builds something suited to a different need. If that process becomes dependable, reconstructing a limited capability may become an everyday option.

PhotoCraft brought attention to the scale of what someone might attempt. REA suggests how the investigation behind future attempts could become repeatable. Whether that produces useful alternatives will depend on the testing, judgement and maintenance that follow. But a software business built partly on the assumption that understanding its product is too much trouble may have reason to reconsider that assumption.

*Sources checked on 19 October 2026.*
