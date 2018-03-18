+++
draft = false
date="2009-03-14 14:23:43"
title="QCon London 2009: Rebuilding guardian.co.uk with DDD - Phil Wills"
tag=['qconlondon', 'qcon', 'infoq']
category=['QCon']
+++

Talk #3 on the <a href="http://qconlondon.com/london-2009/tracks/show_track.jsp?trackOID=228">Domain Driven Design track</a> at <a href="http://qconlondon.com/london-2009/">QCon</a> was by <a href="http://twitter.com/philwills">Phil Wills</a> about how the <a href="http://qconlondon.com/london-2009/presentation/Rebuilding+guardian.co.uk+with+DDD">Guardian rebuilt their website using Domain Driven Design</a>.

I'd heard a little bit about this beforehand from colleagues who had the chance to work on that project but it seemed like a good opportunity to hear a practical example and the lessons learned along the way.

There are no slides available for this one on the QCon website at the moment.

<h4>What did I learn?</h4>

<ul>
<li>Phil started by explaining the reasons that they decided to rebuild their website - tedious manual work was required to keep the site up to date, they were struggling to hire new developers due to their choice of technology stack and it was difficult to implement new features.</li>
<li>They were able to <strong>get domain experts very involved with the team</strong> to help define the domain model and trusted the domain expert to know best. I think the difficulty of making this happen is underestimated - none of the projects that I've worked on have had the domain expert access that Phil described his team as having. The benefit of having this was that they had times when the business pointed out when the model was getting over complicated. The takeaway comment for me was that we should '<strong>strive to a point where the business can see and comprehend what you're trying to achieve with your software</strong>' </li>
<li>Entities are your stars but <strong>we need to also think about value objects</strong>. Entities have the maintenance overhead of having life cycle that we need to take care of so it makes sense to avoid this wherever possible. Phil showed an example of an entity class with around 50 fields in which could have been severely simplified by introducing value objects. Every time I heard value objects being mentioned it reminded me of <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">micro/tiny types</a> which are not exactly the same but seem to be fairly similar in their intent of improving expressiveness and making the code easier to work with. The importance of value objects was also mentioned in <a href="http://www.markhneedham.com/blog/2009/03/13/qcon-london-2009-what-ive-learned-about-ddd-since-the-book-eric-evans/">Eric Evans talk</a>.</li>
<li><strong>The database is not the model</strong> - Phil repeated this multiple times just in case we didn't get the picture, and it was something <a href="http://www.markhneedham.com/blog/2009/03/14/qcon-london-2009-ddd-bdd-dan-north/">Dan mentioned in his talk as well</a> where he referenced Rails use of Active Record as being a particular culprit. Phil mentioned that this had been a difficult idea to grasp for some of the team who didn't give full status to data that didn't have a corresponding place in the database.</li>
<li>The Guardian's core domain is articles - they look to <strong>use 3rd party solutions for parts of the website which aren't part of the core domain</strong>. For example football league tables are pulled from a 3rd party content provided who sends the data in a format which can be easily displayed on the website. I think I would have made a mistake here and tried to model the league table so it was cool that they recognised that there wasn't going to be much value in doing this since it's not their differentiator. This was a really useful example for helping me to understand what the core domain actually is. </li>
<li>Although the database is not the model, Phil pointed out that <strong>keeping the database near to the model helps save the need to do lots of context switching</strong>. Interestingly he also pointed out that it's not always good to completely normalise data - it can lead to expensive joins later on. </li>
<li>One idea which I felt wasn't completely explained was that of <strong>injecting repositories into domain model objects</strong> to get access to some data rather than having to do a traversal by accessing it through other means. Phil said this was considered a bit of a hack but was sometimes a good choice. He did also point out that it can hide problems with the model. </li>
<li>Future plans for the code include adding <strong>domain events</strong> and trying to create a <strong>less monolithic domain</strong> - there is currently a single shared context which makes it difficult to prise stuff that's not in the core domain away.</li>
</ul>
