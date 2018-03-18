+++
draft = false
date="2009-10-13 07:00:53"
title="Scala: Code Kata #2 - Karate Chop - Array Slicing Attempt"
tag=['code-kata', 'scala']
category=['Code Katas', 'Scala']
+++

In my continued attempts to learn a bit of Scala I've been trying out <a href="http://codekata.pragprog.com/2007/01/kata_two_karate.html">the 2nd of Dave Thomas' code katas - Karate Chop</a> - while using an array slicing approach.

I've tried out the iterative approach to this problem in Java about a year ago and it ends up being quite verbose so I thought the array slicing one would be much more concise. 

I didn't drive any of the solutions I worked on from the tests - in fact I only got all the tests provided by Dave Thomas running right at the end which was probably a mistake in retrospect.

My first solution didn't really work at all - it resulted in an 'ArrayIndexOutOfBoundsException'  for pretty much any input where the 'needle' wasn't the middle value:


~~~scala

def chop(needle : Int, haystack : Array[Int]) : Int  = {
	val middleIndex = haystack.length / 2
	if(haystack(middleIndex) == needle)
		return middleIndex
	else if(haystack(middleIndex) < needle) 
		return chop(needle, haystack.slice(0, middleIndex))
	else
		return chop(needle, haystack.slice(middleIndex + 1, haystack.length))
}
~~~

It turns out that the logic is actually the wrong way around - if we find that 'haystack(middleIndex)' is less than 'needle' then we want to be looking at the 2nd half of the array and not the first half!

Attempt number two addressed this problem:


~~~scala

def chop(needle : Int, haystack : Array[Int]) : Int = {
	val midpoint = haystack.length/2
	val valueAtMidpoint = haystack(midpoint)

	if(valueAtMidpoint == needle) return midpoint
	else if(valueAtMidpoint > needle) return chop(needle, haystack.slice(0, midpoint))
	else return chop(needle, haystack.slice(midpoint, haystack.length))
}
~~~

The problem with this solution is that if the 'needle' is in the second half of the array then it will end up reporting us the wrong position with respect to the whole array - we will just get the position of the 'needle' in the remaining array. 

This suggested to me that I would probably need to make use of an inner function to keep track of how many items had been discarded whenever we realised that the item was in the second half of the array.

We could then add that value to the final index position if the 'needle' was found in the array:


~~~scala

def chop(needle : Int, haystack : Array[Int]) : Int = {	
	def chopInner(discardedItems : Int, innerHay : Array[Int]) : Int = {	
		val midpoint = innerHay.length/2
		val originalMidpoint = midpoint + discardedItems
		val valueAtMidpoint = innerHay(midpoint)

		if(valueAtMidpoint == needle)  
			originalMidpoint
		else if(valueAtMidpoint > needle)  
			chopInner(0, innerHay.slice(0, midpoint))
		else  
			chopInner(originalMidpoint, innerHay.slice(midpoint, innerHay.length))
	}
	chopInner(0, haystack)
}
~~~

This solution will find the position of 'needle' if that value exists in the 'haystack' but if the value isn't in the list we end up in an infinite recursion and if the list is empty then we end up with an 'ArrayIndexOutOfBoundsException' when we try to get the value of the midpoint.

My truly hacky solution which solves these two problems looks like this:


~~~scala

def chop(needle : Int, haystack : Array[Int]) : Int = {	
	def chopInner(discardedItems : Int, innerHay : Array[Int]) : Int = {	
		if(innerHay.length == 0) 	
			return -1
		
		val midpoint = innerHay.length/2
		val originalMidpoint = midpoint + discardedItems
		val valueAtMidpoint = innerHay(midpoint)

		if(valueAtMidpoint == needle)  
			originalMidpoint
		else if(valueAtMidpoint > needle)  
			chopInner(0, innerHay.slice(0, midpoint))
		else if(innerHay.length == 1)  
			-1
		else  
			chopInner(originalMidpoint, innerHay.slice(midpoint, innerHay.length))
	}
	chopInner(0, haystack)
}
~~~

I converted Dave Thomas' tests into '<a href="http://code.google.com/p/specs/">specs</a>' tests using the following regular expression:

Find:

~~~text

assert_equal\((.*),[ ]+chop\((.),[ ]+\[(.*)\]\)\)
~~~

Replace:

~~~test

chop($2, Array($3)) mustBe $1
~~~

I then adapted my colleague <a href="http://blog.magpiebrain.com/">Sam Newman's</a> <a href="http://code.google.com/p/bigvisiblewall/source/browse/">bigvisiblewall</a> project so that I could make use of the ant script he's setup which makes specs and ant play nicely together.

All the tests pass but there must be a cleaner solution than what I've ended up with - I think another attempt will be required!
