+++
draft = false
date="2009-02-26 23:43:20"
title="Coding: Using 'ToString'"
tag=['coding']
category=['Coding']
+++

An interesting conversation I've had recently with some of my colleagues is around the use of the ToString method available on all objects created in Java or C#. It was also pointed out in the <a href="http://www.markhneedham.com/blog/2009/02/25/c-wrapping-datetime/#comment-10930">comments on my recent post about wrapping DateTimes in our code</a>.

I think the original intention of this method was to create a string representation of an object, but its use has been overloaded by developers to the point where its expected use is as a mechanism for creating nice output when debugging the code or viewing unit test failures.

The nice thing about it in C# at least is that if you are using an object in your UI you can just put the object into the view and the ToString method will be implicitly called when the object needs to be rendered.

The problem with doing that is its implicitness - other developers might change the ToString method when debugging some code to give more useful output and the display logic of our application has now changed, potentially without us realising until a higher level functional test stops working.

The method name itself is not really that intention revealing anyway - what string format is it creating? A display string? A debugging string? It's not that clear.

The approach we are now taking is a bit more explicit and involves having a more explicit method on objects to achieve the same end result.

Method names such as 'ToDisplayFormat' or 'ToServiceFormat' help us to explain a bit more clearly what we are doing while still getting our object to render a different representation of itself.
