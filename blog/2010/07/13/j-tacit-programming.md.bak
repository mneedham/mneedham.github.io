+++
draft = false
date="2010-07-13 14:47:41"
title="J: Tacit Programming"
tag=['j-2']
category=['J']
+++

A couple of months ago I wrote about <a href="http://www.markhneedham.com/blog/2010/05/10/f-tacit-programming/">tacit programming with respect to F#,</a> a term which I first came across while reading about the <a href="http://en.wikipedia.org/wiki/J_(programming_language)">J programming language</a>.

There's a <a href="http://www.jsoftware.com/help/primer/tacit_definition.htm">good introduction to tacit programming on the J website</a> which shows the evolution of a function which originally has several local variables into a state where it has none at all.

I've been having a go at writing <a href="http://osherove.com/tdd-kata-1/">Roy Osherove's TDD Kata</a> in J and while I haven't got very far yet I saw a good opportunity to move the code I've written so far into a more tacit style.

From my understanding two of the ways that we can drive towards a tacit style are by removing explicitly passed arguments and variables from our code.

<h3>Remove explicitly passed arguments</h3>

The second part of the kata requires us to allow new lines separating numbers as well as commas so with the help of the guys on the J mailing list I wrote a function which converts all new lines characters into commas:


~~~text

replaceNewLines =: 3 : 0
	y rplc ('\n';',')
)
~~~

'rplc'  takes an input as its left hand argument and a 2 column boxed matrix as its right hand argument. 

In this case the left hand argument is 'y' which gets passed to 'replaceNewLines' and the boxed matrix contains '\n' and ','. The left item in the matrix gets replace by the right item.

We want to get to the point where we <strong>don't have to explicitly pass y</strong> - it should just be inferred from the function definition.

As is the case in F# it seems like if we want to do this then we need to have the inferred value (i.e. y) passing as the last argument to a function which in this case means that it needs to be passed as the right hand argument.

'rplc' is actually the same as another function 'stringreplace' which takes in the arguments the other way around which is exactly what we need.


~~~text

replaceNewLines =: 3 : 0
	('\n';',') stringreplace y
)
~~~

The next step is to apply the left hand argument of 'stringreplace' but infer the right hand argument.

We can use the bond conjunction (&) to do this. The bond conjunction creates a new function (or verb in J speak) which has partially applied the left argument to the verb passed as the right hand argument.


~~~text

replaceNewLines =:  ('\n' ; ',') & stringreplace
~~~

'replaceNewLines' represents the partial application of 'stringReplace'. We can now pass a string to 'replaceNewLines' and it will replace the new lines characters with commas.

<h3>Remove local variables</h3>

My 'add' function currently looks like this:


~~~text

add =: 3 : 0
	newY =. replaceNewLines y
 	+/ ". newY
 )
~~~

We want to try and drive 'add' to the point where it's just <strong>a composition of different functions</strong>.

At the moment on line 3 we have '+/' which can be used to get the sum of a list of numbers.

e.g.

~~~text

+/ 1 2 3
> 6
~~~

We also have '".' which converts a character array into numbers.

e.g. 


~~~text

". '1,2,3'
> 1 2 3
~~~

In order to compose our 3 functions together without explicitly passing in 'y' or 'newY' we need to make use of atop conjunction (@) which "combines two verbs into a derived verb that applies the right verb to its argument and then applies the left verb to that result."

It works in the same way as <a href="http://www.markhneedham.com/blog/2009/12/09/haskell-vs-f-function-composition/">Haskell's function composition operator</a> i.e. it applies the functions starting with the one furthest right.

We end up with this:


~~~text

add =: +/ @ ". @ replaceNewLines
~~~

or if we want to inline the whole thing:


~~~text

add =:  +/ @ ". @ ( ('\n' ; ',') & stringreplace )
~~~

<h3>Overall</h3>
I'm still getting the hang of this language - it's taking much longer than with any other languages I've played with - but so far the ideas I've come across are very interesting and it seems like it massively reduces the amount of code required to solve certain types of problems.
