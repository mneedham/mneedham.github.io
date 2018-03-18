+++
draft = false
date="2011-05-11 12:11:46"
title="XP 2011: J.B. Rainsberger - A Simple Approach to Modular Design"
tag=['xp2011']
category=['XP 2011']
+++

After finishing my own session at XP 2011 I attended the second half of <a href="http://twitter.com/#!/jbrains">J.B. Rainsberger's</a>  tutorial on  modular design.

For most of the time that I was there he drove out the design for a point of sale system in Java while showing how architectural patterns can emerge in the code just by focusing on <a href="http://www.jbrains.ca/permalink/the-four-elements-of-simple-design">improving names and removing duplication</a>.

The second half of the session was much more interesting to watch as this was when J.B. had set all the context with the code and we could start to see the points that he was trying to make.

These were some of the interesting bits that I picked up:

<ul>
<li>J.B. talked a lot about being able to <strong>detect smells in code both mechanically and intuitively</strong>. The latter comes from our general feel of code based on our experience while the former comes from following a set of rules/heuristics. He <a href="http://www.jbrains.ca/permalink/becoming-an-accomplished-software-designer">wrote about this earlier in the year</a>.

For example we might feel intuitively that our tests are unclear to read while mechanically we can see that there is duplication between our tests and code which is what's leading to the unclearness.</li>
<li>By removing duplication from the point of sales example code we ended up with the MVC pattern albeit with the responsibilities in the wrong place e.g. the model/controller both had some logic that would typically belong in the view.

I'm curious as to whether other types of code would naturally lead towards another architectural pattern without us noticing. 

It would make sense if they did seeing as patterns are typically extracted when people see a common way of solving a particular problem.</li>
<li>J.B. encouraged us to <strong>use long names to help us see problems in the code</strong>. For example naming something 'priceAsText' might help us see that we have <a href="http://jamesshore.com/Blog/PrimitiveObsession.html">primitive obsession</a> which we may or may not want to do something about.

It was interesting how using longer/more descriptive names made it easier to see which bits of code were similar to each other even though it wasn't initially obvious.</li>
<li>I hadn't heard of <strong>temporal duplication</strong> which was defined as 'unnecessarily repeating a step across the run time of a program'.

In the example code we were creating a map of bar code -> price every time we called the method to scan the bar code which was unnecessary - that map could be injected into the class and therefore only be created once.
<li>J.B. described his 3 values of software which he suggested he uses to explain why we need to keep our code in good shape:
<ol>
<li><em>Features</em> - lead to the customer making money in some shape or form</li>
<li><em>Design</em> - we want to try and keep the marginal cost of features low i.e. we want to build a code base where there is a similar cost no matter what feature we decided to implement next.</li>
<li><em>Feedback</em> - we want to get the customer to say "not what I meant" as soon as possible since they're bound to say it at some stage i.e. we want to reduce the cost of a wrong decision</li>
</ol>
</li>

He drew an exponential curve showing the cost of software if we only focus on features. It was interesting to note that if you finish the project early enough then it might not be such a big deal.</li>
</ul>

I think it's very easy to dismiss the important of naming in our code because it seems so trivial.

After this session I can now see that I should be spending much more time than I currently do on naming and have much room for improvement.
