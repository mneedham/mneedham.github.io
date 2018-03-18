+++
draft = false
date="2009-09-16 01:11:58"
title="Book Club: SOLID Principles (Uncle Bob Martin)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed Uncle Bob Martin's presentation to the <a href="http://www.ndc2009.no/en/">Norwegian Developers Conference</a> on '<a href="http://www.viddler.com/explore/RoyOsherove/videos/18/">SOLID Design</a>'.

These principles of object oriented design are also <a href="http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod">written up on Uncle Bob's website</a> and are also in his book '<a href="http://www.amazon.co.uk/Software-Development-Principles-Patterns-Practices/dp/0135974445/ref=sr_1_2?ie=UTF8&s=books&qid=1252963866&sr=8-2">Agile Principles, Patterns and Practices</a>'. 

I read most of the book a couple of years ago but I don't always remember all of the principles when I'm coding so it was good to revisit them again.

These are some of my thoughts and our discussion:

<ul>
<li>Something that we've noticed on the project I'm working on at the moment with respect to the single responsibility principle is that <strong>often classes start off adhering to this principle but as soon as changes come along that single responsibility is pretty much ruined</strong>. 

It often seems like a new piece of functionality fits quite nicely onto an existing object but then when we look back on it in retrospect it didn't really fit that well and then another bit of code that fits even less well is added and an object is carrying out 3 responsibilities before we know it.

One way to potentially get around this is to write the responsibility of a class at the top of the file so that hopefully people will read that before adding anything new.

In a recent coding dojo we were reading through some of the <a href="http://code.google.com/p/jetlang/source/browse/#svn/trunk/src/main/java/org/jetlang/channels">Jetlang</a> code and that approach is followed on a lot of the classes which has the added benefit of making the code easier to follow if you're new to the code base.</li>
<li>Uncle Bob talks quite a lot about ensuring that we <strong>design flexibility into the areas of the code that are likely to change</strong> so that if we do have to change the code then we can do so easily.

I've read this type of advice before but I'm never sure how exactly you know where those areas of change are likely to be unless you've worked on a similar system before. 

From what I've seen any code which relies on another system's data/representations needs to be designed in this way as we don't know when it is going to change and it might even change without much warning so we need to adapt to that situation fairly quickly.</li>
<li>He didn't mention the <strong>Interface Segregation Principle</strong> in this presentation but I find this one the most interesting, probably because I haven't seen it followed on any projects I've worked on yet and I'm intrigued as what a code base that followed it would be like to work on.

I like the idea of having role based interfaces although I imagine it would probably be quite easy to abuse this principle and end up with interfaces that are so finely grained that we lose the domain's meaning.</li>
<li>While I have no doubt that if we followed these principles all the time when coding our code base would probably be much cleaner, it feels to me that <strong>these principles are quite difficult to remember when you're coding</strong>. 

From what I've noticed we find it much easier to follow ideas like <a href="http://en.wikipedia.org/wiki/Don%27t_repeat_yourself">Don't Repeat Yourself</a>, perhaps because it's easier to see when we are breaking principles like this. 

In addition, most people tend to agree about what makes repetition of code but when it comes to something like the Single Responsibility Principle, for example, people seem to have different opinions of what a responsibility is which makes it difficult to get consensus.

I quite like the newspaper metaphor to writing code which Uncle Bob describes in <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Clean Code</a> and he elabroates on this further in a recent post about <a href="http://blog.objectmentor.com/articles/2009/09/11/one-thing-extract-till-you-drop">extracting method until you drop</a>. I find ideas like that easier to follow when coding.

My current thinking is that the principles are really good for when we're analysing code having taken a step back but when we're actually coding they're not necessarily always the first thing to come to mind, at least for me! 

Perhaps that's normal but I'm intrigued as to whether more experienced developers than me are able to keep these ideas in mind all the time?</li>
</ul>
