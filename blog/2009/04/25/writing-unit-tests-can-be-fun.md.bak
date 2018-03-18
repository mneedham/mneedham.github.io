+++
draft = false
date="2009-04-25 19:51:10"
title="Writing unit tests can be fun"
tag=['testing', 'unit-test']
category=['Testing']
+++

I recently came across <a href="http://blog.brodzinski.com/">Pavel Brodzinski's blog</a> and while browsing through some of his most recent posts I came across one discussing <a href="http://blog.brodzinski.com/2009/04/when-unit-testing-doesnt-work.html">when unit testing doesn't work</a>.

The majority of what Pavel says I've seen happen before on projects I've worked on but I disagree with his suggestion that writing unit tests is boring:

<blockquote>
6. Writing unit tests is boring. That’s not amusing or challenging algorithmic problem. That’s not cool hacking trick which you can show off with in front of your geeky friends. That’s not a new technology which gets a lot of buzz. It’s boring. People don’t like boring things. People tend to skip them.
</blockquote

I think it depends on the way that the unit tests are being written.

When I first started working at ThoughtWorks I used to think that writing tests was boring and that it was much more fun writing production code. A couple of years have gone by since then and I think I actually get more enjoyment out of writing tests these days.

There are some things we've done on teams I've worked on which contribute to my enjoyment when writing unit tests:

<h3>Small steps</h3>
While working on a <a href="http://www.markhneedham.com/blog/2009/04/23/ddd-making-implicit-concepts-explicit/">little application to parse some log files</a> last week I had to implement an algorithm to find the the closing tag of an xml element in a stream of text.

I had a bit of an idea of how to do that but coming up with little examples to drive out the algorithm helped me a lot as I find it very difficult to keep large problems in my head.

The key with following the small steps approach is to <a href="http://www.markhneedham.com/blog/2008/12/09/tdd-one-test-at-a-time/">only writing one test at a time</a> as that helps keep you focused on just that one use of this class which I find much easier than considering all the cases at the same time.

The feeling of progress all the time, however small, contributes to my enjoyment of using this approach.

<h3>Test first</h3>
I think a lot of the enjoyment comes from writing unit tests before writing code, TDD style.

The process of moving up and down the code as we discover different objects that should be created and different places where functionality should be written means that writing our tests/examples first is a <a href="http://www.markhneedham.com/blog/2008/12/22/testing-first-vs-testing-last/">much more enjoyable process</a> <a href="http://www.markhneedham.com/blog/2008/11/28/tdd-suffering-from-testing-last/">than writing them afterwards</a>.

The additional enjoyment in this process comes from the fact that we often discover scenarios of code use and problems that we probably wouldn't have come across if we hadn't driven our code that way.

<h3>Ping pong pairing</h3>
I think this is the most fun variation of <a href="http://www.markhneedham.com/blog/category/pair-programming/">pair programming</a> that I've experienced, the basic idea being that one person writes a test, the other writes the code and then the next test before the first person writes the code for that test.

I like it to become a bit of a game whereby when it's your turn to write the code you write just the minimal amount of code possible to make the test pass before driving out a proper implementation with the next test you write.

I think this makes the whole process much more light hearted than it can be otherwise.

<h3>In Summary</h3>
The underlying premise of what makes writing unit tests pretty much seems to be about driving our code through those unit tests and preferably while working with someone else.

Even if we choose not to unit test because we find it boring <a href="http://www.markhneedham.com/blog/2009/04/18/i-dont-have-time-not-to-test/">we're still going to test the code</a> whether or not we do it in an automated way!
