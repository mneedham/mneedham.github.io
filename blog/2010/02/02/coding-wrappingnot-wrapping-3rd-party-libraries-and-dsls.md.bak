+++
draft = false
date="2010-02-02 23:54:21"
title="Coding: Wrapping/not wrapping 3rd party libraries and DSLs"
tag=['coding']
category=['Coding']
+++

One of the things which Nat Pryce and Steve Freeman suggest in their book <a href="http://www.amazon.com/gp/product/0321503627?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321503627">Growing Object Oriented Software guided by tests</a> is the idea of wrapping any third party libraries that we use in our own code.

We came across a situation where we did this and then later on I made the mistake of not following this advice.

To start with my colleague <a href="http://ilovemartinfowler.com/">David</a> had created a DSL which kept all the calls to Selenium nicely wrapped inside one class.

The problem we were experiencing was that we hadn't evolved the DSL with the webpage evolution to the point where we weren't taking into account that some fields on the page weren't visible until ones before them had been filled in.

We needed to change the DSL slightly and it seemed like an interesting opportunity to try and convert them to use Webdriver as it seems more suited for heavy filling in of forms which is our use case.

My first thought was that it should just be possible to change those Selenium calls to call the equivalent Webdriver methods instead but having done that we realised that the way the two tools interact with the page is slightly different so the direct replacement approach wasn't really working. 

We decided to adopt a different approach whereby we would just try and change individual tests to use Webdriver instead and leave all the other tests as they are using Selenium.

I thought about creating another version of the DSL to encapsulate the Webdriver interaction with the page but decided against the idea as it didn't seem like it would add much value and the only way I thought of at the time was to create a clone of the original DSL.

We managed to get one of our tests working more effectively using Webdriver having sorted out the problems with the different interactions between fields but unfortunately the current C# API doesn't seem that stable and seems to fail somewhat randomly for reasons we haven't been able to work out yet.

As a result we now want to convert those tests I'd rewritten to take advantage of the new way they're written but to use Selenium instead!

Sadly the approach I took has made this really difficult and it's now a very frustrating journey to get the tests back into shape.

It's quite frustrating to make this type of mistake especially when I read about a solution so recently.

In hindsight I think a better approach may have been to pull our an interface to represent our DSL - currently it's a series of method calls on a few classes - and then create Webdriver and Selenium specific versions of that. 

A few of things stand out for me from this experience:

<ul>
<li>I talked myself out of wrapping Webdriver because I saw the main reason for doing so being to shield us in case we chose to change the library and I didn't anticipate having to do that. As it is I was wrong but I didn't totally appreciate how we can benefit from defining an API that defines how we want to interact with the web page rather than how the library wants us to.</li>
<li>We need to evolve our DSLs with the application and not be afraid to change them if the application changes.</li>
<li>It probably wasn't a good idea to try and fix the DSL and change the underlying library at the same time. Small steps!</li>
</ul>
