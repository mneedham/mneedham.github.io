+++
draft = false
date="2010-01-07 23:31:37"
title="F#: Refactoring to active patterns"
tag=['f']
category=['F#']
+++

I've been playing around with more F# code and after realising that I'd peppered the code with if statements I thought it would be interesting to try and refactor it to make use of active patterns.

The code is part of my F# solution to <a href="http://osherove.com/tdd-kata-1/">Roy Osherove's TDD Kata</a> and is used to parse the input string and find which delimeters are being used. 

This is the original code:


~~~ocaml

    let hasCustomDelimeter (value:string) = value.Length > 2 && "//".Equals(value.Substring(0, 2))
    let hasMultipleDelimeters (value:string) = hasCustomDelimeter value && "[".Equals(value.Substring(2,1))

    let delimeter value = if (hasCustomDelimeter value) then value.Substring(2, value.IndexOf("\n") - 2) else ","
    let delimeters (value:string) = Regex.Matches(value, "\[(.)\]") |> 
                                    Seq.cast |> 
                                    Seq.map (fun (x:Match) -> x.Groups) |>
                                    Seq.map (fun x -> x |> Seq.cast<Group> |> Seq.nth 1) |>
                                    Seq.map (fun x -> x.Value) |>
                                    Seq.to_array   

    let digits value = 
        let delimeter = delimeter value
        if (hasMultipleDelimeters value) then value.Substring(value.IndexOf("\n")) |> split (delimeters value) |> Array.map parse  
        else if (hasCustomDelimeter value) then value.Substring(value.IndexOf("\n")) |> split [| delimeter |] |> Array.map parse
        else value.Replace("\n", delimeter) |> split [|delimeter |] |> Array.map parse
~~~

The active pattern that we want to use is known as a 'multi case active pattern' which <a href="http://blogs.msdn.com/chrsmith/archive/2008/02/21/Introduction-to-F_2300_-Active-Patterns.aspx">Chris Smith</a> defines as "partitioning the entirety of the input space into different things". In this case given an input string we want to determine what type of delimeters are contained within that string.

This is the code after I'd created the active pattern:


~~~ocaml

    let (|MultipleCustomDelimeters|SingleCustomDelimeter|NoCustomDelimeter|) (value:string) =  
        if (value.Length > 2 && "//".Equals(value.Substring(0, 2))) then
            if ("[".Equals(value.Substring(2,1))) then MultipleCustomDelimeters(delimeters value)
            else SingleCustomDelimeter(delimeter value)
        else NoCustomDelimeter(delimeter value)    
    
    let digits value =  
        match value with 
        | SingleCustomDelimeter(delimeter)     -> value.Substring(value.IndexOf("\n")) |> split [| delimeter |] |> Array.map parse
        | MultipleCustomDelimeters(delimeters) -> value.Substring(value.IndexOf("\n")) |> split delimeters  |> Array.map parse 
        | NoCustomDelimeter(delimeter)         -> value.Replace("\n", delimeter) |> split [|delimeter |] |> Array.map parse
~~~

One thing I didn't realise is that you can set different types for the constructor values of each of the active patterns. In this case I want to match single or multiple delimeters and then return those delimeters. We can define one active pattern which matches a single delimeter and just returns that and then another one which returns an array of delimeters which is quite neat.

The way it works is quite similar to <a href="http://tomasp.net/articles/fsharp-ii-functional.aspx">discriminated unions</a>.

I found that that having all the code around parsing the input in the same function made it easier for me to understand that code and I quite like that it's possible to match the pattern and also get the delimeter/delimeters in one expression.

Although there are more lines of code I think this code is more expressive and it wouldn't be too hard to add in another active pattern if there's another delimeter type that needs to be handled.

I can't decide whether the 'value.SubString' and 'value.Replace' code should also be contained within the active pattern or not. At the moment I'm thinking perhaps not because it's not related to the actual delimeters. 
