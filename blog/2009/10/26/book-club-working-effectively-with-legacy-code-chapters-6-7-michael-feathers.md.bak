+++
draft = false
date="2009-10-26 23:10:45"
title="Book Club: Working Effectively With Legacy Code - Chapters 6 & 7 (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we covered chapters 6 & 7 - 'I Don't Have Much Time And I Have To Change It' and 'It Takes Forever To Make A Change' - of Michael Feathers' '<a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1255440556&sr=8-1">Working Effectively With Legacy 
Code</a>'.

The first chapter discusses various different techniques that we can use to add in new code to a legacy code base. These include:

<ul>
<li>Sprout method - create a new method for our new functionality and make a call to it from existing code.</li>
<li>Sprout class - create a new class for our new functionality and call to that class from existing code.</li>
<li>Wrap method - rename an existing method; create a new method with the old one's name; add in the new functionality in the new method & then delegate to the newly named existing method.</li>
<li>Wrap class - create a new class which takes in the old one in its constructor and then delegates to the original for most methods but also implements new functionality. Typically the <a href="http://en.wikipedia.org/wiki/Decorator_pattern">decorator pattern</a>.</li> 
</ul>

The second chapter discusses some common problems we may experience while trying to make changes.

These are some of my thoughts and our discussion of these chapters:

<ul>
<li>The thing that stood out for me in our discussion was the realisation that applying any of these techniques is probably going to <strong>make the code worse in the short term</strong> but hopefully lead us to a situation where we can make it better. If we use the 'sprout class' technique, for example, then we will end up with a new class which just does our new bit of functionality. Our <strong>code is therefore in an inconsistent state</strong>. 

I would actually prefer to leave the code in an inconsistent state if we are driving to a better solution although I have worked with colleagues who prefer to keep things consistent instead. I can certainly see why you might want to do this on a short running project where there may not be time to make all the changes that you'd like to.</li>
<li><a href="http://watchitlater.com/blog/">Tom</a> also pointed out that we need to remember that <strong>what we are doing is not design </strong> - that can come later on when the code is testable. Using these techniques is an alternative to rewriting the code which <a href="http://blog.objectmentor.com/articles/2009/01/09/the-big-redesign-in-the-sky">often doesn't work out as well as we'd hope</a>.</li>
<li>I quite liked the following observation:

<blockquote>
Typically, changes cluster in systems. If you are changing it today, chances are, you'll have a change close by pretty soon
</blockquote>
On the projects I've worked on there are often lots of areas in the code base that require refactoring but we tend to focus on the area that we're currently working on as that tends to give us the biggest pay back for the time spent.

Having said that I quite like <a href="http://fabiopereira.me/blog/2009/09/01/technical-debt-retrospective/">Fabio's idea of finding how various items of technical debt fall in terms of the pain they're causing and the effort it costs to fix them</a>. I wonder if the code we're working on now would be more likely to fall into the high 'pain' areas of that type of matrix.</li>
<li><a href="http://camswords.wordpress.com/">Cam</a> pointed out that with the sprout method and <a href="http://xunitpatterns.com/Sprout%20Class.html">sprout class</a> techniques it's quite cool that Feathers suggests driving their API by making a call to them the from existing method. That way we can see what values the new method will need to take in based on how it will actually be used.

While discussing this Alex pointed out something I hadn't quite grasped - the techniques described are useful for <strong>minimising the amount of change to the original method</strong> as well as making the new pieces of code easier to test.   

It's really easy to make mistakes when coding and when there is no safety net to save us we should look to avoid tinkering with that code too much until we've created one!</li>

</ul>
