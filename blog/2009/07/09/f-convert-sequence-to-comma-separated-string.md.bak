+++
draft = false
date="2009-07-09 22:32:55"
title="F#: Convert sequence to comma separated string"
tag=['f']
category=['F#']
+++

I've been continuing playing around with <a href="http://www.markhneedham.com/blog/2009/07/08/f-parsing-cruise-build-data/">parsing Cruise data</a> as I mentioned yesterday with the goal today being to create a graph from the build data.

After recommendations from <a href="http://twitter.com/deanrcornish/statuses/2513727860">Dean Cornish</a> and <a href="http://twitter.com/samnewman/statuses/2514527870">Sam Newman</a> on Twitter I decided to give the <a href="http://code.google.com/apis/chart/types.html#line_charts">Google Graph API</a> a try to do this and realised that I would need to create a comma separated string listing all the build times to pass to the Google API.

My initial thinking was that I could just pipe the sequence of values through 'Seq.fold' and add a comma after each value:


~~~ocaml

let ConvertToCommaSeparatedString (value:seq<string>) =
    let initialAttempt = value |> Seq.fold (fun acc x -> acc + x + ",") ""
    initialAttempt.Remove(initialAttempt.Length-1)
~~~

It works but you end up with a comma after the last value as well and then need to remove that on the next line which feels very imperative to me.

My next thought was that maybe I would be able to do this by making use of a recursive function which matched the sequence on each iteration and then when it was on the last value in the list to not add the comma.

I know how to do this for a list so I decided to go with that first:


~~~ocaml

let ConvertToCommaSeparatedString (value:seq<string>) =
    let rec convert (innerVal:List<string>) acc = 
        match innerVal with
            | [] -> acc
            | hd::[] -> convert [] (acc + hd)
            | hd::tl -> convert tl (acc + hd + ",")           
    convert (Seq.to_list value) ""
~~~

That works as well but it seems a bit weird that we need to convert everything in a list to do it.

A bit of googling revealed an <a href="http://cs.hubfs.net/forums/thread/7596.aspx">interesting post by Brian McNamara</a> where he suggests creating an <a href="http://www.markhneedham.com/blog/2009/05/10/f-regular-expressionsactive-patterns/">active pattern</a> which would cast the 'seq' to a 'LazyList' (which is deprecated but won't be removed apparently) and then do some pattern matching against that instead.

The active pattern which Brian describes is like this:


~~~ocaml

let rec (|SeqCons|SeqNil|) (s:seq<'a>) =
    match s with
    | :? LazyList<'a> as l ->
        match l with
        | LazyList.Cons(a,b) -> SeqCons(a,(b :> seq<_>))
        | LazyList.Nil -> SeqNil
    | _ -> (|SeqCons|SeqNil|) (LazyList.of_seq s :> seq<_>)
~~~

This doesn't cover the three states of the sequence which I want to match so I adjusted it slightly to do what I want:


~~~ocaml

let rec (|SeqCons|SeqNil|SeqConsLastElement|) (s:seq<'a>) =
    match s with
    | :? LazyList<'a> as l ->
        match l with
        | LazyList.Cons(a,b) -> 
            match b with
                | LazyList.Nil -> SeqConsLastElement(a)
                | LazyList.Cons(_,_) -> SeqCons(a,(b :> seq<_>))
        | LazyList.Nil -> SeqNil
    | _ -> (|SeqCons|SeqNil|SeqConsLastElement|) (LazyList.of_seq s :> seq<_>)
~~~

Our function to convert sequences to a comma separated string would now look like this:


~~~ocaml

let ConvertToCommaSeparatedString (value:seq<string>) =
    let rec convert (innerVal:seq<string>) acc = 
        match innerVal with
            | SeqNil -> acc
            | SeqConsLastElement(hd) -> convert [] (acc + hd)
            | SeqCons(hd,tl) -> convert tl (acc + hd + ",")           
    convert (value) ""  
~~~

An example of this in action would be like this:


~~~text

ConvertToCommaSeparatedString (seq { yield "mark"; yield "needham" });;
val it : string = "mark,needham"
~~~
