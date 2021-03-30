# Plagiarism Checker
## Introduction #
Plagiarism means presenting someone else’s work as your own. With the advent of the Internet, it has become very easy to plagiarize. A plagiarism checker application locates instances of similar content within someone’s work or documents. This application is widely used in the academic industry to catch plagiarism cases within student’s work.

The scenario and problems we will discuss in this chapter relate to the identifying similar content functionality and how we can improve it.

## Statement #
Assume you are a developer hired by an educational institute to improve their current plagiarism checker application. The institute wants you to add the ability to catch plagiarism between multiple students’ code snippets.

We will follow a new strategy where we convert code snippets into specific alphabetic tokens. These tokens can then be matched against each other to filter out what content and how much content is the same. Students can add dummy statements or comments between copied content to throw off the application. So, we need our application to be robust to this sort of modification. We also need to return the number of sources a given document may have been copied from and highlight the similar portions in two documents.

## Features #
We will need to introduce the following features to implement the functionalities discussed above:

- Feature #1: Match a student’s code with the rest of the class’s code samples to identify the number of possible matches.

- Feature #2: Match code samples of two students to identify which part has been copied and altered to avoid plagiarism detection.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into the plagiarism application. In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, we suggest that you think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
