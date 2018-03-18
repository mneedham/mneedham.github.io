+++
draft = false
date="2009-04-11 12:33:03"
title="The Mythical Man Month: Book Review"
tag=['fred-brooks', 'mythical-man-month']
category=['Books']
+++

<h3>The Book</h3>

<a href="http://www.amazon.co.uk/Mythical-Month-Essays-Software-Engineering/dp/0201835959/ref=sr_1_1?ie=UTF8&s=books&qid=1238933179&sr=8-1">The Mythical Man Month</a> by Fred Brooks Junior

<h3>The Review</h3>

Pretty much since I started working at ThoughtWorks 2 1/2 years ago I've been told that this is a book I have to read and I've finally got around to doing so.

Maybe it's not that surprising but my overriding thought about the book is that just about every mistake that we make in software development today is covered in this book!

<h4>What did I learn?</h4>

<ul>
<li>The title of the book and the second chapter of the book  refers to the situation that surely everyone who has ever worked on a software development project is aware of - <strong>if a project is late then adding new people onto it will make it even later</strong>. This is due to the fact that a big part of software development is communication and adding people makes that communication more complicated than it previously was, therefore meaning it takes longer to get things done. My colleague Francisco has a nice post describing the ways that <a href="http://blog.franktrindade.com/2009/04/06/more/">adding people can slow down a development team</a>. The idea that <a href="http://fabiopereira.me/blog/2008/12/16/9-pregnant-women/">a baby can't be produced any quicker by having 9 women rather than just one</a> is a particularly common metaphor used to explain this.</li>
<li><strong>Incompleteness and inconsistencies of ideas only becomes clear during implementation</strong> - pretty much putting a dagger into the idea that we can define everything up front and then code it just like that. This is certainly the area that the <a href="http://agilemanifesto.org/">agile</a> and <a href="http://en.wikipedia.org/wiki/Lean_software_development">lean</a> approaches look to change and certainly the earlier we can try out different ideas by using approaches such as <a href="http://bradfordcross.blogspot.com/2009/03/set-based-triangulation-and.html">set based concurrent engineering</a> the more quickly we can end up with a useful solution.</li>
<li>An interesting idea about creating a <strong>surgical team</strong> ,with a few very experienced people doing the majority of the coding and being assisted by other members of the team, is suggested as being a successful route to delivering software. It sounds quite different to the teams that I have worked on where everyone on the team is involved although the objectives behind it seem valid - reducing the communication points and ensuring the conceptual integrity of the solution. Uncle Bob recently wrote about this describing these teams as <a href="http://blog.objectmentor.com/articles/2009/04/01/master-craftsman-teams">master craftsman teams</a> but it sounds as if this would require quite a radical shift in the recruiting strategies of organisations. Dave Hoover also has an <a href="http://nuts.redsquirrel.com/post/93120388/my-take-on-master-craftsman-teams">interesting post on this subject</a> but he takes the angle of building apprentices on teams like this.</li>
<li>This seems closely linked to another idea about team composition described later on in the book which speaks of the need for a team to have a <strong>technical director and a producer</strong> - the technical director sounds to be quite similar to Toyota's idea of the <a href="http://blog.scottbellware.com/2008/12/chief-engineer.html">Chief Engineer</a> and they would be technically in charge while the producer (<a href="http://www.youtube.com/watch?v=cbNmVUbdKRo">Iteration Manager</a>?) is in charge of everything else. The underlying idea here is that we don't just have one person in charge of a team, there are two distinct and important roles.</li>
<li>Brooks says the most <strong>important aspect of the design of a system is to ensure its <a href="http://c2.com/cgi/wiki?ConceptualIntegrity">conceptual integrity</a></strong> i.e. a consistent set of design ideas. In order to achieve this Brooks suggests the need for a system architect - while I agree with this idea I think it is more a role and maybe one that can be done by the Tech Lead on a project. The Poppendieck's also talk of the need for conceptual integrity in <a href="http://www.markhneedham.com/blog/2008/12/20/lean-software-development-book-review/">Lean Software Development</a>. The point here is to create a system which is easy to use both in terms of function to conceptual complexity. I am reminded of a <a href="http://dannorth.net">Dan North</a> quote at this stage: "We're done not when there's nothing more to add, but when there's nothing more to take away"</li>
<li>The <strong>productivity increases gained by using high level languages</strong> are mentioned - the underlying idea being that using these allow us to avoid an entire level of exposure to error. I think this makes sense and as an example I think the introduction of <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">functional collection parameters into C# 3.0</a> will lead to a reduction in the amount of time spent debugging loop constructs since we no longer have to use these so frequently.</li>
<li>When talking about object oriented programming Brooks speaks of the need to <strong>design objects which describe the concepts of the client</strong>.

<blockquote>
If we design large grained classes that address concepts our clients are already working with, they can understand and question the design as it grows, and they can cooperation in the design of test cases.
</blockquote>

In other words...<a href="http://domaindrivendesign.org">Domain Driven Design</a>! Reading this part of the book very much reminded me of <a href="http://www.markhneedham.com/blog/2009/03/14/qcon-london-2009-rebuilding-guardiancouk-with-ddd-phil-wills/">Phil Will's QCon presentation</a> where he spoke of the way that the business and software development teams at the Guardian were able to collaborate to drive the design of the domain model for their new website. 
</li>
<li></li>
<li>The idea of only <strong>performing system debugging when each individual component actually works</strong> is something which should be obvious but is often not followed. If we know a component doesn't work on its own then we can guarantee it is not going to work when we try to integrate it with other components so the exercise seems slightly pointless to me. Common sense advice I think!</li>
<li>Speaking of code reuse Brooks points out that the key here is the <strong>perceived cost of finding a component to reuse</strong> that is important - this ties in nicely with an idea from <a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">Dan Bergh Johnsson's QCon presentation</a>

<blockquote>
Your API has 10-30 seconds to direct a programmer to the right spot before they implement it [the functionality] themselves
</blockquote>
</li>
<li>Brooks talks of the <strong>need to have documentation for our projects</strong> - he uses a project workbook to do this and I think the modern day equivalent would be the project wiki. The idea of creating self documenting programs to help minimise the documentation that needs to be written is also covered. The importance of <a href="http://fabiopereira.me/blog/2009/02/12/naming-convention-taken-to-another-level/">how we name concepts in our code</a> is especially important in this area.</li>
<li>The need to <strong>progressively refine the system by growing it rather than building it</strong> is suggested later on in the book - the limitations of the waterfall model are described and the approaches of agile/lean are pretty much described - building frequently, getting it working end to end, rapid prototyping and so on. </li>
</ul>

<h3>In Summary</h3>
I really enjoyed reading this book and seeing how a lot of the ideas in more modern methodologies were already known about in the 1980s and aren't in essence new ideas.

I'd certainly recommend this book.
