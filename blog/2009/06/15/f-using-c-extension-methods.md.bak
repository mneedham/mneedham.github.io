+++
draft = false
date="2009-06-15 20:03:34"
title="F#: Using C# extension methods"
tag=['f']
category=['F#']
+++

An interesting thing I noticed about referencing C# libraries from F# is that you can't access C# extension methods on generic open types in the same way that you would be able to if you were using the library from C# code.

I came across this problem when playing around with the <a href="http://ayende.com/projects/rhino-mocks.aspx">Rhino Mocks framework</a> in some F# code.

I wrote a simple test to see whether I could get an expectation to work correctly, without paying any regard for the fact that you can't use all C# extension methods in the same way as you can from C# code!


~~~ocaml

open Xunit
open Rhino.Mocks

type IFoo =
    abstract Bar : string -> string

type Foo() =
    interface IFoo with
        member x.Bar (value) = value

type Baz(foo: IFoo) =
    member x.Barry(value) = foo.Bar(value) |> ignore

[<Fact>]
let my_mocking_test () =
    let foo = MockRepository.GenerateMock<IFoo>()

	foo.Expect(fun f -> f.Bar("random")).Return("someValue")
    
    let baz = new Baz(foo)
    baz.Barry("random") |> ignore
    
    foo.VerifyAllExpectations();
~~~

That code doesn't compile with lines 18 and 23 being the offending ones.

If we want to use Rhino Mocks' extension methods in our F# code we need to call them specifically. With a little exploration through Rhino Mocks I came up with the following code.


~~~ocaml

...
[<Fact>]
let my_mocking_test () =
    let foo = MockRepository.GenerateMock<IFoo>()
    (RhinoMocksExtensions.Expect<IFoo, string>(foo, fun f -> f.Bar("random"))).Return("someValue") |> ignore
    
    let baz = new Baz(foo)
    baz.Barry("random") |> ignore
    
    RhinoMocksExtensions.VerifyAllExpectations(foo)
~~~

It doesn't read particularly fluently although it does work. I imagine an equivalent extension method could be written in F# to get around the problem although I ended up not needing to do any mocking after I first wrote this code so I haven't looked into how to do that yet.

* Update *
I've updated this post to point out that this problem occurs when trying to use C# extension methods on open generic types rather than all C# extension methods, something which Matthew Podwysocki points out in the comments.

I had originally thought that you couldn't use any C# extension methods since they didn't show up on the Intellisense drop down in Visual Studio and I assumed they were just a language feature of C# 3.0.

As it turns out you can get the Intellisense by importing the 'System.Linq' namespace although if you want to use a C# extension method you will need to ensure the type has been evalualted which can sometimes mean you need to put brackets around the code. 

For example:


~~~ocaml

[1..5]. (* No extension methods will show up *)
([1..5]). (* All the extension methods that can be applied to IEnumerable show up  *)
~~~

Under the covers the same thing seems to be happening as if we called the extension methods from C# code. Scott Hanselman has a <a href="http://www.hanselman.com/blog/HowDoExtensionMethodsWorkAndWhyWasANewCLRNotRequired.aspx">nice post which explains how this works</a>. 
