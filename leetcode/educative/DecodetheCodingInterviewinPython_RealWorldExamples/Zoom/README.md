# Zoom
## Introduction #
Zoom is a widely popular video-conferencing application. In addition to personal use by individuals, it is also used by businesses around the world to manage remote work meetings, host virtual events, and more. Zoom allows meetings to be conducted using video-only, audio-only, or both, all while conducting live chats. Moreover, it lets you record sessions to view later.

The scenario and problems we will discuss in this chapter relate to Zoom’s participant management functionality and how to implement it.

## Statement #
Imagine you are working as a developer for Zoom. The team you are working for handles participant management.

First, you have to implement pagination for the meeting lobby’s “Gallery Mode,” which will display the participant names in alphabetical order. Next, you need to develop a serializer/deserializer that will serialize data before transmission through the network and deserialize it when it reaches the destination.

As teams navigate the unprecedented challenges of working from home, they regularly engage in remote fun team-building activities. At Zoom, you want to help out by integrating mini games into the application. As a pilot, you will start with one game.

## Features #
We will need to introduce the following features to implement the functionalities discussed above:

- Feature #1: Implement pagination for the display showing the names of participants present in a meeting.

- Feature #2: Participant data needs to be serialized from the server to the network and de-serialized at the client.

- Feature #3: Implement an algorithm to find the correct answer of minigame that prompts the user to find the minimum number of steps taken to reach from one point to another.

The coming lessons will discuss these features and their implementation in detail. The solutions to these basic problems are also applicable to many other common coding interview questions.
