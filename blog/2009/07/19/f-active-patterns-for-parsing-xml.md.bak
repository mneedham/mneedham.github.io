+++
draft = false
date="2009-07-19 12:12:13"
title="F#: Active patterns for parsing xml"
tag=['f', 'active-patterns']
category=['F#']
+++

I decided to spend some time doing some refactoring on the <a href="http://www.markhneedham.com/blog/2009/07/12/f-a-day-writing-a-feedburner-graph-creator/">FeedBurner application</a> that I started working on last week and the first area I worked on was cleaning up the way that the xml we get from FeedBurner is parsed.

While <a href="http://www.markhneedham.com/blog/2009/07/16/f-passing-command-line-arguments-to-a-script/">playing around with the application from the command line</a> I realised that it didn't actually cover error conditions - such as passing in an invalid feed name - very well and I thought this would be a good opportunity to make use of an <a href="http://blogs.msdn.com/chrsmith/archive/2008/02/21/Introduction-to-F_2300_-Active-Patterns.aspx">active pattern</a> to handle this.

I wanted to try and test drive this bit of code so my first idea was to try and call the active pattern directly from my test - I am testing using <a href="http://www.infoq.com/news/2009/05/nunit-release">NUnit 2.5</a> which now allows us to create tests without the need for a class with a [TestFixture] attribute on:


~~~ocaml

[<Test>]
let should_return_no_feed_given_invalid_xml () =
	let feedType = Xml.(|NoFeedFound|FeedBurnerFeed|) "invalid xml"
	// other code
~~~


~~~ocaml

let (|NoFeedFound|FeedBurnerFeed|) xml = 
	NoFeedFound()
~~~

The problem I ran into with this approach is that the value of feedType when this test ran was 'Microsoft.FSharp.Core.Choice`2+_Choice1Of2' and I couldn't see a way to access this at compile time in order to assert against it. Either way a test asserting that the return value was 'Choice1Of2' doesn't seem to be the most expressive test anyway.

I chatted with about this a bit with <a href="http://intwoplacesatonce.com/">Dave</a> and he suggested that it would probably be easier to test the active pattern via the function while actually makes use of it.

I ended up with the following three tests:


~~~ocaml

open FeedBurnerService

[<Test>]
let should_throw_exception_if_feed_xml_is_invalid () =
    Assert.Throws<FailureException>(fun () -> FeedBurnerService.Parse "some broken xml" |> ignore) |> ignore

[<Test>]
let should_throw_exception_if_no_feed_found () =
    let feedXml = @"<?xml version=""1.0"" encoding=""utf-8"" ?>
                    <rsp stat=""fail"">
                        <err code=""1"" msg=""Feed Not Found"" />
                    </rsp>"

    Assert.Throws<FailureException>((fun () -> FeedBurnerService.Parse feedXml |> ignore), "Failed to process feed: Feed Not Found") |> ignore   
                                    
[<Test>]     
let should_retrieve_circulation_and_date_if_valid_xml () =
    let feedXml = @"<?xml version=""1.0"" encoding=""UTF-8""?>
                    <rsp stat=""ok"">
                        <feed id=""tdv0bg210cr731gc3nssn512cg"" uri=""MarkNeedham"">
                            <entry date=""2009-07-16"" circulation=""630"" hits=""1389"" reach=""629"" />
                        </feed>
                    </rsp>"
    
    let feedBurnerApi = FeedBurnerService.Parse feedXml
    let entry = feedBurnerApi |> Entries |> Seq.hd

    Assert.AreEqual(entry.Circulation, 630) 
    Assert.AreEqual(entry.Date, "2009-07-16")
~~~

The interesting thing here is that the 'Assert.Throws' method takes in a C# delegate so we need to wrap the call to 'FeedBurnerService.Parse' inside a function. As with <a href="http://www.markhneedham.com/blog/2009/03/28/f-forcing-type-to-unit-for-assertshouldthrow-in-xunitnet/">xUnit.NET's equivalent method</a> we need to ignore the results of the function call in these tests.


~~~ocaml

module FeedBurnerService = 
    open System.Xml.Linq
    open System

    let GetDescendants element (xDocument:XDocument)  = xDocument.Descendants(xName element)
    let GetAttribute element (xElement:XElement) = xElement.Attribute(xName element)   

	type FeedBurnerApi(entries:seq<Entry>) =	
    		member x.Entries = entries
	and
		Entry(date : string, circulation : int) =
        		member x.Date = date 
        		member x.Circulation = circulation

    let Entries (feedBurnerApi:FeedBurnerApi) = feedBurnerApi.Entries 

    let (|NoFeedFound|FeedBurnerFeed|) xml = 
        try 
            let document = xml |> XDocument.Parse
            let entries = document |> 
                          GetDescendants "entry" |> 
                          Seq.map (fun element -> GetAttribute "circulation" element, GetAttribute "date" element) |>
                          Seq.map (fun attribute -> new Entry(circulation =  Int32.Parse((fst attribute).Value), date = (snd attribute).Value) )
            
            match Seq.length entries with 
                | 0 -> NoFeedFound((document |> GetDescendants "err" |> Seq.hd |> GetAttribute "msg").Value)
                | _ -> FeedBurnerFeed(new FeedBurnerApi(entries))
        with 
            | :? System.Xml.XmlException as ex -> NoFeedFound(ex.Message)

    let Parse xml =
        match xml with 
            | NoFeedFound(error) -> failwith ("Failed to process feed: " + error)
            | FeedBurnerFeed(entries) -> entries  
~~~

I continued using the idea of <a href="http://www.markhneedham.com/blog/2009/07/12/f-wrapping-net-library-calls/">creating F# functions to wrap C# style method calls</a> with the 'Entries' function which delegates to the 'Entries' property on 'FeedBurnerApi' which reduces the need to store intermediate state. I probably could have done the same for the 'Date' and 'Circulation' properties although I couldn't see a significant improvement in the readability of the code by doing this.

I have also made use of the 'and' keyword to define the 'Entry' type because it is referenced by the 'FeedBurnerApi' type and therefore needs to be defined at that stage. The other way to ensure this was the case would be to define 'Entry' before 'FeedBurnerApi' although this doesn't seem to read as nicely to me.

We are making use of a multi case active pattern in the code which means that the input we are processing with the active pattern can be split into two different things in this case. Don Syme goes into <a href="http://blogs.msdn.com/dsyme/archive/2007/04/07/draft-paper-on-f-active-patterns.aspx">more detail on the different types of active patterns in his paper</a> and <a href="http://blogs.msdn.com/chrsmith/archive/2008/02/21/Introduction-to-F_2300_-Active-Patterns.aspx">Chris Smith also covers them in his post</a>.

The code for the active pattern feels a bit too imperative at the moment although I wasn't sure of the best way to cover the different scenarios without writing it this way - no doubt there is a more functional way to do this but I can't see it yet.

Making use of the active pattern in the code has made it much easier to work with than passing around a sequence of tuples as I was doing previously. It has also made it easy to exit from the program early if there is a problem with the data inputted.
