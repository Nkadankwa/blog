+++
date = '2026-10-26T00:00:00+08:00'
title = 'PHP2Shell: a short prompt, a long repair job'
description = 'The PHP security emergency exposed a widening gap between finding vulnerabilities, coordinating disclosure and getting dependable fixes into service.'
image = '/images/php2shell-editorial.png'
categories = ['My Two Cents']
tags = ['AI', 'Security', 'Open Source', 'Software']
+++

A website taken offline for safety looks much the same to its visitor as a website that has failed. A form cannot be submitted. Someone refreshes a page and wonders whether the problem is their connection.

That was part of the disruption around PHP2Shell last week. The emergency involved two critical vulnerabilities in PHP, the software underneath many web applications. It also produced hurried shutdowns, competing accounts of exploitation and a public argument about when protective updates should have been released.

Then there was the sentence that seemed to explain the whole episode: an AI had reportedly been asked to “find bad vulnerabilities in PHP”.

It is an arresting detail. It is also an incomplete explanation. What interests me is the distance between that short instruction and the work required to make millions of separate installations safer. Discovery can accelerate without the rest of the repair process accelerating with it.

## Two flaws, and more than one kind of damage

The main vulnerabilities are CVE-2026-109618 and CVE-2026-109619. Wiz's research describes memory-safety problems in PHP's handling of fatal errors and exhausted memory, with demonstrations of unauthenticated remote code execution and sensitive memory disclosure. Exploitability depends on the particular path and deployment; a widely used runtime is not evidence that every website was successfully attacked. [Wiz's research](https://www.wiz.io/blog/php2shell-php-rce).

The danger warranted an urgent response. The NSA advised identifying affected systems, applying vendor updates and considering taking systems offline when an immediate update was not feasible. [NSA advisory, 21 October](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-critical-patches-recommended-for-php-vulnerabilities/).

The resulting disruption was real even where no breach was reported. The Netherlands' National Cyber Security Centre says it temporarily disabled its own website as a precaution. Hosting company Sebsoft says it took customer environments offline on 21 October, later restoring its websites, Moodle installations and other applications. [NCSC-NL's account](https://www.ncsc.nl/en/alerts/update-php-vulnerabilities-remain-a-reason-for-immediate-patching), [Sebsoft's service report](https://sebsoft.nl/en/news/php2shell-service-restored/).

Those are protective shutdowns, not admissions that attackers stole the data. That distinction should have survived every headline. An organisation can make a responsible security decision and still impose a substantial cost on the people who need its service.

## What was actually reported about the prompts

Chainguard CEO Dan Lorenc supplied the clearest exact wording I could verify. In his own account of the disclosure dispute, he said his team independently rediscovered the issue using its harness and a frontier model with this basic prompt:

> find bad vulnerabilities in PHP

He said the team had already been told that something was coming in PHP, and subsequently confirmed that some findings matched the original report. This is his description of the work, not a publicly reproducible transcript I have tested. [Lorenc's account](https://www.linkedin.com/feed/update/urn:li:activity:7518756994284077056/).

A research harness supplies a working environment around the model. The short prompt does not describe the tools, the investigation, the intermediate instructions or the validation. Prior knowledge that a serious PHP issue was coming also narrows the task. None of that makes the claim uninteresting. It makes it a claim worth understanding accurately.

Wiz separately reports using Wiz Atlas, Gemini 4 Argon and GPT-5.6 Sol across discovery, exploit development and patch validation, including repeated testing and adaptation. That account describes a research process rather than publishing a complete set of prompts that a reader can reproduce. [Wiz's account of AI's role](https://www.wiz.io/blog/php2shell-php-rce).

I would not turn that into several invented quotations or claim that one sentence automatically produced a working attack against the web. The verified prompt is striking enough without adding a mythology around it.

## The repair problem was older than the viral sentence

The PHP Foundation says signs of the out-of-memory problem were identified in 2024. Fixes became stuck among compatibility, performance and implementation trade-offs, with too few specialists available. Reports in August 2026 established the remote-code-execution impact more clearly. The Foundation acknowledges a structural failure in the earlier process. [PHP Foundation's retrospective](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/).

That history changes the lesson. AI did not create the underlying weakness. It helped researchers establish consequences that had previously been difficult to demonstrate. A flaw can become more dangerous in practice when the effort needed to exploit it falls, even though the vulnerable code has not changed.

Finding it was valuable. So was making a repair that would survive contact with an enormous variety of existing applications. A change that prevents one dangerous failure can introduce another problem or break a dependency somewhere else. The people deciding which compromise to ship carry a responsibility that a model's promising output does not remove.

This is where the celebratory story about discovery runs into the less photogenic story about maintenance. One produces a finding. The other has to leave working systems behind.

## The disclosure process became another source of instability

According to the PHP Foundation, circulating CVE identifiers and an accidentally published demonstration video disrupted coordination. The release moved from 22 to 21 October. It says Chainguard then published fixed images more than six hours before the agreed release, exposing changes while other distributors were still preparing updates. [Foundation's disclosure timeline](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/).

Lorenc defended early publication on the basis of the ease of rediscovery, available information and reports of attacks. The Foundation disputed the decision. [Chainguard CEO's explanation](https://www.linkedin.com/feed/update/urn:li:activity:7518756994284077056/).

The tension is understandable even if the decision remains contentious. Waiting can leave users exposed. Publishing a fix can also help an attacker infer the flaw before other users have a convenient update. A coordinated release tries to reduce that unevenness.

Faster analysis makes the window more difficult to manage. It does not make the window irrelevant. A vendor able to protect its own customers quickly is not necessarily in the best position to decide how much preparation time everyone else can afford to lose.

I would want emergency disclosure decisions to rest on shared, clearly described evidence and a process for changing the plan. Independent rediscovery is a reason to reassess the timetable. It does not, by itself, tell us which timetable protects the most people.

## The panic also outran some of the evidence

Sophos initially reported successful exploitation in customer environments, then corrected that assessment on 22 October. Its updated account described scanning and failed attempts, with no evidence of a successful compromise in that telemetry at the time of the correction. [Sophos's timestamped correction](https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619).

On 23 October, NCSC-NL likewise said exploitation appeared complex and the likelihood of large-scale exploitation was lower than initially estimated. It continued to recommend urgent updates. [NCSC-NL's revised assessment](https://www.ncsc.nl/en/alerts/update-php-vulnerabilities-remain-a-reason-for-immediate-patching).

Neither account establishes what happened on every network. They do show why a scan, an attempted exploit, a laboratory demonstration and a confirmed compromise must remain separate claims. Urgency does not require pretending those categories mean the same thing.

For ordinary readers, the confusion is costly. An unavailable page becomes proof of a breach; a successful demonstration becomes proof of universal compromise. Administrators then have to repair systems and explain a story that has already acquired more certainty than the evidence supports.

## Faster discovery needs somewhere for the work to go

My concern is that the industry will spend heavily on finding more flaws while treating the capacity to resolve them as somebody else's overhead. A useful report still creates work: someone must reproduce it, assess it, choose a repair, test it, package it and help operators understand what changed.

The PHP Foundation is asking organisations that depend on PHP to fund sustained security work. [Foundation's funding appeal](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). I think that is the most consequential request in the whole episode. Companies that depend on shared infrastructure should budget for its upkeep before the emergency forces them to calculate its value in lost operating hours.

The reported prompt deserves attention because it suggests that sophisticated investigation may become easier to initiate. The shutdowns deserve attention because they show who bears the interruption when risk cannot be resolved quickly. The disclosure dispute deserves attention because independently rational decisions can still produce a badly coordinated result.

PHP2Shell should leave us with better tools and a stronger repair organisation. If all we retain is a screenshot of a five-word prompt, we will have remembered the easiest part of the crisis and neglected the work that made recovery possible.
