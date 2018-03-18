+++
draft = false
date="2010-06-13 13:37:39"
title="The Refactoring Dilemma"
tag=['coding']
category=['Coding']
+++

On several of the projects that I've worked on over the last couple of years we've seen the following situation evolve:

<ul>
<li>The team starts coding the application.</li>
<li>At some stage there is a breakthrough in understanding and a chance to really improve the code.</li>
<li>However the deadline is tight and we wouldn't see a return within the time left if we refactored the code now</li>
<li>The team keeps on going with the old approach</li>
<li>The project ends up going on for longer than the original deadline</li>
<li>It's now much more work to move towards the new solution</li>
</ul>

In the situations I describe the refactorings could have been done incrementally but doing that would take longer than continuing with the original approach and also <a href="http://www.markhneedham.com/blog/2010/05/05/consistency-in-the-code-base-and-incremental-refactoring/">leave the code in an inconsistent state</a>.

I think the reason this situation evolves consistently in this manner is because <strong>although we talk about writing maintainable code, delivery is often considered more important</strong>. Pushing out a delivery date in order to refactor code so that it will be easier to work with in the future isn't something that I've seen happen.

Pushing a delivery date out is a cost that we can see straight away.

On the other hand it's quite difficult to estimate how much of a gain you'll get by refactoring to a more maintainable/easier to test solution and that gain will not be immediate.

We therefore end up in the situation where we tend to make major refactorings only if we're going to see a benefit from doing that refactoring before the project ends.

In one sense that seems reasonable because we're trying to ensure that we're adding as much value as possible while the client is paying for our time.

On the other hand we're making life harder for future maintainers of the code base which may in fact be us!

I'd be keen to hear how others handle these types of situations because it feels like this trade off is quite a common one and the way we've dealt with it doesn't seem optimal.
