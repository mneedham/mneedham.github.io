+++
draft = false
date="2009-03-18 10:44:48"
title="Coding: Make it obvious"
tag=['coding']
category=['Coding']
+++

One of the lessons that I've learned the more projects I work on is that the most important thing to do when coding is to do so in a way that you make life easier for the next person who has to come across that code, be it yourself or one of your team mates.

I think the underlying idea is that we need to <strong>make things as obvious as possible</strong>.

<h3>Obvious naming</h3>

This one seems like it should be so easy and yet it's incredibly easy to get it wrong. 

In a <a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">presentation I watched by Dan Bergh-Johnsson</a> last week he talked about the need to name methods and classes in an obvious way because when a developer wants to implement some functionality they will spend a maximum of 30 seconds seeing whether it's been done before and if they don't find anything they'll do it themself.

I recently started reading through <a href="http://www.amazon.co.uk/Code-Complete-Practical-Handbook-Construction/dp/0735619670/ref=sr_1_1?ie=UTF8&s=books&qid=1237325786&sr=8-1">Code Complete</a> again having left it on the shelf for the last 3 years and there are some excellent ideas in the book about the best way to name things in our code.

Describing variables in terms of the problem domain instead of in terms of the technical solution i.e. describing the <strong>what not the how</strong> is one of the best pieces of advice from the chapter on variable naming.

Beyond that we need to know what the <strong>purpose of a variable is in a given context</strong> otherwise it can be very easy to choose a name that will make no sense to someone later on. 

For example I recently named a variable 'DefaultCustomerDetails' to indicate that if that variable was set then that meant the customer details should be defaulted and not be editable. I thought it made sense but when a colleague read it they had no idea what I meant by it - what we actually wanted to say was 'AreCustomerDetailsEditable' which is what I should have named it! The purpose on this occasion was to indicate whether to show a read only or editable version of the customer details section of the page.

<h3>Obvious use of patterns</h3>

This is one that was only recently pointed out to me by <a href="http://twitter.com/davcamer">Dave</a> when discussing the way I had implemented the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">builder pattern</a> in our code base.

I was trying to remove the need to call a 'Build' method by making use of <a href="http://www.markhneedham.com/blog/2009/02/22/c-implicit-operator/">C#'s implicit method</a> which I thought was a good idea to remove noise from the code, but as Dave pointed out wasn't what other people would expect when they came across the use of the pattern and therefore created confusion.

I'm not sure whether this means that we should <a href="http://www.markhneedham.com/blog/2008/08/16/naming-the-patterns-we-use-in-code/">name all of the patterns we use in code</a> but I think at least we should <strong>use them in a consistent way</strong> and pick the most obvious pattern for the job rather than choosing a solution that may be clever but less clear to other people.

Patterns are useful for helping to make our code more expressive and if we keep this idea in mind then I think it will guide us down the right path and not create a level of indirection in vain.

<h3>Obvious examples of API use</h3>

In terms of obviousness our test code is just as important as our production code.

Tests shouldn't have clutter in them and they should have just enough context needed to understand how the different objects in our system interact and the APIs available for each of them.

Making use of the builder or object mother to <strong>avoid polluting our tests with too much data</strong>, following a <strong>consistent pattern</strong> such as 'Act-Arrange-Assert' in the tests so people can quickly work out what's going on as well as <strong>naming tests accurately</strong> all help in this aspect.

<h3>In Summary</h3>
These are the main three areas where I've found being obvious can have the most benefit.

I'm sure there are others that I haven't thought of so feel free to let me know your favourite ways of writing code that others on your team can use with ease.
