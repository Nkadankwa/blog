+++

date = '2025-12-01T09:00:00+08:00'

image = '/images/open-source-paths-editorial.png'

title = 'Why I started experimenting with self-hosting'

categories = ['Journal']

tags = ['Self-hosting', 'Privacy', 'Learning']

+++
I did not begin self-hosting because I wanted a rack full of servers. I began with a smaller question: if a project depends on a service, how much of that service do I actually understand or control?
That question became real while I was leading a healthcare project. We had to think about where information would live, which external services the project would depend on, and what would happen if a free plan changed. Healthcare data made privacy feel less like a checkbox and more like a responsibility. I started looking at components we could host ourselves, even though I was still learning what that commitment meant.
Control has a cost
The attractive version of self-hosting is easy to describe: no monthly subscription, more privacy, and complete control. The real version includes updates, failed containers, storage, backups, certificates, account security, and the possibility that I am the person who has to fix everything.
I learned this as soon as I moved beyond installing a single application. Services needed databases, volumes, networks, environment variables, and a recovery plan. Getting a page to load was only the beginning. I also had to ask whether the data would survive a restart and whether I could restore it after a mistake.
But for private projects and tools I want to manage myself, the trade-off feels worthwhile. I learn how a service is configured, what it depends on, and how to recover when something breaks.
Why I keep returning to it
As a student, cost matters. So does not treating my personal data as an afterthought. But the strongest reason I keep returning to self-hosting is learning. Docker networking stopped being an abstract topic when two services could not communicate. File permissions became memorable when an application could not write to its own storage. Backups became important when I had something I did not want to rebuild.
I do not plan to self-host everything. Email, for example, carries risks and maintenance that I am not ready to own. For a service I use occasionally, a reliable hosted option may be cheaper once my time is counted.
The point is not to reject the cloud. It is to make the dependency a decision. Self-hosting turns software from something I only consume into a system I can inspect, break, repair, and gradually understand. That is the experiment I actually signed up for.
