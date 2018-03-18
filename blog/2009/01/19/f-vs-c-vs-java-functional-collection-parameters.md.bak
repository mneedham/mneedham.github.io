+++
draft = false
date="2009-01-19 19:24:25"
title="F# vs C# vs Java: Functional Collection Parameters"
tag=['c', 'java', 'f', 'functional-programming']
category=['.NET', 'Java']
+++

I wrote a post about a month ago on using <a href="http://www.markhneedham.com/blog/2008/12/17/functional-collection-parameters-in-c/">functional collection parameters</a> in C# and over the weekend <a href="http://fabiopereira.me/blog/">Fabio</a> and I decided to try and contrast the way you would do this in Java, C# and then F# just for fun.

<h3>Map</h3>

Map evaluates a high order function on all the elements in a collection and then returns a new collection containing the results of the function evaluation.

Given the numbers 1-5, return the square of each number

Java

~~~java

int[] numbers = { 1,2,3,4,5};
for (int number : numbers) {
    System.out.println(f(number));
}

private int f(int value) {
    return value*value;
}
~~~

C#

~~~csharp

new List<int> (new[] {1, 2, 3, 4, 5}.Select(x => x*x)).ForEach(Console.WriteLine);
~~~

F#

~~~text

[1..5] |> List.map (fun x -> x*x) |> List.iter (printfn "%d");;
~~~

<h3>Filter</h3>

Filter applies a predicate against all of the elements in a collection and then returns a collection of elements which matched the predicate.

Given the numbers 1-5, print out only the numbers greater than 3:

Java

~~~java

int[] numbers = { 1,2,3,4,5};
for (int number : numbers) {
    f(number);
}

private void f(int value) {
    if(value > 3) {
        System.out.println(value);
    }
}
~~~

C#

~~~csharp

new List<int> { 1,2,3,4,5}.FindAll(x => x > 3).ForEach(Console.WriteLine);
~~~

F#

~~~text

[1..5] |> List.filter (fun x -> x > 3) |> List.iter (printfn "%d");;
~~~

<h3>Reduce</h3>

Reduce applies a high order function against all the elements in a collection and then returns a single result.

Given a list of numbers 1-5, add them all together and print out the answer

Java

~~~java

int sum = 0;
int[] numbers = { 1,2,3,4,5};
for (int number : numbers) {
    sum += number;
}
System.out.println(sum);
~~~

C#

~~~java

Console.WriteLine(new[] {1, 2, 3, 4, 5}.Aggregate(0, (accumulator, x) => accumulator + x));
~~~

F#

~~~text

[1..5] |> List.fold_left (+) 0 |> printfn "%d";;
~~~

<h3>In Summary</h3>
I was surprised that we could achieve these results in relatively few lines of Java. The C# and F# versions are still more concise but the Java version isn't too bad. The <a href="http://commons.apache.org/collections/api-2.1.1/org/apache/commons/collections/CollectionUtils.html#select(java.util.Collection,%20org.apache.commons.collections.Predicate)">Apache Commons Library has a class</a> which allows you to write these in a functional way but the need to use anonymous methods means it's not as clean as what you can achieve in C# and F#.

I think there is still a bit of a mindset switch to make from thinking procedurally about these things to thinking in a way that allows you to make the most of functional programming concepts.

Keeping the code as declarative as possible and reducing the amount of state in our code are the most obvious things I have learned so far from playing with F#.

