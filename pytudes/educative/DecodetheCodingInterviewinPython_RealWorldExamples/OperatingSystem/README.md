# Operating System
## Introduction #
A modern Operating System (OS) is a complex piece of software. It must manage finite, yet complex hardware resources while efficiently providing services to user software. In terms of hardware management, the OS must handle management of processing, storage and input/output resources. Another important part of the OS is user shell, which handles user interactions.

The scenario and problems we will discuss in this chapter relate to the memory and process manager modules of operating system software.

## Statement #
Suppose you are a developer on a famous OS engineering team, and the team. Your team is working on several features related to scheduling of processes as well as efficient allocation of memory to processes. Another module that you are working on deals with efficient encoding of files on disk.

## Features #
To implement the above-mentioned functionalities, we will need to introduce the following features:

- Feature #1: First, we need to determine the number of possible ways one or more running processes with contiguous memory allocation can be preempted to free up memory for a new process.

- Feature #2: Second, we need to locate the nth process to resume from a list of process IDs that are currently in memory.

- Feature #3: Order the processes in such a way that whenever a process is scheduled, all of its dependencies are already met.

- Feature #4: Deploy a compression strategy to identify and isolate all concatenated words.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into the operating system.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
