+++
draft = false
date="2009-12-22 06:01:04"
title="One change at a time"
tag=['software-development']
category=['Software Development']
+++

I'm reading through Paul Butcher's '<a href="http://www.amazon.com/gp/product/193435628X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=193435628X">Debug It</a>' book and one of his suggestions when trying to diagnose a problem in our code is to <strong>only change one thing at a time</strong>. 

In a way this might seem fairly obvious but I've certainly fallen into the trap of making multiple changes at the same time in the misled belief that it'll lead to the problem being solved more quickly.

When making changes to code Butcher has the following piece of advice which I quite like:
<blockquote>
Once you see a change in behavior, undo whatever apparently caused it, and verify that the behavior retur ns to what it was before-hand. This is a very power ful indication that you’re looking at cause and effect rather than serendipity. 
</blockquote>

I noticed this while debugging my <a href="http://www.markhneedham.com/blog/2009/12/18/f-word-count-a-somewhat-failed-attempt/">F# word count application</a>. As I mentioned, <a href="http://www.markhneedham.com/blog/2009/12/20/f-word-count-using-a-dictionary/">I thought that the problem was that I was storing the text from all the files in memory</a> so instead of doing that I made that part of the application lazy so that the text would only be loaded when required.

When I first did this the program still didn't work but it failed later on than it had previously.

I thought that had shown where the problem was so I put the code back to how it was previously to check. 

To my surprise it still failed in the same place which meant that the change in how it executed had been coincidental rather than related to any code change I'd made.

I think this idea is more widely applicable though as I've noticed that  <a href="http://www.markhneedham.com/blog/2009/02/08/refactoring-comment-it-out-vs-small-steps-removal/">it works quite well when refactoring</a> as well. If we can be really certain about which changes work and which don't to a very fine grained level then we have more chance of successfully refactoring our code while ensuring that it still functions correctly.

The goal seems to be the same in both of these situations - take small steps and then get feedback quickly on how successful that small step was.
