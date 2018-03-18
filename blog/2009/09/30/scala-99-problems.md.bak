+++
draft = false
date="2009-09-30 23:39:16"
title="Scala: 99 problems"
tag=['scala']
category=['Scala']
+++

My colleague <a href="http://lizdouglass.wordpress.com/">Liz Douglass</a> and I have been playing around with Scala and Liz recently pointed out Phil Gold's '<a href="http://aperiodic.net/phil/scala/s-99/">Ninety Nine Scala Problems</a>' which we've been working through. 

One in particular which is quite interesting is number 7 where we need to flatten a nested list structure.

Therefore given this input:


~~~scala

flatten(List(List(1, 1), 2, List(3, List(5, 8))))
~~~

We would expect this output:


~~~scala

res0: List[Any] = List(1, 1, 2, 3, 5, 8)
~~~

I tried this out on my own using recursion but kept ending up creating a stack overflow by writing code that never terminated!

We decided to try it out while pairing together using a more imperative approach so that we could get something that actually worked to begin with and ended up with this:


~~~scala

def flatten[A](list : List[A]) : List[A] =  {

	var flattenedList : List[A] = Nil
	for(item <- list) {
		item match {
		   case x : List[A] => flattenedList = flatten(x) ::: flattenedList
           case _    => flattenedList = item :: flattenedList
		}
	}
	flattenedList
}
~~~

It works and we've got a bit of recursion going on but we're still mutatating the state of a variable so it feels like we're missing out on the strength of a language which provides us with the ability to work in a functional way.

Our second attempt made use of the knowledge we gained from this first attempt with respect to that cases that existed for flattening the list and we made use of a technique which I picked up while learning a bit of F# - the inner function which keeps an accumulator with the flattened list on each recursion:


~~~scala

def flatten[A](list : List[A]) : List[A] = {
	def flat[A](rest : List[A], flattenedList : List[A]) : List[A] = rest match {
			case Nil => flattenedList
			case (head:List[A])::tail =>  flat(tail, flat(head, List()) ::: flattenedList)
			case head::tail => flat(tail, head :: flattenedList) 		
	}
	
	flat(list, Nil).reverse
}
~~~

I like the fact that we don't have to mutate any state with this solution but the second case statement is pretty difficult to understand.

We had to distinguish between whether the head of the list was another list or just an element in order to determine whether we needed to break that value down further or just add it to the new list.

Is there a better way to do that than to explicitly state the type of head as we've done here?

Another colleague, Ben Barnard, came over to work with us on the next iteration of this solution which was somewhat driven by seeing how Phil Gold had solved the kth item problem for which he describes a solution which narrows down the initial list each time while still calling the same function:


~~~scala

  def nth[T](n: Int, l: List[T]): T = (n, l) match {
    case (0, e :: _   ) => e
    case (n, _ :: tail) => nth(n - 1, tail)
    case (_, Nil      ) => throw new NoSuchElementException
  }
~~~

In this case when we reduce the list we are searching on we also reduce the index that we are looking for by one which works quite nicely.

For the flatten function we were able to recurse on the original function by running the list back through the flatten function whenever we didn't know if the 'head' was an element:


~~~scala

def flatten[A](list : List[A]) : List[A] = list match {
	case Nil => list
	case (head:List[A])::tail => flatten(head) ::: flatten(tail)
	case head::tail => head :: flatten(tail)
}
~~~

The nice thing about this solution is that the list is in the correct order at the end so we don't need to reverse it as we did with the previous solutions. 

This way of coding is still not quite intuitive to me but I think the solution is cleaner and easier to read than the others. 
