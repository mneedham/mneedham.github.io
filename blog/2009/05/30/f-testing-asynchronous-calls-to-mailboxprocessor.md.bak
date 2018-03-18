+++
draft = false
date="2009-05-30 20:38:02"
title="F#: Testing asynchronous calls to MailBoxProcessor"
tag=['f', 'xunitnet', 'asynchronous']
category=['F#']
+++

Continuing with my attempts to test some of the code in my <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">twitter</a> <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">application</a> I've been trying to work out how to test the <a href="http://www.markhneedham.com/blog/2009/05/02/f-erlang-style-messaging-passing/">Erlang style messaging</a> which I set up to process tweets when I had captured them using the <a href="http://code.google.com/p/tweetsharp/">TweetSharp API</a>.

The problem I had is that that processing is being done asynchronously so we can't test it in our normal sequential way.

Chatting with <a href="http://twitter.com/davcamer">Dave</a> about this he suggested that what I really needed was a latch which could be triggered when the asynchronous behaviour had completed, thus informing the test that it could proceed.

In the .NET library we have two classes which do this, <a href="http://msdn.microsoft.com/en-us/library/zd6a283y.aspx">AutoResetEvent</a> and <a href="http://msdn.microsoft.com/en-us/library/system.threading.manualresetevent.aspx">ManualResetEvent</a>. The main difference that I can see between them is that AutoResetEvent will automatically reset itself after one call to Set whereas ManualResetEvent lets any number of calls go through and doesn't reset its state unless you explicitly call the Reset method. 

In terms of what I wanted to do it doesn't actually make a big difference which one is used so I decided to use AutoResetEvent since that seems a bit simpler.

This is the code I'm trying to test:

~~~ocaml

    open Dimebrain.TweetSharp.Model

    type Message = Phrase of TwitterStatus | Stop

    type ILinkProcessor =
        abstract Send : TwitterStatus -> Unit
        abstract Stop : Unit -> Unit

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
      interface ILinkProcessor with 
            member x.Send(status:TwitterStatus) = agent.Post(Phrase(status))       
            member x.Stop() = agent.Post(Stop)
    
    type MainProcessor(linkProcessor:ILinkProcessor) =
      let agent = MailboxProcessor.Start(fun inbox ->
        let rec loop () =
          async {
                  let! msg = inbox.Receive()
                  match msg with
                  | Phrase item when item |> hasLink -> 
                    linkProcessor.Send(item)
                    return! loop()
                  | Phrase item ->
                    return! loop()
                  | Stop ->
                    return ()
                }
        loop()
      )
       
       member x.Send(statuses:seq<TwitterStatus>) =  statuses |> Seq.iter (fun status -> agent.Post(Phrase(status)))       
       member x.Stop() = agent.Post(Stop)
~~~

In particular I want to test that when I send a message to the MainProcessor it gets sent to the LinkProcessor if the message contains a link.

The idea is to stub out the LinkProcessor and then trigger the 'Set' method of our latch when we are inside the 'Send' method of our stubbed LinkProcessor:


~~~ocaml

[<Fact>]
let should_send_message_to_link_processor_if_it_contains_link_mutable () = 
    let latch = new AutoResetEvent(false)
    let messageWithLink = (new MessageBuilder(message = "a message with http://www.google.com link")).Build()
 
    let mutable interceptedMessage = ""
 
    let linkProcessorStub = { 
        new ILinkProcessor  with
            member x.Send (message) =
                 interceptedMessage <- message.Text
                 latch.Set() |> ignore
            member x.Stop() = ()  }
    
    (new MainProcessor(linkProcessorStub)).Send(seq { yield messageWithLink }) 

    let wasTripped = latch.WaitOne(1000)
    
    Assert.True(wasTripped)
    Assert.Equal(messageWithLink.Text, interceptedMessage)
~~~

The problem is this doesn't actually compile, we get an error on line 11:


~~~text

The mutable variable 'interceptedMessage' is used in an invalid way. Mutable variables may not be captured by closures. Consider eliminating this use of mutation or using a heap-allocated mutable reference cell via 'ref' and '!'.
~~~

I wasn't immediately sure how to get rid of the mutation so as the error message suggested I decided to try and use a <a href="http://lorgonblog.spaces.live.com/blog/cns!701679AD17B6D310!677.entry">heap allocated reference cell</a>:


~~~ocaml

 [<Fact>]
 let should_send_message_to_link_processor_if_it_contains_link_ref () = 
     let latch = new AutoResetEvent(false)
     let messageWithLink = (new MessageBuilder(message = "a message with http://www.google.com link")).Build()
  
     let interceptedMessage = ref ""
  
     let linkProcessorStub = { 
         new ILinkProcessor  with
             member x.Send (message) =
                  interceptedMessage := message.Text
                  latch.Set() |> ignore
             member x.Stop() = ()  } 
     
     (new MainProcessor(linkProcessorStub)).Send(seq { yield messageWithLink }) 
      
     let wasTripped = latch.WaitOne(1000)
  
     Assert.True(wasTripped)
     Assert.Equal(messageWithLink.Text, !interceptedMessage)
~~~

Now this works but I don't really like the look of line 6 where we setup the reference cell, it feels a little hacky. 

My next attempt was to try to get rid of the mutation by testing the message inside the linkProcessorStub:


~~~ocaml

[<Fact>]
let should_send_message_to_link_processor_if_it_contains_link_closure () = 
    let latch = new AutoResetEvent(false)
    let messageWithLink = (new MessageBuilder(message = "a message with http://www.google.com link")).Build()

    let linkProcessorStub =
        { new ILinkProcessor with   
            member x.Send (message) =
                 Assert.Equal(messageWithLink.Text, message.Text)
                 latch.Set() |> ignore
            member x.Stop() = ()  } 

    (new MainProcessor(linkProcessorStub)).Send(seq { yield messageWithLink }) 

     let wasTripped = latch.WaitOne(1000)

    Assert.True(wasTripped)
~~~

This seems like it should work the same as the previous example but in fact the Assert.Equal call on line 9 is being done on another thread since it is within the asynchronous operation. This means that when there is a failure with this assertion we don't get to hear about it.

I'm still trying to work out if there is a better way of doing this, perhaps by wrapping the AutoResetEvent in a custom type:


~~~ocaml

type AutoResetEvent with
    member x.WasTripped = x.WaitOne(1000)

type MyOneTimeLatch (autoResetEvent: AutoResetEvent) =
    let mutable savedMessage =  None
    member x.MessageReceived (message:TwitterStatus) = 
        savedMessage <- Some(message)
        autoResetEvent.Set() |> ignore
    member x.WasTripped = autoResetEvent.WasTripped
    member x.RetrieveMessage = 
        if(savedMessage.IsSome) then savedMessage.Value.Text else ""
~~~

Our test would then read like this:


~~~ocaml

[<Fact>]
let should_send_message_to_link_processor_if_it_contains_link_custom_type () = 
    let latch = new MyOneTimeLatch(autoResetEvent = new AutoResetEvent(false))
    let messageWithLink = (new MessageBuilder(message = "a message with http://www.google.com link")).Build()

    let linkProcessorStub = { 
        new ILinkProcessor  with
            member x.Send (message) =
                 latch.MessageReceived(message)
            member x.Stop() = ()  } 

    (new MainProcessor(linkProcessorStub)).Send(seq { yield messageWithLink }) 

    Assert.True(latch.WasTripped)
    Assert.Equal(messageWithLink.Text, latch.RetrieveMessage)
~~~
Does the job and maybe it's fine to have this as a stub for testing purposes. I'd be interested in hearing if anyone's found any good ways to do this kind of thing.
