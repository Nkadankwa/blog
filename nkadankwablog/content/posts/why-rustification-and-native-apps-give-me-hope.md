+++
date = '2026-11-09T09:00:00+08:00'
title = 'Why Rustification and the return to native apps give me hope'
description = 'Rust and renewed interest in native desktop software offer a welcome opportunity to make applications respect the computers people already own.'
image = '/images/rust-native-apps-editorial.png'
categories = ['My Two Cents']
tags = ['Rust', 'Native Apps', 'Software Design', 'Local Software']
+++

I want an installed application to feel as though it belongs on my computer. Opening a local file should be straightforward, typing should feel responsive, and keeping several useful tools open should not make ordinary work unnecessarily demanding. My frustration with desktop software often begins when an application asks for the space and privileges of an installed program while offering little more independence than a website.

That is why the interest in Rust and purpose-built desktop interfaces has caught my attention. Zed uses Rust and its GPUI framework to build a GPU-rendered editor, while System76 has built COSMIC around a Rust-based desktop environment and application toolkit. These are concrete examples of investment in desktop software, although they do not establish that the whole industry is abandoning web interfaces. [Zed's account of its architecture](https://zed.dev/blog/zed-1-0), [System76's COSMIC overview](https://system76.com/cosmic).

I see this direction as a welcome development. My interest is less in which language wins attention than in whether applications become more considerate of the machines running them. A renewed willingness to take desktop performance seriously could improve everyday computing, particularly for people who want to keep existing hardware useful. The examples here explain why I am optimistic; they are not a performance comparison I have carried out myself.

## What I mean by Rustification

“Rustification” can describe replacing existing components with Rust or choosing it for new software that might otherwise have used another language. That can involve a command-line utility, a background service or an entire application. It does not necessarily describe what appears on the screen.

Rust's ownership system checks rules about memory management during compilation. That offers developers a way to manage resources without relying on a conventional garbage collector and helps prevent important classes of memory errors in safe Rust. It does not make incorrect algorithms, excessive allocations or poor product decisions disappear. Unsafe code and interactions with other languages also require careful review. [The Rust book's explanation of ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html).

The distinction matters because enthusiasm for a language can become a substitute for assessing the result. An application rewritten in Rust may still do too much work, start unnecessary processes or depend on a remote service for a task that could have stayed local. A rewrite deserves credit for improvements users can experience and maintainers can support.

What encourages me is the possibility of making efficient, dependable software easier to sustain. That is a useful reason to adopt a language, even if most users never need to know its name.

## Rust and native interfaces are related choices

Zed provides an example of a team deliberately choosing a different foundation for its interface. In its April 29, 2026 announcement, the team explains that it moved beyond its experience building Atom with Chromium and developed GPUI in Rust around GPU rendering. This is the developer's account of the architectural decision, rather than an independent finding that it makes every workflow faster. [Zed's 1.0 announcement](https://zed.dev/blog/zed-1-0).

COSMIC shows a related investment at the desktop level. System76 describes a common toolkit for applications, applets and other desktop components, built around Rust. The significance for this argument is the commitment to a desktop environment and its surrounding tools, rather than a claim that every application must look like a traditional operating-system widget. [COSMIC's desktop and application approach](https://system76.com/cosmic).

There is also a middle ground. Tauri combines a Rust-based application core with interfaces rendered through webviews. Its architecture can use web technologies for the interface while relying on the system webview rather than requiring each application to bundle its own browser engine. That makes it a different approach to packaging desktop software, but it remains a web-rendered interface. [Tauri architecture](https://tauri.app/concept/architecture/), [Tauri overview](https://beta.tauri.app/start/).

These distinctions give the discussion a more useful foundation. Rust is an implementation choice, rendering is an interface choice, and offline operation is a product choice. A project can improve one without changing all three.

## The computer should benefit from the engineering

The advantage I want to see is practical. If an application opens sooner, responds consistently and leaves more resources available for other work, the improvement extends beyond its own window. A browser, editor, notes application and communication tool have to share the same machine.

This is particularly relevant when hardware cannot simply be replaced whenever software becomes more demanding. Modest savings across several everyday applications could make an existing computer more comfortable to use. That would be a useful outcome even without a dramatic benchmark result.

It also changes what software developers treat as normal. A simple task should not require users to accept an increasingly heavy application without explanation. There may be good reasons for complex infrastructure, but the benefit should justify the cost to the person whose memory, storage and battery it consumes.

My preference for [local tools]({{< relref "/posts/why-i-sometimes-prefer-local-tools.md" >}}) comes from similar expectations. Working with a nearby file can be more direct than uploading it, waiting for processing and downloading the result. Native development can support that experience, but developers still have to choose it. A Rust application that sends every useful operation to a server has not automatically given its owner more independence.

## Web technology has earned its place too

The strongest argument for web-based desktop applications is that they make it practical to support several operating systems with a shared interface and widely available development skills. That can allow a small team to serve people it could not otherwise support. Users benefit from that reach, and successful applications should not be dismissed because of their framework.

Electron's architecture also has purposes beyond drawing a window. It inherits Chromium's process model, separating a main process from renderer processes. A process list therefore cannot be read simply as a count of unnecessary work; reliability and isolation are part of the design. [Electron's process-model documentation](https://www.electronjs.org/docs/latest/tutorial/process-model).

A native rewrite has its own costs. Accessibility, text input, keyboard behaviour, platform integration, internationalisation and maintenance all need attention. A smaller download is a limited improvement if the result becomes difficult to use with assistive technology or loses functionality people depend on.

For me, the case for native software is strongest when it improves the complete experience. I would rather have a well-maintained application built with web technology than a technically fashionable replacement that neglects essential behaviour. The renewed interest in native development is valuable because it broadens the choices and raises expectations, not because it makes every existing application obsolete.

## A better desktop is worth building

I would judge this movement through the work it makes easier. Can a person keep several applications open comfortably? Does the interface remain responsive while a task runs? Are local files easy to reach, permissions understandable and core functions available without a connection where the task allows it? Can people with different accessibility needs use the result?

Those questions provide a more useful standard than a Rust logo or a promise that something has been rewritten. They also give developers room to choose the architecture that genuinely suits their application.

The prospect of better desktop software is what makes Rustification encouraging to me. It suggests that some teams are prepared to reconsider assumptions about the resources ordinary applications should require. If that produces responsive tools that integrate well, remain maintainable and keep existing computers useful, it is a direction worth supporting.

The computer should feel more capable because its software has improved. That is the outcome I would like this renewed attention to native applications to deliver.
