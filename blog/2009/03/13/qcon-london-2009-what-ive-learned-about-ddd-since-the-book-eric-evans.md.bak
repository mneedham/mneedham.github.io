+++
draft = false
date="2009-03-13 20:56:07"
title="QCon London 2009: What I've learned about DDD since the book - Eric Evans"
tag=['qconlondon', 'qcon', 'infoq']
category=['QCon']
+++

I went to the <a href="http://qconlondon.com/london-2009/">QCon conference in London</a> on Thursday, spending the majority of the day on Eric Evans' <a href="http://qconlondon.com/london-2009/tracks/show_track.jsp?trackOID=228">Domain Driven Design track</a>. 

The opening presentation was by Eric Evans, himself, and was titled '<a href="http://qconlondon.com/london-2009/presentation/What+I%27ve+learned+about+DDD+since+the+book">What I've learned about DDD since the book</a>'.

<blockquote>
In the 5 years since the book was published, I've practiced DDD on various client projects, and I've continued to learn about what works, what doesn't work, and how to conceptualize and describe it all. Also, I've gained perspective and learned a great deal from the increasing number of expert practitioners of DDD who have emerged.
</blockquote>

We're currently reading <a href="http://domaindrivendesign.org/">Domain Driven Design</a> in our technical book club in the ThoughtWorks Sydney office so I was intrigued to hear about Eric's experiences with DDD and how those compared with ours. 

The slides from the presentation are <a href="http://qconlondon.com/london-2009/file?path=/qcon-london-2009/slides/EricEvans_WhatIveLearnedAboutDDDSinceTheBook.pdf">here</a>.

<h4>What did I learn?</h4>

<ul>
<li>We started with a look at what Evans considers the most essential parts of DDD - creative collaboration between the software experts and the domain experts was identified as being important if we are to end up with a good model. If we can make the process of defining the model fun then all the better but <strong>we need to utilise domain experts properly and not bore them</strong>. 

Taking a domain expert through some screens and talking about the validation needed on different fields is a bad way to use them - they want to do valuable work and if this is their experience of what it's like working with the software experts then we'll never see them again.
</li>
<li>When we're modeling <strong>we need to come up with at least three models</strong> - don't stop at the first model, it's probably not going to be the best one. If we stop after one model then we're leaving opportunities on the table - white boarding different models is a very cheap activity so we should make sure we take advantage of that and do it more frequently.

When we talk of three models Evans' pointed out that these should be different to each other and that this would involved coming up with some radically different ideas. Creating an environment where we can celebrate 'bad' ideas is necessary to encourage people to step into the riskier territory. <strong>If we're only coming up with good ideas we're not being creative</strong>. This was a definite take away for me - I'm certainly guilty of only considering the first model I discover so this is something to improve on.</li>
<li>He touched on a couple of others including the need to <strong>constantly reshape the domain model</strong> as we learn more about it and that we can get the biggest gain from DDD by keeping the <strong>focus on our core domain</strong> before we got onto <a href="http://devlicio.us/blogs/casey/archive/2009/02/11/ddd-bounded-contexts.aspx">explicit context boundaries</a> - I've always found this to be the most interesting part of the book and Evans said he wished he'd made it one of the earlier chapters. 

I spoke with him afterwards about whether or not the UI was considered to be a separate bounded context. He said to consider a bounded context as an observation [of the system] and that if the model of the UI was significantly different to the underlying model then it would be reasonable to consider it as another bounded context.</li>
<li>We moved onto the building blocks of DDD - services, entities, value, objects, factories, repositories - which Evans considers to be over emphasised. They are important but not essential. Evans did also point out that <strong>value objects tend to get neglected</strong>. This was also mentioned in several of the other presentations.</li>
<li>Despite this Evans added a new building block - <strong>domain events</strong>. He described this as 'something happened that the domain experts care about'. They provide a way of representing the state of an entity and lead to clearer, more expressive model. This sounded very similar to an approach <a href="http://pilchardfriendly.wordpress.com/">Nick</a> has described to me whereby we would have a new object that represented a specific state of an object. 'Every change to an object is a new object' was the take away quote from this part of the talk for me - I think an <a href="http://www.markhneedham.com/blog/2009/02/28/coding-implicit-vs-explicit-modeling/">explicit approach to modeling is far superior to an implicit one</a>.

The example given was a baseball game where a domain event might be someone swinging at the ball - when this happens statisticians will need to be informed so that they can update their statistics i.e. we often want to record to events that happen in our domain. He described the use of an <strong>event stream</strong> which we could put events onto and they could be subscribed to by whoever cares e.g. the reporting service. </li>
<li>Evans made an interesting point when talking about strategic design - <strong>just because you have been working in a domain for a long period of time does not make you a domain expert</strong>. There is a subtle difference between someone working as a software expert in a domain and the actual domain expert - when looking at problems the software expert is responsible for looking at how software can help, the domain expert is responsible for removing that problem!</li>
<li>Evans came up with a <strong>context mapping step-by-step</strong> which he said could be followed to help us work out where the different bounded contexts in our system are and how they interacted:

<ol>
<li>What models do we know of? (draw blob for each & name it)</li>
<li>Where does each apply?</li>
<li>Where is information exchanged?</li>
<li>What is the relationship?</li>
<li>Rinse and repeat</li>
</ol>

I've never drawn a context map before but it sounds like a potentially valuable exercise - might try and do one for my current project!
</li>
<li>He also added a couple more patterns in this area - <strong>big ball of mud</strong> and <strong>partners</strong>. For big ball of mud he said we should identify these in our context maps and then not worry too much about applying design techniques when in this context - just take a pragmatic approach and 'reach in and change it'

Partners was described as being similar to a <a href="http://en.wikipedia.org/wiki/Three-legged_race">three-legged race</a> - both teams need to cooperate on their modeling efforts because they have a mutual dependency, neither can deliver without the other. </li>
<li>Some final take away quotes included '<strong>not all of a large system will be well designed</strong>' and '<strong>precision designs are fragile</strong>' - where we have the latter in our code we need to protect them with an anti corruption layer and with the former we should pick a specific area (that matters) to design well and accept that other bits might not be as good as this bit.
</ul>

Gojko Adzic has a <a href="http://gojko.net/2009/03/12/qcon-london-2009-eric-evans-what-ive-learned-about-ddd-since-the-book/">write up of this talk</a> as well - a very informative talk and it's definitely cool to hear the guy who coined the approach talking about it.
