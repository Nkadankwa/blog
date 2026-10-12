+++
date = '2026-10-12T00:00:00+08:00'
title = 'Should the rules change when copying gets easier?'
description = 'PhotoCraft revives an old software argument. AI makes competing implementations easier to build. Should that change what intellectual property protects?'
image = '/images/photocraft-ip-editorial.png'
categories = ['My Two Cents']
tags = ['AI', 'Open Source', 'Software', 'Subscriptions']
+++

Before a developer could ask an AI agent to build a competing application, reproducing a mature program presented a formidable obstacle of its own. Someone had to investigate its behaviour, work out how to produce similar results, write an implementation and keep testing the places where the resemblance broke down. Knowing what a program did was a long way from having another program that could do it.

That difficulty protected established software businesses alongside whatever protection the law provided. A competitor might be allowed to reproduce a function and still lack the time, money or people to make the attempt worthwhile. The distinction mattered less when the practical obstacle was enough to keep most challengers out.

AI is making that distinction harder to ignore. If some of the work becomes dramatically cheaper, should the rules expand to replace the protection that difficulty once supplied?

The argument around PhotoCraft and its Adobe-inspired sibling applications is a useful place to ask. I do not think a company should acquire broader ownership of a function because somebody has found a faster way to implement it. The harder question is what happens to the incentive to invent when following becomes much easier than leading.

## We have argued about this before

In 2012, well before today's coding agents, the Court of Justice of the European Union addressed a dispute between SAS Institute and World Programming. World Programming had built software intended to run programs written for the SAS system. It studied the behaviour of the original without access to its source code.

