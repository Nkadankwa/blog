+++
date = '2026-09-28T09:00:00+08:00'
image = '/images/java-spring-editorial.png'
title = 'How I decide when a coding project is finished'
categories = ['Journal']
tags = ['Software Engineering', 'Testing', 'Student Project']
+++

I consider a coding project finished when its core functions work as expected, the planned supporting features work, and testing no longer reveals visible bugs that block normal use.

That definition begins with scope. I need a clear idea of what the project promised to do. New ideas will always appear during development, and adding every one of them can keep the finish line moving forever. I record useful extras separately instead of allowing them to delay the original goal.

## I test the expected paths first

I check the main workflows and the feature functions around them. Automated tests help confirm rules that should remain stable, while manual testing shows whether the application behaves sensibly from a user's perspective.

Passing tests increases my confidence, but tests only cover the cases I thought to write. I still look for visible errors, unclear messages, broken navigation, and data that ends up in the wrong state.

## Another person sees a different application

I also ask a friend who does not know the internal logic to try the project through black-box testing. They interact with the available inputs and outputs without knowing how I expected the code to work.

That distance is valuable. I may unconsciously follow the correct path because I designed it. A new user can reveal confusing labels, unexpected sequences, and assumptions that never appeared in my tests.

Finished does not mean the software has no possible improvement. It means the agreed purpose works, serious known problems have been addressed, and the project can be handed to someone without requiring an explanation at every step. At that point, I document the result and decide whether later ideas belong in another version. Completion gives me space to learn from the whole project and move to the next one.
