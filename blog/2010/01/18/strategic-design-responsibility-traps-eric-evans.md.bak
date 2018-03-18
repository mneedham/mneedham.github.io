+++
draft = false
date="2010-01-18 22:52:15"
title="Strategic Design (Responsibility Traps) - Eric Evans"
tag=['domain-driven-design', 'strategic-design']
category=['Software Development']
+++

Reading through some of Simon Harris' blog entries I came across <a href="http://www.harukizaemon.com/2009/10/responsibility-traps.html">his thoughts</a> on a presentation Eric Evans did at QCon titled '<a href="http://www.infoq.com/presentations/design-strategic-eric-evans">Strategic Design - Responsibility Traps</a>' which seems to cover a lot of the ground from the second half of <a href="http://domaindrivendesign.org/">Domain Driven Design</a> and more.

In the presentation Evans make some really insightful comments and points out a lot of mistakes that I've made on projects. It certainly serves as a reminder to go back and read part 4 of the book again and really understand the material from that section.

These were the most interesting observations for me:

<ul>
<li>In this talk he makes some similar points to those that he made in his '<a href="http://www.markhneedham.com/blog/2009/03/13/qcon-london-2009-what-ive-learned-about-ddd-since-the-book-eric-evans/">What I've learned about DDD since the book</a>' presentation that I had the chance to see at QCon in London last year. One of these is that <strong>there is no such thing as a "right model"</strong> - there are only models and some will help us describe our system better than others.</li>
<li>Evans suggests that we need to <strong>spend most of our time modeling in the core domain</strong> since this is the code that gives us a competitive advantage and allows us to differentiate ourselves from competitors. 

I often wonder where the best places to focus efforts on code bases is and I've typically been of the opinion that the pain points are the best place to work on since we can see an immediate reward from doing this. As I've mentioned before I quite like <a href="http://fabiopereira.me/blog/2009/09/01/technical-debt-retrospective/">Fabio's technical debt quadrant</a> as a mechanism for measuring where we should focus our efforts with this approach.

It still seems different to what Evans suggests although I'm inclined to believe that the areas of most pain could well be the areas we need to be subtle to change and there could therefore be some correlation between those areas and the core domain. 

I've not seen a distinction between the core domain and other parts of the domain model on any projects I've worked on so it'd be interesting to hear other opinions on this.</li>
<li>A related point to this which I haven't completely grasped is that <strong>there are some areas of the code which we shouldn't bother trying to improve</strong> and instead should just work around and not worry too much about creating intricate models. 

I like this advice in a way although it seems a little dangerous to me and perhaps seems to conflict with Uncle Bob's idea of following the boy scout rule and improving the code slightly every time we touch it. As I understand it, Evans advice would be to only follow this advice when we're working in the core domain. </li>
<li>Evans points out that we should try to <strong>avoid the universal domain model</strong>, something which <a href="http://dannorth.net/classic-soa">Dan North also points out in his article on SOA</a>. As I see it we can either decide to explicitly mark out multiple different models in our code explicitly otherwise we'll just end up with one mediocre model being bent to fit the needs of every part of the system.

I guess it seems intuitive to try and reduce the amount of code required in a system by just doing the modeling once but different teams in different contexts have different meanings and uses for the model that it doesn't make sense as an approach.</li> 
<li>My favourite quote from the presentation is the following:

<blockquote>Be truly responsible, don't just satisfy the emotional need to be responsible.</blockquote>

I really like refactoring code so this is a good reminder to me to take a step back when I find myself doing that and consider whether what I'm doing is actually useful.

Evans suggests that <strong>it's pointless being the team janitor</strong> and cleaning up the code after everyone else has rushed to get features delivered. The suggestion seems to be to get the strongest developers on the team working on the most important domain code rather than creating the infrastructure/platform for the rest of the team to work from.
</li>
</ul>

At the moment I feel like watching this presentation has made me think more about the value of what I'm doing when working on a code base. I don't feel so inclined to randomly refactor code and I'm more keen to work out which bits of the system I'm working on would benefit from this kind of attention.

As I mentioned earlier I now need to finish off reading section 4 of the big blue book!
