+++
draft = false
date="2009-06-02 23:35:31"
title="Coding: Putting code where people can find it"
tag=['coding', 'communication']
category=['Coding', 'Communication']
+++

I've previously written about the <a href="http://www.markhneedham.com/blog/2009/01/21/c-builder-pattern-still-useful-for-test-data/">builder pattern</a> which I think is a very useful pattern for helping to setup data.

It allows us to setup custom data when we care about a specific piece of data in a test or just use default values if we're not bothered about a piece of data but need it to be present for our test to execute successfully.

One problem that I noticed was that despite the fact we had builders for quite a number of the classes we were using in our tests, when new tests were being added test data was still being setup by directly using the classes instead of making use of the builders which had already done the hard work for you.

A colleague and I were pairing last week and I pointed out one of these areas and he suggested that we should try and introduce the builder pattern to try and solve it! 

We actually didn't have a builder for that particular piece of data yet but I pointed out several other builders we did have which he wasn't aware actually existed.

Clearly I hadn't done a very good job of communicating the existence of the builders but when discussing this we realised that the turn around time for checking whether or not a builder existed was actually not very quick at all.

<ul>
<li>Start writing test and realise that test data setup was a bit complicated</li>
<li>At best search for 'ClassNameBuilder' if you knew that was the naming convention for these builders</li>
<li>Create test data for the test by typing 'new ClassNameBuilder()...'</li>
</ul>

We therefore came up with the idea of anchoring the builders to a common class which we called 'GetBuilderFor'. 

It is now possible to create test data by writing code like this:


~~~csharp

var car = GetBuilderFor.Car().Year("2009").Make("Audi").Build();
~~~

The nice thing about this is that we now only have to type in 'GetBuilderFor' and then a '.' and ReSharper will show us all the builders that are available to us. If there isn't one then we can create it.

Communication wise we've both been mentioning this approach in our stand ups and to other people when we pair with them and hopefully this approach will stop the duplication of test data creation.

For those in the Java world <a href="http://blog.jayfields.com/2009/01/most-java-unit-tests-consist-of-class.html">Jay Fields wrote a cool post a few months ago where he describes a way to do a similar thing in Java</a>. I think this is one place where having static imports makes the code read really fluently.
