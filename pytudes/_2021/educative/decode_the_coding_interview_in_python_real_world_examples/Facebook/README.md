# Facebook
## Introduction #
Facebook is the biggest social media company in the world. The company also owns other social media platforms like Instagram as well, and the engineering team at Facebook keeps trying to find better ways to connect people among all their platforms. This allows users to share and view content by their connections throughout all the platforms.

The scenario and the problems discussed in this chapter relate to Facebook’s content sharing and viewing functionality across different platforms and how we can improve them.

## Statement #
Let’s say you are a developer on the Facebook engineering team. Your team needs to improve the integration among the sister platforms. An important concern in this integration is achieving operational efficiency through not only efficient code, but also API rate limiters and elimination of similar requests by the same user on different platforms. Your team has also been requested to take this opportunity to implement features to detect potentially objectionable content.

## Features #
We will need to introduce the following features to implement the functionalities we discussed above:

- Feature #1: Find all the people on Facebook that are in a user’s friend circle.

- Feature #2: We want all the user’s friends on Facebook to be suggested on Instagram as well. Since Instagram is a different platform, all of its connections need to be copied to a separate database.

- Feature #3: Sync the Facebook stories list with Instagram.

- Feature #4: Limit the request rate from users. The same request cannot be sent from the other platform until a specified amount of time has elapsed since the request from the first platform.

- Feature #5: Identify the morphed versions of abused and profane words so posts containing them can be flagged inappropriate.

- Feature #6: Group the similar gibberish posts together so a decoding pattern can be observed.

- Feature #7: Mining for patterns in posts by a user needs to be done on a high-performance cluster. You need to suggest an optimal assignment of posts to cluster nodes so that their processing power is optimally utilized.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into Facebook’s system.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, we suggest that you think about how you would implement these features. You may realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
