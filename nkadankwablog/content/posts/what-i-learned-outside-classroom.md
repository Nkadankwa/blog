+++
date = '2025-11-06T09:00:00+08:00'
image = '/images/movie-gala-editorial.png'
title = 'What I learned outside the classroom'
categories = ['Journal']
+++

## A project that made the lessons feel real

During a practical semester, I built a WeChat mini program called **The Movie Gala**. It was a movie hub where a user could search for films, view details, simulate rentals, leave a review, and see review locations on a map.

The project used the OMDb API for movie information. To keep the home screen manageable, the app showed results in groups of ten as the user scrolled. Searches combined the API base URL, key, and search term, then used the returned titles and posters in the interface.

## What the app taught me

The cart and purchase flow were deliberately simulated: purchases and reviews were stored locally, and a random outcome represented a successful or failed payment. The profile page brought purchases and reviews together, while the map showed saved cinemas and review markers.

The difficult parts were not the features I expected. Removing only the chosen item from the cart needed careful copying of the existing list. Map markers and the route polyline took repeated testing before they behaved properly.

## The lesson I am keeping

Classroom examples teach the building blocks. A project teaches where they bend, connect, and occasionally refuse to work exactly as expected. The Movie Gala made that difference visible, and that is why I remember it as more than an assignment.
