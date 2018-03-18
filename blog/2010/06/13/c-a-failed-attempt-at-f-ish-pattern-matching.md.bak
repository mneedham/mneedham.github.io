+++
draft = false
date="2010-06-13 22:35:14"
title="C#: A failed attempt at F#-ish pattern matching"
tag=['c', 'f']
category=['.NET', 'F#']
+++

A few weeks ago we had some <a href="http://www.markhneedham.com/blog/2010/04/20/functional-c-an-imperative-to-declarative-example/">C# code around calcuations</a> which had got a bit too imperative in nature.

The code looked roughly like this:


~~~csharp

public class ACalculator
{
	public double CalculateFrom(UserData userData)
	{
		if(userData.Factor1 == Factor1.Option1)
		{
			return 1.0;
		}

		if(userData.Factor2 == Factor2.Option3)
		{
			return 2.0;
		}

		if(userData.Factor3 == Factor3.Option2)
		{
			return 3.0
		}
		return 0.0;
	}
}
~~~

I think there should be a more object oriented way to write this code whereby we push some of the logic onto the 'UserData' object but it struck me that it reads a little bit like <a href="http://www.markhneedham.com/blog/2010/01/12/f-refactoring-to-pattern-matching/">pattern matching code you might see in F#</a>.

I decided to drive the code to use a dictionary which would store functions representing each of the conditions in the if statements:


~~~csharp

public class ACalculator
{
	private Dictionary<Func<UserData, bool>, double> calculations;
	
	public ACalculator()
	{
    		calculations = new Dictionary<Func<UserData,bool>,double>
                       {
                           {u => u.Factor1 == Factor1.Option1, 1.0},
                           {u => u.Factor2 == Factor2.Option3, 2.0},                                       
                           {u => u.Factor3 == Factor3.Option2, 3.0}                                 
                       };	
	}	

	public double CalculateFrom(UserData userData)
	{
    		var calculation = calculations.Keys.FirstOrDefault(calc => calc(userData));
    		if(calculation != null)
    		{
        		return calculations[calculation];
    		}

    		return 0.0;
	}
}
~~~

It's less readable than it was before and it's not obvious that the adding of the functions to the dictionary needs to be in that order in order for it to work.

I've simplified the real example a bit to show the idea but I don't think it works as the best abstraction in this situation either way although it was an interesting experiment.
