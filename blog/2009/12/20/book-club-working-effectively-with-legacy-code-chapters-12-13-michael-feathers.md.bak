+++
draft = false
date="2009-12-20 03:52:12"
title="Book Club: Working Effectively With Legacy Code - Chapters 12 & 13 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In the last Sydney book club that I attended before I moved back to the UK we discussed Chapters 12 and 13 of Michael Feathers' '<a href="http://www.amazon.com/gp/product/0131177052?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0131177052">Working Effectively With Legacy Code</a>'

<a href="http://lizdouglass.wordpress.com">Liz</a> has taken over the <a href="http://lizdouglass.wordpress.com/2009/12/10/book-club-working-effectively-with-legacy-code-–-chapters-14-15-and-16-michael-feathers/">summarising of the book club</a> now that I'm not there so if you want to keep on reading about the book club Liz's blog is the place to go!

<h4>Chapter 12 - I Need to Make Many Changes in One Area. Do I Have to Break Dependencies for All the Class Involved?</h4>

One of the ideas suggested in this chapter is that <strong>when writing tests we should try and write these as close to the change point as possible</strong>. Ideally we want to write a test directly against the method that we're changing but sometimes that isn't possible.

In this case Feathers suggests writing a test at the closest interception point (place to detect effects) and then changing the code at the change point to ensure that the test fails as expected. Tony Pitluga describes this approach in more detail in <a href="http://tonypitluga.blogspot.com/2009/05/gain-confidence-before-you-refactor.html">his post about gaining confidence before refactoring</a>. 

When working out where we need to write our tests, Feathers suggests that we need to look for <strong>pinch points</strong> i.e. methods from which we can detect changes in other methods in a class.

Feathers has a nice analogy where he compares this approach to 'walking several steps into a forest and drawing a line, saying "I own all of this area".'

We can then work with the code in that area of the code base with some degree of safety until we've got the code into a better state at which point we might decide the pinch point tests are no longer needed.

<h4>Chapter 13 - I Need to Make a Change, but I Don't Know What Tests to Write</h4>

Feather suggests writing <a href="http://www.markhneedham.com/blog/2009/12/03/book-club-working-effectively-with-legacy-code-chapter-11-michael-feathers/">characterisation tests</a> - tests to document what the system currently does - for the parts of the code base that we're currently working on. 

This is the approach that <a href="http://intwoplacesatonce.com/">Dave</a> encouraged on the last project I worked on - trying to write tests for code that we're not currently working on is a bit risky since we're not really sure what the behaviour is supposed to be. In addition we don't get much benefit from them since we're not changing anything in that area.

Feathers also points out that we shouldn't try to fix any 'bugs' that we come across while writing these tests - we should instead raise them and see if anything needs to be done. I remember watching an Uncle Bob presentation where he described how he had 'fixed a bug' which actually broke all dependent systems which relied on the bug being there. This is the situation we're trying to avoid!

Another approach suggested if we're having difficulty testing a large chunk of code is to refactor it into smaller methods and then test directly against those instead. I think this works well as a short term approach until we can test more easily from elsewhere.
