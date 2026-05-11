+++
date = '2026-05-11T09:00:00+08:00'
image = '/images/java-spring-editorial.png'
title = 'How I keep secrets out of Git'
categories = ['Posts']
tags = ['Git', 'Environment Variables', 'IntelliJ IDEA']
+++

The safest secret in a Git repository is the one that never enters the working directory.

I use environment variables for values such as passwords, tokens, and connection details, but a `.env` file inside a project can still be committed by mistake. Adding it to `.gitignore` helps, yet ignore rules do not protect a file that was already tracked or a value pasted directly into code.

## Keeping the real values elsewhere

Where practical, I keep the file containing real values outside the repository and reference it from the run configuration. In IntelliJ IDEA, that can mean defining environment variables for the application without storing their values in a committed project file. The code reads the variable name; my local environment supplies the value.

Inside the repository, I can keep an example file containing only safe placeholders:

```text
DATABASE_URL=
DATABASE_USERNAME=
DATABASE_PASSWORD=
```

That documents what the application needs without publishing the answers.

## Git history changes the response

Checking the current files is not enough. If a secret was committed and later deleted, it may still exist in the history. The first action should be to revoke or rotate the credential, because rewriting history cannot make an already exposed password trustworthy again. Cleaning the repository comes after containing the risk.

I also avoid printing secrets in logs, including them in screenshots, or sending a configuration archive without checking it. Moving values outside Git solves only one path of exposure.

Environment variables are not an end all be all. They are a boundary that keeps code and deployment-specific values separate. Combined with external local configuration, safe examples, credential rotation, and careful run settings, that boundary makes an accidental commit much less likely.
