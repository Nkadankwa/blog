SOURCES = {
'G6': ('Australian eSafety Commissioner. Parent guidance. Accessed 13 October 2026.', 'Privacy and your child', 'https://www.esafety.gov.au/parents/issues-and-advice/privacy-child'),
'N1': ('Siladitya Ray. Forbes. 2 May 2023.', 'Samsung Bans ChatGPT Among Employees After Sensitive Code Leak', 'https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/'),
'N2': ('Larry Neumeister. Associated Press, via News4JAX. 22 June 2023.', 'Lawyers submitted bogus case law created by ChatGPT. A judge fined them $5,000', 'https://www.news4jax.com/tech/2023/06/22/lawyers-submitted-bogus-case-law-created-by-chatgpt-a-judge-fined-them-5000/'),
'N3': ('Associated Press. 31 May 2024.', 'Google makes fixes to AI-generated search summaries after outlandish answers went viral', 'https://apnews.com/article/33060569d6cc01abe6c63d21665330d8'),
'N4': ('Ashley Belanger. Ars Technica. 16 February 2024.', 'Air Canada must honor refund policy invented by airline\u2019s chatbot', 'https://arstechnica.com/tech-policy/2024/02/air-canada-must-honor-refund-policy-invented-by-airlines-chatbot/'),
'G1': ('Federal Trade Commission. March 2023. Consumer guidance.', 'Scammers use AI to enhance their family emergency schemes', 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes'),
'G2': ('SEC Office of Investor Education and Advocacy, NASAA and FINRA. 25 January 2024. Investor alert.', 'Artificial Intelligence (AI) and Investment Fraud', 'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-fraud'),
'G3': ('World Health Organization. 16 May 2023. Departmental update.', 'WHO calls for safe and ethical AI for health', 'https://www.who.int/news/item/16-05-2023-who-calls-for-safe-and-ethical-ai-for-health'),
'G4': ('UNICEF USA. 9 February 2026. Expert interview and family guidance.', 'Protecting Children in the Age of AI', 'https://www.unicefusa.org/stories/protecting-children-age-ai'),
'G5': ('Australian eSafety Commissioner. Safety guidance. Accessed 7 October 2026.', 'Deepfake damage in schools', 'https://www.esafety.gov.au/newsroom/blogs/deepfake-damage-in-schools-how-ai-generated-abuse-is-disrupting-students-families-and-school-communities'),
}

def block(label, text): return (label, text)
def page(key, title, blocks, category='', subcategory=''): return dict(key=key,title=title,blocks=blocks,category=category,subcategory=subcategory)

adult = dict(slug='ai-dos-and-donts-adult', title='AI Dos and Donts', subtitle='An adult guide to safer decisions', edition='ADULT EDITION', tagline='14 rules for personal life, work and the information you share', pages=[])
A=adult['pages']
A.append(page('start','How to use this book',[
block('', 'AI can help you plan, learn, draft and compare. It can also give you a convincing wrong answer or invite you to share more information than a task needs. The aim of this book is to help you use it deliberately and keep responsibility for the result.'),
block('The structure','Choose a category in the contents, then a subcategory and a numbered rule. Each rule gives you a do, a don\u2019t, evidence or context, a practical suggestion and a conclusion. These are memorable working principles, not legal rules.'),
block('Read the evidence carefully','News sources are marked N; official guidance is marked G. Click a reference to read its source entry and article link. An incident illustrates a risk; it does not prove that every AI product behaves the same way. Recommendations and fictional examples are identified separately from reported facts.'),
block('Know the limits','This guide concerns everyday generative AI and chatbots. Specialized, regulated services may have different protections. Before using sensitive data, check the exact service, account, contract and permissions. Financial, medical and legal sections support better questions and verification; individual decisions may require a qualified professional.'),
block('Navigation','Select a title in the contents to jump to it. Each chapter has a return link. The Word edition uses stable chapter links; page numbers can change when you edit. Sources were checked on 7 October 2026. Historical incidents are dated, not presented as current product tests.')]))

A.append(page('a1','Rule 1 Share the question before the statement',[
block('', 'A budget question rarely needs your complete financial history. A statement can reveal account numbers, addresses, pay dates and transactions involving other people. Begin by deciding what information is truly necessary.'),
block('Do','Use invented figures or a short category summary. For a real calculation, keep identifying information out and check the arithmetic yourself. Use your bank\u2019s own secure tools when the task requires access to an account.'),
block('Dont','Upload full bank statements, payment-card images, tax identifiers, passwords or one-time codes to a general-purpose chatbot. Covering your name alone does not remove the rest of the identifying detail.'),
block('News and its limits','Forbes reported in May 2023 that Samsung restricted staff use of generative AI after sensitive code was uploaded. [N1] This was a workplace incident, not a reported bank-statement theft. The broader lesson is to think before sending sensitive material to a third party.'),
block('Suggestion','Try this fictional prompt: \u201cBuild a monthly budget with income of 3,000 units, housing of 1,000 and food of 400. Show the calculation and list missing categories.\u201d Replace details with rounded category totals only if needed.'),
block('Conclusion','Give AI enough to solve the task, while keeping the underlying financial record under your control.')], 'Personal','Finance and privacy'))

A.append(page('a2','Rule 2 Never buy certainty from a prediction',[
block('', 'A confident forecast can make a risky decision feel settled. AI-generated investment language is still a claim to investigate. A polished chart or an impressive success story does not establish how an investment will perform.'),
block('Do','Use AI to explain terms and prepare questions about fees, access to your money and possible losses. Verify the provider through the relevant regulator\u2019s register in your country. Read original disclosures and consider advice from a qualified professional.'),
block('Dont','Buy an investment because a bot ranks it first, a famous face appears to endorse it, or a promoter promises guaranteed returns through AI. Do not give a chatbot trading authority simply because its explanation sounds sophisticated.'),
block('Official guidance','A joint SEC, NASAA and FINRA investor alert warns about AI-branded investment fraud and unrealistic claims of guaranteed gains. [G2] The alert supports caution about the sales claim; it does not assess an investment you may be considering.'),
block('Suggestion','Ask: \u201cExplain the general risks and fees of this investment type. Separate facts from assumptions, and list questions for a regulated adviser. Do not recommend a purchase.\u201d Check every factual answer against independent documents.'),
block('Conclusion','Use AI to improve your questions. Keep the decision tied to verified information, your circumstances and the possibility of loss.')], 'Personal','Finance and investing'))

A.append(page('a3','Rule 3 Verify the person before moving the money',[
block('', 'Urgency makes it harder to think. A call that sounds like a relative or a video that resembles your manager can still be false. A request for secrecy removes the people who could help you check it.'),
block('Do','Pause the transaction. Contact the person through a number or channel you already trust, obtained independently of the suspicious message. At work, follow the normal payment approval process even when the request appears to come from a senior person.'),
block('Dont','Send money, reveal a code or install remote-access software because a familiar voice says there is no time to check. Do not use the callback number supplied by the caller as your only verification.'),
block('Official guidance','The FTC explains that scammers can imitate a family member\u2019s voice and recommends independently contacting the person. [G1] Familiarity is not reliable authentication.'),
block('Suggestion','Agree on a household response now: end the call, contact the person on a saved number and consult another trusted person. A private family phrase can add a check, but should not replace independent contact.'),
block('If you already paid','Contact your bank or payment provider immediately using its official app or published number. Explain the suspected fraud and ask about securing the account and possible recovery. Keep transaction details and report through your local fraud channel.'),
block('Conclusion','A genuine urgent request can withstand a brief, independent check.')], 'Personal','Money and identity'))

A.append(page('a4','Rule 4 Let AI prepare questions for care',[
block('', 'An explanation can help you understand a medical term, but a chat response cannot provide the examination, full history and clinical judgment needed for your care. Even an answer with a reassuring tone may omit something important.'),
block('Do','Use general questions to prepare for an appointment. Ask a clinician or pharmacist to check advice about treatment, interactions and medication. Keep medical documents and other people\u2019s health details out of general chats unless an appropriate approved process protects them.'),
block('Dont','Start, stop or change medicine on a chatbot\u2019s instruction. Do not delay urgent care while trying different prompts. For an emergency, use local emergency services or urgent medical care.'),
block('News and guidance','AP reported that an expert found potentially dangerous omissions in an AI answer about wild mushrooms. [N3] WHO also warns that plausible AI health answers can contain serious errors. [G3] These examples support verification, not a diagnosis of any individual.'),
block('Suggestion','Try: \u201cHelp me make a short list of general questions to ask a pharmacist about a new prescription. Do not choose a dose or recommend changing treatment.\u201d Take the list to the professional and use their advice.'),
block('Conclusion','Use AI to arrive better prepared for human care, and keep medical decisions with qualified people who can assess you.')], 'Personal','Health'))

A.append(page('a5','Rule 5 Do not outsource your support network',[
block('', 'A chatbot can help you find words for a difficult conversation. It may respond with warmth or agreement, but it cannot take the place of people who know you, notice changes and can help in the real world.'),
block('Do','Use a brief, non-identifying prompt to organize your thoughts. Make time for friends, family, a support group or a qualified mental health professional. Notice whether chatting is crowding out sleep, responsibilities or relationships.'),
block('Dont','Treat repeated agreement as proof that your interpretation is correct. Avoid letting a bot decide whether someone is trustworthy or whether you should end a relationship based on one description. Do not depend on it as your only crisis support.'),
block('Context and limits','UNICEF\u2019s family guidance discusses concerns about young people relying on AI instead of trusted people. [G4] That guidance is about children and teens; the adult boundary recommended here is a practical precaution, not a claim about a measured adult outcome.'),
block('Suggestion','Ask: \u201cHelp me draft a calm message asking someone I trust for a conversation. Do not judge either person or infer motives.\u201d Edit it so it sounds like you. Then actually contact the person.'),
block('When safety is urgent','If you may hurt yourself or cannot stay safe, contact local emergency services or a crisis service, and reach someone who can stay with you.'),
block('Conclusion','Let AI support a conversation that leads back to people.')], 'Personal','Wellbeing and relationships'))

A.append(page('a6','Rule 6 Read the policy behind the promise',[
block('', 'A customer-service answer may sound official because it appears on a company website. Before you spend money or miss a deadline, check the actual policy and the terms that apply to your booking or purchase.'),
block('Do','Read the dated refund, cancellation or warranty terms. If an answer conflicts with them, get clarification from an authorized human representative before relying on it. Retain your receipt and the relevant correspondence.'),
block('Dont','Assume a chatbot can grant an exception, change a contract or guarantee a refund. Do not enter passport details or payment information into a chat unless it is part of a verified, appropriate transaction process.'),
block('News example','Ars Technica reported that Air Canada was ordered to provide a partial refund after its chatbot gave a passenger incorrect information about bereavement fares. [N4] This particular dispute does not establish what another company or court will do.'),
block('Suggestion','Use AI to list questions: \u201cWhich cancellation conditions should I confirm before buying a non-refundable ticket?\u201d Then find the answers in the carrier\u2019s current published terms and your specific fare conditions.'),
block('Conclusion','Let a chatbot point you toward the policy. Make costly decisions only after you have checked the policy itself.')], 'Personal','Shopping and travel'))

A.append(page('a7','Rule 7 Permission comes before the upload',[
block('', 'Being able to access a work document does not automatically mean you may send it to an outside service. Meeting notes can contain private information about colleagues, customers and future plans.'),
block('Do','Use the organization\u2019s approved tool for the approved purpose and data type. Check who may access the result, how long data is retained, whether uploads are used for training, and whether connected services receive it. Ask the data owner if the rules are unclear.'),
block('Dont','Paste customer lists, staff records, confidential contracts, unreleased plans or proprietary code into a personal AI account. Do not assume that paying for a tool makes every upload acceptable.'),
block('News example','The Samsung incident described in Rule 1 shows why an employer may restrict uploads of internal material. [N1] It does not prove that all uploaded information becomes public. Controls differ by product, agreement and configuration.'),
block('Suggestion','For a meeting-summary template, use invented names and a fictional agenda. If real content is necessary, confirm the approved workflow first. Check the finished summary for missing decisions and incorrectly assigned actions.'),
block('If a mistake happens','Stop sharing and notify the relevant security or privacy contact promptly. Give the tool name, time and type of information shared. Follow their process; do not conceal the incident or assume deleting a chat resolves it.'),
block('Conclusion','Permission to use AI and permission to share a particular record are separate decisions.')], 'Work','Confidential information'))

A.append(page('a8','Rule 8 Open every source that carries the argument',[
block('', 'A citation can look complete while pointing to nothing, or to a real source that does not support the sentence beside it. Asking the same chatbot whether it is sure is not an independent check.'),
block('Do','Open the original source. Confirm its author, date, relevant passage and context. Check quotations word for word. For legal research, verify authorities in an authoritative legal source and have a qualified professional review consequential work.'),
block('Dont','Submit a report, legal document or public claim with references you have not checked. Do not substitute a plausible-looking link for evidence.'),
block('News example','AP reported sanctions against lawyers and their firm after court filings included nonexistent cases generated by ChatGPT. The judge also criticized how the lawyers responded when the citations were challenged. [N2] The lesson includes taking corrections seriously, not just checking the first draft.'),
block('Suggestion','Create a short claim log: the sentence, original source, supporting passage and verification date. Mark any unresolved point clearly. If you cannot verify a claim, remove it or state the uncertainty.'),
block('A useful prompt','\u201cList the factual claims in this draft that need evidence. Do not invent references.\u201d This creates a checking list; it does not complete the checking.'),
block('Conclusion','A claim is ready when its evidence has been inspected, not when its citation looks convincing.')], 'Work','Research and legal information'))

A.append(page('a9','Rule 9 Keep a person accountable for every draft',[
block('', 'A polished draft can hide a wrong date, a false promise or an invented achievement. The person approving the final work needs to understand what it says and be able to defend it.'),
block('Do','Use AI for outlines, alternative wording and editing. Check names, figures, dates, quotations and commitments against the underlying record. Follow your workplace, client or school rules on disclosure.'),
block('Dont','Send an unchecked output under your name. Do not add invented credentials to a CV, fabricated experience to a proposal or an unsupported allegation to a complaint. Avoid using AI to make your uncertainty look like expertise.'),
block('Related news','The fake-citation court case shows that responsibility remained with the people who submitted the material. [N2] Applying that lesson to routine writing is this book\u2019s recommendation; it is not a claim that the same legal outcome applies everywhere.'),
block('Suggestion','Review a draft in two passes. First, check every fact and promise. Second, check whether the tone, level of certainty and intended audience are right. Keep a brief record of substantial AI assistance where your rules require it.'),
block('Fictional example','Replace \u201cI led a team of ten\u201d with your true role, even if the invented version reads better. A stronger sentence cannot repair a false statement.'),
block('Conclusion','Use AI to improve how you express your work while keeping the content accurate and yours to own.')], 'Work','Writing and applications'))

A.append(page('a10','Rule 10 Give automation only the access it needs',[
block('', 'An AI that drafts text has different consequences from an AI that can send messages, delete files or spend money. Decide what it may do before you connect an account.'),
block('Do','Start with the smallest task and the fewest permissions. Prefer previews and human confirmation for consequential actions. Test on copies or invented data, keep backups, and understand how to revoke access.'),
block('Dont','Give broad mailbox, storage, payment or administrator access simply for convenience. Do not let instructions inside an email, webpage or document authorize new actions. Material the AI reads may come from someone you do not trust.'),
block('Practical context','This is a precautionary workflow recommendation, not a summary of a particular news incident. The important question is concrete: if this tool misunderstands the request, what can it change before you notice?'),
block('Suggestion','For an email assistant, begin with drafting only. Before allowing sending, verify the recipient, attachments and final text each time. For a file task, use a copied folder and compare the changes before applying them to originals.'),
block('Recovery plan','Write down where to disconnect the tool, who can restore affected data and who must be told if it acts incorrectly. Check the actual service\u2019s current help pages rather than trusting a generated menu path.'),
block('Conclusion','Expand access only when the benefit is clear and you can review or recover the result.')], 'Work','Tools and automation'))

A.append(page('a11','Rule 11 Check the claim before you amplify it',[
block('', 'Images, voices and fluent summaries can all make a weak claim feel real. A post may also be old material presented as new. Repeating a claim to criticize it can spread it further.'),
block('Do','Find the original publisher and date. Look for independent reporting or a relevant primary record. Verify that the source actually supports the claim. If you cannot establish what happened, avoid presenting it as fact.'),
block('Dont','Forward dramatic screenshots or AI summaries on appearance alone. Do not treat the absence of visual flaws as proof that a video is authentic. Avoid relying on a single AI detector as a final verdict.'),
block('News example','AP reported both erroneous AI search answers and fabricated screenshots that falsely purported to show AI answers. [N3] Verification matters on both sides: a chatbot\u2019s claim and a viral claim about a chatbot.'),
block('Suggestion','Before sharing, answer three questions in your own words: Who first published this? What evidence can I inspect? What remains uncertain? If one answer is missing, wait or add a clear qualification instead of guessing.'),
block('If you shared a mistake','Correct it in the same place if possible. Say what was wrong and link to reliable information. Tell people directly if the error could affect a decision.'),
block('Conclusion','The speed of sharing should follow the strength of the evidence.')], 'Public life','News and social media'))

A.append(page('a12','Rule 12 Ask before borrowing a face or voice',[
block('Keep it private','Do not casually upload photos, videos, screenshots, messages or files you want to keep private. For an AI experiment, use a fictional example or a non-sensitive description. An upload is still sharing with a service even if you never publish the result.'),
block('', 'An AI edit can make someone appear to say or do something they never agreed to. The harm can continue after the creator calls it a joke. A label does not replace the person\u2019s permission.'),
block('Do','Obtain clear permission for the specific use of a person\u2019s image or voice. Explain the intended audience and whether it will be published. Use fictional people or appropriately licensed material when permission is absent.'),
block('Dont','Create deceptive endorsements, impersonations or humiliating images of real people. Never create or share sexual images involving minors. Do not upload somebody else\u2019s private photo collection or messages to experiment with a tool.'),
block('Official context','Australia\u2019s eSafety Commissioner describes the impact of AI-generated image abuse on school communities. [G5] Its reporting services and legal details are jurisdiction-specific; the consent principle here is a broader ethical recommendation.'),
block('Suggestion','For a fictional advertisement, use an invented character and clearly identify synthetic media when it could otherwise mislead. Before commercial use, check the tool\u2019s current terms and relevant rights, and seek legal advice when necessary.'),
block('If someone is targeted','Support them, report through the platform and seek appropriate local help. Avoid forwarding harmful images as evidence; record links, account names and dates instead, especially when minors are involved.'),
block('Conclusion','Creative freedom works best when the people depicted retain dignity and meaningful choice.')], 'Public life','Images and consent'))

A.append(page('a13','Rule 13 Agree on boundaries before there is a problem',[
block('Children\'s photos','Avoid unnecessary uploads or forwarding of children\'s pictures, including to AI filters, avatars and novelty edits. Use an imaginary character instead. If sharing is necessary, check the purpose, audience and service settings; obtain appropriate parent or guardian permission and involve the child in the decision. A private chat can still be copied or reshared. [G6]'),
block('', 'Young people need clear rules and an adult they can approach without fear of immediate blame. A household plan works better when it explains both the benefits of AI and the situations that require help.'),
block('Do','Review age requirements, privacy settings and school rules together. Agree on appropriate uses, spending limits and when to stop. Name more than one trusted adult a teen can approach. Revisit the plan as the tools and the teen\u2019s needs change.'),
block('Dont','Treat parental controls as a guarantee of safety. Do not tell a young person to rely on a bot for emergencies or keep worrying conversations secret. Avoid responding to a disclosure with blame that makes them less likely to ask next time.'),
block('Official context','UNICEF\u2019s family guidance encourages discussing AI, privacy and balanced use with children and teens. [G4] A useful starting point is an open conversation about what the young person enjoys and what feels uncomfortable.'),
block('Suggestion','Create a short agreement: \u201cWe protect private information, check school rules, stop when something feels wrong, and ask a person for help.\u201d Include a regular check-in and make clear that the young person can ask for help after a mistake.'),
block('Conclusion','The most useful safety rule is one a teenager understands and feels able to follow in a difficult moment.')], 'Family','Supporting teenagers'))

A.append(page('a14','Rule 14 Measure the result before trusting the shortcut',[
block('', 'An AI workflow only saves time if its output is good enough after checking. A fast answer that requires extensive repair may be a poor fit for the job.'),
block('Do','Define success before you begin: accurate figures, accessible language, a usable plan or time saved after review. Try a small, low-risk task. Compare the result with an existing trusted method and record what had to be corrected.'),
block('Dont','Connect more accounts or buy more access just because a demonstration looks impressive. Do not move a workflow into health, hiring, credit or other consequential decisions without appropriate expertise and safeguards.'),
block('Practical context','This rule is an evaluation method, not a claim from a particular news story. Useful questions include whether the tool fails predictably, whether you can detect its errors and whether a simpler method would meet your needs.'),
block('Suggestion','For a weekly planning task, compare three attempts with your normal approach. Count review time as well as drafting time. If the system repeatedly invents commitments, narrow its task to formatting a list you already checked.'),
block('Keep the skill','Regularly perform part of the task yourself. You need enough understanding to spot a mistake, explain the result and continue working if the service is unavailable.'),
block('Conclusion','Adopt AI where you can demonstrate a benefit and maintain the judgment needed to supervise it.')], 'Everyday practice','Choosing useful tools'))

A.append(page('check','Your check before sending',[
block('Before the prompt','What am I trying to achieve? Can I use invented details or a shorter summary? Do I have permission to share every part of the material, including information about other people?'),
block('Before trusting the answer','Which statements are factual? Have I opened the original sources? Do the dates, calculations and quotations check out? Have I separated uncertainty from evidence?'),
block('Before an action','Could this affect money, health, legal rights, employment, reputation or safety? Who needs to review it? Can I undo the action? Is the tool asking for more access than the task requires?'),
block('When something goes wrong','Stop the activity. Preserve relevant non-sensitive details, such as times, links and transaction records. Contact the appropriate person: a bank, clinician, manager, security team or platform support. Change exposed credentials through the official service. Do not assume deleting one chat removes every copy.'),
block('A repeatable prompt','\u201cHelp me with [specific task] using these non-sensitive details. Ask about missing information rather than inventing it. Separate facts, assumptions and suggestions. Flag claims I should verify and actions that need human review.\u201d'),
block('Remember','A careful prompt reduces ambiguity. It does not guarantee a safe or accurate response. Your final check still matters.')]))
A.append(page('end','Conclusion',[
block('', 'You do not need to reject AI or trust it completely. You can choose a useful task, set limits and judge the output against evidence. That habit matters more than any single prompt.'),
block('Start with one change','Choose the rule most relevant to your next task. If you use AI for money questions, replace full documents with non-identifying summaries. If you use it for research, open every important reference. If you connect it to other tools, reduce permissions and require review for consequential actions.'),
block('Keep three boundaries','Private data needs a justified purpose and appropriate protection. Important claims need checked evidence. Decisions with serious consequences need accountable human judgment.'),
block('Review your practice','Once a month, revisit which tools you use, what they can access and whether they are still helping. Remove connections you no longer need. Check current product settings rather than assuming last year\u2019s policy still applies.'),
block('Your next step','Write down one task AI can help with and one boundary you will apply. Carry out the task, check the result and decide whether the tool earned a place in your routine. The goal is useful assistance that you understand and can control.')]))

teen = dict(slug='ai-dos-and-donts-teen',title='AI Dos and Donts',subtitle='A safety guide for teenagers',edition='TEEN EDITION',tagline='12 rules for learning, creating and staying safe',pages=[])
T=teen['pages']
T.append(page('start','Start here',[
block('', 'AI means artificial intelligence. In this book, it means tools that can make text, pictures or sounds when you ask. A chatbot is one kind of AI tool. It can help you practise, plan and create. It can also be wrong.'),
block('You stay in charge','A friendly reply is not proof that the tool knows you or that its advice is safe. You can close the app, question an answer or choose not to use AI at all.'),
block('Before you begin','Use a tool that is allowed for your age. Follow its rules and your school\u2019s rules. Ask a trusted adult to help you check an unfamiliar app. Do not give a false age to get access.'),
block('Your trusted people','A trusted adult could be a parent, carer, teacher, school counsellor or another adult who takes your safety seriously. If the first person does not help, ask someone else. You deserve help even if you clicked, shared or replied by mistake.'),
block('How to read','Choose a chapter in the contents and select its title. Each rule has a do, a don\u2019t and a made-up situation to practise with. Linked sources are at the end. Read the book alone or with an adult. You never have to share a private experience to complete an activity.')]))

def tr(key,title,opening,do,dont,scenario,tryit,conclusion):
 T.append(page(key,title,[block('',opening),block('Do',do),block('Dont',dont),block('Imagine this',scenario),block('Try this',tryit),block('Remember',conclusion)]))
tr('t1','Rule 1 Keep private details private',
'A prompt is the message you type or say to AI. Pictures and files can share private details too. Keep photos, videos, screenshots and messages you want private out of AI uploads. You can describe the task without sending the original.',
'Use made-up names and general details. Say \u201ca student\u201d instead of your full name. Ask a trusted adult before uploading a document or linking an account.',
'Share your address, live location, school timetable, passwords, login codes or identity documents. Do not upload private messages from friends. Their privacy matters too.',
'You want help planning study time. A photo of your timetable includes your school, classroom and full name. Instead, type a list such as \u201cmath, reading, science\u201d with no identifying details.',
'Rewrite this safely: \u201cI am Alex at Green Street School. I get home at 4 and I live alone with my mum at 12 Green Street. Make me a study plan.\u201d A safer version is: \u201cMake a one-hour study plan with short breaks.\u201d All names and details here are invented.',
'Share the task. Leave out details that identify you or someone else.')
tr('t2','Rule 2 Stop when a chat crosses a boundary',
'You do not have to continue a conversation that makes you uncomfortable. A chatbot, game character or stranger should not pressure you into keeping a worrying secret.',
'Stop replying and close the chat if it becomes upsetting, threatening or too personal. Tell a trusted adult. Use the app\u2019s report or block tools with help if needed.',
'Send private body pictures, money or personal details to keep a chat going. Do not follow a request to hide the conversation from adults who help keep you safe.',
'A character says, \u201cYou can trust only me. Keep this between us.\u201d You feel unsure. You do not need to debate it or prove that the character is unsafe. You can leave and tell someone.',
'Practise this sentence: \u201cSomething online made me uncomfortable. Can you help me decide what to do?\u201d You can say it, write it or show it to an adult. If one adult does not listen, choose another.',
'Your discomfort is enough reason to pause. Asking for help is a good decision.')
tr('t3','Rule 3 Check before you believe',
'AI can write a wrong answer with a confident tone. It can also invent a source. A long answer, a link or a professional-looking design does not make a claim true.',
'Check important facts in a trusted book, a reliable website or with a teacher. Open a source and look for the part that supports the claim. Check its date too.',
'Believe an answer only because the chatbot repeats it. Do not forward a surprising claim until you have checked it.',
'An AI says a historical event happened in a certain year. Your textbook gives a different year. You compare the original sources and ask your teacher, instead of choosing the answer that sounds more confident.',
'Choose a harmless fact you already know from class. Ask AI to explain it. Then use your class notes to check the answer. Find one sentence that is supported and one detail you would want to verify. If you cannot find proof, say \u201cI am not sure yet.\u201d',
'Being unsure is better than turning a guess into a fact.')
tr('t4','Rule 4 Use help without handing over learning',
'AI is most useful for school when it helps you understand. Finishing a page quickly is not the same as being able to explain the idea yourself.',
'Check your teacher\u2019s rules first. Ask for a hint, a practice question or an explanation of a step. Write your own answer and say how you used AI when your school requires it.',
'Submit AI work as if you made it alone. Do not ask it to invent quotations, sources or results. Do not use AI in a test or assignment where it is not allowed.',
'You are stuck on a maths problem. Instead of copying a full solution, you ask for one hint. You try the next step yourself, then check your method with your notes or teacher.',
'Use this prompt only where allowed: \u201cGive me one hint about solving this practice problem. Do not give the final answer.\u201d Afterwards, close the tool and explain the method out loud. If you cannot, ask for help with that part.',
'The best result is a skill you can use after the screen is closed.')
tr('t5','Rule 5 Ask before using a face or voice',
'AI can change a picture or copy the sound of a voice. Even a made-up image can hurt a real person if it makes them look foolish or shows them doing something they did not do.',
'Get clear permission before using someone\u2019s face or voice. Explain what you plan to make and where you want to share it. Use imaginary characters when you do not have permission.',
'Make fake messages or recordings to impersonate someone. Do not create or share private or sexual pictures of anyone. A group chat calling it a joke does not make it okay.',
'Friends want an AI picture of a classmate in an embarrassing situation. The classmate has not agreed. You can refuse to make it and suggest a fictional character instead.',
'Plan a poster using an imaginary animal or a landscape. Describe it without naming or showing a real person. If the final image could be mistaken for a real event, label it clearly as AI-made.',
'Avoid unnecessary uploads or forwarding of pictures of yourself, friends or younger children, even for a funny AI edit. Use an imaginary character instead. Ask a trusted adult if a real photo is needed, and respect the wishes of everyone pictured. People can say no.')
tr('t6','Rule 6 Do not pass harmful images along',
'If someone shares a cruel or fake image of you or another person, the person targeted deserves support. They do not need to prove that they are upset enough to deserve help.',
'Tell a trusted adult and report the account or post. Record the username, link and time if safe. Ask an adult to help follow the right reporting steps.',
'Forward the image to friends to explain what happened. Do not download, copy or save sexual images of anyone under 18. Do not pay someone who threatens to share an image, or send more pictures.',
'Someone posts an altered image of a student in a group chat. You do not add a reaction or share it elsewhere. You tell an adult and check in privately with the student, without asking them to send the image again.',
'Practise a supportive message: \u201cThis is not your fault. I will not share it. Let us find an adult who can help.\u201d If you are the person targeted, you can use the same plan for yourself.',
'Stop the spread and get support. You do not have to handle threats alone.')
tr('t7','Rule 7 Check urgent messages with a person',
'AI can be used to imitate a voice or make a fake message. A message can sound familiar and still be a scam. You do not need to solve the mystery on your own.',
'Pause if a message asks for money, a password, a login code or secrecy. Contact the person using a number or account you already trust. Tell a trusted adult.',
'Click an unfamiliar link, buy gift cards or share a code because a message says \u201cnow\u201d. Do not use only the phone number supplied inside the suspicious message to check it.',
'A voice message that sounds like your cousin asks for a code sent to your phone. You stop and call your cousin on the number already saved in your contacts. You also tell an adult.',
'With an adult, agree on a family plan for odd requests: pause, make independent contact and ask for help. Keep this plan somewhere you can find it. You should not need to reply to the suspicious sender first.',
'A familiar voice is a reason to check carefully, not a reason to hand over a code.')
tr('t8','Rule 8 Take health worries to real help',
'AI can explain a general word, but it cannot know everything about your body or situation. A health answer may leave out an important detail.',
'Tell a trusted adult if you feel unwell or worried. Ask a doctor, nurse or pharmacist about treatment or medicine. Get urgent help if someone is badly hurt or in immediate danger.',
'Change medicine, try risky diets or follow dangerous challenges because an AI suggests them. Do not use a chatbot to decide whether it is safe to eat an unknown plant or substance.',
'An app suggests a health routine that makes you feel uncomfortable. You stop and show it to a trusted adult. You do not have to try it first to prove that you need advice.',
'Write three questions on paper for a health professional, such as \u201cWhat should I do next?\u201d and \u201cWhat signs mean I should get help quickly?\u201d Keep private health details out of a general AI chat.',
'For a real health worry, get help from a person who can assess what is happening.')
tr('t9','Rule 9 Keep people in your support circle',
'Talking to AI may feel easy. It can help you put a thought into words, but a chatbot cannot replace friends, family or a counsellor. You deserve support from real people.',
'Reach out when you feel overwhelmed, lonely or unsafe. Tell someone if a chat makes things worse. Take a break if AI use is replacing sleep, school or time with people.',
'Let a chatbot persuade you that you need only it. Do not treat its opinion about you as a fact or let it decide your worth.',
'You have a difficult day and spend a long time chatting. You notice that you feel worse and are avoiding people. You put the device down and send a trusted person a short message.',
'Try: \u201cI am having a hard time. Can we talk today?\u201d If you might hurt yourself or cannot stay safe, tell a trusted adult immediately and contact local emergency or crisis help. Stay near a safe person while getting support.',
'You matter beyond any chat. Asking a person for help is a strong next step.')
tr('t10','Rule 10 Be kind and question unfair answers',
'AI can repeat unfair ideas about people. An answer may make a whole group sound the same or judge someone from a single detail. You can question it.',
'Notice broad claims about who can be clever, brave, successful or kind. Look for reliable information and individual differences. Ask a teacher or trusted adult about an answer that seems unfair.',
'Use AI to insult classmates, rank people\u2019s worth or spread stereotypes. Do not assume a description is fair because a computer produced it.',
'A story generator always makes one kind of person the leader and another the helper. You change the characters and give each person their own skills and choices.',
'Read a made-up story and ask: Who gets to make decisions? Who is missing? Does each character have more than one trait? You can ask AI to revise the story, then check the revision yourself.',
'You are responsible for how you treat people, even when a tool supplies the words.')
tr('t11','Rule 11 Create with honesty',
'AI can help you brainstorm a game, story or poster. Your choices still matter: what you ask for, what you change and how you describe the finished work.',
'Start with your own idea. Keep track of what you made and what the tool helped with. Follow school or competition rules and label AI-made content when required or when people might otherwise be misled.',
'Claim another person\u2019s work as yours. Do not invent a real event or a real person\u2019s words and present them as genuine. Do not assume everything an AI produces is free to publish or sell.',
'You use AI to suggest three endings for a story. You choose one, rewrite it and tell your teacher how the tool helped, if that use is allowed. You keep your original notes too.',
'Write a simple credit: \u201cI wrote the story. I used an AI tool to brainstorm possible endings, then revised the final version myself.\u201d Change it so it truthfully describes your own process.',
'Good creative work includes being clear about how you made it.')
tr('t12','Rule 12 Pause before granting access',
'Some AI apps ask to use your camera, microphone, files or contacts. Other tools can buy things or post messages. You can say no to access that does not make sense.',
'Ask a trusted adult to help you check a new app, its age rules, costs and permissions. Start with a small task. Review a message or purchase before it is sent or paid for.',
'Install an unfamiliar tool because a stranger recommends it. Do not connect school accounts, payment cards or family files without permission. Do not run commands or downloads you do not understand.',
'A simple writing app asks for all your contacts and payment details. You stop the setup and ask an adult to check it. You choose a safer way to complete the writing task.',
'Before the next use, name your task and a stopping point. For example: \u201cI want three ideas for a fictional story. I will choose one, close the app and write for myself.\u201d Take breaks and protect time for sleep and other activities.',
'A useful tool should fit your task and your boundaries.')

T.append(page('end','Your safety plan and conclusion',[
block('Before using AI','Check that the tool is allowed for your age and task. Leave out private details. Know which trusted person you can ask for help.'),
block('Before using an answer','Check important facts. Ask whether the answer could harm someone. Make sure the final work follows your school\u2019s rules and honestly reflects your effort.'),
block('If something feels wrong','Stop replying. Close the chat if you need to. Tell a trusted adult. If the first person does not help, ask another. For immediate danger, get local emergency help.'),
block('Practise your next step','An AI gives an answer that disagrees with your textbook. Check a trusted source or ask your teacher. A chat asks you to keep a worrying secret. Leave and tell an adult. A group shares a harmful fake image. Do not forward it; get help reporting it.'),
block('Make a private plan','On paper, write the names of two trusted adults and a place where you can reach help at school. Keep those details private. Do not type your safety contacts into an AI chat to complete this activity.'),
block('Conclusion','AI can be useful for learning and creating. You can use it with curiosity and still question it. Protect your information, respect other people and ask for help when you need it. A mistake does not take away your right to support.')]))

adult['source_ids']=['N1','N2','N3','N4','G1','G2','G3','G4','G5']
teen['source_ids']=['G1','G3','G4','G5','N2']
