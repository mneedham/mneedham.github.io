+++
draft = false
date="2009-12-18 02:58:34"
title="F#: Word Count - A somewhat failed attempt"
tag=['f']
category=['F#']
+++

I came across <a href="http://blogs.sourceallies.com/2009/12/word-counts-example-in-ruby-and-scala/">Zach Cox's word count problem</a> via <a href="http://twitter.com/samaaron/status/6701378774">Sam Aaron</a> and <a href="http://twitter.com/olabini/status/6705741285">Ola Bini's</a> twitter streams and I thought it'd be interesting to try it out in F# to see what the solution would be like. 

The solution needs to count word frequencies from a <a href="http://kdd.ics.uci.edu/databases/20newsgroups/20newsgroups.html">selection of newsgroup articles</a>.

I wanted to see if it was possible to write it in F# without using a map to keep track of how many of each word had been found.

My thinking was that I would need to keep all of the words found and then calculate the totals at the end.

After a bit of fiddling this is the version I ended up with:

word-count.fsx

~~~ocaml

#light
open System
open System.IO
open System.Text.RegularExpressions

let (|File|Directory|) path = if(Directory.Exists path) then Directory(path) else File(path)
let getFileSystemEntries path = Directory.GetFileSystemEntries path |> Array.to_list

let files path = 
    let rec inner fileSystemEntries files =
        match fileSystemEntries with
            | [] -> files
            | File path :: rest -> inner rest (path :: files)  
            | Directory path :: rest -> inner (List.append rest (getFileSystemEntries path)) files  
    inner (getFileSystemEntries path) []

let downloadFile path = 
    use streamReader = new StreamReader(File.OpenRead path)
    streamReader.ReadToEnd()    
    
let words input= Regex.Matches(input, "\w+") |> Seq.cast |> Seq.map (fun (x:Match) -> x.Value.ToLower())
 
let wordCount = files >> 
                List.map downloadFile >>
                List.map words >>
                List.fold (fun acc x -> Seq.append acc x) Seq.empty >> 
                Seq.groupBy (fun x -> x) >> 
                Seq.map (fun (value, sequence) -> (value, Seq.length sequence))

let writeTo (path:string) (values:seq<string * int>) = 
    use writer = new StreamWriter(path)
    values |> Seq.iter (fun (value,count) -> writer.WriteLine(value + " " + count.ToString()))  

let startTime = DateTime.Now
let count = wordCount "Z:\\20_newsgroups"

printfn "Writing counts in alphabetical order"
count |> Seq.sort |> writeTo "C:\\results\\counts-alphabetical-fsharp.txt"

printfn "Writing counts in descending order"
count |> Seq.sortBy (fun (_, count) -> count * -1) |> writeTo "C:\\results\\counts-descending-fsharp.txt"

let endTime = DateTime.Now
printfn "Finished in: %d seconds" (endTime - startTime).Seconds 
~~~

The problem is that this version results in a StackOverFlow exception when I try to execute it with all the newsgroup articles although it does work correctly if I select just one of the folders.

From what I can tell the exception happens on line 24 when I get the text out of each of the files and store it in the list.

I tried changing this bit of code so that instead of doing that I combined the 'words' and 'downloadFile' functions so that the whole string wouldn't be saved but this doesn't seem to help that much. The exception just ended up happening a bit further down.

I'm not sure if it's possible to make this work by making use of lazy collections - I'm not that familiar with those yet so I"m not sure how to do it - or if this approach is just doomed!

Despite the fact it doesn't quite work there were some interesting things I noticed while playing with this problem:

<ul>
<li>At one stage <a href="http://twitter.com/markhneedham/statuses/6744178046">I was trying to deal with a list of sequences</a> whereby I had a list of sequences of words for each of the newsgroup articles. I found this really difficult to reason about as I was writing a 'List.map' and then a 'Seq.map' inside that.

I originally had the 'List.fold (fun acc x -> Seq.append acc x) Seq.empty' line happening later on in that composition of functions such that I grouped all the words and then counted how many there were before folding down into a single sequence. 

I realised this didn't make much sense and it would be much easier to just go to the sequence earlier on and make the code easier to follow.</li>
<li>I've previously written about <a href="http://www.markhneedham.com/blog/2009/07/12/f-wrapping-net-library-calls/">wrapping .NET library calls</a> and I was doing this quite a lot when I started writing this code.

For example I had written a function called 'isDirectory' which wrapped 'Directory.Exists' which I wrote more out of habit than anything else but it doesn't really add much value. I think when we're talking about wrapping static methods this is probably always the case. It's when we want to call a method on a C# object that the wrapping approach can be helpful.</li>
<li>I quite like the Ruby way of writing to a file...


~~~ruby

open("counts-descreasing-ruby", "w") do |out|
  counts.sort { |a, b| b[1] <=> a[1] }.each { |pair| out << "#{pair[0]}\t#{pair[1]}\n" }
end
~~~

...so I thought I'd see what it would look like to change my 'writeTo' function to be more like that:


~~~ocaml

let writeTo (path:string) (f: StreamWriter -> Unit) = 
    use writer = new StreamWriter(path)
    f writer  
~~~


~~~ocaml

writeTo "C:\\results\\counts-alphabetical-fsharp.txt" (fun out -> 
    count |> Seq.sort |> Seq.iter (fun (v,c) -> out.WriteLine(v + " " + c.ToString())))
~~~

I'm not sure it reads as well as the original version - the writing to file seems to becomes more prominent in this version than the data being written to it.</li>
</ul>

If anyone has any ideas about how I can get this not to blow up that would be cool!

These are some of the other solutions that I've come across:

<ul>
<li>
<a href="http://www.bestinclass.dk/index.php/2009/12/clojure-vs-ruby-scala-transient-newsgroups/comment-page-1/#comment-1234">Lau B. Jensen comments on Zach's post and provides an additional version in Clojure</a>
</li>
<li><a href="http://gist.github.com/257079">A version in Ruby by Sam Aaron</a></li>
<li><a href="https://gist.github.com/257236/e08eed68c89fef6c6ae1f857a8190bc3b5e3c278">A version in Ioke by Sam Aaron</a></li>
<li><a href="https://gist.github.com/257236/4b9ce470fda49282cc3bc2d89617506062811035">Ola Bini's slightly modified version of Sam Aaron's Ioke version</a></li>
<li><a href="http://gist.github.com/257164">A version by Shot in Ruby</a></li>
</ul>

