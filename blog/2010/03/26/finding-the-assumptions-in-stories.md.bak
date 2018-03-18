+++
draft = false
date="2010-03-26 01:14:15"
title="Finding the assumptions in stories"
tag=['agile', 'stories']
category=['Agile']
+++

My colleague J.K. has written <a href="http://jkwerner2.wordpress.com/2010/03/23/so-that-so-what/">an interesting blog post where he describes a slightly different approach that he's been taking to writing stories</a> to help move the business value in a story towards the beginning of the description and avoid detailing a solution in the 'I want' section of the story.

To summarise, J.K.'s current approach involves moving from the traditional story format of:


~~~text

As I...
I want.. 
So that...
~~~

To the following:


~~~text

As I... 
I want..
By...
~~~

I quite like this idea and I've noticed that even without using this story format technical solutions are sometimes described as the business requirement and we need to look beyond the 'I want' section of the story card to find the real value and locate assumptions which have led to the story being written in that way.

To give a recent example, a colleague and I picked up the following story:


~~~text

As the business
I want a HTTP module to be included on the old site
So that I can redirect a small percentage of traffic to the new site
~~~

We assumed that other options for redirecting traffic must have already been analysed and written off in order for this to be the suggested solution so we initially started looking at how to implement it.

After a bit of investigation it became clear that this was going to be quite an invasive solution to the problem and would involve re-testing of the whole old site (since we would be making a change there) before it could be put into production. That would take 2 weeks.

Speaking with <a href="http://www.the-arm.com/">Toni</a> and <a href="http://twitter.com/a5hok">Ashok</a> about the problem it became clear that it should be possible to  control whether traffic was going to the old or new site by changing the configuration in our load balancer, <a href="http://www.citrix.com/English/ps2/products/product.asp?contentID=21679">Netscaler</a>.

Discussing this further we found out that this had been tried previously and hadn't quite worked out as expected which was why it hadn't been considered as an option.

We spent some time talking through using Netscaler with the network team and agreed to try it out on a performance environment and see whether it would balance traffic in the way that we wanted which it did.

We still need to make sure that it works as expected in production but it was an interesting example of how solutions can be excluded based on prior experience even though they might still be useful to us.

I'll certainly be more aware of noticing when a story details a solution and try and look for the actual requirement after this experience.
