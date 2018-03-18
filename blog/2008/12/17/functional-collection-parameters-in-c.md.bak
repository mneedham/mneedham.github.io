+++
draft = false
date="2008-12-17 22:13:28"
title="Functional Collection Parameters in C#"
tag=['c', 'functional']
category=['.NET']
+++

While talking through my understanding of the Select method which can be applied to collections in C# with a colleague, it became clear that C# doesn't seem to use the same names for these type of operations as are used in the world of functional programming.

Coincidentally on the same day I came across Bill Six's post about using <a href="http://billsix.blogspot.com/2008/03/functional-collection-patterns-in-ruby.html">functional collection parameters in Ruby</a>, so I thought I'd see what the equivalent operations are in C#.

<h3>Map</h3>

Map evaluates a high order function on all the elements in a collection and then returns a new collection containing the results of the function evaluation.

In C# we can use the 'Select' method. For example, to capitalise all the items in a list:


~~~csharp

var someValues = new List<string> {"mark", "sydney", "sunny"};
var upperCaseValues = someValues.Select(item => item.ToUpper());
~~~

The responsibility for iterating the collection has been taken away from me and I can just focus on what I want to do with the collection rather than worrying too much about the details. A more declarative approach.

If I want to see the results of that operation I just do the following:


~~~csharp

upperCaseValues.ForEach(Console.WriteLine);
~~~


~~~text

MARK
SYDNEY
SUNNY
~~~

<h3>Filter</h3>

Filter applies a predicate against all of the elements in a collection and then returns a collection of elements which matched the predicate.

Conveniently there is actually a built in delegate called 'Predicate' which when combined with the 'FindAll' method can be used to solve this problem.


~~~csharp

var someValues = new List<string> {"mark", "sydney", "sunny"};
var valuesWithSIn = someValues.FindAll(item => item.Contains("s"));
valuesWithSIn.ForEach(Console.WriteLine);
~~~


~~~text

sydney 
sunny
~~~

If we just want the first value in the collection that matches the predicate we would use the 'Find' method instead:


~~~csharp

var someValues = new List<string> {"mark", "sydney", "sunny"};
var valueWithSIn = someValues.Find(item => item.Contains("s"));
Console.WriteLine(valueWithSIn);
~~~


~~~text

sydney
~~~

<h3>Reduce</h3>

Reduce applies a high order function against all the elements in a collection and then returns a single result.

We can use the 'Aggregate' method to achieve this:


~~~csharp

var someValues = new List<string> {"mark", "sydney", "sunny"};
var valuesConcatenated = someValues.Aggregate("",(accumulator, item) => accumulator + item);
Console.WriteLine(valuesConcatenated);
~~~


~~~text

marksydneysunny
~~~

The "" passed in as the first parameter to 'Aggregate' is the initial value for the accumulator.

<h3>Combining expressions</h3>
As with Ruby we can chain these expressions together to return even greater results.

For example, to get concatenate all the items which contain an s we would do the following:


~~~csharp

var someValues = new List<string> {"mark", "sydney", "sunny"};
var valuesConcatenated = someValues.FindAll(item => item.Contains("s"))
                                   .Aggregate("",(accumulator, item) => accumulator + item);
Console.WriteLine(valuesConcatenated);
~~~


~~~text

sydneysunny
~~~

<h3>Overall</h3>
I really like having this high order functions available to us - it has taken away the need to write some of the most boring code that we used to have to write and makes our code more concise and easier to read.
