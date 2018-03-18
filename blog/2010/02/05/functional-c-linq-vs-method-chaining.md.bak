+++
draft = false
date="2010-02-05 18:06:28"
title="Functional C#: LINQ vs Method chaining"
tag=['c']
category=['.NET']
+++

One of the common discussions that I've had with several colleagues when we're making use of some of the higher order functions that can be applied on collections is whether to use the LINQ style syntax or to chain the different methods together.

I tend to prefer the latter approach although when asked the question after <a href="http://www.markhneedham.com/blog/2010/01/31/ddd8-mixing-functional-and-object-oriented-approaches-to-programming-in-c/">my talk at Developer Developer Developer</a> I didn't really have a good answer other than to suggest that it seemed to just be a personal preference thing.

<a href="http://www.twitter.com/damianpowell">Damian Marshall</a> suggested that he <strong>preferred the method chaining approach because it more clearly describes the idea of passing a collection through a pipeline where we can apply different operations to that collection</strong>.

I quite like that explanation and I think my preference for it would have probably been influenced by the fact that when coding in F# we can use the <a href="http://www.markhneedham.com/blog/2009/01/06/f-forward-operator/">forward piping operator</a> to achieve code which reads like this. 

For example if we had a list and wanted to get all the even numbers, double them and then add them up we might do this:


~~~ocaml

[1..10] |>
List.filter (fun x -> x % 2 = 0) |>
List.map (fun x -> x * 2) |>
List.fold (fun acc x -> acc + x) 0
~~~

If I was in C# I'd probably do this:


~~~csharp

Enumerable.Range(1, 10)
.Where(x => x % 2 == 0)
.Select(x => x * 2)
.Sum(x => x);
~~~

I found it quite difficult to work out what the equivalent LINQ syntax would be because I don't use it but I think something like this would be what you'd need to write to do the same thing:


~~~csharp

from x in Enumerable.Range(1, 10)
where x%2 == 0
select x * 2).Sum(x => x);
~~~

I'm not sure if there's a way to do the sum within the LINQ statement or whether you need to do it using the method as I have here.

Even just writing this example I found that the way I had to write the LINQ code seemed quite counter intuitive for me with the way that I typically try to solve problems like this.

At least now thanks to Damian I now understand why that is!
