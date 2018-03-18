+++
draft = false
date="2010-04-20 07:08:09"
title="Functional C#: An imperative to declarative example"
tag=['c', 'net']
category=['.NET']
+++

I <a href="http://www.markhneedham.com/blog/2010/04/18/coding-another-outside-in-example/">wrote previously about how we've been working on some calculations</a> on my current project and one thing we've been trying to do is write this code in a fairly declarative way.

Since we've been test driving the code it initially started off being quite imperative and looked a bit like this:


~~~csharp

public class TheCalculator
{
	...
	public double CalculateFrom(UserData userData)
	{
		return Calculation1(userData) + Calculation2(userData) + Calculation3(userData);
	}

	public double Calculation1(UserData userData)
	{
		// do calculation stuff here
	}

	public double Calculation2(UserData userData)
	{
		// do calculation stuff here
	}
	...
}
~~~

What we have on line 7 is a series of calculations which we can put in a collection and then sum together:


~~~csharp

public class TheCalculator
{
	...
	public double CalculateFrom(UserData userData)
	{
		var calculations = new Func<UserData, double>[] { Calculation1, Calculation2, Calculation3 };

		return calculations.Sum(calculation => calculation(userData));
	}

	public double Calculation1(UserData userData)
	{
		// do calculation stuff here
	}
	...
}
~~~

We can <a href="http://www.markhneedham.com/blog/2010/04/17/functional-c-using-custom-delegates-to-encapsulate-funcs/">pull out a 'Calculation' delegate</a> to make that a bit more readable:


~~~csharp

public class TheCalculator
{
	private delegate double Calculation(UserData userData);

	public double CalculateFrom(UserData userData)
	{
		var calculations = new Calculation[] { Calculation1, Calculation2, Calculation3 };

		return calculations.Sum(calculation => calculation(userData));
	}
	...	
}
~~~

One of the cool things about structuring the code like this is that if we want to add a new Calculation we can just go to the end of the array, type in the name of the method and then Resharper will create it for us with the proper signature.

We eventually came across some calculations which needed to be subtracted from the other ones, which seems like quite an imperative thing to do!

Luckily <a href="http://twitter.com/christianralph">Christian</a> saw a way to wrap these calculations in a 'Subtract' function so that we could stay in declarative land:


~~~csharp

public class TheCalculator
{
	private delegate double Calculation(UserData userData);

	public double CalculateFrom(UserData userData)
	{
		var calculations = new [] { Calculation1, Calculation2, Calculation3, Subtract(Calculation4) };

		return calculations.Sum(calculation => calculation(userData));
	}
	...	
	public Calculation Subtract(Calculation calculation)
	{
		return userData => calculation(userData) * -1;
	}
}
~~~

Having a method which explicitly has the 'Calculation' signature allows us to remove it from the array declarative which is pretty neat.

We can also change the method signature of 'Subtract' to take in a variable number of calculations if we need to:


~~~csharp

public class TheCalculator
{
	...	
	public double CalculateFrom(UserData userData)
	{
		var calculations = new [] { Calculation1, Calculation2, Calculation3, Subtract(Calculation4, Calculation5) };

		return calculations.Sum(calculation => calculation(userData));
	}

	public Calculation Subtract(params Calculation[] calculations)
	{
		return userData => calculations.Sum(calculation =>  calculation(userData)) * -1;
	}
}
~~~

The other nice thing about coding it this way is that we ran into a problem where when we fed real data through the code we were getting the wrong values returned and we wanted to understand where it was falling down.

We could easily temporarily add in a 'Console.WriteLine' statement like this to help us out:


~~~csharp

public class TheCalculator
{
	...	
	public double CalculateFrom(UserData userData)
	{
		var calculations = new [] { Calculation1, Calculation2, Calculation3, Subtract(Calculation4, Calculation5) };

		return calculations
			.Select(calculation =>
					{
						Console.WriteLine(calculation.Method.Name + " = " + calculation(userData));
						return calculation;
					})
			.Sum(calculation => calculation(userData));
	}
	...
}
~~~

It then printed the results down the page like so:


~~~csharp

Calculation1: 23.34
Calculation2: 45.45
...
~~~
