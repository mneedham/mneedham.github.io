+++
draft = false
date="2010-01-14 08:01:29"
title="F#: Refactoring to sequence/for expressions"
tag=['f']
category=['F#']
+++

Since I started playing around with F# one of the things I've been trying to do is not use the 'for' keyword because I was trying to avoid writing code in an imperative way and for loops are a big part of this for me.

Having read <a href="http://fsharpnews.blogspot.com/2009/12/zach-cox-word-count-challenge.html">Jon Harrop's solution</a> to the <a href="http://www.markhneedham.com/blog/2009/12/20/f-word-count-using-a-dictionary/">word count problem</a> where he made use of both sequence and for expressions I thought it'd be intersting to see what some of the code I've written would look like using that approach.

An example of a function that I wrote which could be rewritten the other way is the following:


~~~ocaml

let delimeters (value:string) = Regex.Matches(value, "\[([^]]*)\]") |> Seq.cast |> 
                                Seq.map (fun (x:Match) -> x.Groups) |>
                                Seq.map (fun x -> x |> Seq.cast<Group> |> Seq.nth 1) |>
                                Seq.map (fun x -> x.Value)
~~~

This could be written like this if we used a sequence expression instead of chaining map operations: 


~~~ocaml

let delimeters (value:string) = seq { for m in Regex.Matches(value, "\[([^]]*)\]") do yield m.Groups.Item(0).Value } 
~~~

One interesting thing I found about writing it like this was that I noticed that 'GroupCollection' had the 'Item' property on it which would let me get the match much more easily. 

I completely missed that when I was writing the first solution so I'm not sure if that was just due to my lack of knowledge of that part of the API or whether the second approach actually encouraged me to explore more and therefore end up with a simpler solution. 

Another example I found was this expression for getting the matches for a regular expression:


~~~ocaml

let regex pattern input = Regex.Matches(input, pattern) |> Seq.cast |> Seq.map (fun (x:Match) -> x.Value)
~~~

That can be simplified to the following with a sequence expression:


~~~ocaml

let regex pattern input = seq { for m in Regex.Matches(input, pattern) do yield m.Value }
~~~

One neat thing about using sequence expressions is that we don't need to make use of 'Seq.cast' to convert a value to a typed sequence - we can just use it as it is.

The following function can be rewritten to just use a for expression:


~~~ocaml

let writeTo (path:string) (values:seq<string * int>) = 
    use writer = new StreamWriter(path)
    values |> Seq.map (fun (value, count) -> value + " " + count.ToString()) |> Seq.iter (fun x -> writer.WriteLine(x))  
~~~

Like so:
    

~~~ocaml

let writeTo (path:string) (values:seq<string * int>) = 
    use writer = new StreamWriter(path)
    for (value,count) in values do writer.WriteLine(value + " " + count.ToString())
~~~

We eventually iterate through the sequence anyway so I think it's more intention revealing to just do the iteration and mapping in one step.

This is a function from when I was <a href="http://www.markhneedham.com/blog/2009/07/12/f-a-day-writing-a-feedburner-graph-creator/">writing the little Feedburner application</a>:


~~~ocaml

let calculateWeeklyAverages =
    Seq.reverseSequence >>
    Seq.windowed days >>
    Seq.map (fun (entries:array<Entry>) -> 
                (entries.[0]).Date , entries |> Array.map (fun e -> e.Circulation |> toDecimal) |> Array.average ) >>
    Seq.reverseSequence  
~~~

If we use a sequence expression it'd look like this:
                

~~~ocaml

let calculateWeeklyAverages entries =
    seq { for (e:array<Entry>) in (entries |> Seq.reverseSequence |> Seq.windowed days) do 
              yield ((e.[0]).Date, entries |> Array.map (fun e -> e.Circulation |> toDecimal) |> Array.average) } 
    |> Seq.reverseSequence
~~~

The resulting code is shorter but it seems to me like the focus when you read the code has moved to the line which yields the tuple whereas in the first version I find that I read the function as a whole.

I've not really used sequence expressions that much so it's been interesting going through the code and seeing where they might be useful.

I found several places where I'd used lists because I find those easier to pattern match against but I wonder whether it would make sense to use sequences there as well. 
