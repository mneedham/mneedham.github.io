+++
draft = false
date="2009-03-04 23:58:48"
title="Coding: Good Citizens"
tag=['coding']
category=['Coding']
+++

I was recently reading Brad Cross' recent post about creating objects which are <a href="http://bradfordcross.blogspot.com/2009/02/good-citizens.html">Good Citizens</a> in code and he certainly nails one aspect of this with regards to ensuring that our <strong>objects are in a usable state post construction</strong>.

<blockquote>
In OO design, an object is considered to be a good citizen if it is in a fully composed and usable state post-construction.  This means that once the constructor exits, the class is ready to use - without the need to call additional setters or init() methods. 
</blockquote>

This is the main reason I find the <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">C# object initializer syntax</a> such a nightmare - it gets blatantly abused and you end up with half constructed objects all around the code base and you're never sure where your next Null Object Exception is going to come from so you pepper the code with null checks to try and avoid them.

Apart from this though I think another important aspect of an object being a good citizen is that <strong>when it makes use of other objects it does so in the way that object would expect it to</strong>.

For example I wouldn't expect object A to call object B and pass in null as one of its parameters. When we're not on the edges of our <a href="http://domaindrivendesign.org/discussion/messageboardarchive/BoundedContext.html">bounded context</a> then I think it's reasonable for objects to trust each other and assume that they will call each other in a non-evil way.

In a brief discussion with <a href="http://twitter.com/davcamer">Dave</a> about this he suggested that we might have different expectations of what makes a good citizen <strong>depending on the context</strong> in which we are using them.

For example, in our production code a good citizen wouldn't try to break encapsulation of another object by using reflection - it should tell the object what to do rather than taking data our of it.

In test code though it may be perfectly acceptable for us to make use of reflection to check the state of an object after we have performed an operation on it.

Dan North and Aslak Hellesoy have written up <a href="http://docs.codehaus.org/display/PICO/Good+Citizen">a more stringent list of what makes a good citizen</a> on the Pico Container website - I agree with the majority of them although I'd question whether every object should have an equals method on it unless its' actually used and I'm still undecided about whether objects should fail on construction if passed bad data.

Either way, it's definitely good to consider these types of things when writing code.
