+++
draft = false
date="2009-07-26 23:45:14"
title="F#: Playing around with asynchronous workflows"
tag=['f', 'asynchronous-workflows']
category=['F#']
+++

I spent a bit of time over the weekend playing around with F# <a href="http://www.infoq.com/articles/pickering-fsharp-async">asynchronous workflows</a> and seeing how they could be used to launch Firefox windows asynchronously for my <a href="http://www.markhneedham.com/blog/2009/07/12/f-a-day-writing-a-feedburner-graph-creator/">FeedBurner graph creator</a>.

Initially I decided to try out the 'Async.RunWithContinuations' function which I <a href="http://codebetter.com/blogs/matthew.podwysocki/archive/2009/06/20/f-async-running-with-continuation-scissors.aspx">recently read about on Matthew Podwysocki's blog</a>.

Matthew describes this as being a function which is useful for executing a single operation asynchronously and this worked out quite well for me as my application only has the ability to get one feed and then create a graph from its data.

I changed the Execute function (which <a href="http://www.markhneedham.com/blog/2009/07/16/f-passing-command-line-arguments-to-a-script/">takes in arguments from the command line</a> as I wrote about previously) to launch a firefox window with the graph loaded:


~~~ocaml

let launchInFirefox url = async { System.Diagnostics.Process.Start(@"C:\Program Files\Mozilla Firefox\firefox.exe", url) |> ignore }

let timeNow () = System.DateTime.Now.ToLongTimeString()

let Execute args =    
    if (Array.length args <> 3) 
    then printfn "Expected usage: [feedName] [startDate yyyy-mm-dd] [endDate yyyy-mm-dd]" 
    else 
        let feedName, startDate, endDate = args.[0], args.[1], args.[2]
        let graphUri = (ShowFeedBurnerStats feedName startDate endDate).AbsoluteUri

        Async.RunWithContinuations ( (fun cont -> printfn "Downloaded feed graph for %s at %s" feedName (timeNow())), 
                                     (fun ex -> printfn "Failed to download feed graph for %s - %s %s " feedName (ex.Message) (ex.StackTrace)), 
                                     (fun cancelled -> printfn "Feed graph downloading for %s was cancelled" feedName),
                                     (launchInFirefox graphUri) ) 
~~~ 

The function actually takes in three continuations as well as the asynchronous computation to run: 

<ul>
<li>A continuation to run if the computation completes successfully</li>
<li>An exception continuation to run if the computation throws an exception. I was able to test this out by trying to launch a process which did not exist</li>
<li>A cancellation continuation to run if there is a signal for the computation to be cancelled</li>
</ul>

We then pass in the asynchronous computation as the last argument to the function which in this case is a process which launches FireFox with the url of the graph.

This works quite nicely but you don't really notice that much different between launching the browser this way and just doing it using the 'Async.RunSynchronously' function.

It becomes a bit more interesting if we try to execute more than one asynchronous computations which in this case means creating multiple graphs at the same time.

My first attempt was to launch each of these computations synchronously:


~~~ocaml

let CreateGraphs (feeds:seq<string>) =
    feeds |> 
    Seq.map (fun f -> ShowFeedBurnerStats f "2009-03-01" "2009-07-25") |>
    Seq.map (fun uri -> launchInFirefox uri.AbsoluteUri ) |> 
    Seq.iter (Async.RunSynchronously)
~~~

I called this function like so:


~~~ocaml

let feeds = seq { yield "markneedham"; yield "scotthanselman"; yield "codethinked"; yield "haacked"; yield "Iserializable" };
CreateGraphs feeds
~~~

That works fine although there is a noticeable pause as each of these is loaded into the browser one after the other.

One way to get around this is to make use of the 'Async.Parallel' function which converts a sequence of asynchronous computations into a single asynchronous computation which can execute all of the individual asynchronous computations.

I initially got confused here and thought that passing a sequence of asynchronous computations to 'Async.Parallel' actually executed them but as I learnt you actually need to pass the result to one of the functions which actually runs the asynchronous computations.

We don't need to change our function too much to achieve this:


~~~ocaml

let CreateGraphsParallel (feeds:seq<string>) =
    feeds |> 
    Seq.map (fun f -> ShowFeedBurnerStats f "2009-03-01" "2009-07-25") |>
    Seq.map (fun uri -> launchInFirefox uri.AbsoluteUri ) |> 
    Async.Parallel |>
    Async.RunSynchronously
~~~


~~~ocaml

let feeds = seq { yield "markneedham"; yield "scotthanselman"; yield "codethinked"; yield "haacked"; yield "Iserializable" };
CreateGraphsParallel feeds
~~~

The graphs seem to get launched in FireFox much more quickly using this method and there is no real pause, just a flurry of new tabs being launched as each of the graphs is opened.

I thought the 'Async.Start' function might allow us to achieve a similar result as the API comments state 'Start the asynchronous computation in the thread pool. Do not await its result' but I saw similar behaviour to when I used 'Async.RunSynchronously'


~~~ocaml

let CreateGraphsSpawn (feeds:seq<string>) =
    feeds |> 
    Seq.map (fun f -> ShowFeedBurnerStats f "2009-03-01" "2009-07-25") |>
    Seq.map (fun uri -> launchInFirefox uri.AbsoluteUri ) |> 
    Seq.iter(Async.Start)
~~~


~~~ocaml

let feeds = seq { yield "markneedham"; yield "scotthanselman"; yield "codethinked"; yield "haacked"; yield "Iserializable" };
CreateGraphsSpawn feeds
~~~

Out of these 'Async.Parallel' seems to be the best function to use to get quick feedback from multiple computations. 

There are also a few other functions that I haven't tried out yet and I'm intrigued as to whether we would achieve good results by making use of <a href="http://www.markhneedham.com/blog/2009/05/30/f-testing-asynchronous-calls-to-mailboxprocessor/">MailBoxProcessors</a> or not.
