+++
date = '2026-02-09T09:00:00+08:00'
image = '/images/java-spring-editorial.png'
title = 'My first steps with Java and Spring Boot'
categories = ['Journal']
tags = ['Java', 'Spring Boot', 'Learning']
+++

My first Spring Boot project was not ambitious. I wanted to make a small task manager: create a task, see the list, change its status, and remove it. The modest scope was useful because every new concept had somewhere visible to land.

## Moving from Java exercises to an application

Learning Java through classes, methods, and collections gave me individual building blocks. Spring Boot made me think about how those pieces cooperate when a request arrives from outside the program.

The first time I saw an endpoint return data, it felt almost too simple. An annotation marked a class, another marked a method, and the framework handled work I could not see. That convenience was exciting, but it also made me cautious. I did not want to finish with a project that worked only because I knew which annotations to copy.

I slowed down and traced the path: a request reaches a controller, the controller calls the application logic, and the data is returned as a response. Once I could describe that route in plain language, the generated folders and unfamiliar names felt less intimidating.

## What the task manager exposed

Even a small task needs decisions. Does it have an ID, title, description, status, and date? Which fields can change? What should happen if the requested task does not exist? Where does the list live after the application stops?

Keeping the first version in memory let me focus on the request-and-response flow, but it also made the limitation obvious: restarting the application erased everything. Adding persistence later would not be a decorative upgrade; it would change where the application’s truth lives.

Error handling was another lesson. The happy path is easy to demonstrate. A useful application must also respond clearly when input is missing or an ID is wrong. Thinking about those cases made the project feel more real than simply returning a successful response.

## What I want to build next

My next step is to connect the application to a database, validate input, and add tests around the behaviour I already understand. I want each addition to answer a problem I can explain instead of appearing because it is common in a tutorial.

Spring Boot has shown me how much structure a framework can provide. My goal is to keep looking beneath that structure until I know which work belongs to Java, which belongs to Spring, and which decisions still belong to me.
