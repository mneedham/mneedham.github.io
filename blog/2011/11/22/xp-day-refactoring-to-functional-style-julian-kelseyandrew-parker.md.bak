+++
draft = false
date="2011-11-22 00:13:40"
title="XP Day: Refactoring to functional style (Julian Kelsey/Andrew Parker)"
tag=['xpday']
category=['XP Day']
+++

I'm attending <a href="http://xpday-london.editme.com/Monday-Schedule">XP Day</a> this year and the first talk I attended was one by <a href="http://twitter.com/scrawlings">Julian Kelsey</a> and <a href="http://twitter.com/#!/aparker42">Andrew Parker</a> titled 'Refactoring to functional style'.

I've worked on a Scala project for the last 6 months and previously given a <a href="http://www.markhneedham.com/blog/2010/01/31/ddd8-mixing-functional-and-object-oriented-approaches-to-programming-in-c/">couple</a> <a href="http://www.markhneedham.com/blog/2010/04/02/ldnug-mixing-functional-and-object-oriented-approaches-to-programming-in-c/">of talks</a> about adopting a functional style of programming in C# so this is a subject area that I find quite interesting.

The talk focused on 5 refactorings that the presenters have identified to help move imperative code to a more functional style:

<ul>
<li><strong>Isolate mutation</strong> - keeping mutation in one place rather than leaking it everywhere</li>
<li><strong>Isolate predicate</strong> - making it possible to filter collections</li>
<li><strong>Separate loops</strong> - iterating over collections more than once if we're doing more than one thing with the collection</li>
<li><strong>Decide on branches once</strong> - putting conditional logic into a map as functions</li>
<li><strong>Separate sequence of operations from execution of operations</strong> - composing functions and executing them at the end</li>
</ul>

Since they were coding in Java they made use of the <a href="http://code.google.com/p/guava-libraries/">Google Guava collections library</a> to make it easier to work with collections in a functional way.

As you might imagine some of the code ends up being quite verbose due to the inability to pass functions around in Java. 

I was reminded of a coding dojo we did a couple of years ago where we compared how <a href="http://www.markhneedham.com/blog/2009/09/04/coding-dojo-22-scala-lamdaj-project-euler/">code written using lambdaj would compare to Scala code</a>.

Despite the verbosity it was interesting to see that it's actually possible to achieve a similar style of programming to what you would expect in languages like Scala, F# and Clojure.

My former colleague <a href="http://twitter.com/#!/DanielBodart">Dan Bodart</a> has an alternative library for working with collections in Java called <a href="http://code.google.com/p/totallylazy/">totallylazy</a> which based on some of the <a href="http://code.google.com/p/totallylazy/source/browse/test/com/googlecode/totallylazy/lambda/LambdasTest.java?spec=svnef8d51c119ad4391dbe84e9daaa037d13c48d2ba&r=ef8d51c119ad4391dbe84e9daaa037d13c48d2ba">latest commits</a> looks quite neat.

One interesting thing the speakers suggested is that they are <strong>better able to see data dependencies</strong> in their code when chaining functions together which they wanted to apply to that data.

I hadn't really thought about the data dependencies before but I generally find code written using function composition to be easier to read than any other approach I've seen so far.

The main reason I picked up for why the authors thought we would want to adopt a functional approach to start with is the fact that it <strong>limits the number of things that we have to reason about</strong>. 

Interestingly <a href="http://twitter.com/#!/tirsen/status/137172172102832128">Jon Tirsen recently tweeted the following</a>:

<blockquote>
In my experience large purely functional codebases are very painful. Shared immutable, local mutable is the way to go.
</blockquote>

We've mostly kept our Scala code base immutable but it's not large by any measure (5,000 lines of production code so far) and probably not as complex as the domains Jon has worked with.

It's an interesting observation though...immutability is no silver bullet!
