+++
draft = false
date="2009-04-25 01:26:38"
title="Pimp my architecture - Dan North"
tag=['software-development', 'architecture']
category=['Software Development']
+++

My colleague <a href="http://dannorth.net/">Dan North</a> presented a version of a talk he first did at <a href="http://qconlondon.com">QCon London</a> titled '<a href="http://qconlondon.com/london-2009/presentation/Pimp+my+architecture">Pimp my architecture</a>' at the ThoughtWorks Sydney community college on Wednesday night. He'll also be presenting it at <a href="http://jaoo.com.au">JAOO</a> in <a href="http://jaoo.com.au/sydney-2009/">Sydney</a> and <a href="http://jaoo.com.au/brisbane-2009/">Brisbane</a> in a couple of weeks time.

The slides for the talk are <a href="http://qconlondon.com/london-2009/file?path=/qcon-london-2009/slides/DanNorth_PimpMyArchitecture.pdf">here</a> and it's also <a href="http://www.infoq.com/presentations/north-pimp-my-architecture">available on InfoQ</a>.

<h4>What did I learn?</h4>

<ul>
<li>I quite liked the way the talk was laid out - Dan laid out a series of problems that he's seen on some projects he's worked on and then showed on the next slide where he planned to take the architecture. The rest of the talk then detailed the story of how the team got there. 

To begin with it was a case of SOA gone bad with clients heavily coupled to services via WSDL definitions, a lot of code duplication, a complex/flaky architecture featuring a non standard JBoss and a team where the developers worked in silos.

The aim was to get to a 'good SOA' where the services were actually helpful to clients, the code would be stable in production/deterministically deployable and a happy team would now exist.</li>
<li>The role of an architect is to play a key role in design, to be the technology expert on the team, to act as a coach and a social anthropologist/shaman. An interesting theme for me in the talk was that so much of it centred around the <strong>human aspects of architecture</strong>. I guess maybe that's obvious but a lot of what I've read about architecture comes from the technical side and providing the technical direction so it was refreshing to see a different approach. </li>
<li>As mentioned above, Dan spoke of the need to have a project <a href="http://en.wikipedia.org/wiki/Shamanism">shaman</a> - someone who can share the history of the project and why certain decisions were made on the project and explain those to people when they join the team. It can be the architect but it doesn't actually matter as long as someone on the team assumes the role. Another colleague of mine pointed out that this role is also about envisioning the future of the system. As with most things when we know the <a href="http://www.markhneedham.com/blog/2009/04/05/coding-criticising-without-context/">context in which something was done</a> the decision doesn't seem quite so stupid.</li>
<li>One of the interesting ideas which Dan spoke of was that of having a <strong>transitional architecture</strong> on your way to the architecture that you actually want. You know that it's not the end goal but it's a much better place to be than where you were and can provide a nice stepping stone to where you want to be. The example he gave was refactoring the architecture to a stage where the services could be accessed via a service locator. It's never going to be the end goal but provides a nice middle ground.</li>
<li>Dan provided quite an interesting alternative to the 'yesterday I did this, today I'm doing that...' style of <a href="http://martinfowler.com/articles/itsNotJustStandingUp.html">standups</a> which I haven't seen used before. The idea is that the team <strong>consider what would make today the best possible day</strong> in achieving their goal, and then going around the circle each team member adds in information that will help the team teach that goal - be it stuff they learnt the day before or areas that they have been struggling in. He also spoke of the idea of people helping each other rather than pairing to try and get past the reluctance of having two people working on the same machine.</li>
<li>The idea that you <a href="http://blog.franktrindade.com/2009/04/21/what-is-your-goal/">you get what you measure</a> was also mentioned - if we measure the performance of developers by the number of story points they complete then we increase the chance that they're just going to finish stories as quickly as possible without caring as much about the quality of the code being written potentially leading to more buggy code. I'm interested in reading the <a href="http://www.amazon.co.uk/Influencer-Change-Anything-Kerry-Patterson/dp/007148499X/ref=sr_1_1?ie=UTF8&s=books&qid=1240537593&sr=8-1">Influencer</a> to understand more about this type of thing.</li>
<li>Dan pointed out that we should <strong>never write caches</strong> unless that happens to be our differentiator - they've been done loads of times before and there are plenty to choose from. This ties in with the Domain Driven Design idea of focusing our efforts on the <a href="http://dotnet.org.za/hannes/archive/2009/04/07/core-domains-and-sub-domains-in-ddd.aspx">core domain</a> and not worrying so much about other areas since they aren't what makes us special. </li>
<li>It was also pointed out that <strong>we won't fix everything</strong> on a project. I think this is a very astute observation and makes it easier to work with code bases where we want to make a lot of changes. At times it can feel that you want to change just about everything but clearly that's not going to happen. </li>

</ul>
