+++
draft = false
date="2009-10-31 17:54:31"
title="Coding: Copy/Paste then refactor"
tag=['coding']
category=['Coding']
+++

We're currently reading Michael Feathers '<a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1256973419&sr=8-1">Working Effectively With Legacy Code</a>' in our <a href="http://www.markhneedham.com/blog/category/books/">technical book club</a> and one interesting technique which he describes in the Test Driven Development section is copying and pasting some existing code, changing the appropriate part to make the test pass before refactoring to remove the duplication we just created.

I can't remember coming across this approach previously but I found myself using it to solve a Scala problem last week.

I wanted to find the smallest number in a list having previously written the code to find the largest number in a list. 

This was the code I already had:


~~~scala

  def max(values : List[Int]) : Int = {
    def inner(remainingValues : List[Int], currentMax : Int) : Int = remainingValues match {
      case Nil => currentMax
      case head::tail if head > currentMax => inner(tail, head)
      case _::tail => inner(tail, currentMax)
    }
    inner(values, Math.MIN_INT)
  }
~~~

I figured finding the smallest value would be quite similar to that but I couldn't quite see where the duplication between the two functions was going to be.

I somewhat reluctantly found myself copying and pasting my way to the following code:


~~~scala

  def min(values : List[Int]) : Int = {
     def inner(remainingValues : List[Int], currentMin : Int) : Int = remainingValues match {
      case Nil => currentMin
      case head::tail if head < currentMin => inner(tail, head)
      case _::tail => inner(tail, currentMin)
    }
    inner(values, Math.MAX_INT)
  }
~~~

Having done that it became clearer that the duplication between the two functions was on line 4 where we do the comparison of values and on line 7 where we choose the initial max/min value.

My first attempt at refactoring was to try and pull out the comparator function on line 4:


~~~scala

def comparator(x : Int, y : Int, f : Function2[Int, Int, Boolean]) : Boolean = f(x,y)
~~~

Which resulted in the 'max' function looking like this:


~~~scala

  def max(values : List[Int]) : Int = {
    def inner(remainingValues : List[Int], currentMax : Int) : Int = remainingValues match {
      case Nil => currentMax
      case head::tail if comparator(head, currentMax, (x,y) => x > y) => inner(tail, head)
      case _::tail => inner(tail, currentMax)
    }
    inner(values, Math.MIN_INT)
  }
~~~

At this point I realised that I was doing the refactoring the wrong way around and that I should be trying to make 'max' and 'min' call another function while passing in the differences as parameters to that function.

I ended up with this common function:


~~~scala

   def findValue(values : List[Int], comparisonFunction : Function2[Int, Int, Boolean], startingValue : Int) : Int = {
    def inner(remainingValues : List[Int], current : Int) : Int = remainingValues match {
      case Nil => current
      case head::tail if comparisonFunction(head, current) => inner(tail, head)
      case _::tail => inner(tail, current)
    }
    inner(values, startingValue)
  }
~~~


~~~scala

  def max(values : List[Int]) : Int = findValue(values, (x,y) => x>y, Math.MIN_INT)
  def min(values : List[Int]) : Int = findValue(values, (x,y) => x<y, Math.MAX_INT)
~~~

I'm not sure whether the name 'findValue' is a very good one for the common function but I can't think of a better one at the moment.

The neat thing about this approach is that it made it much easier to <a href="http://www.markhneedham.com/blog/2009/08/30/coding-group-the-duplication-then-remove-it/">see where the duplication was</a> and I was able to have both the functions working before trying to do that refactoring. 

I'm not sure if there are built in functions to do these calculations. I looked quickly and couldn't find any and thought it would be an interesting exercise to write the code anyway.

It worked out much better than I thought it would.

