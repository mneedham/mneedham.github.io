+++
draft = false
date="2010-01-20 22:45:55"
title="Functional collectional parameters: Some thoughts"
tag=['c', 'net']
category=['Coding', 'Hibernate']
+++

I've been reading through a bit of Steve Freeman and Nat Pryce's '<a href="http://www.amazon.com/gp/product/0321503627?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321503627">Growing Object Oriented Software guided by tests</a>' book and I found the following observation in chapter 7 quite interesting:

<blockquote>
When starting a new area of code, we might temporarily suspend our design judgment and just write code without attempting to impose much structure. 
</blockquote>

It's interesting that they don't try and write perfect code the first time around which is actually something I thought experienced developers did until I came across Uncle Bob's <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Clean Code</a> book where he suggested something similar.

One thing I've noticed when working with collections is that if we want to do something more complicated than just doing a simple map or filter then I find myself initially trying to work through the problem in an imperative hacky way.

When pairing it sometimes also seems easier to talk through the code in an imperative way and then after we've got that figured out then we can work out a way to solve the problem in a more declarative way by making use of <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">functional collection parameters</a>.

An example of this which we came across recently was while looking to parse a file which had data like this:


~~~text

some,random,data,that,i,made,up
~~~

The file was being processed later on and the values inserted into the database in field order. The problem was that we had removed two database fields so we needed to get rid of the 2nd and 3rd values from each line.



~~~csharp

var stringBuilder = new StringBuilder();
using (var sr = new StreamReader("c:\\test.txt"))
{
    string line;
    
    while ((line = sr.ReadLine()) != null)
    {
        var values = line.Split(',');

        var localBuilder = new StringBuilder();
        var count = 0;
        foreach (var value in values)
        {
            if (!(count == 1 || count == 2))
            {
                localBuilder.Append(value);
                localBuilder.Append(",");
            }
            count++;
        }

        stringBuilder.AppendLine(localBuilder.ToString().Remove(localBuilder.ToString().Length - 1));
    }
}

using(var writer = new StreamWriter("c:\\newfile.txt"))
{
    writer.Write(stringBuilder.ToString());
    writer.Flush();
}
~~~

If we wanted to refactor that to use a more declarative style then the first thing we'd look to change is the for loop populating the localBuilder.

We have a temporary 'count' variable which is keeping track of which column we're up to and suggests that we should be able to use one of the higher order functions over collection which allows us to refer to the index of the item.

In this case we can use the 'Where' function to achieve this:


~~~csharp

...
while ((line = sr.ReadLine()) != null)
{
    var localBuilder = line.Split(',').
                        Where((_, index) => !(index == 1 || index == 2)).
                        Aggregate(new StringBuilder(), (builder, v) => builder.Append(v).Append(","));

    stringBuilder.AppendLine(localBuilder.ToString().Remove(localBuilder.ToString().Length - 1));
}
~~~

I've been playing around with 'Aggregate' a little bit and it seems like it's quite easy to overcomplicate code using that. It also seems that when using 'Aggregate' it makes sense if the method that we call on our seed returns itself rather than void.

I didn't realise that 'Append' did that so my original code was like this:


~~~csharp

    var localBuilder = line.Split(',').
                        Where((_, index) => !(index == 1 || index == 2)).
                        Aggregate(new StringBuilder(), (builder, v) => {
                           builder.Append(v);
                           builder.Append(",");
                           return builder;
                        });
~~~

I think if we end up having to call functions which return void or some other type then it would probably make sense to add on an extension method which allows us to use the object in a fluent interface style.

Of course this isn't the best solution since we would ideally avoid the need to remove the last character to get rid of the trailling comma which could be done by creating an array of values and then using 'String.Join' on that. 

Given that I still think the solution written using functional collection parameters is easier to follow since we've managed to get rid of two variable assignments which weren't interesting as part of what we wanted to do but were details about that specific implementation.

