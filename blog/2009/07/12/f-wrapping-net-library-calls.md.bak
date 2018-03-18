+++
draft = false
date="2009-07-12 12:11:46"
title="F#: Wrapping .NET library calls"
tag=['f']
category=['F#']
+++

I've been spending a bit of time writing some code to parse the xml of my Feedburner RSS feed and create a graph to show both the daily and weekly average subscribers which you can't currently get from the Feedburner dashboard.

One thing which I found while doing this is that calls to the .NET base class library don't seem to fit in that well with the way that you would typically compose functions together in F#.

For example one of the first things I wanted to do was print the date and the circulation count to the console which I originally did like this:


~~~ocaml

open System.IO
open System.Net
open Microsoft.FSharp.Control
open System.Xml.Linq
open System

let xName value = XName.Get value

// GetXml is a function of type string -> string

let GetFeedBurnerStats url = 
    let feedBurnerXml = GetXml url |> XDocument.Parse
    feedBurnerXml.Descendants(xName "entry") |> 
    Seq.map (fun x -> x.Attribute(xName "circulation"), x.Attribute(xName "date")) |>
    Seq.iter (fun x -> printfn "%s %s" (fst x).Value (snd x).Value)
~~~	

It's quite annoying that we need to store the XDocument as a value before being able to call one of the methods on it to get the data that we want.

I realised that if I created a function which took in the element whose descendants I wanted to find and the XDocument I could then call the 'XDocument.Descendants()' method inside that function:


~~~ocaml

let xName value = XName.Get value
let GetDescendants element (xDocument:XDocument)  = xDocument.Descendants(xName element)

let GetFeedBurnerStats = 
    GetXml >> 
    XDocument.Parse >> 
    GetDescendants "entry" >>
    Seq.map (fun x -> x.Attribute(xName "circulation"), x.Attribute(xName "date")) >>
    Seq.iter (fun x -> printfn "%s %s" (fst x).Value (snd x).Value)
~~~

Since we no longer need to store the intermediate step of creating the XDocument we can now just chain together the functions using the <a href="http://www.markhneedham.com/blog/2009/01/12/f-partial-function-application-with-the-function-composition-operator/">functional composition operator</a> instead of the <a href="http://www.markhneedham.com/blog/2009/01/06/f-forward-operator/">forward operator</a>.

We can also do this with the calls to 'Attribute' in the 'Seq.map' function on line 9 which helps simplify the code around there.


~~~ocaml

let xName value = XName.Get value
let GetDescendants element (xDocument:XDocument)  = xDocument.Descendants(xName element)
let GetAttribute element (xElement:XElement) = xElement.Attribute(xName element)

let GetFeedBurnerStats = 
    GetXml >> 
    XDocument.Parse >> 
    GetDescendants "entry" >>
    Seq.map (fun x -> GetAttribute "circulation" x, GetAttribute "date" x) >>
    Seq.iter (fun x -> printfn "%s %s" (fst x).Value (snd x).Value)
~~~
