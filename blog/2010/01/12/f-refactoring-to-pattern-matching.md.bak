+++
draft = false
date="2010-01-12 01:33:58"
title="F#: Refactoring to pattern matching"
tag=['f']
category=['F#']
+++

I was looking through some of the F# code I've written recently and I realised that I was very much writing C# in F# with respect to the number of if statements I've been using.

I thought it would be interesting to see what the code would look like if I was able to refactor some of that code to make use of pattern matching instead which would be a more idiomatic way of solving the problem in F#.

The first example of if statements is in <a href="http://www.markhneedham.com/blog/2010/01/10/roy-osheroves-tdd-kata-an-f-attempt/">my post about my F# solution to Roy Osherove's TDD Kata</a>.

I originally wrote a parse function which was able to parse a string and give it's decimal value or 0 if it couldn't be parsed.


~~~ocaml

let parse value = 
    let (itParsed, value) = Decimal.TryParse value
    if (itParsed) then value else 0.0m
~~~

If we use a pattern match expression we'd end up with the following:


~~~ocaml

let parse value = match Decimal.TryParse value with | (true, value) -> value | (false, _) -> 0.0m
~~~

The neat thing about this approach is that we don't need to store the result of the 'Decimal.TryParse' function as we did in my original version. 

We could in theory also write it like this...


~~~ocaml

let parse value = match Decimal.TryParse value with | (true, value) -> value | (_, _) -> 0.0m
~~~

...but while that is slightly less code I quite like the other version because it's a bit more intention revealing that 0 will be returned if we fail to parse the string. I think there's less thinking needed to understand the code.

Another example is this bit of code:


~~~ocaml

let add value = if ("".Equals(value) or "\n".Equals(value)) then 0.0m
                else match digits value |> Array.filter (fun x -> x < 1000m) with 
                     | ContainsNegatives(negatives) -> raise (ArgumentException (buildExceptionMessage negatives))
                     | NoNegatives(digits)          -> digits |> Array.sum
~~~

If we convert that to use pattern matching we would get this:


~~~ocaml

let add value = match value with
                | "" -> 0.0m
                | "\n" -> 0.0m
                | value ->  match digits value |> Array.filter (fun x -> x < 1000m) with 
                            | ContainsNegatives(negatives) -> raise (ArgumentException (buildExceptionMessage negatives))
                            | NoNegatives(digits)          -> digits |> Array.sum
~~~

That's maybe slightly easier to read mainly because of the splitting up of the two inputs which lead to a 0 result. 

The final example of using if statements is the following bit of code:


~~~ocaml

let (|CustomDelimeter|NoCustomDelimeter|) (value:string) = 
	...
 
     if (value.Length > 2 && "//".Equals(value.Substring(0, 2))) then
         if ("[".Equals(value.Substring(2,1))) then CustomDelimeter(delimeters value)
         else CustomDelimeter([| value.Substring(2, value.IndexOf("\n") - 2) |])
     else NoCustomDelimeter(",") 
~~~

The only way I could see how to make this use active patterns is on the boolean statements like so:


~~~ocaml

let (|CustomDelimeter|NoCustomDelimeter|) (value:string) = 
	...
 
    match (value.Length > 2 && "//".Equals(value.Substring(0, 2))) with
    | true -> match ("[".Equals(value.Substring(2,1))) with 
              | true  ->  CustomDelimeter(delimeters value)
              | false ->  CustomDelimeter([| value.Substring(2, value.IndexOf("\n") - 2) |])
    | false -> NoCustomDelimeter(",") 
~~~

I quite like that it lines up the return values of the active pattern which seems to make it a bit more readable.

I think overall maybe the pattern matching versions are slightly more readable but maybe not by much. What do you think?
