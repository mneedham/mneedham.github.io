+++
draft = false
date="2009-01-17 16:02:33"
title="The danger of commenting out code"
tag=['coding']
category=['Coding']
+++

An idea which is considered common sense by most developers but which is not always adhered to is that of not commenting out code.

Code is nearly always under source control anyway so commenting out code which is not being used doesn't really serve any positive purpose and it can have quite a few negative effects.

<h3>Clutter</h3>

Ideally we should be able to read through the code without too much confusion - each method's name being descriptive enough that we can work out what is going on.

Having commented out code stops the flow of your eyes as you go down the code - <strong>there is a distraction</strong> and you want to know what it is. 

Even more time is then wasted trying to work out why the code was commented out and whether it might still be useful or not.

<h3>Misleading</h3>
Unless we trawl through the source control history it is difficult to know when and why a piece of code was commented out. 

Sometimes when we discover a bug in our code we eventually end up debugging an area of the code which has some code commented out. 

If that bug didn't previously exist then the natural thought is that perhaps commenting out that code is what caused the bug to appear. Clearly that is not always the case!

I have debugged code before which had parts commented out where uncommenting the code actually made the situation even worse. 

Leaving uncommented code in seems fairly harmless but <strong>it can waste quite a bit of time if someone misunderstands why it was commented out</strong> in the first place.

<h3>Broken Window Theory</h3>
The <a href="http://www.codinghorror.com/blog/archives/000052.html">Broken Window Theory</a> proposes the idea that if we do one bad thing in our code (i.e. break a window) then it becomes more likely that the next person who encounters that code will do something bad as well eventually leading to the <strong>degeneration of the code</strong>.

This is the same when commenting out code - if people see that there is code commented out then it becomes more acceptable for them to also comment out code and before you know it there are large chunks of code commented out and noone really knows why.

<h3>So is commenting ever ok...</h3>
I think commenting in the sense I describe here only really makes sense in the short term i.e. commenting out some code to see whether it is actually needed or not, running the tests, and then deleting it permanently if necessary.

If our aim is to produce expressive and easy to understand code then removing code when it is no longer needed can go a long way to helping us achieve this.
