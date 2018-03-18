+++
draft = false
date="2010-02-15 00:05:17"
title="F#: Passing an argument to a member constraint"
tag=['f']
category=['F#']
+++

I've written previously about <a href="http://www.markhneedham.com/blog/2009/04/28/f-overloading-functionspattern-matching/">function overloading in F# and my struggles working out how to do it</a> and last week I came across the concept of <a href="http://www.markhneedham.com/blog/2010/02/10/f-inline-functions-and-statically-resolved-type-parameters/">inline functions and statically resolved parameters</a> as a potential way to solve that problem.

I came across a problem where I thought I would be able to make use of this while playing around with some code parsing Xml today.

I had a 'descendants' function which I wanted to be applicable against 'XDocument' and 'XElement' so I originally just defined the functions separately forgetting that the compiler wouldn't allow me to do so as we would have a duplicate definition of the function:


~~~ocaml

let descendants name (xDocument:XDocument) = xDocument.Descendants name
let descendants name (xElement:XElement) = xElement.Descendants name
~~~

I wanted to make use of the inline function to define a function which would allow any type which supported the 'Descendants' member:


~~~ocaml

let inline descendants name (xml:^x) =  
    (^x : (member Descendants : XName -> seq<XElement>) (xml))
~~~

I couldn't work out how I could pass the 'name' input parameter to 'Descendants' so I was getting the following error:


~~~text

expected 2 expressions, got 1
~~~

I <a href="http://stackoverflow.com/questions/2260939/f-overloading-functions">posted the problem to StackOverflow</a> and 'Brian' pointed out the syntax that would allow me to do what I wanted:


~~~ocaml

let inline descendants name (xml:^x) =  
	(^x : (member Descendants : XName -> seq<XElement>) (xml,name))
~~~

Tomas Petricek pointed out that in this case we could just write a function which took in 'XContainer' since both the other two types derive from that anyway:


~~~ocaml

let descendants name (xml:XContainer) = xml.Descendants name
~~~

In this situation that certainly makes more sense but it's good to know how to write the version using member constraints for any future problems I come across.
