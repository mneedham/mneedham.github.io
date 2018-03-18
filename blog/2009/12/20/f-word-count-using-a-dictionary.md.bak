+++
draft = false
date="2009-12-20 10:09:30"
title="F#: Word Count using a Dictionary"
tag=['f']
category=['F#']
+++

Having spent some time unsuccessfully trying to make <a href="http://www.markhneedham.com/blog/2009/12/18/f-word-count-a-somewhat-failed-attempt/">my F# attempt at the word count problem</a> work I decided to follow the lead of the other examples I've read and make use of a Dictionary to keep count of the words.

I originally thought that I might be having a problem with the downloading of the files and storing of those strings in memory so I tried to change that bit of code to be lazily evaluated:


~~~ocaml

let downloadFile path = 
    lazy(use streamReader = new StreamReader(File.OpenRead path)
    streamReader.ReadToEnd())   
~~~

That didn't seem to make much difference though and it seemed like the StackOverflowException was happening on the 'List.fold' line:


~~~ocaml

let wordCount = files >> 
                List.map downloadFile >>
                List.map words >>
                List.fold (fun acc x -> Seq.append acc x) Seq.empty >> 
                Seq.groupBy (fun x -> x) >> 
                Seq.map (fun (value, sequence) -> (value, Seq.length sequence))
~~~

I couldn't see a way of changing the solution such that the current approach wouldn't need that line so I rewrote part of it ending up with the following solution:


~~~ocaml

#light
#r "FSharp.PowerPack"
open System
open System.IO
open System.Text.RegularExpressions
open System.Collections.Generic

let (|File|Directory|) path = if(Directory.Exists path) then Directory(path) else File(path)
let getFileSystemEntries path = Directory.GetFileSystemEntries path |> Array.to_list
 
let files path = 
    let rec inner fileSystemEntries files =
        match fileSystemEntries with
            | [] -> files
            | File path :: rest -> inner rest (path :: files)  
            | Directory path :: rest -> inner (List.append rest (getFileSystemEntries path)) files  
    inner (getFileSystemEntries path) []
 
let download path = using (new StreamReader(File.OpenRead path)) (fun reader -> reader.ReadToEnd())
let writeTo (path:string) f = using (new StreamWriter(path)) (fun writer -> f writer)

let words input = Regex.Matches(input, "\w+") |> Seq.cast |> Seq.map (fun (x:Match) -> x.Value.ToLower()) 
let apply (dict:Dictionary<string,int>) key f = if(dict.ContainsKey(key)) then dict.[key] <- f dict.[key] else dict.[key] <- f 0
 
let startTime = DateTime.Now
let dict = new Dictionary<string, int>()

files "Z:\\20_newsgroups" |> List.iter (fun file -> download file |> words |> Seq.iter (fun word -> apply dict word ((+) 1) )) 

printfn "Writing counts in alphabetical order"
writeTo "C:\\results\\counts-alphabetical-fsharp.txt" (fun out -> 
    dict |> Seq.sortBy (fun x -> x.Key) |> Seq.iter (fun entry -> out.WriteLine(entry.Key + " " + entry.Value.ToString())))
 
printfn "Writing counts in descending order"
writeTo "C:\\results\\counts-descending-fsharp.txt" (fun out -> 
    dict |> Seq.sortBy (fun x -> x.Value * -1) |> Seq.iter (fun entry -> out.WriteLine(entry.Key + " " + entry.Value.ToString())))
 
let endTime = DateTime.Now
printfn "Finished in: %d seconds" (endTime - startTime  ).Seconds
~~~

As I wrote about previously I found out that I could use the 'using' function instead of the 'use' keyword with the 'StreamWriter' and 'StreamReader' so those bits of code are a bit simplified.

The way of interacting with dictionaries in F# doesn't seem as nice as in Ruby so I've ended up with the somewhat verbose bit of code on line 23. Is there a cleaner way of doing that?

By using a Dictionary I think it's now more difficult to parallelise the counting up of the words which was something I thought might be possible when I first came across the problem. 

This seems like the perfect problem for the <a href="http://en.wikipedia.org/wiki/MapReduce">MapReduce</a> approach although I'm not quite sure about the implementation details. 

My thinking is that we'd have a Dictionary for each node/actor and it would sum up the words in its file before passing the result to another actor which would be responsible for taking all the dictionaries and accumulating the word counts?

This was an interesting problem for showing what happens if you try to store too much data in memory and it's something that I've not come across before because I don't typically work with data sets that are this big. 
