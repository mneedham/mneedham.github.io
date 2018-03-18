+++
draft = false
date="2009-04-28 23:43:22"
title="F#: Overloading functions/pattern matching"
tag=['f']
category=['F#']
+++

While trying to <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">refactor my twitter application</a> into a state where I could use Erlang style message passing to process some requests asynchronously while still hitting twitter to get more messages I came across the problem of wanting to overload a method.

By default it seems that you can't do method overloading in F# unless you make use of the OverloadID attribute which I learnt about from reading <a href="http://www.scottseely.com/blog/09-03-06/Method_Overloading_in_F.aspx">Scott Seely's blog post</a>:

<blockquote>
Adding the OverloadID attribute to a member permits it to be part of a group overloaded by the same name and arity. The string must be a unique name amongst those in the overload set. Overrides of this method, if permitted, must be given the same OverloadID, and the OverloadID must be specified in both signature and implementation files if signature files are used.
</blockquote>

I therefore ended up with this somewhat horrible looking code:


~~~ocaml

type TwitterMessageProcessor =
	let agent = MailboxProcessor.Start(fun inbox ->
	(* ... *)
		[<OverloadID("Send.TwitterStatus")>]
		member x.Send(message:TwitterStatus) = agent.Post(Phrase(message))
		[<OverloadID("Send.list.TwitterStatus")>]
		member x.Send(message: seq<TwitterStatus>) = message |> Seq.iter (fun message -> agent.Post(Phrase(message)))
~~~

This allows me to either send a single TwitterStatus or a collection of TwitterStatuses to the TwitterMessageProcessor but it feels like the C# approach to solving the problem.

Talking to <a href="http://www.twitter.com/davcamer">Dave</a> about this problem he suggested that maybe pattern matching was the way to go about this problem but I wasn't sure how to do pattern matching based on the input potentially being a different type.

A bit of googling turned up a <a href="http://stackoverflow.com/questions/501069/f-functions-with-generic-parameter-types">Stack Overflow thread about defining functions to work on multiple types of parameters</a>.

I tried this out and ended up with the following code which uses type constraints:


~~~ocaml

type TwitterMessageProcessor() =
	let agent = MailboxProcessor.Start(fun inbox ->
	(* ... *)
		member x.Send(message) =
     		match box message with
         		| :? seq<TwitterStatus> as message -> message |> Seq.iter (fun message -> agent.Post(Phrase(message)))
         		| :? TwitterStatus as message -> agent.Post(Phrase(message))
         		| _ -> failwith "Unmatched message type"
~~~

This seems a bit nicer but obviously we lose our type safety that we had before - you can pretty much send in anything you want to the Send method. Looking at the code in <a href="http://www.red-gate.com/products/reflector/">Reflector</a> confirms this:


~~~csharp

public void Send<T>(T message)
{
    object obj2 = message;
    IEnumerable<TwitterStatus> $typeTestResult@37 = obj2 as IEnumerable<TwitterStatus>;
    if ($typeTestResult@37 != null)
    {
        IEnumerable<TwitterStatus> message = $typeTestResult@37;
        Seq.iter<TwitterStatus>(new Twitter.clo@37_1(this), message);
    }
    else
    {
        TwitterStatus $typeTestResult@38 = obj2 as TwitterStatus;
        if ($typeTestResult@38 != null)
        {
            TwitterStatus message = $typeTestResult@38;
            this.agent@16.Post(new Twitter.Message._Phrase(message));
        }
        else
        {
            Operators.failwith<Unit>("Unmatched message type");
        }
    }
}
~~~

I'm not really happy with either of these solutions but I haven't come across a better way to achieve this but I'd be interested in doing so if anyone has any ideas.
