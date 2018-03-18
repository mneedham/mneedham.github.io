+++
draft = false
date="2009-04-25 22:12:43"
title="F#: Not equal/Not operator"
tag=['f']
category=['F#']
+++

While continuing playing with <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">my F# twitter application</a> I was trying to work out how to exclude the tweets that I posted from the list that gets displayed.

I actually originally had the logic the wrong way round so that it was only showing my tweets!


~~~ocaml

let excludeSelf (statuses:seq<TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus ->  eachStatus.User.ScreenName.Equals("markhneedham"))
~~~

Coming from the world of Java and C# '!' would be the operator to find the screen names that don't match my own name. So I tried that.


~~~ocaml

let excludeSelf (statuses:seq<TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus -> !(eachStatus.User.ScreenName.Equals("markhneedham")))
~~~

Which leads to the error:


~~~text

Type constraint mismatch. The type 'bool' is not compatible with the type 'bool ref'. 
~~~

If we look at the definition of '!' we see the following:


~~~ocaml

(!);;

> val it : ('a ref -> 'a)
~~~

It's not a logical negation operator at all. In actual fact it's an operator used to deference a mutable reference cell. 

What I was looking for was actually <a href="http://stackoverflow.com/questions/239888/logical-negation-operator-in-f-equivalent">the 'not' operator</a>.


~~~ocaml

let excludeSelf (statuses:seq<TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus ->  not (eachStatus.User.ScreenName.Equals("markhneedham")))
~~~

I could also have used the '<>' operator although that would have changed the implementation slightly:


~~~ocaml

let excludeSelf (statuses:seq<TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus ->  eachStatus.User.ScreenName <> "markhneedham")
~~~

The <a href="http://research.microsoft.com/en-us/um/cambridge/projects/fsharp/manual/FSharp.Core/Microsoft.FSharp.Core.Operators.html">Microsoft Research F# website</a> seems to be quite a useful reference for understanding the different operators.
