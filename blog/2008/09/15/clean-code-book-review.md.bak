+++
draft = false
date="2008-09-15 10:52:33"
title="Clean Code: Book Review"
tag=['object-mentor', 'clean-code', 'uncle-bob']
category=['Books']
+++

<h3>The Book</h3>
<a href="http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&s=books&qid=1221268338&sr=8-1">Clean Code</a> by <a href="http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&s=books&qid=1221268338&sr=8-1">Robert 'Uncle Bob' Martin</a>

<h3>The Review</h3>

I first heard of Uncle Bob a couple of years ago in a conversation with <a href="http://blog.obiefernandez.com/content/">Obie Fernandez</a> and having previously read his <a href="http://www.amazon.co.uk/Principles-Patterns-Practices-Robert-Martin/dp/0131857258/ref=sr_1_2?ie=UTF8&s=books&qid=1221410457&sr=8-2">Agile Principles, Patterns and Practices in C#</a> book, when my colleague <a href="http://blog.m.artins.net/">Alexandre Martins</a> came back from <a href="http://jaoo.com.au/sydney-2008/conference/">JAOO Sydney</a> raving about a talk on 'Clean Code' he'd seen I knew I had to buy this book when it came out.

In a good trend which I've noticed in a lot of Martin Fowler books, Uncle Bob lays out in the opening chapter how he thinks the book can best be read. Uncle Bob suggested that it was necessary to really immerse yourself in the code presented to get the most value from the book, I think I got a lot more from reading the book this way rather than just skim reading as I often tend to do.

<h4>What I learned</h4>
<ul>
<li>The best idea in this book for me was the <strong>newspaper metaphor</strong> that is mentioned with regards to formatting your code. This describes the idea of making code read like a newspaper article. We should be able to get a general idea of how it works near the top of the class before reading more and more details further down. This can be achieved by breaking the code out into lots of small methods. It was strange how involved I got with the newspaper metaphor. Having read about it early on I started looking at all code after that to be in that format and when it wasn't (when showing examples of not such clean code) I became disappointed.
</li>

<li>
<strong>Learning Tests</strong> - the idea of writing tests to gain understanding of how a 3rd party code works - was an idea I had not come across before. The idea here is to write simple tests which describe the way that you think a 3rd party library works for example. If a new version of the library is released we can rerun these to check that it still works the same way. Previously I have always written throwaway pieces of code to gain this understanding but writing tests that we can later refer back to is a much better way of achieving the same aim.
</li>

<li>
Treating the <strong>test code as being as important as the actual code</strong> was another idea that came across. Writing expressive tests is something that I am very interested in, and my colleague <a href="http://fragmental.tw/">Phillip Calcado</a> has written about the idea of <a href="http://fragmental.tw/2008/07/02/domain-driven-tests/">Domain Driven Tests</a>. Uncle Bob mentions a similar idea which he refers to as a Domain Specific Testing Language - a set of functions and utilities to help derive a testing API. The same ideas about keeping the tests expressive and clutter free apply. To end on a quote which is oh so true

<blockquote>If you let the tests rot, then the code will rot too</blockquote>
</li>

<li>
I came out with an improved understanding of how the <a href="http://en.wikipedia.org/wiki/Open/closed_principle">Open Closed Principle</a>, <a href="http://en.wikipedia.org/wiki/Single_responsibility_principle">Single Responsibility Principle</a> and <a href="http://www.dcmanges.com/blog/37">Law of Demeter</a> can be adhered to in a code base. The examples used in the book are very like code I have seen on projects so it was much easier to relate to. I found the context they were presented in in this book made them much easier to understand as it was part of a bigger picture of writing clean objects rather than just addressing the ideas in a standalone fashion.
</li>

<li>One of my favourite quotes from the book is the following
<blockquote>Master programmers think of systems as stories to be told rather than programs to be written</blockquote>
This almost requires a paradigm shift and makes it unacceptable to write code that isn't expressive. I am far from being a Master programmer but if I can write code that is easy for other people to understand then I feel I'm starting to get somewhere. 

I also found the following statement revealing as I was under the assumption that experienced developers wrote code like this first time

<blockquote>
When I write functions they come out long and complicated...then I massage and refine that code, splitting out functions, changing names and eliminating duplication...all the whole keeping the tests passing.
</blockquote>
</li>

<li>
I really liked the approach used in the case studies used in the last three chapters of the book. The code was presented, the problem with it identified, a solution proposed (and it's name referenced) and then the implementation was detailed. It reminded me of the approach taken in Joshua Kerievsky's <a href="http://www.industriallogic.com/xp/refactoring/">Refactoring to Patterns</a> in its <strong>pragmatic approach</strong> to aiding learning.

I found it useful to refer to Chapter 17 'Smells and Heuristics' when reading the case studies to check exactly what the smell/heuristic was describing. A reference (e.g. G30) is given in brackets after the paragraph which describes how to improve the code.
</li>

</ul>

<h3>In summary</h3>

This is the best book I've ever read about writing good code. On multiple occasions I found myself wishing I could be on the same team as Uncle Bob to watch him carry out code improvements for real.

The key ideas that stand out for me are keeping your code <strong>simple</strong> and <strong>expressive</strong> - the code should do pretty much what you'd expect it to do so that when you (or anyone else) come back to read this can be done quickly and easily.

I would recommend reading this book before reading Agile Principles, Patterns and Practices as I found the examples used in this book to explain OO principles much easier to follow. You can then go into more detail on the theory in the other book.

I read this book while I was on holiday and not really looking at any real code. I think reading the book while working on  a project would probably be even more valuable. I will certainly be referencing it frequently when I get back to the code.
