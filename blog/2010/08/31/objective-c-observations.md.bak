+++
draft = false
date="2010-08-31 18:27:10"
title="Objective C: Observations"
tag=['objective-c-2']
category=['Objective C']
+++

I've been playing around with Objective C over the last month or so and  although my knowledge of the language is still very much limited I thought it'd be interesting to describe some of the things about the language that I think are quite interesting and others that keep catching me out.

<h3>Protocols</h3>

I touched on protocols a bit in <a href="http://www.markhneedham.com/blog/2010/08/04/objective-c-parsing-an-xml-file/">my first post</a> but they seem like an interesting middle ground between interfaces and duck typing.

I like the fact that protocols can define optional methods so that if we're not interested in some parts of the protocol we can just ignore those parts.

From the <a href="http://developer.apple.com/iphone/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocProtocols.html#//apple_ref/doc/uid/TP30001163-CH15">documentation page</a>:
<blockquote>
Protocols free method declarations from dependency on the class hierarchy, so they can be used in ways that classes and categories cannot. Protocols list methods that are (or may be) implemented somewhere, but the identity of the class that implements them is not of interest. What is of interest is whether or not a particular class conforms to the protocol
</blockquote>

<h3>Smalltalkish style method names</h3>

We <a href="http://www.markhneedham.com/blog/2009/05/21/coding-dojo-15-smalltalk/">played with Smalltalk in a coding dojo a bit last year</a> and the first thing that I noticed with Objective C is that the method names are very similar to those in Smalltalk. 

I think this influences the way that we define the method name and its parameters as you try and define those in such a way that when you call the method it will read better.

For example I created the following method:


~~~objc

UILabel *aLabel	= [self createLabelFrom:project withXCoordinate:x withYCoordinate:y];	
~~~

If I didn't have to name the parameters when calling the method I doubt I would have used such descriptive names. I would have just used 'x' and 'y' as the names!

<h3>All methods are public/Defining methods in header files</h3>

As I understand it all the methods defined on an object are available to any other object to call i.e. all the methods are public

I've read about others using <a href="http://developer.apple.com/iphone/library/documentation/cocoa/conceptual/objectivec/Articles/ocCategories.html">categories</a> to simulate the idea of having non public methods but I haven't tried anything myself yet.

Interestingly we get a compiler warning when trying to call methods on an object if those methods haven't been defined in the appropriate header file although the code still seems to execute fine at run time.

<h3>Messages not method calls</h3>

One other thing that I sometimes forget is that we're dealing with messages rather than method calls.

We still need to send the message to 'self' even if it's a message being sent to another method on the same object.
