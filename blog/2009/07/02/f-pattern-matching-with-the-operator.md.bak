+++
draft = false
date="2009-07-02 23:10:19"
title="F#: Pattern matching with the ':?' operator"
tag=['f', 'pattern-matching']
category=['F#']
+++

I've been doing a bit more reading of the <a href="http://code.google.com/p/fake/">Fake</a> source code and one interesting thing which I came across which I hadn't seen was an active pattern which was making use of the ':?' operator to match the input type against .NET types.


~~~ocaml

  let (|File|Directory|) (fileSysInfo : FileSystemInfo) =
    match fileSysInfo with
      | :? FileInfo as file -> File (file.Name)
      | :? DirectoryInfo as dir -> Directory (dir.Name, seq { for x in dir.GetFileSystemInfos() -> x })
      | _ -> failwith "No file or directory given."    
~~~

I thought maybe this was just a wild card operator to say that we don't care what the value is as long as it matches 'FileInfo' or 'DirectoryInfo' respectively but I couldn't see it defined on the <a href="http://research.microsoft.com/en-us/um/cambridge/projects/fsharp/manual/FSharp.Core/Microsoft.FSharp.Core.Operators.html">list of operators on the Microsoft Research website</a>.

A bit of googling led me to <a href="http://weblogs.asp.net/podwysocki/archive/2008/03/17/adventures-in-f-f-101-part-5-pattern-matching.aspx">Matthew Podwysocki's post about pattern matching</a> which explained the purpose of the operator (about 1/3 of the way down):

<blockquote>
What the above example does is check for the corresponding .NET types by using the ':?' operator especially reserved for this behavior. 
</blockquote>

I've been playing around with a simple 'add' function to try and understand F#'s type inference and one thing I noticed is that if you just define it with minimal code you end up with a function which takes in 2 integers and returns an integer as the result:


~~~ocaml

let add a b = a + b

val add: int -> int -> int
~~~

I had thought that the signature and result of that function might remain generic due to the fact that there are more types than just 'int' with which you can make use of the addition operator.

For example, it is possible to add two string together but in fact you need to be more explicit about that:


~~~ocaml

let add (a:string) (b:string) = a + b

val add: string -> string -> string
~~~

From what I can tell if we wanted to write a generic add function we would need to do something like this - I originally tried just returning 'new A + new B' from each of the pattern matches but the return type of add3 then becomes 'string' since the first path in the pattern matching returns a 'string'. 


~~~ocaml

    let add3 a b =
        match (box a,box b) with
            | (:? string as newA),(:? string as newB) -> newA +  newB |> box
            | (:? int as newA),(:? int as newB) -> newA + newB |> box
            | (:? decimal as newA),(:? decimal as newB) -> newA + newB |> box
            | _ -> failwith "you can't add these together" 
~~~

Which is slightly verbose and has a type of "'a -> 'b -" obj' - I haven't been able to work out whether it's possible to create a generic function like this without needing to cast the result down to 'obj'.

I thought it might be possible to get rid of the boxing by making use of the  <a href="http://msdn.microsoft.com/en-us/library/dd233220(VS.100).aspx">downcast operator</a>:

<blockquote>
You can also use the downcast operator to perform a dynamic type conversion. The following expression specifies a conversion down the hierarchy to a type that is inferred from program context.
</blockquote> 

I tried surrounding the 'newA + new B |> box' code with a call to 'downcast' but that just resulted in the following error message when trying to make use of the function:


~~~text

Value restriction. The value 'it' has been inferred to have generic type
	val it : '_a
Either define 'it' as a simple data term, make it a function with explicit arguments or, if you do not intend for it to be generic, add a type annotation.
~~~

I'd be intrigued to see if anyone has worked out how to do this as I'm out of ideas.

