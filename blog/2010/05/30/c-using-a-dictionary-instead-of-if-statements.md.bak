+++
draft = false
date="2010-05-30 23:13:25"
title="C#: Using a dictionary instead of if statements"
tag=['c']
category=['.NET']
+++

A problem we had to solve on my current project is how to handle form submission where the user can click on a different button depending whether they want to go to the previous page, save the form or go to the next page.

An imperative approach to this problem might yield code similar to the following:


~~~csharp

public class SomeController
{
	public ActionResult TheAction(string whichButton, UserData userData)
	{
		if(whichButton == "Back")
		{
			// do the back action
		}
		else if(whichButton == "Next")
		{
			// do the next action
		}
		else if(whichButton == "Save")
		{
			// do the save action
		}

		throw Exception("");
	}
}
~~~

A neat design idea which my colleague <a href="http://twitter.com/dermotkilroy">Dermot Kilroy</a> introduced on our project is the idea of using a dictionary to map to the different actions instead of using if statements.


~~~csharp

public class SomeController
{
	private Dictionary<string, Func<UserData,ActionResult>> handleAction = 
		new Dictionary<string, Func<UserData,ActionResult>>
		{ { "Back", SaveAction },
		  { "Next", NextAction },
		  { "Save", SaveAction } };

	public ActionResult TheAction(string whichButton, UserData userData)
	{
		if(handleAction.ContainsKey(whichButton))
		{
			return handleAction[whichButton](userData);
		}

		throw Exception("");
	}

	private ActionResult NextAction(UserData userData)
	{
		// do cool stuff
	}
}
~~~
It's quite similar in a way to a problem we had on another project where we needed to <a href="http://www.markhneedham.com/blog/2010/01/15/c-a-functional-solutional-to-a-modeling-problem/">deal with user inputs and then create an object appropriately</a>.

The way we have to read the code is a bit more indirect than with the original approach since you now need to click through to the individual methods for each action.

On the other hand I like the fact that we don't have if statements all over the place anymore.

* Updated * - updated to take Dhananjay Goyani's comments into account
