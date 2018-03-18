+++
draft = false
date="2008-09-14 16:28:27"
title="Alt.NET UK Conference 2.0"
tag=['net', 'altdotnet', 'altnetuk']
category=['.NET']
+++

I spent most of yesterday at the 2nd <a href="http://altnetuk.com/">Alt.NET UK</a> conference at Conway Hall in London.

First of all kudos to  <a href="http://codebetter.com/blogs/ian_cooper/">Ian Cooper</a>, <a href="http://thoughtpad.net/alan-dean.html">Alan Dean</a> and <a href="http://blog.benhall.me.uk/">Ben Hall</a> for arranging it.  There seemed to be a lot more people around than for the one in February which no doubt took a lot of arranging.

It was again run using the <a href="http://en.wikipedia.org/wiki/Open_Space_Technology">open spaces</a> format and we started with an interesting discussion on what Alt.NET actually is. There's been <a href="http://codebetter.com/blogs/david_laribee/archive/2008/09/14/the-two-alt-net-criterion.aspx">quite a bit </a>of <a href="http://codebetter.com/blogs/glenn.block/archive/2008/09/11/the-alt-net-criterion.aspx">discussion</a> in the blogosphere and everyone seemed to have a slightly different opinion - for me it's a group of people who are interested in improving how they work in .NET. Ian Cooper pointed out the <a href="http://codebetter.com/blogs/karlseguin/archive/2008/06/24/foundations-of-programming-ebook.aspx">Foundations of Programming e-book</a> as something concrete which has been released regarding what Alt.NET actually is.

The day was again split into four streams - I stuck to the more general software development oriented discussions.

<h3>Agile</h3>

This session focused on <a href="http://www.infoq.com/articles/agile-estimation-techniques">agile estimation session techniques</a>. <a href="http://www.amazon.co.uk/Agile-Estimating-Planning-Robert-Martin/dp/0131479415/ref=sr_1_1?ie=UTF8&s=books&qid=1221383370&sr=8-1">Mike Cohn's book</a> is probably the best known reading in this area.

Ian Cooper raised an interesting idea around the discussion of estimates - he suggested getting the person with the highest and lowest estimates to explain why they had given that estimate to help bring out the different assumptions that people were making regarding the story.

He also spoke about his use of <a href="http://alistair.cockburn.us/index.php/Main_Page">Alistair Cockburn's</a> <a href="http://www.amazon.co.uk/Crystal-Clear-Human-Powered-Methodology-Small/dp/0201699478/ref=sr_1_1?ie=UTF8&s=books&qid=1221394810&sr=8-1">Crystal</a> methodology which advocates a 3 phase approach to development whereby you start with the skeleton of the system early on and gradually fill it out in future iterations. I have read a little bit of the book but never used it myself so it was interesting to hear a practical experience.

The idea of only releasing software when it is actually needed rather than at frequent 2 week intervals regardless was also raised but from what I've seen on my projects when there are releases it is because the software is needed by the users. I think this is more a case of pragmatically using the methodology rather than sticking to precise rules.

<h3>Acceptance Testing</h3>

A lot of the focus in this session was around how we can improve the communication between BAs, QAs and Developers when it comes to writing acceptance criteria.

<a href="http://gojko.net/">Gojko Adzic</a> suggested the idea of having an Acceptance Testing 3-Some before  a story is played so that these tests can be written with all opinions taken into account. The idea here was that the tests written would be more accurate and hopefully reduce the problem of having to go back and change them later on.

While this idea seems good I am more of the opinion that we should just go with the acceptance tests that the QA writes, implement those, then check with the business whether everything is covered. The feedback loop in this approach is much shorter and as the key to software development for me is getting frequent feedback I prefer this approach. This is certainly the way we have done things on the ThoughtWorks projects I've been a part of. <a href="http://www.amazon.co.uk/Requirements-Collaboration-Workshops-Defining-Needs/dp/0201786060/ref=sr_1_1?ie=UTF8&s=books&qid=1221398020&sr=8-1">Requirements by Collaboration</a> was pointed out as being a good book to read with regards to getting everyone involved in the process.


The idea of having a ubiquitous language that everyone in the team used to describe acceptance tests was another good idea that came out of discussions - although I think if a team is developing software using a Domain Driven approach then this is likely to happen anyway.

A large part of the session focused on UI tests and the problems people experienced with regards to brittleness and long running time. One way to get around this is clearly not to have so many tests at this level - one idea was to only have automated UI level tests for critical scenarios e.g. logging into the system and then manual test other scenarios.

