# Amazon
## Introduction #
Amazon is the most widely used online store around the world. After their success in e-commerce, the company has now branched out into other technologies such as cloud computing, digital streaming, artificial intelligence, etc. However, most people still know Amazon for its online store because it connects customers to vendors across the globe. Through Amazon, customers can get better deals and a bigger variety of items as compared to buying from a brick and mortar store.

The scenario and the problems discussed in this chapter relate to Amazon’s online store and the exclusive deals that it offers its customers.

## Statement #
Consider you are a developer in Amazon’s online store team. Your team is working on several features related to product recommendations, promoting special deals and up-selling of items. In addition to these customer-facing features, you are also working on optimizations of delivery fleet management as well as integration with other e-commerce companies that Amazon acquired.

## Features #
We will need to introduce the following features to implement the functionalities we discussed above:

- Feature #1: All orders above a certain total amount are eligible for free delivery. If a customer’s total bill is near the free-shipping threshold, recommend items to add to cart to avail free delivery.

- Feature #2: Some customers have won a coupon worth $200 to buy up to three items. Suggest a bundle of three items to these lucky users.

- Feature #3: Up-sell a random product from a set of related products by recommending it to users at checkout.

- Feature #4: We are integrating data from a recently acquired e-commerce website. Create a deep copy of a list of products from the acquired company’s website so that it may be imported to Amazon.

- Feature #5: We want to showcase order-processing milestones on a dashboard. We need to mine daily stats to populate this dashboard.

- Feature #6: Show product recommendations with items that are frequently viewed together.

- Feature #7: Help the logistic division of the company to optimally utilize contractor delivery trucks.

- Feature #8: Merge product recommendations using the data from an acquired company.

- Feature #9: Allow a user to set a minimum and maximum price range filter to the list of products.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, we suggest that you think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
