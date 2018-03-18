+++
draft = false
date="2009-04-19 23:03:01"
title="Coding: Applying levels of abstraction"
tag=['coding', 'software-development']
category=['Coding']
+++

One interesting situation that we often arrive at when writing code is working out when the best time to apply a level of abstraction is.

I think there is always a <a href="http://www.markhneedham.com/blog/2009/03/02/trade-offs-some-thoughts/">trade off</a> to be made when it comes to creating abstractions - creating the abstraction adds to the complexity of the code we're writing but it is often the case that creating it makes it easier for us to navigate the code base.

The trick then seems to be working out when the benefits we get from making that abstraction outweigh the complexity/indirection that we create in the code. Of course if we can name the abstraction in an <a href="http://www.markhneedham.com/blog/2009/03/18/coding-make-it-obvious/">obvious</a> way that it need not be the case that we over complicate the code that much. 

If we apply a pattern or abstraction effectively then we would hope that the code becomes <strong>more expressive and readable</strong>.

A recent situation where I was confronted with this decision was in a bit of code being used to render the view model for one of our pages.

The code started out quite simple and there was originally just one path that we would go down when creating that model.

Soon though there became a second path where the data being rendered differed slightly if there was a logged in user.

It felt like there was a need to try and abstract this into a Model Renderer or something similar but it felt like I would be over engineering the solution if I went for this approach. Possible case of <a href="http://en.wikipedia.org/wiki/You_Ain%27t_Gonna_Need_It">YAGNI</a> linked to <a href="http://www.cuberick.com/2007/11/down-with-if.html">my dislike of having to write if statements in the code</a>!

Anyway I didn't apply the abstraction and now unfortunately that code has ended up having 5 different paths and it's quite tricky to refactor since the logic is spread all over the place.

Although I felt the decision I made at the time was reasonable I don't think it satisfied one of the ideas that I've picked up from speaking to <a href="http://dannorth.net/">Dan North</a> - that <strong>we should make it easy for people to do the right thing in the code</strong>. If I'd gone with the abstraction when I considered it then maybe the code would have taken a different and better direction.

One idea suggested to me recently by <a href="http://pilchardfriendly.wordpress.com/">Nick</a> about when to create the abstraction is based on the idea of what I think might be a myth of the <a href="http://en.wikipedia.org/wiki/Australian_Aboriginal_enumeration">aboriginal counting system</a> but nevertheless is quite useful here. 

The idea is that we only have three numbers '1', '2', and 'Many'. When we reach the stage where we have 'Many' branches in an if/else statement for example that might be a good time to create an abstraction to take care of that complexity.

I know there generally <a href="http://www.markhneedham.com/blog/2009/02/13/ferengi-programmer-and-the-dreyfus-model/">aren't rules that we can apply at all times in software development</a> but this seems a reasonable rule to keep in mind. Maybe it should also be the type of idea that goes together with the coding conventions that a team decides to follow.
