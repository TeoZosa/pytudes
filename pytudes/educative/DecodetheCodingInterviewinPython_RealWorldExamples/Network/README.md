# Network
## Introduction #
A Network is an interconnection of computers, routers, or switches spanning a geographic area. The devices in a network communicate with each other through different protocols. Corporations typically use LAN to set up private networks for their employees. It can be used to simultaneously send data and messages to all devices available in the network. Most often, a network is connected to the global Internet so that devices on the same network can access resources on the Internet, too.

The scenario and the problems we will discuss in this chapter relate to data propagation in a network and how we can improve it.

## Statement #
You work for a company that develops devices for LANs, high-performance compute clusters and overlay networks. Your team develops software for features in these devices, efficient communication protocols as well as analytics on network data. These devices enable efficient scientific as well as enterprise networks.

## Features #
We will need to introduce the following features to implement the functionalities we discussed above:

- Feature #1: A message is transmitted from the server to the clients. Given the delays for each hop in the network, we want to determine the earliest time at which the message will be received by all the clients, assuming there are no errors along the way.

- Feature #2: Given that a specific Time-to-live (TTL) has been set in a message, find all the nodes on the network where the packet can travel from the current device.

- Feature #3: Each router in a linear virtual network topology can send a packet a certain maximum hops forward. We need to determine the minimum number of transmissions required to get a packet from the first router to the last.

- Feature #4: Disseminate an important packet to the maximum number of routers in a grid topology, subject to certain forwarding constraints.

- Feature #5: Efficiently update the VLAN IDs of network switches in a grid topology.

- Feature #6: A pair of machines have a request-response message exchange. Identify if the request and response packets used the same path.

- Feature #7: Distribute files over a network to high-performance cluster nodes to minimize communication overhead.

- Feature #8: Identify the most out of sync routers in a network topology.

- Feature #9: Determine the time for an update request to propagate through all routers in a grid topology.

- Feature #10: Determine the longest stretch of days for which a customer’s traffic variation was within a specified threshold.

Understanding these feature requests and designing their solutions will help us implement the requested functionality into the network.

In the next few lessons, we’ll discuss the recommended implementations of these features. Before we start, think about how you would implement these features. As you do, you’ll realize some of the underlying problems that you’ll need to solve. The solutions to these basic problems are also applicable to other common coding interview questions.
