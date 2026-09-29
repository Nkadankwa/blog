+++
date = '2025-10-20T09:00:00+08:00'
image = '/images/movie-gala-editorial.png'
title = 'A small win I almost overlooked'
categories = ['Journal']
tags = ['WeChat Mini Program', 'Student Project']
+++

During a practical semester, we were asked to build a WeChat mini program. I chose a movie app called **The Movie Gala**: a small movie hub where users could search for films, view details, simulate rentals, leave reviews, and see reviews represented on a map.

At the time, I was focused on getting the features to work. Only afterwards did I notice how much the project had asked me to combine.

## What I built

The app used the OMDb API to fetch movie information. To keep the home page manageable, I displayed the first ten search results and loaded the next group as the user reached the bottom of the list. A search combined the base URL, API key, and query, then used the returned title, poster, and other details in the interface.

I also created a simulated purchase flow. A user could add a film to a locally stored cart or start from the details page. At checkout, the app updated the purchase record, cleared the cart, and refreshed the interface. A random result represented whether a payment succeeded or failed, while an action sheet and modal made the process feel more realistic without pretending it was a real payment system.

The news page collected content from three RSS feeds, cleaned special-character codes, and opened the original articles in a web view. The profile page brought together purchased films and reviews. Stored titles were passed back through the API so the app could retrieve their current movie details.

## The difficult parts

The map and cart features taught me the most. Removing one item from the cart without affecting the others required creating a new list without that item. Reviews were saved with an ID so that selecting a map marker could open the relevant review and film. I also spent time getting markers and the route polyline to behave as expected.

## The win I nearly missed

My project was recommended for an award, although I did not receive it. At first, I almost treated that as the end of the story. Later, I realised that the recommendation itself mattered. A teacher who sees work from students with different strengths chose to put mine forward, and that is something worth acknowledging.

I celebrated in a small way. More importantly, I kept the reminder: a project does not need to win everything to show that I have grown. The Movie Gala made the lessons from class feel real, and that is a win I do not want to overlook.
