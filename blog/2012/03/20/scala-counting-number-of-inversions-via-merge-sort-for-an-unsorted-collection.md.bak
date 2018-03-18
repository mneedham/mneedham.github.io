+++
draft = false
date="2012-03-20 06:53:18"
title="Scala: Counting number of inversions (via merge sort) for an unsorted collection"
tag=['scala', 'algo-class']
category=['Scala']
+++

The first programming questions of <a href="https://www.coursera.org/algo/class/index">algo-class</a> requires you to calculate the number of inversions it would take using merge sort to sort a collection in ascending order.

I found quite <a href="http://www.cp.eng.chula.ac.th/~piak/teaching/algo/algo2008/count-inv.htm">a nice explanation here too</a>:

<blockquote>
Finding "similarity" between two rankings. Given a sequence of n numbers 1..n (assume all numbers are distinct). Define a measure that tells us how far this list is from being in ascending order.  The value should be 0 if a_1 < a_2 < ... < a_n and 
should be higher as the list is more "out of order".

e.g.

2 4 1 3 5

1 2 3 4 5

The sequence 2, 4, 1, 3, 5 has three inversions (2,1), (4,1), (4,3).
</blockquote>

The simple/naive way of solving this problem is to iterate through the collection in two loops and compare each value and its current index with the others, looking for ones which are not in the right order.

I wrote the following Ruby code which seems to do the job:


~~~ruby

def number_of_inversions(arr)
  count = 0
  arr.each_with_index do |item_a, index_a|
    arr.each_with_index do |item_b, index_b|
      if index_b >= index_a && item_a > item_b
        count +=1
      end
    end 
  end
  count
end
~~~


~~~text

>> number_of_inversions [6,5,4,3,2,1]
=> 15
~~~

That works fine for small collections but since we're effectively doing nested for loops it actually takes O(n&sup2;) time which means that it pretty much kills my machine on the sample data set of 100,000 numbers.  

An O(n log(n)) solution is explained in the lectures which involves recursively splitting the collection in half (like in merge sort) and then counting how many elements remain in the left collection when we select an item from the right collection since this will tell us how many positions/inversions out of place that element is.

e.g. if we're trying to work out how many inversions in the collection [1,3,5,2,4,6] we eventually end up merging [1,3,5] and [2,4,6]

<ul>
<li>Our first iteration puts '1' from the left collection into the new array.</li>
<li>The second iteration puts '2' from the right collection into the new array and there are two elements left in the left collection ('3' and '5') so we have 2 inversions (3,2 and 5,2).</li>
<li>Our third iteration puts '3' from the left collection into the new array.</li>
<li>Our fourth iteration puts '4' from the right collection into the new array and there is one element left in the left collection ('5') so we have 1 inversion (5,4)</li>
<li>Our fifth iteration puts '5' from the left collection and the sixth puts '6' from the right collection in.</li>
</ul>

The number of inversions for that example is therefore 3.

My colleague <a href="https://twitter.com/#!/anagri">Amir</a> and I decided to try and write some Scala code to do this and ended up with the following adapted merge sort:


~~~scala

import io.Source

object MSort {
  def main(args:Array[String]) {
    val fileWithNumbers = "/Users/mneedham/Documents/algo-class/IntegerArray.txt"
    val inversions: BigInt = numberOfInversions(Source.fromFile(new java.io.File(fileWithNumbers)).getLines().map(Integer.parseInt).toList)
    println(inversions)
  }

  def numberOfInversions(collection: List[Int]): BigInt = {
    var count: BigInt = 0
    def inversionsInner(innerCollection: List[Int]): List[Int] = {
      def merge(left: List[Int], right: List[Int]): Stream[Int] = (left, right) match {
        case (x :: xs, y :: ys) if x < y=> { Stream.cons(x, merge(xs, right)) }
        case (x :: xs, y :: ys) => { count = count + left.length; Stream.cons(y, merge(left, ys)) }
        case _ => if (left.isEmpty) right.toStream else left.toStream
      }
      val n = innerCollection.length / 2
      if (n == 0) innerCollection
      else {
        val (lowerHalf, upperHalf) = innerCollection splitAt n
        merge(inversionsInner(lowerHalf), inversionsInner(upperHalf)).toList
      }
    }

    inversionsInner(collection)
    count
  }
}
~~~

The interesting line is number 15 where we are going to select a value from the right collection and therefore increment our count by the number of items left in the left collection.

It works but it's a bit annoying that we had to use a 'var' to keep track of the count since that's not really idiomatic Scala.

I've been trying to find a way of passing the count around as an accumulator and returning it at the end but really struggled to get the code to compile when I started doing that and seemed to make the code a lot more complicated than it is now.

I'm sure there is a way to do it but I can't see it at the moment!

Since the mutation is reasonably well encapsulated I'm not sure whether it really matters that much but it's always interesting an interesting exercise to try and write code which doesn't mutate state so if anyone can see a good way to do it let me know.
