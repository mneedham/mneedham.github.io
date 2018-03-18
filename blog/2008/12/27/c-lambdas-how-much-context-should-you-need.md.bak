+++
draft = false
date="2008-12-27 23:15:31"
title="C# lambdas: How much context should you need?"
tag=['coding', 'net', 'lambdas']
category=['.NET']
+++

I had an interesting discussion with a colleague last week about the names that we give to variables inside lambda expressions which got me thinking about the context that we should need to hold when reading code like this.

The particular discussion was around an example like this:


~~~csharp

public class Foo
{
    private String bar;
    private String baz;

    public Foo(String bar, String baz)
    {
        this.bar = bar;
        this.baz = baz;
    }

    public override string ToString()
    {
        return string.Format("{0} - {1}", bar, baz);
    }

}
~~~


~~~csharp

var oneFoo = new Foo("bar", "baz");
var anotherFoo = new Foo("otherBar", "otherBaz");

new List<Foo> {oneFoo, anotherFoo}.Select(foo => foo.ToString().ToUpper()).ForEach(Console.WriteLine);
~~~

I suggested that we could just replace the 'foo' with 'x' since it was obvious that the context we were talking about was applying a function on every item in the collection.

My colleague correctly pointed out that by naming the variable 'x' anyone reading the code would need to read more code to understand that x was actually referring to every 'Foo' in the collection. In addition naming the variable 'x' is quite lazy and is maybe equally bad as naming normal variables x,y and z (unless they're loop indexes) since it is completely non descriptive. 

The only real argument I can think of for having it as 'x' is that it makes the code a bit more concise and for this particular example I had to change the name of my first Foo to be 'oneFoo' so that I could use the variable name 'foo' inside the block since other variables in the same method are accessible from the closure.

I'm not sure what the good practice is in this area. I've done a little bit of work with Ruby closures/blocks and the convention there seemed to be that using single letter variables for blocks was fine.

In this case the extra context wouldn't be that great anyway but I think trying to keep the necessary context that someone needs to remember as small as possible seems to be a reasonable rule to follow. 
