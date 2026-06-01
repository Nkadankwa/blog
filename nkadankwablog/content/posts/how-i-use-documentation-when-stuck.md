+++
date = '2026-06-01T09:00:00+08:00'
image = '/images/java-spring-editorial.png'
title = 'How I use documentation—and AI—when I get stuck'
categories = ['Journal']
tags = ['Documentation', 'Java', 'AI']
+++

When I get stuck in a Java project, one method I use is generating the project's Javadoc in IntelliJ IDEA, putting the relevant documentation into an archive, and giving it to an LLM along with a description of the problem.

The important part is that the documentation gives the model the classes, methods, parameters, and relationships that belong to this project instead of forcing it to guess from a generic description. My explanation adds the part Javadoc cannot know: what I expected, what happened instead, and what I already tried.

## A better question needs evidence

Before asking, I try to reduce the issue. I include the error message, the smallest relevant path through the code, and the behaviour I can reproduce. If the answer recommends a method, I can compare that suggestion with the generated documentation and the implementation rather than accepting it because it sounds familiar.

This approach is most useful when the problem comes from how parts of my own code connect. For framework behaviour, library details, or version-specific questions, the official external documentation still matters. Javadoc generated from my project does not explain everything the dependencies do.

## What I should not send

An archive can contain more than I intended. Before uploading anything, I need to check for credentials, private source, internal URLs, personal information, and generated pages that expose sensitive names or values. If the code is not mine to share, an external AI service is not the right place for it.

AI does not remove the need to understand the project. It becomes more useful when I give it accurate context and then verify the response against that same context. Generating documentation helps me do both: it gives the question a map and gives me something concrete to use when checking the proposed route.
