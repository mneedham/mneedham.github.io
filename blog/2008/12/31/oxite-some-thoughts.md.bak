+++
draft = false
date="2008-12-31 01:26:37"
title="Oxite: Some Thoughts"
tag=['microsoft', 'aspnet', 'mvc', 'oxite']
category=['.NET', 'Reading Code']
+++

The recently released <a href="http://www.codeplex.com/oxite">Oxite</a> code base has taken a <a href="http://www.lostechies.com/blogs/chad_myers/archive/2008/12/20/oxite-review.aspx">bit</a> <a href="http://codebetter.com/blogs/glenn.block/archive/2008/12/19/on-oxite.aspx">of</a> <a href="http://www.hanselman.com/blog/ASPNETMVCSamplesOxiteAndCommunity.aspx">a</a> <a href="http://blog.wekeroad.com/blog/some-thoughts-on-oxite/">hammering</a> in the blogosphere for a variety of reasons - the general feeling being that it doesn't really serve as a particularly good example of an ASP.NET MVC application.

I was intrigued to read the code though - you can always learn something by doing so and reading code is one of the ares that I want to improve in.

So in a style similar to that of a <a href="http://www.markhneedham.com/blog/2008/11/12/technicalcode-base-retrospective/">Technical Retrospective</a> these are my thoughts.

<h3>Things I like</h3>
<ul>
<li>The <strong>Repository</strong> pattern from <a href="http://domaindrivendesign.org/">Domain Driven Design</a> is used for providing access to the entities and provides encapsulation around the LINQ to SQL code.</li>
<li>There is some quite clever use of extension methods on FormCollection in the AdminController to create Posts and Tags from the data collected from the page. There are others as well - the developers really seem to grok extension methods in a way that I currently don't. It will be interesting to see if I start using them more as I code more with C# 3.0.
</ul>

<h3>Things I'd change</h3>
<ul>
<li>Testing wise there are some tests covering the MetaWeblogService class although it feels like the setup in each of the tests is a bit heavy. I'd refactor the tests using <a href="http://www.industriallogic.com/xp/refactoring/composeMethod.html">compose method</a> to try and remove some of the noise and rename the tests so that they follow the <a href="http://www.markhneedham.com/blog/2008/09/04/bdd-style-unit-test-names/">BDD style</a> more closely.</li>
<li>When time is used in the code it is done by directly using the DateTime class. Testing time based code is made much easier when we can control the time in our tests, so have a <a href="http://www.markhneedham.com/blog/2008/09/24/testing-with-joda-time/">Time Provider</a> or System Clock class can be a very useful approach here.</li>
<li>A <a href="http://martinfowler.com/articles/mocksArentStubs.html">classicist</a> approach has been taken towards testing with no mocks in sight! It feels like a lot of work went into creating the fake versions of the classes which could maybe have been done much more easily using a stub in <a href="http://ayende.com/projects/rhino-mocks.aspx">Rhino Mocks</a> for example. </li>
<li>A lot of the ViewData code is weakly typed by putting values into an array. We started with this approach on a project I worked on and it's so easy to misspell something somewhere that we came to the conclusion that <strong>if we can get strong typing we should strive for that</strong>. Jeremy Miller's <a href="http://codebetter.com/blogs/jeremy.miller/archive/2008/10/23/our-opinions-on-the-asp-net-mvc-introducing-the-thunderdome-principle.aspx">Thunderdome Principle</a> works well here. </li>
<li>AdminController seems to have a massive number of responsibilities which is perhaps not surprising given the name. I think it'd be better to have the administrative tasks handled from the individual controllers for those tasks. This would also help lead the design towards a more <a href="http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm">RESTful</a> approach</li>
<li>The <strong>Domain model is very driven from the definition of the database tables</strong> from my understanding. The domain objects are effectively representations of database tables. If we want to create a richer domain model then it would make more sense to design the classes in terms of what makes sense in the domain rather than what makes sense at a database level. An ORM tool could then be used to map the database tables to the code.</li>
<li>A lot of the <strong>domain objects implement an interface</strong> as well which I don't think is really necessary. Although there are exceptions, in general when we refer to domain objects we care about the implementation rather than a contract describing what it does.</li>
<li>The <strong>Routes collection is passed around</strong> quite a few of the controllers, seemingly so that URLs can be generated inside other pages. It seems a bit overkill to pass this around to achieve such a simple goal and my thinking is that maybe a wrapper class which generated the URLs might be more intention revealing.</li>
<li>There is a bit more logic than I'm comfortable with in some of the views - I think it would be good to move this logic into ViewModel classes. This will have the added benefit of allowing that logic to be tested more easily.</li>
</ul>

<h3>Want to know more about</h3>
<ul>
<li>I'm curious as to <strong>why LINQ to SQL is being used</strong> as the interface to the database as I was under the impression that it is being <a href="http://codebetter.com/blogs/david.hayden/archive/2008/10/31/linq-to-sql-is-dead-read-between-the-lines.aspx">phased out</a> by Microsoft. The syntax seemed quite readable but I think the problem of interacting between code and the database in a clean way has been largely solved by <a href="http://www.hibernate.org/343.html">NHibernate</a> although the <a href="http://weblogs.asp.net/fbouma/archive/2008/05/19/why-use-the-entity-framework-yeah-why-exactly.aspx">Entity Framework</a> is a newish addition in this area.</li>
<li>One interesting thing I noticed was a <strong>lot of Background Services</strong> running in this codebase - I've not come across this in a web application before. They are actually being used for creating trackbacks, sending trackbacks and sending email messages.</li>

</ul>

<h3>My learning from reading the code</h3>
<ul>
<li>I asked for some <a href="http://twitter.com/markhneedham/status/1063734022">advice on the best way to read code</a> on Twitter and the most popular advice was to <strong>debug through the code</strong>. Unfortunately I couldn't seem to do this without having a database in place so another approach was necessary. Instead I started reading from the tests that were available and then clicked through to areas of interest from there. I think it worked reasonably well but it wasn't as focused as if I had debugged and I couldn't see the state of the program as it executed.</li>
<li>I wanted to find a way to read the Oxite code and navigate to areas of the ASP.NET MVC source using <a href="http://www.red-gate.com/products/reflector/">Reflector</a> without having to do so manually. <a href="http://www.testdriven.net/">TestDriven.NET</a> was recommended to me and it worked really well. Clicking the 'Go to Reflector' option from the menu takes you to the current class in the Reflector window. Impressive.</li>
<li>Changing the Resharper find usages menu to show 'Namespace + Type' makes it much easier to try and work out what the code is doing rather than the default setting of just 'Namespace'.</li>
<li>From looking at some of the ASP.NET MVC code I realised that a lot of data is stored in static variables in order to make the data globally accessible. It's something I had never considered this before and it makes sense in a way but feels a little nasty</li>
<li>I found that I was getting <strong>side tracked quite a lot</strong> by irrelevant details in the code. I'm used to having a pair guide me through a new code base so looking at this one alone was a bit different for me. Separating noise/signal when reading code and identifying common patterns to allow me to do this is something I am working on.</li>
</ul>

<h3>Overall</h3>

I think it's really cool that the Oxite team put their code out there for people to look at and learn from. A number of highly experienced developers have made suggestions for improvement so clearly this is quite a useful way to get feedback and code better in the future.

From what I understand, Rob Conery is working on some <a href="http://blog.wekeroad.com/blog/oxite-refactor-take-1/">refactorings for this code base</a> so it will be interesting to see what it looks like when this is done. 
