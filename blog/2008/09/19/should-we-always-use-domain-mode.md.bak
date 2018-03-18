+++
draft = false
date="2008-09-19 08:34:35"
title="Should we always use Domain Model?"
tag=['pragmatic', 'ddd']
category=['Domain Driven Design']
+++

During the <a href="http://www.markhneedham.com/blog/2008/09/14/altnet-uk-conference-20/">discussion</a> about Domain Driven Design at the <a href="http://www.altnetuk.com/">Alt.NET</a> conference I felt like the idea of the Rich Domain Model was being represented as the only way to design software but I don't feel that this is the case.

As always in software we <a href="http://www.virtualschool.edu/mon/SoftwareEngineering/BrooksNoSilverBullet.html">never have a silver bullet</a> and there are times when Domain Model is not necessarily the best choice, just as there are times when OOP is not necessarily the best choice.

To quote from Martin Fowler's <a href="http://martinfowler.com/books.html#eaa">Patterns of Enterprise Application Architecture</a> 

<blockquote>
It all comes down to the complexity of the behaviour in your system. If you have complicated and everychanging business rules involving validation, calculations, and derivations...you'll want an object model.
</blockquote>

<h3>What are the alternatives?</h3>

Domain Model is not a silver bullet and Martin suggests two alternatives when a model driven approach may not be the best choice

<ol>
<li><a href="http://martinfowler.com/eaaCatalog/transactionScript.html">Transaction Script</a> - The best thing about this is its simplicity. It is easy to understand as all the logic is in one place and it is a good choice for applications with a small amount of logic.</li>
<li><a href="http://martinfowler.com/eaaCatalog/tableModule.html">Table Module</a> - This is a database driven approach with one class per table. If the system you're working on is using a very table-orientated approach to storing data then this approach may be a good choice.</li>
</ol>

I think in order to make a Domain Model approach work, everyone in the team (including QAs,BAs etc) needs to buy into the idea and you need some people who have experience in using it so that you can use it in a pragmatic way.

While we have some great tools and techniques available to us in the world of software it is important to remember what problem we are trying to solve and pick the appropriate tool for the job.

*Updated* 
I've edited the phrasing of this after conversation - I intended to refer to the Rich Domain Model concept used in Domain Driven Design and was presenting alternatives to this rather than to DDD as a whole.
