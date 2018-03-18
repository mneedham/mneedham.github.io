+++
draft = false
date="2009-09-30 00:42:29"
title="Book Club: Design Sense (Michael Feathers)"
tag=['book-club']
category=['Book Club']
+++

In our latest technical book club we discussed a presentation given at the <a href="http://www.ndc2009.no/en/">Norwegian Developers Conference</a> by Michael Feathers titled '<a href="http://www.viddler.com/explore/RoyOsherove/videos/9/">Design Sense</a>'.

In this presentation he presents quite a number of different ideas that he has learned from his experiences in software development over the years.

These are some of my thoughts and our discussion:

<ul>
<li>The first part of the presentation talks about method size and Feathers observes that there seems to be a power law with relation to the size of methods in code bases - i.e. there are a lot of small methods and fewer large methods but there will always be some a very small number of massive methods.

<a href="http://intwoplacesatonce.com/">Dave</a> suggested that perhaps this is related to <a href="http://en.wikipedia.org/wiki/Benford%27s_law">Benford's Law</a> which describes exponential growth processes. 

I wonder whether this observation is somehow linked to the <strong>broken window theory </strong>whereby if a method is large then it is likley to increase in size since it probably already has some problems so it doesn't seem so bad to throw some more code into the method. With small methods this temptation might not exist.

From what I've noticed the messiest methods tend to be around the edges of the code base where we are integrating with other systems - in these cases there is usually a lot of mapping logic going on so perhaps the benefit of extracting small methods here is not as great as in other parts of the code base.</li>
<li>I really like the observation that <strong>protection mechanisms in languages are used to solve a social problem rather than a technical problem</strong>. 

For example if we don't want a certain class to be used by another team then we might ensure that it isn't accessible to them by ensuring it's not public or if we dont' want certain methods on a class to be called outside that class then we'd make those methods private.

I think this is a reasonable approach to take to protect us from although it was pointed out that in some languages, like Python, methods are publically accessible by default and the idea <a href="http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private">when using private methods is to make it difficult to access them from outside the class but not impossible</a>. I guess this is the same with most languages as you could use some sort of metaprogramming to gain access to whatever you want if needs be.

There's an interesting post on the Python mailing list which talks through <a href="http://groups.google.com/group/comp.lang.python/msg/b977ed1312e10b21.">some of the benefits of using languages which don't impose too much control over what you're trying to do</a>.</li>
<li>The observation that <strong>names are provisional</strong> is something that I've noticed quite a lot recently.

Feathers points out that we are often reluctant to change the names of classes even if the responsibility of that class has completely changed since it was originally created. 

I've noticed this a lot on projects I've worked on and I wonder if this happens because we become used to certain types being in the code and there would be a period of adjustment for everyone in the team while getting used to the new names - it might also ruin the mental models that people have of the system.

Having said that I think it's better to have names which describe what that class is actually doing now rather than keeping an old name which is no longer relevant.</li>
<li>I quite like the idea that the <strong>physical architecture of a system can shape the logical architecture</strong> and that often we end up with a technological solution looking for a problem.

I'm not sure if it's completely related but one way that this might happen is that in an environment where <a href="http://dahliabock.wordpress.com/2009/08/06/why-i-think-layer-teams-are-a-bad-idea/">we structure a team in layers</a> it's possible that certain functionality will end up being implemented by the team that can turn it around the quickest rather than being implemented in the layer where it might best logically belong.

He also mentions <a href="http://en.wikipedia.org/wiki/Conway%27s_Law">Conway's law</a> which suggests "...organizations which design systems ... are constrained to produce designs which are copies of the communication structures of these organizations." - that seems to link in quite closely with the above ideas.
</li>
<li>Amongst the other ideas suggested I quite liked the idea that <strong>requirements are just design decisions</strong> but that they are product design decisions rather than technical design decisions. 

I like this as it opens up the idea that requirements aren't set in stone and that we can work with them to come up with solutions that actually solve business problems instead of 'design by laundry list' as Feathers coins it.

I think his recent post about the <a href="http://michaelfeathers.typepad.com/michael_feathers_blog/2009/09/thoughts-on-the-future-of-the-boutique-software-shop.html">boutique software shop</a> explains these ideas in more detail.</li>
</ul>

There's a lot of other ideas in this talk as well but these are some of the ones that made me think the most.
