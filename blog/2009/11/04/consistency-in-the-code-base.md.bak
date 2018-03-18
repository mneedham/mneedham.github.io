+++
draft = false
date="2009-11-04 21:39:28"
title="Consistency in the code base"
tag=['coding']
category=['Coding', 'Incremental Refactoring']
+++

I've had quite a few discussions with various different colleagues about coding consistency over the last year or so and <a href="http://www.thekua.com/atwork/2008/11/death-by-a-thousand-differences/">Pat</a> <a href="http://www.thekua.com/atwork/2009/02/what-differences-cause-your-project-death/">Kua </a>and <a href="http://blog.franktrindade.com/2008/10/17/we-need-standards/">Frank Trindade</a> have both written posts suggesting that we should look to have coding standards on projects in order to avoid the type of pain that having an inconsistent approach can lead to.

From what I've noticed there seem to be two reasons that we end up with inconsistent code on projects:

<ol>
<li>People's personal preferences for how certain bits of code should be written vary.</li>
<li>The team is trying to incrementally move towards an improved solution to a problem encountered but isn't completely there yet.</li>
</ol>

I think the first of these is the area which Frank and Pat are addressing in their posts.

However I think there is some overlap between the two. For example someone may rewrite a bit of code in their own style and while they would suggest that what they are doing is improving the code base their team mates may think that what they are doing is merely creating more inconsistency.

Potential coding inconsistency falls into three categories as I see it:

<h3>Personal Preferences</h3>
A simple example of this that we had on the last project I worked on was around how we should write simple conditional statements when used as <a href="http://c2.com/cgi/wiki?GuardClause">guard clauses</a>.

These were the 3 different ways that people preferred and we had all the different styles across the code base!


~~~csharp

public String SomeMethod()
{
	if(SomeCondition()) return "hello";
}
~~~


~~~csharp

public String SomeMethod()
{
	if(SomeCondition()) 
		return "hello";
}
~~~


~~~csharp

public String SomeMethod()
{
	if(SomeCondition()) 
	{
		return "hello";
	}
}
~~~

We eventually agreed to use the last one because it was the least controversial choice and although people who preferred the other two approaches thought it was too verbose they were fine with using that as a compromise.

<a href="http://www.thekua.com/atwork/2009/02/what-differences-cause-your-project-death/">Pat covers a lot of the other types of code</a> that I would classify as being linked to personal preference and I think that it would be beneficial to have coding standards/agreement in the team for the patterns we favour/names we're going to use in this area.

It's way easier to just go and write code in your own personal style and I do this way too frequently but it's much better for the team if we follow a common style.

<h3>Improving the code but perhaps not significantly</h3>

I've written previously about the way that we've been making use of a '<a href="http://www.markhneedham.com/blog/2009/06/02/coding-putting-code-where-people-can-find-it/">GetBuilderFor</a>' class to hang our test builders off and while this worked quite well <a href="http://www.markhneedham.com/blog/2009/08/15/builders-hanging-off-class-vs-builders-in-same-namespace/">there is a better way</a> to do this which requires less code being written overall.

We can make use of C#'s object initializer syntax to setup fields with values instead of having to create methods to do that and we don't need to write the code to make the builder hang off 'GetBuilderFor'.

As long as we put all the builders in the same namespace we can just type 'new BuilderNameSpace.' and then the IDE will show us the choices of builder that we have.

The problem we experienced was that that we already had 30-40 builders written using the 'GetBuilderFor' approach and there wasn't a significant advantage to be gained by going and rewriting all that code to use the new approach.

In the interests of consistency we therefore decided to keep using the 'GetBuilderFor' approach even though the next time I come across this problem I'd definitely favour the other approach.

Reg Braithwaite has a really interesting post in which he talks about '<a href="http://weblog.raganwald.com/2008/05/narcissism-of-small-code-differences.html">the narcissism of small code differences</a>' and how different authors 'improve' the code by adding their own personal touch.

I think he describes the type of code changes that I would classify in this and the previous category although it does make me wonder where the line between refactoring and adding your own personal touch to a piece of code lies. 

<h3>Improving the code significantly</h3>
These are the code changes that may create inconsistency but help us to drive a design improvement which will have a big impact on the way we work.

An example of this that we had on my last project was moving <a href="http://www.markhneedham.com/blog/2008/12/28/internalexternal-domain-models/">our 'domain' model from being defined in WCF messages</a> to being defined independently of other layers in the system.

We wanted to make this change to make the dependency between our code base and the service layer more loosely coupled and we started making that change around about February.

It took maybe a month to move the most awkward parts across since we did it bit by bit in an incremental way rather than stopping everything and making that change.

Along the way the code in these areas was in an inconsistent state and anyone looking at the code base who didn't know the reason why it was like that would think it was truly insane! 

Even now there are still bits of code which are more reminiscent of the old approach than the new and these tend to get changed when people are working in that area.

I think this type of inconsistency is somewhat inevitable if we're incrementally making improvements to our code base or <a href="http://www.informit.com/articles/article.aspx?p=1235624&seqNum=6">following the boy scout rule</a> as Uncle Bob puts it.

<h3>In Summary</h3>
These are my current observations on coding inconsistency but I'm sure there are other factors which can affect this as well.

I think we should look to reduce the inconsistencies in the first two categories as much as possible and ensure that everyone is driving towards the same outcome with respect to the last category.
