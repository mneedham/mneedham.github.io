+++
draft = false
date="2010-02-10 23:06:14"
title="F#: Inline functions and statically resolved type parameters"
tag=['f']
category=['F#']
+++

One thing which I've often wondered when playing around with F# is that when writing the following function the type of the function is inferred to be 'int -> int -> int' rather than allowing any values which can be added together:


~~~ocaml

let add x y = x + y
> val add : int -> int -> int
~~~

It turns out if you use the 'inline' keyword then the compiler does exactly what we want:


~~~ocaml

> let inline add x y = x + y
val inline add : 
	^a -> ^b -> ^c
	when ( ^a or  ^b) : (static member ( + ) :  ^a *  ^b ->  ^c)
~~~

Without the inline modifier type inference forces the function to take a specific type, in this case int. With it the function has a statically resolved type parameter which means that "the type parameter is replaced with an actual type at compile time rather than run time".

In this case it's useful to us because it allows us to implicitly define a member constraint on the two input parameters to 'add'. From the <a href="http://msdn.microsoft.com/en-us/library/dd548046(VS.100).aspx">MSDN page</a>:

<blockquote>
Statically resolved type parameters are primarily useful in conjunction with member constraints, which are constraints that allow you to specify that a type argument must have a particular member or members in order to be used. There is no way to create this kind of constraint by using a regular generic type parameter.
</blockquote>

The neat thing about the second definition is that we can add values of any types which support the '+' operator:


~~~ocaml

add "mark" "needham";;
> val it : string = "markneedham"
~~~


~~~ocaml

> add 1.0 2.0;;
val it : float = 3.0
~~~

From a quick look at the IL code in Reflector it looks like the 'add' function defined here makes use of the '<a href="http://stuff.mit.edu/afs/athena.mit.edu/software/mono/current/arch/i386_deb40/FSharp-1.9.6.2/lib/FSharp.Core/prim-types.fsi">AdditionDynamic</a>' function internally to allow it to be this flexible.

One thing which I found quite interesting while reading about <a href="http://msdn.microsoft.com/en-us/library/dd548047(VS.100).aspx">inline functions</a> is that it sounds like it's quite similar to duck typing in that we're saying a function can be passed any value which supports a particular method.

<a href="http://www.atrevido.net/blog/2008/08/31/Statically+Typed+Duck+Typing+In+F.aspx">Michael Giagnocavo has a post</a> where he covers the idea of <a href="http://msdn.microsoft.com/en-us/library/dd548046(VS.100).aspx">statically type resolved parameters</a> in more detail and describes what he refers to as 'statically typed duck typing'.
