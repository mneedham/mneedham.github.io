+++
draft = false
date="2010-05-13 07:00:18"
title="Evolving a design: Some thoughts"
tag=['software-development']
category=['Software Development']
+++

Phil wrote <a href="http://fragmental.tw/2010/05/09/agile-anti-patterns-democratic-design/">an interesting post recently about the Ubuntu decision making process with respect to design</a> and suggested that we should look to follow something similar on agile software development teams.

The Ubuntu design process basically comes down to this:

<blockquote>
This is not a democracy. Good feedback, good data, are welcome. But we are not voting on design decisions.
</blockquote>

Phil suggests the following:

<blockquote>
That doesn’t mean that there is an Architect (capital A, please), designing the system for the less-skilled developers to write. Architecture is an ongoing thing; team members make architecture decisions every day.

What that means is that, every time a design decision has to be made, the decision must come from an individual or very small group of people that have the skills and experience required –excluding coaching and teaching, of course.
</blockquote>

I agree with this to an extent.

At a higher level it does make sense that the Tech Lead of the team makes the decisions on the general direction of the code but when it comes down to specifics of a certain part of an application I don't know how well this works. 

If they aren't actually working in that part then it can be very difficult to make a decision about how it should be designed. 

<h3>Evolving a design</h3>

From my experience it's often the case that the pair working in that area is best placed to evolve the design.

The tech lead on a team can make a suggestion about the way that they want that part of the system to be designed but if it evolves slightly differently then I think that's still fine and we don't need to re-discuss it and check that they agree with that evolution.

For example <a href="http://twitter.com/dermotkilroy">Dermot</a> and I were working on a bit of code that is used to validate forms and the original design that we had quite tightly coupled the form creation and the adding of validators to each of the fields.


~~~csharp

public class FormFactory 
{
	public AForm CreateWithValidation(UserData userData)
	{
		...
	}
}
~~~

We had a requirement to validate the same form in a different context which had never happened previously so we had to change the design.

When we talked about this problem abstractly it seemed that the easiest way to do this was to add another method to the object which would create a form with validation for the new context.

We started trying to do that but as we did so it became really obvious that it would make our life easier if we split the form creation and adding of validators - we would be driving towards the builder pattern.

That was a decision that was made while in the code and it wasn't clear that the code would end up going that way when we discussed it beforehand.

I think it's fine for a pair to make this type of decision.

<h3>Tech lead facilitating design</h3>

I spoke to Phil about this and he suggested that what will often happen is that the tech lead will act as a facilitator and help the pair address all the issues of the part of the system that they're designing.

I like this way of describing the approach better as it ensures that the design we come up with will be compatible with any upcoming requirements - which the tech lead would be more aware of - and the other developers still have input on the way that the code is designed.

From my experience if the tech lead makes these decisions without being seen to take into consideration the opinions of the others on the team then it will quickly create a culture where developers on the team stop thinking about design problems and just delegate their thinking to the tech lead.

Equally as they won't have any buy in they'll probably be secretly hoping the design fails rather than looking for ways that it can evolve successfully. 

The facilitation approach helps address this.
