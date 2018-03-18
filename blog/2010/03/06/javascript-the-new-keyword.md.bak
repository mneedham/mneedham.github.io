+++
draft = false
date="2010-03-06 15:16:02"
title="Javascript: The 'new' keyword"
tag=['javascript']
category=['Javascript']
+++

I came across an <a href="http://ejohn.org/blog/simple-class-instantiation/">interesting post by John Resig where he describes a 'makeClass' function</a> that he uses in his code to create functions which can instantiate objects regardless of whether the user calls that function with or without the new keyword.

The main reason that the new keyword seems to be considered harmful is because we might make assumptions in our function that it will be called with the new keyword which changes the meaning of 'this' inside that function.

For example in my <a href="http://gist.github.com/317106">Bowling Game example</a> I assume that the 'BowlingGame' function will be called with the new keyword.

I wanted to see if I could refactor that code to use the <a href="http://yuiblog.com/blog/2007/06/12/module-pattern/">module pattern</a> instead so as a first step I changed the instantiation of the 'bowlingGame' variable in the <a href="http://gist.github.com/317533">tests</a> to not call the function with 'new' to see if it would make any noticeable difference:


~~~javascript

Screw.Unit(function() {
	describe("bowling game scorecard", function() {
		var bowlingGame;
 
		before(function() {
	    	     bowlingGame = BowlingGame();
	  	});
~~~

There is no noticeable difference in the way any of the tests work but in fact <a href="http://stackoverflow.com/questions/383402/is-javascript-s-new-keyword-considered-harmful">all of the functions I defined have been added to the global object</a> (in this case window) instead of onto 'BowlingGame'.

I changed one of the tests to check that this was the case...


~~~javascript

...
			it("should score a single throw", function() {
				console.log(window.roll);
				
				bowlingGame.roll(5);
				(19).times(function() { gutterBall(); });

				expect(bowlingGame.score()).to(equal, 5);
			});
...	
~~~

...which logs 'undefined' to Firebug if the new keyword is used to instantiate 'bowlingGame' and 'function()' if it wasn't.

The danger here is that you could change the meaning of the 'roll' function outside of the 'BowlingGame' if you wanted to.

To give a contrived example perhaps we could change 'roll' so that it actually called the original function twice instead of once:


~~~javascript

...
			it("should score a single throw", function() {
				var originalRoll = window.roll;
				window.roll = function() {
					originalRoll.apply(this, arguments);
					originalRoll.apply(this, arguments);
					console.log("roll isn't what you'd expect anymore")				
				};
				
				bowlingGame.roll(5);
				(19).times(function() { gutterBall(); });

				expect(bowlingGame.score()).to(equal, 5);
			});	
...
~~~

In this case you would probably never do that because it's just a small bit of code but you wouldn't want to add random functions to the global object in any reasonably sized javascript application.

<a href="http://stackoverflow.com/questions/383402/is-javascript-s-new-keyword-considered-harmful#383503">Shog9 points to a bit of code which allows us to stop users from calling constructor functions without the new keyword</a>:


~~~javascript

BowlingGame  = function() {
	if ( !(this instanceof arguments.callee) ) 
	   throw Error("Constructor called as a function");
...	
~~~

When 'BowlingGame' is called without the new keyword then 'this' will refer to 'window' which means that it won't be an instance of 'arguments.callee' which in this case is the 'BowlingGame' function.
