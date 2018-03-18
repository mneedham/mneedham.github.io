+++
draft = false
date="2009-06-16 18:55:38"
title="C#/F#: Using .NET framework classes"
tag=['c', 'net', 'f']
category=['.NET', 'F#']
+++

I was recently discussing F# with a couple of colleagues and one thing that came up is the slightly different ways that we might choose to interact with certain .NET framework classes compared to how we use those same classes in C# code.

One of those where I see potential for different use is the Dictionary class. 

In C# code when we're querying a dictionary to check that a value exists before we try to extract it we might typically do this:


~~~csharp

public string GetValueBy(string key) 
{
	var dictionary = new Dictionary<string, string>() { {"key", "value" } };

	if(dictionary.ContainsKey(key)) 
	{
		return dictionary[key];
	}	 
	return ""; // maybe we'd do something else here but for the sake of this we return the empty string
}	
~~~

There is an alternative way to do this but it makes use of the 'out' keyword so it's generally frowned upon.


~~~csharp

public string GetValueBy(string key)
{
	var dictionary = new Dictionary<string, string>() {{"key", "value"}};
	string value = "";
	dictionary.TryGetValue(key, out value);
	return value;
}
~~~

In F# when we make use of a method which effectively defines a second return parameter by using the 'out' keyword the return value of that method becomes a tuple containing that value.

For example when querying Dictionary:


~~~ocaml

open System.Collections.Generic
open System
open System.Globalization

let testDictionary = 
    let builder = new Dictionary<string, string>()
    builder.Add("key1", "value")
    builder

let getByKey key =
    let result, value =  testDictionary.TryGetValue(key)
    if(result) then value result else ""
~~~

The return type of TryGetValue is 'bool * string' in this case and by assigning that result to two different values we can get the appropriate values. This is certainly a time when <a href="http://www.markhneedham.com/blog/2009/06/02/f-tuples-dont-seem-to-express-intent-well/">tuples</a> are really useful for simplifying our code.

We could have made use of an 'out' parameter as we did in C# but I think it's much easier to just use the tuple. Dustin Campbell <a href="http://diditwith.net/2008/01/29/WhyILoveFResultTuples.aspx">describes the other ways we could extract a value from a dictionary on his blog</a>.

It's not significantly more concise code wise compared to the C# way of doing things although from a brief look at the way that the Dictionary code works in <a href="http://www.red-gate.com/products/reflector/">Reflector</a> theoretically we are making less calls to the underlying data structure to get the value from it. 

I tried timing 100,000 accesses to a dictionary with each approach to see if the total time would be significantly different but there wasn't any noticeable difference.

There are other 'Try...' methods defined in the base class library - DateTime for example has some more - which I've never used in C# so I'd be intrigued to see whether other languages that run on the CLR will make use of these methods.
