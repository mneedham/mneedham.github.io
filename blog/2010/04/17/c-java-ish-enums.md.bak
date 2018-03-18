+++
draft = false
date="2010-04-17 10:33:16"
title="C#: Java-ish enums"
tag=['net']
category=['.NET']
+++

We've been writing quite a bit of code on my current project trying to encapsulate user selected values from drop down menus where we then want to go and look up something in another system based on the value that they select.

Essentially we have the need for some of the things that a Java Enum would give us but which a C# one doesn't!

Right now we have several classes similar to the following in our code base to achieve this:


~~~csharp

public class CustomerType
{
    public static readonly CustomerType Good = new CustomerType("Good", "GoodKey");
    public static readonly CustomerType Bad = new CustomerType("Bad", "BadKey");

    private readonly string displayValue;
    private readonly string key;
    private static readonly CustomerType[] all = new[] { Good, Bad };

    private CustomerType(string displayValue, string key)
    {
        this.displayValue = displayValue;
        this.key = key;
    }

    public static CustomerType From(string customerType)
    {
        return all.First(c => c.displayValue == customerType);
    }

    public static string[] Values
    {
        get { return all.Select(c => c.DisplayValue).ToArray(); }
    }

    public string DisplayValue
    {
        get { return displayValue; }
    }

    public string Key
    {
        get { return key; }
    }
}
~~~

To get values to display in drop downs on the screen we call the following property in our controllers:


~~~csharp

CustomerType.Values
~~~

And to map from user input to our type we do this:


~~~csharp

CustomerType.From("Good")
~~~

Right now that will blow up if you trying to parse a value that doesn't have an instance associated with it.

<a href="https://twitter.com/christianralph">Christian</a> came up with the idea of storing each of the public static fields in an array and then using 'First' inside  the 'From' method to select the one that we want. 

We previously had a somewhat over complicated dictionary with the display value as the key and type as the value and looked it up that way.

So far this does all that we need to do and the only annoying thing is that if we add a new instance then we need to manually add it to the 'all' array. 

An alternative would be to do that using reflection which I think would work but it's simple enough like this so we haven't taken that approach yet.
