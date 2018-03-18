+++
draft = false
date="2009-11-08 20:44:18"
title="Coding: The agent noun class"
tag=['coding']
category=['Coding']
+++

I refer quite frequently to a post written by my colleague Peter Gillard Moss where he describes the <a href="http://jupitermoonbeam.blogspot.com/2008/09/agent-nouns-are-code-smells.html">agent noun code smell for class names</a>.

An agent noun is <a href="http://en.wikipedia.org/wiki/Agent_noun">defined by Wikipedia</a> as:

<blockquote>
In linguistics, an agent noun (or nomen agentis) is a word that is derived from another word denoting an action, and that identifies an entity that does that action. 
</blockquote>

Some typical examples of this are classes which end in the name 'Manager', 'Retriever', 'Helper' or even 'Controller' <a href="http://www.lixo.org/archives/2008/09/12/opportunity-makes-the-thief/">as Carlos points out</a>.

It's often the case that these classes better describe a method which belongs on another object and I quite like Peter's idea that agent nouns are useful for describing the <a href="http://www.markhneedham.com/blog/2009/10/18/coding-role-based-interfaces/">roles that our objects carry out</a>. 

We came across an interesting problem related to this a while ago where we wanted to calculate the age of a given customer and then send that data to another web page where it would be displayed.

The date of birth was an attribute on the 'Customer' object and we didn't need any of the other attributes of a customer on this web page so my first thought was that we needed an 'AgeCalculator' class.


~~~csharp

public class AgeCalculator 
{
	private readonly IClock clock;

	public AgeCalculator(IClock clock)
	{
		this.clock = clock;
	}

	public int CalculateAge(DateTime dataOfBirth)
	{
		// do some calculation with clock & date of birth here
	}
}
~~~


~~~csharp

public void SomeMethod()
{
	var age = new AgeCalculator(new Clock()).CalculateAge(customer.DateOfBirth);
	// and so on 
}
~~~

This approach worked quite well as it allowed us to easily test the age calculation logic in isolation and we could then pass on the age returned to the web page.

The thing I didn't like about this solution is that it seems a lot like an agent noun class. 

The giveaway in this case is that the method name is just a variation on the class name. This suggests that this behaviour belongs on another object instead.

It's not as object oriented as it could be but it doesn't seem as bad as some of the other examples such as classes ending in 'Manager' since this object is only solving one problem and we do have calculators in real life.

Some colleagues suggested that perhaps age should be an attribute on the customer which does seem to be a better place for this logic to reside.

On the other hand age isn't used anywhere else in the application and we don't need any of the other attributes of customer as I mentioned earlier.

I'm not sure what the 'right' solution is but there seem to be a few different potential approaches:

<ul>
<li>Should age be an attribute of the customer? There could be a tiny type 'Age' which does the above logic.</li>
<li>Should we have a role/interface 'ICalculateAges' which the customer implements?</li>
<li>Should we just keep the 'AgeCalculator'?</li>
<li>Is there some other solution that I'm not seeing?!</li>
</ul>


--

In reality after we'd discussed all these alternatives it turned out that the requirement was slightly wrong and that we actually needed to send down the date of birth and not the age. 

I still think it's an interesting problem though and one that I'm bound to come across again!

