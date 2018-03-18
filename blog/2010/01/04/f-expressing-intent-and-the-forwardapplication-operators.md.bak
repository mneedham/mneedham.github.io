+++
draft = false
date="2010-01-04 11:11:10"
title="F#: Expressing intent and the forward/application operators"
tag=['f']
category=['F#']
+++

A while ago I wrote about F#'s <a href="http://www.markhneedham.com/blog/2009/06/27/f-more-thoughts-on-the-forward-application-operators/">forward and application operators</a> where I'd looked at how these could be used to simplify code and while trying out <a href="http://osherove.com/tdd-kata-1/">Roy Osherove's TDD Kata</a> I realised that perhaps the choice of which of these to use or whether to use them at all depends on what intent we're expressing.

The specific bit of code I was writing was for raising an exception if negative values were provided and I originally thought I'd use the forward operator to express this code:


~~~ocaml

    let digits = [| 1;2;3;-3 |] 
    let buildExceptionMessage negatives = sprintf "No negative numbers allowed. You provided %s" 
                                                  (String.Join(",", negatives |> Array.map (fun x -> x.ToString())))

    raise (ArgumentException (digits |> Array.filter (fun x -> x < 0) |> buildExceptionMessage))
~~~

I think in this case the forward operator doesn't actually express the intent of the code better because it puts the focus on the digits rather than on the building of the exception message. 

I changed that a bit to emphasise the importance of the 'buildExceptionMessage' function:


~~~ocaml

raise (ArgumentException (buildExceptionMessage (digits |> Array.filter (fun x -> x < 0))))
~~~

I thought it might be possible to get rid of the brackets around the filtering of the digits and instead apply that expression to 'buildExceptionMessage' using the application operator:


~~~ocaml

raise (ArgumentException (buildExceptionMessage <| digits |> Array.filter (fun x -> x < 0)))
~~~

That actually results in the following error message:


~~~text

Type mismatch. Expecting a  string -> string but given a  'a array -> 'a array. The type 'string' does not match the type ''a array'
~~~

The problem is that it applies digits to 'buildExceptionMessage' first and then tries to apply the result of that to Array.filter instead of applying the filter to the digits and then passing the result of that calculation to 'buildExceptionMessage'.

One way to get around this is to remove the forward operator and move digits to be the second argument passed to Array.filter instead:


~~~ocaml

raise (ArgumentException (buildExceptionMessage <| Array.filter (fun x -> x < 0) digits))
~~~

This is the version that I've got at the moment and I think it expresses the intent of the code the best. 

I'd be interested in hearing more thoughts on the best way to use or not use these operators in idiomatic F# code. 
