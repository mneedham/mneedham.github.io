+++
draft = false
date="2009-02-25 23:12:57"
title="C#: Wrapping DateTime"
tag=['c', 'net']
category=['.NET']
+++

I think it was <a href="http://darrenhobbs.com/">Darren Hobbs</a> who first introduced me to the idea of wrapping dates in our system to describe what that date actually means in our context, and after suffering the pain of passing some unwrapped dates around our code I think I can safely say that wrapping them is the way to go.

The culprit was a date of birth which was sometimes being created from user input and sometimes being retrieved from another system.

The initial (incorrect) assumption was that we would be passing around the date in the same string format and there was no point wrapping the value as we were never doing anything with the data.

It proved to be a bit of a nightmare trying to work out which state the data of birth was in various parts of the application and we ended up doing conversions to the wrong format and then undoing those and losing the formatting in other places!

Step 1 here was clearly not to pass around the date as a string but instead to convert it to a DateTime as soon as possible. 

This is much more expressive but we can take this one step further by wrapping that date time in a DateOfBirth class.


~~~csharp

public class DateOfBirth 
{
	private DateTime? dateOfBirth

	public DateOfBirth(DateTime? dateOfBirth) 
	{
		this.dateOfBirth = dateofBirth;
	}

	public string ToDisplayFormat()
	{
		return dateOfBirth == null ? "" : dateOfBirth.Value.ToString("dd MMM yyyy");
	}
}
~~~

When we want to display this object on the page we just have to call the ToDisplayFormat() and if that date format needs to change then we have only one place to make that change. Creating this class removed at least 3 or 4 'DateTime.Parse(...)' and 'DateTime.ToString(...)' calls throughout the code.

Now we could achieve the same functionality using an extension method on DateTime? but it's not as expressive as this in my opinion. It is also really obvious when looking at the code to know what type we are dealing with and it is really obvious when reading this class which method we will use to get the format to display to the user.

I will certainly be looking to wrap any DateTimes I come across in future.
