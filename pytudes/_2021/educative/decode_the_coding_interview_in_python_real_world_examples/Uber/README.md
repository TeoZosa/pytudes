# Uber
## Introduction #
Uber is the largest ride-hailing company in the world. They provide services like food and items delivery in addition to the primary service of passenger pick up and drop off. Their user base in terms of consumers and drivers is growing significantly. So, the engineering team at Uber keeps trying to find better ways to efficiently allocate nearby drivers to users.

The scenario and the problems discussed in this chapter discuss efficient driver allocation functionality and how we can improve it.

## Statement #
Imagine you are a developer on the Uber engineering team. The team is targeting some optimizations in driver allocation to rides as well as accessibility features for the client application. wants to optimize the process of driver allocation during rainy days. Whenever a user wants a ride, our system will first select the drivers closest to the user’s location. Then, it’ll plot a path from all the drivers’ locations to the user’s location and check whether it is possible for a driver to reach the pick-up location or not.

The map of a city is divided into several checkpoints, and there is a cost associated with the travel between each checkpoint. We’ll calculate the cost it’ll take for every driver to reach the user’s location through multiple checkpoints. The cost will depend on the amount of rainwater accumulated between checkpoints on each path. The driver having the least cost on their path will then get selected for the user. At the end of the ride, a fare will be calculated and we need to update the accessibility plugin to announce that fare aloud. Additionally, to facilitate new drivers we’ll provide them routes on which the probability and possibility of finding rides will be high. We’ll also tweak the rank system so drivers with low-rank also get a chance to become top-rated drivers.

## Features #
We need to introduce the following features to implement the functionalities we discussed above:

- Feature #1: Select at least the n nearest drivers within the user’s vicinity, avoiding the drivers that are too far away.

- Feature #2: Calculate the max depth of water along the way between two points in a rain-affected city.

- Feature #3: Find a path from each driver’s location to the user’s location and calculate the cost of travel so we can choose the driver with the least cost.

- Feature #4: Convert the calculated fare to English words for our system to recognize.

- Feature #5: Implement the pool functionality in which drivers can pick up multiple customers. On picking up a pool customer, we will suggest a route to the driver on which they may find more pool customers.

- Feature #6: Introduce the longest route of the city that will maximize the possibility of finding customers.

- Feature #7: Instead of always picking the top-ranked drivers, smartly pair drivers to customers so that high-ranked drivers are more likely, but others are also picked sometimes.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into Uber’s system.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, we suggest that you think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
