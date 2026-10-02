+++
date = '2026-10-02T09:00:00+08:00'
image = '/images/smart-tv-surveillance-cover.png'
title = 'When the television watches back'
categories = ['My Two Cents']
tags = ['LG', 'Smart TVs', 'Privacy', 'ACR']
+++

A television should be one of the easiest products to understand. I pay for the screen, place it in my home, connect the devices I choose, and decide what appears on it. The manufacturer builds the television; I own it.

That relationship becomes harder to defend when the television has an operating system, microphones, advertising software, network discovery, and technology designed to identify what is being watched. The screen belongs to the buyer, but the business behind it can continue behaving as if the sale never fully ended.

I do not own an LG TV. I cannot claim that I discovered unusual traffic on my own network or found suspicious files on a television in my home. My concern comes from the evidence presented by Gamers Nexus, independent research into smart-TV tracking, and LG’s own explanation of its technology.

What worries me is not one sensational claim. It is the philosophy connecting all of it: the idea that a device inside somebody’s home can remain a source of data and advertising opportunities long after that person has paid for it.

## The investigation behind the headline

In September 2026, Gamers Nexus published a two-hour investigation called [“216,000,000 Spy TVs | The LG Smart TV Problem”](https://www.youtube.com/watch?v=6IFVTcM28KA). The team says it spent months testing retail LG OLED televisions with help from Level1Techs and security researchers. Its work included capturing network traffic, examining webOS software, reviewing LG’s privacy terms, and studying how LG presents its advertising business to other companies.

The investigation argues that the privacy problem is larger than one optional setting. It points to ACR data, device discovery on the local network, location and network information, voice-related data, and diagnostic logs. It also shows material from LG Ad Solutions in which executives describe LG as owning “the glass” and discuss reaching viewers across the television and other devices in a household.

That language is more revealing than it may first appear. To the person in the shop, the television is a product. To the advertising business, it is continuing access to a screen, a household, and a pattern of attention. “We own the glass” sounds especially wrong because the customer has already bought the glass.

LG may mean that it controls the operating system and the advertising inventory running on it. Even so, the wording exposes a view of ownership that I reject. A manufacturer should not treat a purchased screen as permanent territory inside someone else’s home.

Gamers Nexus also reports finding voice-related records on tested devices, activity while the television was in standby, and data that could be retained locally before a later connection. The team says opting out reduced some traffic but did not make the television completely silent. Those are serious findings, but they are also among the points LG disputes. I think they should be described as the investigation’s findings rather than repeated as universally proven behaviour on every LG model.

Another part of the video concerns security vulnerabilities. Gamers Nexus argues that weaknesses in the television and its software could allow an attacker to turn available microphones or other features into surveillance tools. That is different from proving LG itself is deliberately recording every room. A risky vulnerability and a first-party data-collection feature are both privacy concerns, but they are not the same accusation. Treating them as identical would make the editorial louder but less accurate.

## What ACR actually does

ACR works a little like Shazam for television. It creates a small digital fingerprint from the content being played and compares that fingerprint with a reference library. This can reveal what programme or advertisement is being watched without needing the TV to store an ordinary video recording of the screen.

[LG says](https://www.lg.com/us/newsroom/corporate/statement-understanding-privacy-on-lg-smart-tvs) its current ACR system uses audio fingerprinting rather than screenshots or screen recordings. Where the feature is available and enabled, it can work with live television, LG Channels, and devices connected through HDMI. That last part matters to me. Connecting a laptop or game console does not automatically turn the television into a private, disconnected display.

LG also says ACR-related information may be used for audience measurement and trend analysis. Depending on the market and the agreements accepted during setup, information may be shared with LG Ad Solutions and may support personalised or cross-device advertising.

This is the part that makes the word *spying* feel less ridiculous. The television is not merely showing something. It may also be identifying what is being watched and feeding that activity into a larger advertising and measurement system.

Some people will reject the word because ACR does not need to save a conventional video recording. I think that focuses too much on the mechanism and not enough on the result. If a device quietly identifies viewing behaviour for audience profiling or advertising, the privacy problem remains whether the data began as a screenshot, an audio fingerprint, or something else.

## Consent is the real problem

LG says ACR is optional, off by default, and activated only after the user accepts its Viewing Information Agreement. It also says personalised advertising requires a separate agreement.

On paper, that sounds reasonable. In practice, television setup screens are exactly where many people press “agree” until the picture finally appears. The owner has already unpacked a large product, attached its stand or mounted it, connected it to Wi-Fi, and started moving through a chain of menus. The natural goal is to reach the picture. Every extra screen becomes another obstacle between the buyer and a product that is already sitting in the room.

A company cannot benefit from that impatience and then treat the final click as proof that the customer meaningfully wanted viewing analysis. A long agreement is not the same as a clear choice. Neither is a list that mixes essential terms with optional advertising features.

The distinction between consent and informed consent matters. In 2025, the Texas attorney general sued LG and other manufacturers over their use of ACR. A later [agreement between Texas and LG](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-major-agreement-lg-protect-texans-privacy-and-stop-data-from-being) required LG not to collect viewing data through ACR without informed consent. A legal allegation is not proof of every claim made online, but the agreement shows that the way these choices are presented is not a minor interface detail.

Independent research also gives me a reason to pay attention. A [2024 study of LG and Samsung televisions](https://arxiv.org/abs/2409.06203) observed ACR network traffic even when a smart TV was being used as a “dumb” external display. The researchers also found that opting out stopped traffic to the ACR servers. That is reassuring in one sense—the control made a measurable difference—but it means the control is important enough that owners should know it exists.

The fair standard should be simple: the television works fully as a television before its owner agrees to measurement or advertising. Optional features should be explained separately, in plain language, with “No” given the same visual weight as “Agree.” Refusing should not produce repeated prompts or make basic inputs and software updates feel conditional.

## What about the microphone?

Gamers Nexus makes broader claims about LG TVs retaining voice-related information or listening while apparently turned off. LG disputes those claims. The company says voice data is processed only when the remote’s voice button is held or when an owner has enabled far-field voice recognition and the television detects its wake word. It says unsuccessful wake-word audio is processed locally and immediately deleted rather than transmitted.

I do not want to dismiss the investigation simply because the findings are alarming. Gamers Nexus showed its test equipment, traffic captures, software analysis, and the people involved in the work. That deserves more consideration than a viral post repeating a rumour. It still does not mean that every claim applies identically to every model, software version, country, and privacy configuration.

There is also a meaningful difference between a television continuously uploading private conversations and a locally processed wake-word feature that a user chose to enable. LG’s response addresses that distinction, but it does not erase the wider questions about logs, consent, security, and how much data the platform is designed to produce.

Even if LG’s explanation is accepted completely, the television still contains an advertising and measurement system capable of identifying viewing activity when enabled. It still runs complex software that can create security risks. It still performs device discovery on a private network. It still places important choices inside agreements most buyers are unlikely to study.

The argument should not be reduced to one question about whether the microphone is always recording. The larger question is why a television needs to produce this much uncertainty in the first place.

At the same time, a microphone that can wait for a wake word still deserves a clear switch, a clear explanation, and conservative defaults. “The audio stays on the device unless activated” is useful information, but it should not be buried where most owners will never read it.

## Privacy should not require technical self-defence

Because I do not own an LG TV, I cannot describe these controls from personal experience. If I were considering one, I would want to understand its privacy setup before buying it, not discover it after mounting the television on a wall.

For an existing owner, LG places agreements under **Settings → Support → Privacy & Terms** on current models. Menu names vary by model and webOS version. The important items include the Viewing Information Agreement, interest-based or cross-device advertising, voice recognition, and any setting labelled Live Plus on an older model.

I would want ACR and hands-free voice recognition disabled unless I had a clear reason to use them. I would also want to know whether a major software update could introduce new agreements or change the way those choices are presented.

Keeping a television offline and using an external streaming device may create stronger separation, although it does not eliminate tracking; it moves the trust decision to another company. The Gamers Nexus findings also make me unwilling to assume that “offline for now” and “incapable of collecting or retaining anything” mean the same thing.

The usual technical advice goes further: block domains at the router, isolate the television on a separate network, monitor its traffic, or physically disable networking and microphones. Those measures may be effective. They are also an admission of failure.

Most people buying a television are not network engineers. They should not need Wireshark, a DNS blocklist, a firewall, or a two-hour investigation to understand what the screen is doing. A privacy control is only meaningful when an ordinary owner can find it, understand it, and trust that it will remain effective.

Smart features are not automatically bad. Voice control can improve accessibility. Device discovery can make setup easier. Software updates can repair faults. Content recognition can power recommendations that some people genuinely enjoy. The problem begins when convenience becomes the excuse for invisible observation, and when refusing that observation requires more effort than accepting it.

## Buying the screen should settle who owns it

I do not own an LG television, and I cannot personally test what one sends across a network. I also do not think the available evidence justifies stating that every LG television secretly records every conversation in every room. I do think Gamers Nexus presented enough technical evidence to make LG’s design choices, security, and explanations worthy of much closer scrutiny.

Even LG’s own account confirms that an enabled television can identify viewing activity from supported sources, process information about connected devices, and participate in measurement or advertising systems. The disagreement is partly about what else happens, under which settings, and how honestly those systems are explained to the buyer.

This should concern people beyond LG’s existing customers. LG is the focus because its televisions and advertising operation were examined. The underlying incentive exists across a smart-TV industry that increasingly treats hardware as the entrance to continuing services, ads, and data collection.

The Gamers Nexus investigation matters because it brings the private machinery of a familiar household object into public view. Some findings are disputed. Some concern potential security abuse rather than proven corporate behaviour. Some may vary by model, region, software version, and user settings. Those qualifications should shape the discussion, not end it.

LG’s confirmed ACR system and advertising ambitions are already enough to justify scrutiny. A television should not analyse an HDMI input for an advertising ecosystem unless the owner has made a clear and informed choice. A microphone should not leave doubt about when it is active. A local network should not become a source of household intelligence simply because a screen joined the Wi-Fi.

Most importantly, ownership should mean something. When I buy a television, the manufacturer should not retain a competing claim over the screen, the attention in front of it, or the information passing through it.

The glass belongs to the person who paid for it. The technology—and the business built around it—should behave accordingly.
