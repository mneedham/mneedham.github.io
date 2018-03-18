+++
draft = false
date="2009-08-08 00:49:12"
title="Book Club: Object Role Stereotypes (Jeremy Miller)"
tag=['book-club', 'object-design']
category=['Book Club']
+++

In last week's book club we discussed an article written by <a href="http://codebetter.com/blogs/jeremy.miller/">Jeremy Miller</a> for MSDN Magazine titled '<a href="http://msdn.microsoft.com/en-us/magazine/cc721605.aspx">Object Role Stereotypes</a>' which discusses part of Rebecca Wirfs Brock's book '<a href="http://www.amazon.co.uk/Object-Design-Responsibilities-Collaborations-Addison-Wesley/dp/0201379430/ref=sr_1_1?ie=UTF8&qid=1249549884&sr=8-1">Object Design</a>'.

I've been trying to read Object Design for about a year since coming across the book while reading through the slides from <a href="http://jaoo.com.au/sydney-2008/schedule/monday.jsp">JAOO Sydney 2008</a> but I've often found the reading to be quite abstract and have struggled to work out how to apply the ideas to the coding I do day to day. 

This therefore seemed to be like a good opportunity to get some more opinions and discussion on at least part of the book.

There are some of my thoughts and our discussion of the article:

<ul>
<li><a href="http://lizdouglass.wordpress.com/">Liz</a> pointed out that at <a href="http://www.thoughtworks.com.au/work-for-us/TWU.html">ThoughtWorks University</a> (which we both attended) we were shown the idea of <strong>writing the 'job' of an object</strong> just above the class definition, the point of this being that we would describe the responsibility of the object and ensure that objects only had one responsibility. 

Neither Liz nor I have ever seen this done on any of the projects that we've worked on but it seems quite related to the idea of responsibility driven development which is encouraged in the book. The different role stereotypes would form part of the responsibilities that an object might have.

Matt Dunn suggested that perhaps the tests we write fulfill this role instead in a more indirect way although I think we would probably need to be writing tests with the quality Jimmy Bogard describes in <a href="http://www.lostechies.com/blogs/jimmy_bogard/archive/2008/12/18/getting-value-out-of-your-unit-tests.aspx">his post on getting value our of your unit tests</a>, instead of the pale imitations we often end up writing, to achieve this goal.</li>
<li>I find each of the individual stereotypes quite difficult to remember on their own but Jeremy pointed out that they fit into 3 categories:

<ul>
<li>Knowing (Information Holder, Structurer)</li>
<li>Doing (Service Provider, Interfacer)</li>
<li>Deciding (Controller, Coordinator)</li></ul>

I think the object role stereotypes mix quite nicely with some of the ideas from <a href="http://domaindrivendesign.org/">Domain Driven Design</a> - for example a <a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">value object</a> would probably be an information holder; an entity might be a structurer and an information holder; a factory could be a service provider; a <a href="http://www.markhneedham.com/blog/2009/03/10/ddd-repository-not-only-for-databases/">repository</a> is possibly an interfacer although I think that may be more the case if we are using a repository as a DAO instead of a true DDD repository.</li>
<li>I think it might actually be easier when looking at existing code to question <strong>whether or not a particular object is actually only doing one thing or not before analysing which of the stereotypes it is fulfilling</strong>. We discussed although didn't come to a conclusion whether there are certain stereotypes that should not be mixed together in one object. For example maybe an object which acts as an interfacer wouldn't store state and therefore might not be an information holder as well.</li>
<li>We briefly discussed some other articles which cover similar ideas including <a href="http://isaiahperumalla.wordpress.com/">Isaiah Perumalla's</a> article on <a href="http://msdn.microsoft.com/en-us/magazine/dvdarchive/dd882516.aspx">role based objects</a> and Udi Dahan's idea of the roles being <a href="http://www.testingreflections.com/node/view/7234">described more specifically in the interface name</a>. Both of these articles have some good ideas and I find the latter particularly intriguing although I haven't tried it out on any code I've written as yet.</li>
<li>The article also has some great ideas around coding in general which I think make a lot of sense:

<blockquote>Don't be afraid to create small objects instead of wallowing in the mud of primitive variables</blockquote>

<blockquote>Designing software is often an exercise in managing complexity...you can take steps to limit the complexity of any given class by only assigning it a discrete set of responsibilities</blockquote>
</li>
</ul> 
