+++
draft = false
date="2009-05-19 01:38:31"
title="F#: Object expressions"
tag=['f']
category=['F#']
+++

One of the things I miss a bit from the Java world is the ability to create anonymous inner classes which implement a certain interface.

We can't do this in C# - you always need to define a named class - but in my latest playing around with F# I was quite pleased to learn that we do have this ability using a feature called <strong>object expressions</strong>.

These come in particularly useful when you are only making use of the implementation of an interface in one place in the code and therefore don't want to expose this type to any other code.

Given an interface:


~~~ocaml

type ICarRepository =
    abstract FindAll : Unit -> list<Car>
~~~


~~~ocaml

type Car() =
~~~

The normal way to implement that interface if we are following the C# approach would be like this:


~~~ocaml

type CarRepository() =
	interface ICarRepository with     
	    member self.FindAll () = [ new Car() ] 
~~~

We would then reference the CarRepository in our code:


~~~ocaml

let myCarRepository = new CarRepository();;
~~~

The alternative is to create a value which implements the interface inline, a way of coding which is easier to implement instead of having to create a new type each time we want to implement an interface.


~~~ocaml

let myCarRepository = 
{ new ICarRepository with 
     member self.FindAll () = [ new Car() ] }
~~~

This seems to be quite in keeping with the style of programming being taught in the <a href="http://manning.com/petricek/">Real World Functional Programming</a> book which seems to be around getting code working quickly and then working iteratively towards a more reusable solution.

I'd be interested to see how well this technique would work on a real project since I get the feeling that quite a lot of interface implementations are only used in one place and therefore don't really need to have a type defined purely for implementing them - that decision can be delayed until one is actually needed.
