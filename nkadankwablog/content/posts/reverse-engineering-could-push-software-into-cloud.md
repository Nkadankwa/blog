+++
date = '2026-10-21T00:00:00+08:00'
title = 'If software gets easier to study, companies may stop handing it over'
description = 'Tools such as REA could give Microsoft, Sony and other vendors another reason to move execution into the cloud, leaving users with less software to inspect or keep.'
image = '/images/reverse-engineering-cloud-editorial.png'
categories = ['My Two Cents']
tags = ['AI', 'Software', 'Cloud', 'Privacy']
+++

When software runs on a machine in your home, some part of the product has to be there with you. Its files can be examined. Its behaviour can be tested repeatedly. Someone with sufficient skill and patience can investigate how it works, even without the original source code.

Moving the important work to a company's servers changes that arrangement. Your device can receive the result while the machinery that produces it remains elsewhere.

That is why I think tools such as Reverse Engineer Anything could strengthen the push towards cloud software. If companies become less confident that complexity will discourage someone from studying their products, they have another reason to keep more of those products out of reach.

Microsoft, the company behind Windows, and Sony are obvious examples because both already offer ways to use software running remotely. I am not claiming either has announced a response to REA, or that a single GitHub project will determine their strategy. My concern is that easier reverse engineering could reinforce a direction they already have reasons to pursue.

## PhotoCraft raised one question; REA raises another

The PhotoCraft controversy brought attention to the possibility of a small operation attempting alternatives to a much larger company's applications. In [my earlier editorial]({{< relref "/posts/photocraft-adobe-and-the-right-to-compete.md" >}}), I asked what happens when recreating familiar capabilities becomes easier.

[REA](https://github.com/morluto/rea) addresses part of the work behind such attempts. Its documentation describes connecting coding agents to tools that investigate binaries, application files and runtime behaviour. I have not used it, and its existence does not prove that any commercial product can now be reproduced cheaply or reliably.

But consider how a vendor might assess the possibility. Today, investigating a difficult implementation may require expertise that few potential competitors possess. If agents make that expertise easier to use, the vendor could face more attempts to understand its software.

One response would be to improve the product faster. Another would be to distribute less of the implementation. Those responses could happen together.

## The cloud route already exists

Microsoft's Windows 365 offers Cloud PCs, allowing users to access a Windows environment running in Microsoft's cloud. The product is presented around organisational needs such as management, security and flexible access. It is an existing service, not evidence that ordinary local Windows installations are about to disappear. [Windows 365 overview](https://learn.microsoft.com/en-us/windows-365/overview).

Sony has likewise expanded cloud streaming. Its November 2025 PlayStation Portal announcement added streaming for eligible digital PS5 games in users' libraries, alongside supported catalogue titles, for PlayStation Plus Premium members. That lets supported games run without a local PS5 supplying the session. Eligibility and regional restrictions apply. [Sony's announcement](https://blog.playstation.com/2025/11/05/cloud-streaming-officially-arrives-on-playstation-portal-today-with-new-support-for-digital-ps5-games-in-your-library/).

These services have practical attractions. A business may want centrally managed desktops. A player may want to start a game without installing it or buying the hardware needed to run it locally. Those benefits can explain demand without inventing a secret motive.

They also establish an arrangement in which the customer uses a product without receiving all the software that performs the work. If reverse engineering becomes a more serious competitive concern, that arrangement could become more attractive to the supplier too.

## A screen reveals less than an executable

A downloaded application gives an investigator material to examine: instructions, resources and relationships between components. A streamed session may provide primarily images, sound and the ability to send input. The code executing the application can remain on the remote host.

That does not make cloud software impossible to investigate. People can still compare outputs, explore interfaces and infer behaviour from repeated experiments. Browser applications may also deliver substantial code to the client. Moving a login screen or an update check online would not hide an otherwise local implementation.

The relevant move is to relocate the implementation itself. Recreating a thin client would then leave the investigator without the service behind it. The barriers could include remote computation, private datasets and ongoing operations as well as the code.

For Microsoft, that possibility concerns how much computing remains on the user's PC. For Sony and game publishers, streaming can leave game execution and assets on remote infrastructure. Windows compatibility and game preservation present different technical problems, but both depend partly on what material remains available to study.

I would expect the first changes to be selective. A vendor could retain a local interface while moving a distinctive feature or calculation to a service. It would not need to stream an entire desktop to make one valuable component harder to inspect.

## The customer's bargain could quietly change

My concern is what happens when a useful cloud option becomes the only practical way to obtain a capability.

With a locally runnable application, a customer may be able to keep using an existing version after deciding against an upgrade, subject to its licensing and activation requirements. A service whose essential computation happens remotely depends on the operator continuing to provide it.

That affects more than the monthly bill. An outage can interrupt access. A change in supported regions can matter. When a service closes, retaining a shortcut or a client application does little if the system it contacted has vanished.

For games, the preservation problem is especially stark: a recording can preserve what a session looked like while leaving future players unable to interact with it. For work software, the question may be whether old projects remain usable and whether their data can move to another tool.

The irony would be considerable. Tools that make software easier to understand could encourage vendors to deliver less inspectable software. Greater technical capability on the user's side could be met by a product design that reduces what the user receives.

## There are reasons this would not happen everywhere

Remote execution costs money. Streaming introduces network dependence and latency. Some users need offline work, predictable responsiveness or direct control over their data and hardware. A local competitor could make those qualities a reason to switch.

There is also a distinction between a Cloud PC and a completely sealed service. A remote desktop may still allow an authorised user to install tools and inspect software within that environment. Putting a machine in a data centre does not automatically prevent investigation; what matters is the access the customer retains.

These limits make “everything will move to the cloud” too simple a prediction. I expect pressure towards moving the most strategically valuable parts, where the economics and customer tolerance allow it. REA could add to that pressure without being its main cause.

In [the previous REA editorial]({{< relref "/posts/reverse-engineer-anything-after-photocraft.md" >}}), I considered how easier investigation might create more practical alternatives. The response from established vendors deserves equal attention. Competition could become easier in some areas while other capabilities retreat behind services that are harder to replace.

Microsoft and Sony do not need to abandon local computing for that question to become urgent. They only need to move enough of the useful work elsewhere that the hardware we own increasingly serves as a window into systems we cannot keep.

*Sources checked on 21 October 2026. The argument about REA influencing future cloud strategy is an inference, not a reported Microsoft or Sony policy.*
