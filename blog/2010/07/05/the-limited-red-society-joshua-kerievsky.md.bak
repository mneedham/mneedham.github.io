+++
draft = false
date="2010-07-05 15:02:32"
title="The Limited Red Society - Joshua Kerievsky"
tag=['software-development']
category=['Software Development']
+++

I recently watched a presentation given by Joshua Kerievsky from the Lean Software & Systems conference titled '<a href="http://www.infoq.com/presentations/The-Limited-Red-Society">The Limited Red Society</a>' in which describes an approach to refactoring where we try to minimise the amount of time that the code is in a 'red' state.

This means that the <strong>code should be compiling and the tests green for as much of this time as possible </strong>.

I think it's very important to follow these principles in order to successfully refactor code on a project team and it's an approach that my colleague <a href="http://intwoplacesatonce.com/">Dave Cameron</a> first introduced me to when we worked together last year.

These are some of my observations and thoughts on the talk:

<ul>
<li>Kerievsky talks about <strong>parallel change</strong> which is where we want to make some changes to a bit of code and instead of changing it directly we create a parallel implementation and then gradually change the clients of that code to use the new approach.

An example of this which I wrote about last year was when we wanted to <a href="http://www.markhneedham.com/blog/2009/06/26/safe-refactoring-removing-object-initializer-introducing-builder/">move the creation of objects from using object initializer to the builder pattern</a>. Instead of doing it all in one go we had both approaches in the code base at the same time and gradually moved all the existing code to use the new approach. We also tried to use this approach to <a href="http://www.markhneedham.com/blog/2009/06/12/coding-dojo-17-refactoring-cruise-control-net/">change the API of one of the main objects in the CC.NET code in a dojo last year</a>.

Kent Beck talks about a similar approach in his QCon talk titled '<a href="http://www.infoq.com/presentations/responsive-design">Responsive Design</a>' from November 2008.
</li>
<li>
One interesting point that Josh made in the Q&A session is that there may be times when we don't necessarily want to go straight for parallel change - it might be easier to use a <strong>narrowed change</strong> approach first. 

With narrowed change we would first look to reduce the number of places where we have to make the change we want to make.

For example if we want to change an object to internally use a list instead of an array we could first isolate the places where we add to or retrieve from the data structure into methods. We would then call those methods instead of accessing the data structure directly.

This way we can reduce the number of places we need to change when we eventually change the array to a list.

I haven't used this approach before but will look to do so in future.</li>
<li>There was a discussion about <a href="http://www.markhneedham.com/blog/2009/12/10/tdd-big-leaps-and-small-steps/">small steps and big leaps</a> at the end where one of the attendees pointed out that it often takes much longer to take a small steps approach rather than just taking one big leap.

Josh pointed out that <strong>the appropriate choice depends on the risk involved in the refactoring situation </strong> - if it's low risk then perhaps it does make sense to just change the code in one go. However, an additional advantage of the small steps approach is that it makes it much easier to do a graceful retreat if the refactoring gets out of hand and we end up <a href="http://www.markhneedham.com/blog/2009/11/08/knowing-when-to-persevere-and-when-to-change-approach/">yak shaving</a>.</li></ul> 

Although I already knew some of the approaches shown in this video it's always interesting to see how experienced practitioners put them to use and there were a couple of new ideas that I hadn't come across before.

I particularly liked the fact that there was a 20 minute Q&A section at the end. The discussion is quite interesting to listen to.
