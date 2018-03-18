+++
draft = false
date="2009-05-02 01:53:56"
title="F#: Erlang style messaging passing"
tag=['f']
category=['F#']
+++

As I mentioned in my previous post about over loading methods in F# I've been trying to refactor my twitter application into a state where it can concurrently process twitter statuses while continuing to retrieve more of them from the twitter website.

I played around a bit with Erlang last year and one thing that I quite liked is the message passing between processes to allow operations to be performed concurrently.

I found a <a href="http://weblogs.asp.net/podwysocki/archive/2008/06/18/concurrency-in-net-learning-from-erlang.aspx">cool blog post by Matthew Podwysocki where he explains how we can achieve Erlang message passing in F# by using mail boxes</a> so I decided to try and follow his example to see if I could do a similar thing with my twitter application.

As far as I understand the Erlang approach to messaging follows the <a href="http://en.wikipedia.org/wiki/Actor_model">actor model</a> which is defined as follows:

<blockquote>
An actor is a computational entity that, in response to a message it receives, can concurrently:

   <ul><li>send a finite number of messages to other actors</li>
    <li>create a finite number of new actors</li>
    <li>designate the behavior to be used for the next message it receives.</li></ul>
</blockquote>

I can definitely see the first two ideas in the solution that I've ended up with but I'm not sure how you would do the third.

From reading Joe Armstrong's <a href="http://www.amazon.co.uk/Programming-Erlang-Software-Concurrent-World/dp/193435600X/ref=sr_1_1?ie=UTF8&s=books&qid=1241182065&sr=8-1">Programming Erlang</a> book and <a href="http://strangelights.com/blog/archive/2007/10/24/1601.aspx#2073">Ulf Wiger's comment on Robert Pickering's blog</a>, I understand that the code we can create in F# is not exactly the same as what we can do in Erlang since in Erlang each process has its own mailbox whereas in F# a thread can handle more than one mailbox.

The reason for me wanting to do this is because the twitter API only allows me to retrieve 20 statuses at a time and if I'm getting a large number of them my <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">original design</a> means that we are just waiting for the statuses to be accumulated before we can do anything else with them - I want to make this a bit more real time.

This is what the code looks like at the moment:


~~~ocaml

open System
open Microsoft.FSharp.Control.CommonExtensions
open Microsoft.FSharp.Control
open System.Threading

type Message = Phrase of TwitterStatus | Stop

type LinkProcessor(callBack) =
  let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () =
      async {
              let! msg = inbox.Receive()
              match msg with
              | Phrase item ->
                callBack item
                return! loop()
              | Stop ->
                return ()
            }
    loop()
  )
  
     member x.Send(message) =
        match box message with
            | :? seq<TwitterStatus> as message -> message |> Seq.iter (fun message -> agent.Post(Phrase(message)))
            | :? TwitterStatus as message -> agent.Post(Phrase(message))
            | _ -> failwith "Unmatched message type" 
   
   member x.Stop() = agent.Post(Stop)

let linkProcessor = new LinkProcessor(fun status -> printfn "[%s] %s, thread id: (%d)" status.User.ScreenName status.Text Thread.CurrentThread.ManagedThreadId)

let hasLink (message:TwitterStatus) = message.Text.Contains("http")

type MainProcessor() =
  let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () =
      async {
              let! msg = inbox.Receive()
              match msg with
              | Phrase item when item |> hasLink -> 
                linkProcessor.Send(item)
                return! loop()
              | Phrase item ->
                printfn "in mainprocessor, thread id: (%d)" Thread.CurrentThread.ManagedThreadId
                return! loop()
              | Stop ->
                return ()
            }
    loop()
  )
   
   member x.Send(message) =
        match box message with
            | :? seq<TwitterStatus> as message -> message |> Seq.iter (fun message -> agent.Post(Phrase(message)))
            | :? TwitterStatus as message -> agent.Post(Phrase(message))
            | _ -> failwith "Unmatched message type" 
   
   member x.Stop() = agent.Post(Stop)
   
let centralProcessor = new MainProcessor()
~~~

And this is the code where we process the statuses:


~~~ocaml

let rec findStatuses (args:int64 * int * int * seq<TwitterStatus>) =
    let findOldestStatus (statuses:seq<TwitterStatus>) = 
        statuses |> Seq.sort_by (fun eachStatus -> eachStatus.Id) |> Seq.hd
    match args with 
    | (_, numberProcessed, statusesToSearch, soFar) when numberProcessed >= statusesToSearch -> soFar |> ignore
    | (lastId, numberProcessed, statusesToSearch, soFar) ->  
        let latestStatuses = getStatusesBefore lastId
        centralProcessor.Send(latestStatuses)
        findStatuses(findOldestStatus(latestStatuses).Id, numberProcessed + 20, statusesToSearch, Seq.append soFar latestStatuses)
~~~ 
(The rest of the code is <a href="http://pastie.org/465092">here</a>)

There is certainly some duplication in there - I think it should be possible to get a BaseMailboxProcessor - and I found it annoying that I needed to have a different type of mail box processor for each of the cases so that I could have different pattern matching in each. 

In Erlang that scaffolding is built into the language and you just need to care about the pattern matching which is the important thing here.

I've setup a callback function that's passed to the LinkProcessor which prints out the status when it processes it. The next step is to store that somewhere so I can view them later.

Running this though the threadId is always the same. The console output looks like this:


~~~text

in mainprocessor, thread id: (6)
in mainprocessor, thread id: (6)
in mainprocessor, thread id: (6)
in mainprocessor, thread id: (6)
[jbristowe] Beautiful morning in downtown Edmonton: http://twitpic.com/4c6n8 #YEG, thread id: (6)
[MParekh] ABC News does a fly-by correction of a critical 2007 Torture story. http://bit.ly/C9tNH, thread id: (6)
~~~

They processing of statuses doesn't ever interleave either so it looks like the thread is switching its attention between the two mail boxes.

I was expecting to see different threads processing each mail box but I'm not sure whether that's a correct expectation or not?
