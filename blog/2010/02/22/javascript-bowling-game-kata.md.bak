+++
draft = false
date="2010-02-22 23:14:20"
title="Javascript: Bowling Game Kata"
tag=['javascript']
category=['Javascript']
+++

I spent some time over the weekend playing with the <a href="http://blog.objectmentor.com/articles/2009/10/01/bowling-game-kata-in-ruby">bowling game kata</a> in Javascript.

I thought I knew the language well enough to be able to do this kata quite easily so I was quite surprised at how much I struggled initially. 

These are some of my observations from this exercise:

<ul>
<li>I was using <a href="http://github.com/nkallen/screw-unit">screw-unit</a> as my unit testing framework - I originally tried to  setup <a href="http://code.google.com/p/js-test-driver/">JSTestDriver</a> but I was having problems getting that to work so in the interests of not shaving the yak I decided to go with something I already know how to use.

I don't think I quite get the idea of the 'describe' and 'it' blocks which I believe are inspired by <a href="http://rspec.info/documentation/">Rspec</a>.

I like the idea of describing the behaviour of an object for the different contexts in which it's used but I found myself putting all my examples/tests in the same describe block without realising!

I went back and tried to find the different contexts but the only obvious distinction I noticed was that some tests seemed to be covering fairly basic bowling combinations while others were covering specific types of games:

<ul>
<li>normal games
	<ul>
		<li>should score a single throw</li>
         <li>should score two throws which do not add up to a strike or spare</li>
         <li>should score a spare</li>
         <li>should score multiple spares</li>
         <li>should score a strike</li>
         <li>should score back to back strikes</li>
         <li>should score a combination of strikes and spares</li>
    </ul></li>
<li>special combinations
    <ul>
		<li>should score a full house of strikes</li>
         <li>should score a full house of spares</li>
         <li>should score a gutter game</li>
         <li>should score a dutch 200</li>
	</ul>
</li>
</ul>

There's no specific setup unique to these two contexts which I've often noticed is a tell tale sign when writing tests in C# that we need to split our tests out a bit so I'm not sure whether I've added much value by doing this refactoring.

Following <a href="http://blog.orfjackal.net/2010/02/three-styles-of-naming-tests.html">Esko Luontola's terminology</a> the tests that I've written follow example style test names rather than specification style test names. 

This means that in order to understand the scoring rules of bowling you would need to look at the implementation of the test rather than just read the name.

I think this might be a key difference in the way we write tests in JUnit/NUnit and RSpec/screw-unit.

</li>

<li>At one stage I was making use of the Array '<a href="http://www.w3schools.com/jsref/jsref_splice.asp">splice</a>' function to get an array with an element removed and I had expected that I would be returned a new array with those elements removed. 

In actual fact that function mutates the original array so if we're going to do anything using 'splice' then it seems like we need to get a copy of the original array by using '<a href="http://www.w3schools.com/jsref/jsref_slice_array.asp">slice</a>' otherwise we may end up with some quite unexpected behaviour later on in the program.

The other thing I found strange is that 'splice' returns the elements that have been removed from the array rather than the newly mutated array. 

To get an array with the first element removed we'd do something like this:


~~~javascript

function removeFirstItemFrom(theArray) {
	var copy = theArray.slice(0);
	copy.splice(0, 1);
	return copy;	
}

var anArray = [1,2,3,4,5];
var anArrayWithFirstItemRemoved = removeFirstItemFrom(anArray);
~~~

After my time playing around with functional approaches to programming it's quite strange to see APIs which mutate values and don't return the results that I'd expect them to. Interesting though.
</li>
<li>Since a lot of the test setup involved rolling gutter balls I had a lot of calls to 'bowlingGame.roll(0)' which was making the test quite convoluted and not adding much value.

I wrote a function to extend 'Number' so that I could use a Ruby style '10.times' syntax:


~~~javascript

Number.prototype.times = function(f) {
	for(var i=0; i < this; ++i) {
		f();
	}
	
	return this;
};
~~~

When I tried to use this function like this:


~~~javascript

10.times(function() { bowlingGame.roll(0); });
~~~

I kept getting the following error:


~~~text

SyntaxError: missing ; before statement
~~~

I couldn't work out what I was doing wrong but <a href="http://www.twitter.com/skim">skim</a> pointed out that in Javascript we need to wrap number literals in parentheses in order to call functions on them:


~~~javascript

(10).times(function() { bowlingGame.roll(0); });
~~~

works much better!

I wrote a couple of other general use functions and one thing which I'm not sure about is whether or not I should do validation on the input parameters or is it down to the user of the function to use it correctly?

I'm more used to static languages where it would be more difficult to pass in an unexpected value so I'm not sure what the normal approach would be in a dynamic language.
</li>
<li>I took quite a lot of ideas from the way <a href="http://blog.objectmentor.com/articles/2009/10/01/bowling-game-kata-in-ruby">Brett Schuchert solved the problem in Ruby</a>.

In particular I really like the way that he's broken down the problem into smaller and smaller functions which all do only one thing. It's quite easy to end up writing really complicated functions which are difficult to understand so it was good to see that it is possible to keep it this simple. 

It would be quite interesting to see how this type of solution evolved.</li>
<li>This wasn't my most incremental bit of coding ever - I found that some of the examples I introduced e.g. scoring a strike often resulted in quite a lot of code needing to change to make the test pass.

My current thinking is that for this problem we perhaps need to have some idea of the way that we want the code to evolve before we start writing our solution. A solution doesn't just evolve in front of us when we add in the next test. Either that or I'm not taking steps which are small enough to allow that evolution to happen.
</li>
</ul>
