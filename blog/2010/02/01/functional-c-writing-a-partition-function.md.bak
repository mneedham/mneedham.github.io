+++
draft = false
date="2010-02-01 23:34:02"
title="Functional C#: Writing a 'partition' function"
tag=['c', 'net', 'functional-programming']
category=['.NET']
+++

One of the more interesting higher order functions that I've come across while playing with F# is the partition function which is similar to the filter function except it returns the values which meet the predicate passed in as well as the ones which don't.

I came across an interesting problem recently where we needed to do exactly this and had ended up taking a more imperative for each style approach to solve the problem because this function doesn't exist in C# as far as I know.

In F# the function makes use of a tuple to do this so if we want to create the function in C# then we need to define a tuple object first.


~~~csharp

public class Tuple<TFirst, TSecond>
{
	private readonly TFirst first;
	private readonly TSecond second;

	public Tuple(TFirst first, TSecond second)
	{
		this.first = first;
		this.second = second;
	}

	public TFirst First
	{
		get { return first; }
	}

	public TSecond Second
	{
		get { return second; }
	}
}
~~~


~~~csharp

public static class IEnumerableExtensions
{
	public static Tuple<IEnumerable<T>, IEnumerable<T>> Partition<T>(this IEnumerable<T> enumerableOf, Func<T, bool> predicate)
	{
		var positives = enumerableOf.Where(predicate);
		var negatives = enumerableOf.Where(e => !predicate(e));
		return new Tuple<IEnumerable<T>, IEnumerable<T>>(positives, negatives);

	}
}
~~~

I'm not sure of the best way to write this function - at the moment we end up creating two iterators to cover the two different filters that we're running over the collection which seems a bit strange.

In F# 'partition' is on List so the whole collection would be evaluated whereas in this case we're still only evaluating each item as it's needed so maybe there isn't a way to do it without using two iterators.

If we wanted to use this function to get the evens and odds from a collection we could write the following code:


~~~csharp

var evensAndOdds = Enumerable.Range(1, 10).Partition(x => x % 2 == 0);

var evens = evensAndOdds.First;
var odds = evensAndOdds.Second;
~~~

The other thing that's nice about F# is that we can assign the result of the expression to two separate values in one go and I don't know of a way to do that in C#.


~~~ocaml

let evens, odds = [1..10] |> List.partition (fun x -> x % 2 = 0)
~~~

We don't need to have the intermediate variable 'evensAndOdds' which doesn't really add much to the code. 

I'd be interested in knowing if there's a better way to do this than what I'm trying out.
