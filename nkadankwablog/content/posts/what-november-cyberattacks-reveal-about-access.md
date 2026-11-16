+++
date = '2026-11-17T00:00:00+08:00'
title = 'What November’s cyberattacks reveal about the external access'
description = 'From Sega’s newsletter to the Fugaku supercomputer, recent disclosures show why organisations need to limit what outside services can reach and know how to cut off that access.'
image = '/images/november-cyberattacks-delegated-access.png'
categories = ['My Two Cents']
tags = ['Cybersecurity', 'Data Breaches', 'Third-Party Risk', 'Privacy']
+++

When I set up a service in my homelab, I want to know what I’m allowing it to reach and whether I can cut off that access later. Connecting a service is often the easy part. The harder question is what happens when I no longer trust it, especially if it holds a copy of my data or has credentials that work elsewhere. The cyberattacks disclosed over the first half of November made that question feel relevant well beyond a home setup.

On November 9, Sega said an intrusion at its email delivery provider had exposed nearly 2.2 million newsletter addresses. On November 15, La Poste said a September attack on document delivery provider Maileva had exposed names and postal addresses for about 22 million recipients. In a different kind of incident, Japan’s RIKEN said on November 16 that it had stopped the Fugaku supercomputer after confirming unauthorised access to an operational system. These were separate incidents, with different consequences and different levels of certainty about what was taken. [Sega’s November 9 notice](https://www.sega.co.jp/release/261109_1.html), [La Poste’s November 15 statement](https://www.lapostegroupe.com/fr/actualite/cyberattaque-de-maileva-ce-quil-faut-savoir), [RIKEN’s November 16 disclosure](https://www.riken.jp/pr/news/2026/20261116_2/index.html).

What concerns me is how far the consequences can travel once a service has been given data or access for a routine job. A mailing provider needs addresses, and a support technician sometimes needs control of a machine. Those are reasonable arrangements. I would judge them by what happens when the organisation has to withdraw that trust: what can still be reached, how quickly can access be removed, and who tells the people affected?

## A mailing list is still a copy of customer data

Sega said the affected records included email addresses and, for some entries, related delivery information. It said login passwords and credit card details were outside the scope of the leak, as were addresses held in the separate Sega Account system. That distinction helps readers understand what happened. An exposed newsletter address does not mean someone can log in to a Sega account. It can still give a scammer a reason to send a message that looks relevant to the recipient. That is a possible consequence; Sega said in its November 9 notice that it had not confirmed misuse of the leaked information. [Sega’s disclosure](https://www.sega.co.jp/release/261109_1.html).

Maileva illustrates the same problem for people receiving physical mail. Someone can receive a letter from an organisation they know without ever hearing the name of the company contracted to send it. La Poste said Maileva informed affected business customers, which could then notify recipients. That arrangement makes it particularly important to decide ahead of time who will contact people, how they can verify the message, and what they will be told about their own data. To the person receiving the letter, the service relationship began with the name on the envelope. That is where I would expect responsibility for explaining the breach to begin, too. [La Poste’s statement](https://www.lapostegroupe.com/fr/actualite/cyberattaque-de-maileva-ce-quil-faut-savoir).

## Some connections can reach the next machine

On November 11, ConnectWise disclosed reports of unauthorised access to ScreenConnect partner accounts and the installation of unapproved remote access software in customer environments. Its November 13 update told partners running their own servers to disable five independent extensions and told all partners to verify that each technician’s client had been updated. The company identified about 400 cloud environments with at least one of the extensions and disabled them as a precaution. That was a count of environments with the software installed, rather than a count of confirmed compromises. [ConnectWise’s November 11 and 13 advisories](https://www.connectwise.com/company/trust/advisories).

The case shows why treating all vendor access alike is a mistake. A tool that can control customer machines deserves tighter limits than a service that sends emails. Disabling an extension may close one path, but it cannot by itself remove software already installed on a device. Someone still has to review what happened on those machines and decide which sessions and credentials need to be revoked. [ConnectWise’s guidance](https://www.connectwise.com/company/trust/advisories).

Fugaku shows why that work can extend beyond the original organisation. RIKEN said potentially exposed material included credentials that users had stored to connect to systems outside the institute. It invalidated users’ credentials for logging in to Fugaku and asked them to revoke any credentials stored there at the services where those credentials worked. RIKEN had not confirmed that research results had been taken as of November 16. That uncertainty did not make it sensible to leave potentially exposed credentials active on other systems. [RIKEN’s November 16 notice](https://www.riken.jp/pr/news/2026/20261116_2/index.html).

## Outsource the work and retain the ability to act

There is a strong case for using outside specialists. Running a mail platform or managing remote support in house takes time, and a capable provider can offer expertise that a small team cannot maintain on its own. Bringing a service inside the organisation simply changes who has to patch it, monitor it and respond when it fails. The benefit of outsourcing is real when the provider does the job well and the customer can still see and control what the service is allowed to do.

My expectation is that an organisation should be able to explain those limits before it signs a contract. For a mailing service, that means deciding which fields to share and when old lists must be deleted. For remote support, it means limiting privileged access, keeping records the customer can review, and practising how to cut off a provider’s access without relying on that provider to do it. The more a service can see or change, the more evidence the organisation should require that those controls work.

A customer should not have to study a company’s list of suppliers to understand what will happen to their data. That work belongs with the organisations choosing the suppliers. When they hand out access, they should be ready to say what they handed over, how far it reaches, and what they can do about it on the day something goes wrong.