One way we have got around this on the projects I've worked on is by having a level of tests one level down which test component interaction separate from the UI - typically called functional tests. These could be used to test things such as NHibernate logic rather than doing this through the UI. We would also look to keep minimal logic in the presentation layer as this is the most difficult part of systems to get automated tests around.

<a href="http://texttest.carmen.se/">TextTest</a> was mentioned as being an acceptance testing tool which tested the system by going through the log files. This has the added benefit of forcing you to write more useful logging code. <a href="http://www.greenpeppersoftware.com">Green Pepper</a> was also mentioned as a useful way of using acceptance tests which link together Jira and Confluence.

<h3>Domain Driven Design</h3>

The discussion (perhaps not surprisingly) focused on the concepts described in Eric Evans' <a href="http://www.amazon.co.uk/Domain-driven-Design-Tackling-Complexity-Software/dp/0321125215/ref=sr_1_1?ie=UTF8&s=books&qid=1221399011&sr=1-1">book</a>.

The value of having rich domain objects with the business logic inside was questioned with Ian Cooper pointing out that business logic need not necessarily be business rules but could also describe the way that we traverse the object graph. In particular the <a href="http://www.dcmanges.com/blog/37">Law of Demeter</a> was discussed as a way of avoiding an <a href="http://www.martinfowler.com/bliki/AnemicDomainModel.html">anaemic domain model</a>.

The problem of designing from the database upwards resulting in these anaemic objects was raised - one potential solution being driving the design from acceptance tests i.e. top down.

Ian Cooper pointed out that coding in a Domain Driven way with lots of plain C# objects made testing much easier. I think in general keeping the behaviour and data together in an object makes it easy to test. Doing this using a Domain Driven approach just makes it even easier to use the code as a communication mechanism.

There was also discussion around the use of <a href="http://en.wikipedia.org/wiki/Data_Transfer_Object">Data Transfer Objects</a>, with the general consensus being that using DTOs was good around the UI to save you having to deal with incomplete domain objects around these areas. 

The idea of the UI being outside the bounded context that our domain model is used in was also suggested which strikes me as a good idea - would be good to see it done in practice though.

It was suggested that DDD is only useful in complex domains. I think this is true to an extent but some some of the ideas of DDD are just good software development principles such as having a common/ubiquitous language in the team. Ideas such as bounded context are clearly only necessary when there is a greater level of complexity.

I would certainly recommend picking up a copy of the <a href="http://www.amazon.co.uk/Domain-driven-Design-Tackling-Complexity-Software/dp/0321125215/ref=sr_1_1?ie=UTF8&s=books&qid=1221406080&sr=8-1">book</a> - 90% of what was discussed is in there.

<h3>Developer Education</h3>

This was the most interactive session I attended and the majority of the people in the room were able to offer their opinions which I thought was much more aligned with the spirit of the open spaces format.

The discussion focused on how the environment that you're working in influences your enthusiasm for learning new technologies and new ways of doing things. I am lucky in that working for ThoughtWorks I have <a href="http://blog.m.artins.net/">colleagues</a> who are very enthusiastic about technology and encouraging other people to learn.

The Ruby community was pointed out as one where there appears to be much more enthusiasm than there is in the .NET world. I'm not sure how exactly we can measure this but blogging wise the Ruby guys definitely have the edge. I think some of this can be explained that people who ran with Ruby early on are massive technology enthusiasts and you're unlikely to start working with Ruby because you have to - it normally starts out for the love of the language from my experience.

A suggestion was made that holding <a href="http://en.wikipedia.org/wiki/Brown_bag_seminars">Brown Bag sessions</a> at lunch time where people could share their learnings with colleagues was a good way of helping to share knowledge. This is certainly an idea that we use frequently at ThoughtWorks and there is actually even more value in the conversations which come afterwards. 

The <a href="http://googleblog.blogspot.com/2006/05/googles-20-percent-time-in-action.html">Google idea of 20 % time</a> to dedicate to your own learning was raised as being ideal, although it was pointed out that this was a hard thing to implement as getting things done always takes precedence.

<h3>Overall</h3>

It was an interesting day and it's always good to hear the experiences of other people outside of ThoughtWorks.

I think we need to try and find a way that more people can get involved because most of the sessions I attended were very dominated by a few people who had great knowledge on the subject. While it is no doubt very useful to hear their opinions I think it would be even better if more people could get to speak.
