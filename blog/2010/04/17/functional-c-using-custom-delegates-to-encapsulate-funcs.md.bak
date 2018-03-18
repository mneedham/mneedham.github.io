+++
draft = false
date="2010-04-17 12:16:46"
title="Functional C#: Using custom delegates to encapsulate Funcs"
tag=['c']
category=['.NET']
+++

One of the problems that I've frequently run into when writing C# code in a more functional way is that we can often end up with 'Funcs' all over the place which don't really describe what concept they're encapsulating.

We had some code similar to this where it wasn't entirely obvious what the Func being stored in the dictionary was actually doing: 


~~~csharp

public class Calculator
{
	private Dictionary<string, Func<double, double, double>> lookups = new Dictionary<string, Func<double, double, double>>();

	public Blah()
	{
		lookups.Add("key", (input1, input2) => (input1 * 0.1) / input2);
	}
	...
}
~~~

<a href="https://twitter.com/christianralph">Christian</a> pointed out that we can create a named delegate (something I had completely forgotten!) so that it's a bit more obvious what exactly we're storing in the dictionary just by looking at the code.

We'd then end up with this code:


~~~csharp

public class Calculator
{
	private delegate double PremiumCalculation(double input1, double input2);

	private Dictionary<string, PremiumCalculation> lookups = new Dictionary<string, PremiumCalculation >();

	public Calculator()
	{
		lookups.Add("key", (input1, input2) => (input1 * 0.1) / input2);
	}
	...
}
~~~

Now it's pretty clear from just reading the declaration of 'lookups' what it's being used for without needing to go further into the code to understand that.

This is just a simple example but the problem becomes more obvious the more angle brackets we end up with in our dictionary definition and pulling those Funcs out makes the code much easier to understand.
