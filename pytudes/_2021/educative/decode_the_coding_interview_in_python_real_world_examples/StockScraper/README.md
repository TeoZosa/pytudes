# Stock Scraper
## Introduction #
Extracting data from a website is known as scraping. The main component of scraping is fetching data from the HTML DOM structure after receiving a response from the website. You can think of web scraping as a spider crawling over every corner of an HTML structure and retrieving information of interest.

The scenario and problems we will discuss in this chapter relate to scraping stock data from websites.

## Statement #
You are a developer on a trading company’s engineering team. The company wants you to build a program that will dynamically scrape stock data from different websites, and then perform a profit analysis on the extracted data.

Since websites are represented as a DOM tree of HTML tags, we’ll first have to find a way to traverse this structure. Identifying stock data in an arbitrary HTML will be challenging because every website has a different structure and stock price data can be anywhere on the page.

## Features #
We will need to introduce the following features to implement the functionalities discussed above:

- Feature #1: Develop a way to parse the DOM tree structure of different stock websites.

- Feature #2: Assign a confidence score to each HTML tag in the DOM to represent the likelihood that the tag contains stock price data. Then, filter the minimal subtree of the DOM that has stock price data.

- Feature #3: Stock price data at the same level of the DOM tree is closely related. Develop a new way to efficiently parse the DOM tree structure by introducing a next pointer in each tree node, pointing to the next node in the same level.

- Feature #4: Retrieve the stock increase and decrease percentages from the DOM tree and calculate the maximum profit we could obtain from it.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into the scraper.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
