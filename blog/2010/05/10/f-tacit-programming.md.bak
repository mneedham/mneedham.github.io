+++
draft = false
date="2010-05-10 23:24:39"
title="F#: Tacit programming"
tag=['f']
category=['F#']
+++

I recently came across the idea of <a href="http://en.wikipedia.org/wiki/Tacit_programming">tacit programming</a> which is described as such:

<blockquote>
Tacit programming is a programming paradigm in which a function definition does not include information regarding its arguments, using combinators and function composition (but not λ-abstraction) instead of variables. 

The simplicity behind this idea allows its use on several programming languages, such as J programming language and APL and especially in stack or concatenative languages, such as PostScript, Forth, Joy or Factor. Outside of the APL and J communities, tacit programming is referred to as <strong>point-free style</strong>.
</blockquote>

I realised that this approach quite closely describes what I've been trying to drive towards in my most recent playing around with F# and it's actually quite fun trying to drive any intermediate state or storing of data in variables out of a program and just relying completely on function composition and higher order functions.

It seems like we need to define the signatures of some of the functions more explicitly but once we have a group of these functions we can combine them quite effectively elsewhere in our program.

<h3>Moving towards function composition</h3>

I've been trying to do this with the <a href="http://code.google.com/p/yetanotherbuilder/source/browse/yab/Builder.fs">F# test builder</a> that I've been working on and in a few cases it's helped to reduce the amount of code required.

The build function originally read roughly like this:


~~~ocaml

and build (t:Type) = 
     let shortestConstructor = getShortestConstructor t

     shortestConstructor |>
     invokeWith (fun c -> getParameters c |> Array.map (fun p -> valueFor { Type = p.ParameterType; Name = p.Name })) |>
     andApply (fun t -> getWriteableProperties t |> Array.iter(setValueOn t))
~~~

In order to drive that code toward a 'point-free style' we need to make use of the function composition operator which allows us to get the code to the stage where we don't need to specify the signature of 'build', it can be inferred:


~~~ocaml

and build = getShortestConstructor >>
            invokeWith (getParameters >> Array.map (fun p -> valueFor { Type = p.ParameterType; Name = p.Name })) >>
            andApply (fun t -> getWriteableProperties t |> Array.iter(setValueOn t))
~~~

I think that code is pretty much identical to the first version but I'm getting the following warning message pointing to the 'valueFor' call on line 2:


~~~text

Warning	1	This and other recursive references to the object(s) being defined will be checked for initialization-soundness at runtime through the use of a delayed reference. This is because you are defining one or more recursive objects, rather than recursive functions. This warning may be suppressed by using #nowarn "40" or --nowarn 40.	C:\Playbox\yab\yab\Builder.fs	40	66	yab
~~~

I can't figure out how I can change the code to get rid of that warning. I also haven't worked out whether it's possible to fix the 'andApply' line so that we can use functional composition throughout.

It would be cool if it could written in such a way that 't' wouldn't have to be explicitly specified. I can't quite figure out how to do it because I need to call 'getWriteableProperties' and then iterate through that sequence and set a value on 't' using each one. 

Is there a way to write that bit of code so that 't' could be inferred?

<h3>Some functions need to define signatures?</h3>

In order to write a 'build' function which heavily uses functional composition I've pulled out several helper functions which all currently explicitly define their signatures:


~~~ocaml

    let getWriteableProperties t = t.GetType().GetProperties() |> Array.filter (fun p -> p.CanWrite)

    let invokeWith f (aConstructor:ConstructorInfo) = f(aConstructor) |> aConstructor.Invoke
~~~

If we want to call C# libraries like this then I don't think we have a choice but to explicitly define function signatures. It is possible to push the place at which we need to do this by <a href="http://www.markhneedham.com/blog/2009/07/12/f-wrapping-net-library-calls/">writing F# functions to wrap those C# method calls</a> but at some stage we'll explicitly define a function signature:


~~~ocaml

let getWriteableProperties = getTypeProperties >> Array.filter writeableProperty
~~~

where the extra helper functions are defined like so:


~~~ocaml

let getTypeProperties t = t.GetType().GetProperties()
let writeableProperty (p:PropertyInfo) = p.CanWrite
~~~

I can't see a way around this so again I'd be interested if there is one. I don't think it's a problem anyway, just intrigued how far their programming approach can be taken.
