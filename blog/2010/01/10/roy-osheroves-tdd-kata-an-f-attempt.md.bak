+++
draft = false
date="2010-01-10 01:46:07"
title="Roy Osherove's TDD Kata: An F# attempt"
tag=['tdd', 'f']
category=['F#']
+++

As I've mentioned in a few of my recent posts I've been having <a href="http://www.markhneedham.com/blog/2009/12/25/roy-osheroves-tdd-kata-my-first-attempt/">another go</a> at <a href="http://osherove.com/tdd-kata-1/">Roy Osherove's TDD Kata</a> but this time in F#. 

One thing I've been struggling with when coding in F# is working out <strong>how many intermediate variables we actually need</strong>. They can be useful for expressing intent better but they're clutter in a way.

I've included my solution at the end and in the active pattern which determines whether or not we have a custom delimeter defined in our input string I can't decide whether or not to create a value to represent the expressions that determine that.


~~~ocaml

    let (|CustomDelimeter|NoCustomDelimeter|) (value:string) = 
        ...
        let hasACustomDelimeter = value.Length > 2 && "//".Equals(value.Substring(0, 2))
        
        if (hasACustomDelimeter) then
            if ("[".Equals(value.Substring(2,1))) then CustomDelimeter(delimeters value)
            else CustomDelimeter([| value.Substring(2, value.IndexOf("\n") - 2) |])
        else NoCustomDelimeter(",")  
~~~

In a way it's quite obvious that the expression on line 3 is what we're using to determine if the input string has a custom delimeter because we state that on the next line. 


~~~ocaml

    let (|CustomDelimeter|NoCustomDelimeter|) (value:string) = 
        ...
        if (value.Length > 2 && "//".Equals(value.Substring(0, 2))) then
            if ("[".Equals(value.Substring(2,1))) then CustomDelimeter(delimeters value)
            else CustomDelimeter([| value.Substring(2, value.IndexOf("\n") - 2) |])
        else NoCustomDelimeter(",")  
~~~

I can't decide which I prefer so any thoughts on that would be welcome.

I ran into a bit of trouble trying to make the following requirement work because my original parse function was hiding the fact that the code was failing on this step: 


~~~text

Delimiters can be of any length with the following format:  “//[delimiter]\n” for example: “//***\n1***2***3” should return 6
~~~

The parse function was originally defined to returns a zero value if it failed to parse the string which meant that the function which decomposed the string into a sequences of numbers could fail and we wouldn't see an exception, just a failing test.


~~~ocaml

    let parse value = 
        let (itParsed, value) = Decimal.TryParse value
        if (itParsed) then value else 0.0m
~~~

Having the function defined like this simplified the code a bit because I didn't need to deal with ignoring some characters at the beginning of the string when a custom delimeter was being specified.

One of the instructions for the exercise is to focus on writing tests for the valid inputs and not for invalid inputs which I initially struggled with. Usually if I was test driving code I would have written tests against invalid inputs to help me drive out the design.

Once I started focusing on just making the test past instead of finding a generic solution for the whole problem this became much easier and I didn't need to test with the invalid inputs.

I wrote tests for the code in C# using NUnit so that I could run the tests from Resharper. I still haven't found a good way to run automated tests from inside Visual Studio when they're written in F# otherwise I'd have probably just done that.

All the tests I wrote were against the 'add' function but the way the code is written at the moment it would be possible to write tests against the other functions directly if I wanted to. 

If I was working in C# perhaps some of those functions would be classes and I would write tests directly against those but I haven't done that here and I'm not sure whether it is necessary. 'digits' is the  only function where that would seem to add value.

This is the code I've got at the moment:


~~~ocaml

module FSharpCalculator
    open System
    open System.Text.RegularExpressions
    
    let split (delimeter:array<string>) (value:string) = value.Split (delimeter, StringSplitOptions.None)
    let toDecimal value = Decimal.Parse value
    
    let (|CustomDelimeter|NoCustomDelimeter|) (value:string) = 
        let delimeters (value:string) = Regex.Matches(value, "\[([^]]*)\]") |> Seq.cast |> 
                                        Seq.map (fun (x:Match) -> x.Groups) |>
                                        Seq.map (fun x -> x |> Seq.cast<Group> |> Seq.nth 1) |>
                                        Seq.map (fun x -> x.Value) |>
                                        Seq.to_array
        
        if (value.Length > 2 && "//".Equals(value.Substring(0, 2))) then
            if ("[".Equals(value.Substring(2,1))) then CustomDelimeter(delimeters value)
            else CustomDelimeter([| value.Substring(2, value.IndexOf("\n") - 2) |])
        else NoCustomDelimeter(",")    
    
    let digits value = match value with 
                       | CustomDelimeter(delimeters)  -> value.Substring(value.IndexOf("\n")) |> split delimeters  |> Array.map toDecimal 
                       | NoCustomDelimeter(delimeter) -> value.Replace("\n", delimeter) |> split [|delimeter |] |> Array.map toDecimal
    
    let buildExceptionMessage negatives = 
        sprintf "No negative numbers allowed. You provided %s" (String.Join(",", negatives |> Array.map (fun x -> x.ToString())))
    
    let (|ContainsNegatives|NoNegatives|) digits =
        if (digits |> Array.exists (fun x -> x < 0.0m)) 
        then ContainsNegatives(digits |> Array.filter (fun x -> x < 0.0m))
        else NoNegatives(digits)
    
    let add value = if ("".Equals(value) or "\n".Equals(value)) then 0.0m
                    else match digits value |> Array.filter (fun x -> x < 1000m) with 
                         | ContainsNegatives(negatives) -> raise (ArgumentException (buildExceptionMessage negatives))
                         | NoNegatives(digits)          -> digits |> Array.sum
~~~
