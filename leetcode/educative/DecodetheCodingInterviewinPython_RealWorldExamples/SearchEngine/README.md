# Search Engine
## Introduction #
A search engine is a software that lets users search on the web. Search engines use a database of web pages that they collect using bots. The user’s query is run on the database, and the results are fetched. Some of the most commonly used search engines are Google, Bing, Baidu, Yahoo!, Duckduckgo, etc. All of these search engines contain complex, underlying algorithms for optimized searching and web page ranking for search results.

The scenarios and problems discussed in this chapter also relate to any search engine’s word searching, storage handling, and document fetching functionalities.

## Statement #
For this project, imagine you are developing a search engine at a new startup. This startup is experimenting with new and improved algorithms to carry out word searches in documents.

The first order of business is designing and implementing a system for efficient storage and retrieval of words from the index. The UI team is requesting an auto-complete functionality. Your users are familiar with the auto-complete functionality offered by currently popular search engines. This functionality suggests keywords as the user types the search string. It makes it faster and more convenient for a user to search the web. Moreover, your system should contain a module that checks if the query can be broken into multiple valid words, which is helpful in case the original query does not get any search results. In addition, we will also implement some features related to search ranking, result organization and optimization.

## Features #
We will need to introduce the following features to implement the functionalities we mentioned above:

- Feature #1: Design a system that can store and fetch words efficiently. This can be used to store web pages to make searching easier.

- Feature #2: Implement the auto-complete functionality to apply when the user is entering a query. For this feature, you will be recommending auto-completion using a set of popular, already-available queries.

- Feature #3: Check if white-spaces can be added to a query to create valid words in case the original query does not get any hits on the web.

- Feature #4: As an extension of the previous feature, find all the possible queries that can be created by adding white spaces to the original query.

- Feature #5: Calculate a search ranking factor based on the ranking score of pages that refer to it.

- Feature #6: Rearrange the search results such that results from the same website do not show up together.

- Feature #7: Search engine has many services that are chained or recursive. For optimization efforts, calculate the individual time taken by each service to run.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into the search engine’s system. The coming lessons will discuss these features and their implementations in detail so that you will be able to apply these solutions to different interview problems as well.
