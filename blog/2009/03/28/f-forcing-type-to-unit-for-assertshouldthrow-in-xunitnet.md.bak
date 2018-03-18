+++
draft = false
date="2009-03-28 02:35:27"
title="F#: Forcing type to unit for Assert.ShouldThrow in XUnit.NET"
tag=['net', 'f']
category=['F#']
+++

I've started playing around with F# again and decided to try and create some unit tests around the examples I'm following from <a href="http://manning.com/petricek/">Real World Functional Programming</a>. After reading <a href="http://weblogs.asp.net/podwysocki/archive/2008/06/04/language-oriented-programming-and-functional-unit-testing-in-f.aspx">Matt Podwysocki's blog post about XUnit.NET</a> I decided that would probably be the best framework for me to use.

The example I'm writing tests around is:


~~~ocaml

let convertDataRow(str:string) =
    let cells = List.of_seq(str.Split([|','|]))
    match cells with 
    | label::value::_ -> 
        let numericValue = Int32.Parse(value)
        (label, numericValue)
    | _ -> failwith "Incorrect data format!" 
~~~

I started driving that out from scratch but ran into a problem trying to assert the error case when an invalid data format is passed in.

The method to use for the assertion is 'Assert.ShouldThrow' which takes in an Assert.ThrowsDelegate which takes in an argument of type unit->unit. 

The code that I really want to write is this:


~~~ocaml

[<Fact>]
let should_throw_exception_given_invalid_data () =
    let methodCall = convertDataRow "blah"
    Assert.Throws<FailureException>(Assert.ThrowsDelegate(methodCall))    
~~~

which doesn't compile giving the error 'This expression has type string*int but is used here with type unit->unit'.

I got around the first unit by wrapping the convertDateRow in a function which takes in no arguments but the output was proving tricky. I realised that putting a call to printfn would solve that problem, leaving me with this truly hacky solution:


~~~ocaml

[<Fact>]
let should_throw_exception_given_invalid_data () =
    let methodCall = fun () -> (convertDataRow "blah";printfn "")
    Assert.Throws<FailureException>(Assert.ThrowsDelegate(methodCall))  
~~~

Truly horrible and luckily there is a way to <a href="http://cs.hubfs.net/forums/thread/3157.aspx">not do that printfn which I came across on the hubfs forum</a>:


~~~ocaml

[<Fact>]
let should_throw_exception_given_invalid_data () =
    let methodCall = (fun () -> convertDataRow "blah" |> ignore)
    Assert.Throws<FailureException>(Assert.ThrowsDelegate(methodCall))
~~~

The ignore function provides a neat way of ignoring the passed value i.e. it throws away the result of computations.
