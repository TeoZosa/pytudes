# Netflix
## Introduction #
Netflix is the biggest video streaming platform in the world, offering movies, seasons, biographies, reality shows, and more. Their video repository is growing significantly. So the engineering team at Netflix keeps trying to find better ways to display content to their consumers.

The scenario and the problems discussed in this chapter also relate to any content displaying functionality and how we can improve it.

## Statement #
Let’s pretend you’re a developer on the Netflix engineering team. You are working on improving the user experience in finding content to watch. This involves the improvement of the search as well as recommendation functionality.

## Features #
We will need to introduce the following features to implement the improvements discussed above:

- Feature # 1: We want to enable users to see relevant search results despite minor typos.

- Feature # 2: Enable the user to view the top-rated movies worldwide, given that we have movie rankings available separately for different geographic regions.

- Feature # 3: As part of a demographic study, we are interested in the median age of our viewers. We want to implement a functionality whereby the median age can be updated efficiently whenever a new user signs up for Netflix.

- Feature # 4: For efficiently distributing content to different geographic regions and for program recommendation to viewers, we want to determine titles that are gaining or losing popularity scores.

- Feature # 5: For the client application, we want to implement a cache with a replacement strategy that replaces the least recently watched title.

- Feature # 6: As an alternative to the above, we want to implement a strategy of replacing the least frequently watched titles in the cache.

- Feature # 7: During a user session, a user often “shops” around for a program to watch. During this session, we want to let them move back and forth in the history of programs they’ve just browsed. As a developer, you can smell a stack, right? But, we also want the user to be able to directly jump to the top-ranked program from the one’s they’ve browsed.

- Feature # 8: As you beta tested feature #7, a user complained that the next and previous functionality isn’t working correctly. Using their session history, we want to check if our implementation is correct or indeed buggy.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into Netflix’s system.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, we suggest that you think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