The court held that functionality, programming language and the relevant data-file formats were not protected as expression under the EU software copyright directive. It also recognised that reproducing protected material from a manual could infringe copyright. The distinction concerned reproducing capabilities and appropriating protected expression. [Court summary of SAS Institute v World Programming](https://curia.europa.eu/jcms/upload/docs/application/pdf/2012-05/cp120053en.pdf)

That was a particular ruling under European law, not a universal permission slip for cloning software. It shows that independent reimplementation was already a serious legal question long before an AI could help write the implementation.

US copyright law also excludes ideas, processes, systems and methods of operation from copyright protection. Its legislative history specifically distinguishes a program's expression from the processes it embodies. [17 U.S.C. §102 and its historical notes](https://www.govinfo.gov/content/pkg/USCODE-2022-title17/html/USCODE-2022-title17-chap1-sec102.htm)

These distinctions leave room for competition. A developer can create a valuable product without receiving ownership of every task it performs. Other rights, including patents and trademarks, may raise separate questions; copyright is not the whole of intellectual property.

The old bargain did not promise that competitors would always need the same budget or endure the same difficulties. Much of that protection came from the work itself.

## PhotoCraft makes the old argument feel new

The developer behind the [seven-app announcement](https://www.reddit.com/r/vibecoding/comments/1wvz4ua/100_open_source_clean_room_implementations_of_7/) presented Rust implementations aimed at the work done in Photoshop, Illustrator, Premiere, Lightroom, Acrobat, After Effects and InDesign. PhotoCraft is the image editor. The related projects include VectorCraft, FilmCraft, LightCraft, PrintCraft, EffectCraft and DesignCraft.

[Reporting on the release](https://www.tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings) describes AI-assisted development and the backlash: excitement over alternatives, accusations of copying and scepticism about the software's readiness.

The project's own wording is more restrained than the claim that one person has already replaced Adobe. PhotoCraft's [README](https://github.com/storytold/photocraft) calls it an early alpha and says it is not yet a replacement for daily professional Photoshop work. It distinguishes connecting menu items to commands from matching their behaviour.

I have not tested these applications. They do not need to equal Adobe today for the question to matter. Even an incomplete implementation makes the possibility visible: a much smaller operation attempting a scope of work that once seemed far beyond its resources.

The unsettling part is the apparent compression of effort. A competitor can observe the destination after another company has spent years deciding where to go. AI may then reduce some of the labour needed to follow it. The original developer paid for the experiments, including the ideas that went nowhere. The follower gets to begin with a product whose useful decisions are already visible.

That asymmetry deserves an argument stronger than cheering because Adobe is unpopular.

## Should effort buy a longer period without competition?

Consider a small developer who spends years finding a better way to edit photographs. Once the product succeeds, somebody uses AI to reproduce much of its behaviour and offers an alternative for free. Change the name from Adobe to that small developer and the celebration becomes less comfortable.

This is the strongest case for reconsidering the rules: if imitation becomes cheap enough, the people financing new work may have less opportunity to recover the cost of discovering something worth imitating. A market full of quick followers still needs someone willing to make the first uncertain investment.

I want to know what right we would create in response. Would the first implementation gain control over a workflow? Would competitors need permission to offer a familiar sequence of operations? Would a similar result become evidence of wrongdoing even when the implementation was independent?

Those rules would reach well beyond a viral AI project. They would affect ordinary competitors and open-source developers too. Established firms would have extensive catalogues of features around which to assert new rights. A measure presented as protection for the small inventor could make it harder for that inventor to challenge anyone already in the market.

My objection is to treating a fall in development cost as sufficient reason to expand ownership. The value of the original work is real. A permanent claim over the problem it solved does not follow from that value.

There is an investment on the user's side as well. Years spent learning a tool, organising projects and developing a working routine are not the vendor's contribution alone. Familiar controls and compatible files allow some of that investment to survive a move. Making every alternative unnecessarily unfamiliar would charge the user for the privilege of competition.

## Easier development calls for clearer evidence

AI does change the practical questions around provenance. Someone directing a coding agent may know what they put into the prompt while knowing little about the model's training material. A generated implementation can arrive much faster than a person can inspect its history and dependencies.

PhotoCraft describes its approach as clean-room implementation from public specifications and observed behaviour, without proprietary code, shaders or assets. That is the project's account. A README cannot independently establish the provenance of every contribution. Equally, the use of AI does not by itself demonstrate that protected Adobe material was copied.

The response I would support is more concrete evidence around the work being distributed: records of references, origins of assets, dependency licences, meaningful review and a process for investigating challenged material. These are proposals about accountability, not a claim that one universal legal checklist already exists.

The project's [attribution file](https://github.com/storytold/photocraft/blob/main/ATTRIBUTION.md), which identifies sources and licences for non-code assets, gives the discussion something to examine. A specific disputed file would give it more. A screenshot that feels familiar gives it much less.

The standard should also be symmetrical. A small developer's protected work deserves scrutiny when it appears in a larger company's product. Enthusiasm for cheaper tools should not make the origins of the work irrelevant.

## Giving it away does not settle it

Open-sourcing a program answers a question about the permissions its authors offer. It does not automatically resolve whether everything they distributed was theirs to license.

PhotoCraft includes MIT and Apache 2.0 licence files. Its [MIT licence](https://github.com/storytold/photocraft/blob/main/LICENSE-MIT) permits broad reuse, modification and redistribution while requiring the relevant notices to remain. Those permissions matter to users and future maintainers. They are not an exemption from somebody else's rights.

The opposite assumption is equally unhelpful: that a free implementation must be theft because it competes with an expensive one. Price cannot do the work of examining provenance. Neither can the number of hours spent at a keyboard.

For me, the appropriate change is in the expectations surrounding evidence and responsibility. Faster production gives us reason to demand a credible account of what was produced. It does not give the first vendor a larger claim over the function itself.

Before AI, the cost of recreating software quietly protected a great deal that copyright did not. As that cost falls, we should be honest about what is being lost. A business may be losing the shelter of an expensive development process. That is a significant economic change. Turning it into a new ownership right would be a political choice, with consequences for everyone who wants to build an alternative.

If we make that choice, we should be able to defend it without relying on the idea that competition has become unfair simply because it has become easier.

*Sources checked on 12 October 2026. This editorial discusses the policy question; it does not determine whether any particular release infringes a specific right.*
