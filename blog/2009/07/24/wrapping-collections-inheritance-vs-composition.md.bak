+++
draft = false
date="2009-07-24 01:07:23"
title="Wrapping collections: Inheritance vs Composition"
tag=['coding', 'collections']
category=['Coding']
+++

I wrote previously about the differences between <a href="http://www.markhneedham.com/blog/2009/02/23/c-wrapping-collections-vs-extension-methods/">wrapping collections and just creating extension methods</a> to make our use of collections in the code base more descriptive but I've noticed in code I've been reading recently that there appear to be two ways of wrapping the collection - using composition as I described previously but also extending the collection by using inheritance.

I was discussing this with <a href="http://luning12.blogbus.com/">Lu Ning</a> recently and he pointed out that if what we have is actually a collection then it might make more sense to extend the collection with a custom class whereas if the collection is just an implementation detail of some other domain concept then it would be better to use composition.

In the latter case we probably <strong>don't want to expose all of the methods available on the collection</strong> since we don't want to make it possible for clients of the object to perform all of these operations.

We have both of these approaches in our code base - in the case where we have used inheritance we are extending a 'SelectList' from the .NET API to be a 'PleaseSelectList' so that it will add the value 'please select' to the top of drop down lists that we create on our UI instructing the user to select an option.

In this case I think we really do have a 'SelectList' so I'm not too bothered that we're using inheritance instead of composition - in general though my preference is to use composition because I've found that most of the time we don't actually want to expose all the methods available on a collection API when we pass this data around our code.

For example a fairly common scenario might be that we load up a collection of values from a persistence mechanism and then maybe do some querying on them before displaying something to the user. 

I've noticed that it's quite rare that we would actually want to allow any clients of this code to have the ability to remove an item from this collection but this is one of the methods that would typically be exposed if we decided to pass around a 'List' which is often the case. 

Even if it's not the case we can still convert an 'IEnumerable' value into a 'List' and then do whatever we want to it unless the collection had been defined as being '<a href="http://msdn.microsoft.com/en-us/library/ms132474.aspx">read only</a>' in which case you now have an API which is potentially misleading.

I'm finding myself moving towards the opinion that it only makes sense to create a new type if we actually get some added value in terms of expressing the intent of our code more easily by doing so and a lot of the time it seems that the added value that comes by extending a collection so that we have our own named type doesn't seem to provide a lot of value. In addition, it can actually be quite painful later on if we decide we want to change the way we represent that data.

I think using the inheritance option is often the short term quickest choice since we can just make use of all the methods that already exist on the collection being extended instead of having to write code to delegate to those methods which is the case if we use composition.

It does seem to be a fine line between using inheritance for good and just using it because then you <a href="http://www.markhneedham.com/blog/2009/07/21/good-lazy-and-bad-lazy/">don't have to spend a lot of time thinking about the best solution to the problem you're trying to solve</a>.

Perhaps the choice between the way that we choose to do this comes down to <a href="http://haacked.com/archive/2007/12/11/favor-composition-over-inheritance-and-other-pithy-catch-phrases.aspx">analysing the trade offs between using composition and inheritance</a> as Phil Haack points out in a post he wrote a couple of years ago.
