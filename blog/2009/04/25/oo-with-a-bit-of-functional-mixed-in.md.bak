+++
draft = false
date="2009-04-25 11:14:12"
title="OO with a bit of functional mixed in"
tag=['oop', 'functional-programming']
category=['OOP']
+++

From my experiences playing around with F# and doing a bit of functional C# I'm beginning to think that the combination of functional and object oriented programming actually results in code which I think is more expressive and easy to work with than code written only with an object oriented approach in mind.

I'm also finding it much more fun to write code this way!

In a recent post Dean Wampler <a href="http://blog.objectmentor.com/articles/2009/04/20/is-the-supremacy-of-object-oriented-programming-over">questions whether the supremacy of object oriented programming is over</a> before going on to suggest that the future is probably going to be a mix of functional programming and object oriented programming. 

I agree with his conclusion but there are some things Dean talks about which I don't really understand:

<blockquote>
The problem is that there is never a stable, clear object model in applications any more. What constitutes a BankAccount or Customer or whatever is fluid. It changes with each iteration. It’s different from one subsystem to another even within the same iteration! I see a lot of misfit object models that try to be all things to all people, so they are bloated and the teams that own them can’t be agile. The other extreme is “balkanization”, where each subsystem has its own model. We tend to think the latter case is bad. However, is lean and mean, but non-standard, worse than bloated, yet standardized?
</blockquote>

I don't think an object model needs to be stable - for me the whole point is to iterate it until we get something that fits the domain that we're working in.

I'm not sure who thinks it's bad for each subsystem to have its own model - this is certainly an approach that I think is quite useful. Having the same model across different subsystems makes our life significantly more difficult. There are <a href="http://www.markhneedham.com/blog/2009/03/30/ddd-recognising-relationships-between-bounded-contexts/">several solutions for this</a> outlined in <a href="http://domaindrivendesign.org">Domain Driven Design</a>.

Dean goes on to suggest that in a lot of applications data is just data and that having that data wrapped in objects doesn't add much value.

I've worked on some projects which took that approach and I found the opposite to be true - if we have some data in an application it is very likely that there is going to be some sort of behaviour associated to it, meaning that it more than likely represents some concept in the business domain. I find it much easier to communicate with team mates about domain concepts if they're represented explicitly as an object instead of just as a hash map of data for example.

Creating objects also helps manage the complexity by hiding information and from my experience it's much <a href="http://www.markhneedham.com/blog/2009/03/12/oo-reducing-the-cost-oflots-of-stuff/">easier to make changes</a> in our code base when we've managed data & behaviour in this manner.

I think there is still a place for the functional programming approach though. <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">Functional collection parameters</a> for example are an excellent way to <strong>reduce accidental complexity</strong> in our code and removing useless state from our applications when performing operations on collections.

I don't think using this type of approach to coding necessarily means that we need to expose the state of our objects though - we can still make use of these language features within our objects. 

The most interesting thing for me about using this approach to some areas areas of coding when using C# is that you do need to change your mindset about how to solve a problem.

I typically solve problems with a procedural mindset where you just consider the next step you need to take sequentially to solve the problem. This can end up leading to quite verbose solutions.

The functional mindset seems to be more about considering the problem as a whole and then working out how we can simplify that problem from the outside in which is a bit of a paradigm shift. I don't think I've completely made but it can certainly lead to solutions which are much easier to understand.

The other idea of functional programming that I've been experimenting with is that of trying to keep <strong>objects as immutable as possible</strong>. This pretty much means that every operation that I perform on an object which would previously mutate the object now returns a new instance of it.

This is much easier in F# than in C# where you end up writing quite a lot of extra code to make that possible and can be a bit confusing if you're not used to that approach.

Sadek Drobi did a <a href="http://qconlondon.com/london-2009/presentation/Functional+Programming+with+a+Mainstream+Language">presentation at QCon London</a> where he spoke more about taking a functional programming approach on a C# project and while he's gone further than I have with the functional approach my current thinking is that we should model our domain and manage complexity with objects but when it comes to solving problems within those objects which are more algorithmic in nature the functional approach works better. 
