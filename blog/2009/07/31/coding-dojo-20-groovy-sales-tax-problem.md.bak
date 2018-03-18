+++
draft = false
date="2009-07-31 09:07:26"
title="Coding Dojo #20: Groovy Sales Tax Problem"
tag=['coding-dojo']
category=['Coding Dojo']
+++

Continuing with the Groovy theme, this week we worked on the ThoughtWorks code review tax problem which involved modeling different items that a customer could buy and the associated tax rules that different types of goods had.

<h3>The Format</h3>

We had 3 people this week so most of the time we had all 3 of us involved in driving the code, which was projected onto the television screen again, while rotating every 10 minutes or so. 

<h3>What We Learnt</h3>

<ul>
<li>Although we weren't intentionally following the ideas laid out in <a href="http://www.markhneedham.com/blog/2008/11/06/object-calisthenics-first-thoughts/">object calisthenics</a> we actually ended up with code which fairly closely followed those ideas. We had very small classes, didn't have any getter or setter methods and also <a href="http://www.markhneedham.com/blog/2009/07/24/wrapping-collections-inheritance-vs-composition/">wrapped the collection</a> (Basket) which we had in our code.</li>
<li>We ended up writing tests in classes which were quite context sensitive - normally when I write tests we would have one test class for each object under test but this time we created different classes depending on the way that we were making use of that object in the test. For example we ended up with 'BasketWithOneItem' and 'BasketWithMultipleItems' test classes by the end.

This seems pretty much like the <a href="http://www.code-magazine.com/article.aspx?quickid=0805061">Context-Spec</a> approach to testing that I've read about previously in <a href="http://code.google.com/p/specunit-net/">Scott Bellware's framework</a>. I'm noticing on the project I'm currently working on that our tests are drifting in that way almost naturally due to the different ways that objects are typically used.</li>
<li><a href="http://intwoplacesatonce.com/">Dave</a> took the lead in driving out a <a href="http://martinfowler.com/bliki/FluentInterface.html">fluent interface</a> which worked out quite well - we were able to chain together different items by including an 'and' method on objects which created a 'Basket' containing both items and then returned the Basket, therefore allowing us to add other items too. I was initially against this approach as I felt we should just create a basket with all the items that it held rather than adding them one at a time.

Objects needed to define an 'and' method and a 'totalCost' method in order for them to be chained. Due to the dynamic nature of Groovy we could just pass in objects and assume they would respond to the appropriate methods. 

We therefore ended up with code that looked a bit like this:


~~~groovy

new Book(12.49).and(new Chocolate(1.89)).totalCost()
~~~

If we were working in a static language then we would have needed to create a small interface with the two methods on and then have our objects implement that. This seemed to fit in quite nicely with the <a href="">Interface Segregation Principle</a> where the idea is to define thin cohesive interfaces which don't inadvertently couple their different clients together.

In a discussion with a few colleagues recently it seems that one way of looking at methods on objects in dynamic languages is that each method would be the equivalent in a static language of a one method interface which our object implements.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>I've found the dojos we've done using Groovy to be quite fun - everyone who participates has worked with Java so it doesn't seem to be too much of a jump to use Groovy. Writing less code to achieve the same goal is also nice. We may well continue with Groovy next time!</li>
</ul>
