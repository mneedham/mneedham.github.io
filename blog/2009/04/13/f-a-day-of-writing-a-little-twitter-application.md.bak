+++
draft = false
date="2009-04-13 22:09:37"
title="F#: A day of writing a little twitter application"
tag=['net', 'f']
category=['.NET', 'F#']
+++

I spent most of the bank holiday Monday here in Sydney writing a little application to scan through <a href="http://twitter.com">my twitter feed</a> and find me just the tweets which have links in them since for me that's where <a href="http://www.markhneedham.com/blog/2008/12/07/twitter-as-a-learning-tool/">a lot of the value of twitter lies</a>.

I'm sure someone has done this already but it seemed like a good opportunity to try and put a little of the F# that I've learned from reading <a href="http://manning.com/petricek/">Real World Functional Programming</a> to use. The code I've written so far is at the end of this post.

<h4>What did I learn?</h4>
<ul>
<li>I didn't really want to write a wrapper on top of the twitter API so I <a href="http://twitter.com/markhneedham/status/1505689603">put out a request for suggestions for a .NET twitter API</a>. It pretty much seemed to be a choice of either <a href="http://devblog.yedda.com/index.php/2007/05/16/twitter-c-library/">Yedda</a> or <a href="http://code.google.com/p/tweetsharp/">tweetsharp</a> and since the latter seemed easier to use I went with that. In the code you see at the end I have added the 'Before' method to the API because I needed it for what I wanted to do.</li>
<li>I found it really difficult writing the 'findLinks' method - the way I've written it at the moment uses pattern matching and recursion which isn't something I've spent a lot of time doing. Whenever I tried to think how to solve the problem <strong>my mind just wouldn't move away from the procedural approach</strong> of going down the collection, setting a flag depending on whether we had a 'lastId' or not and so on.

Eventually I explained the problem to <a href="http://blog.m.artins.net/">Alex</a> and working together through it we realised that there are three paths that the code can take:

<ol>
<li>When we have processed all the tweets and want to exit</li>
<li>The first call to get tweets when we don't have a 'lastId' starting point - I was able to get 20 tweets at a time through the API</li>
<li>Subsequent calls to get tweets when we have a 'lastId' from which we want to work backwards from</li>
</ol>

I think it is probably possible to reduce the code in this function to follow just one path by passing in the function to find the tweets but I haven't been able to get this working yet.</li>
<li>I recently watched a <a href="http://vimeo.com/3555080">F# video from Alt.NET Seattle</a> featuring <a href="http://www.pandamonial.com/">Amanda Laucher</a> where she spoke of the need to explicitly state types that we import from C# into our F# code. You can see that I needed to do that in my code when referencing the TwitterStatus class - I guess it would be pretty difficult for the use of that class to be inferred but it still made the code a bit more clunky than any of the other simple problems I've played with before. </li>
<li>I've not used any of the functions on 'Seq' until today - from what I understand these are available for applying operations to any collections which implement IEnumerable - which is exactly what I had! </li>
<li>I had to use the following code to allow F# interactive to recognise the Dimebrain namespace:


~~~text

#r "\path\to\Dimebrain.Tweetsharp.dll"
~~~

I thought it would be enough to reference it in my Visual Studio project and reference the namespace but apparently not.
</ul>


<h4>The code</h4>
This is the code I have at the moment - there are certainly some areas that it can be improved but I'm not exactly sure how to do it.

In particular:

<ul>
<li><strong>What's the best way to structure F# code?</strong> I haven't seen any resources on how to do this so it'd be cool if someone could point me in the right direction. The code I've written is just a collection of functions which doesn't really have any structure at all.</li>
<li><strong>Reducing duplication</strong> - I hate the fact I've basically got the same code twice in the 'getStatusesBefore' and 'getLatestStatuses' functions - I wasn't sure of the best way to refactor that. Maybe putting the common code up to the 'OnFriendsTimeline' call into a common function and then call that from the other two functions? I think a similar approach can be applied to findLinks as well.</li>
<li>The <strong>code doesn't feel that expressive to me</strong> - I was debating whether or not I should have passed a type into the 'findLinks' function - right now it's only possible to tell what each part of the tuple means by reading the pattern matching code which feels wrong. I think there may also be some opportunities to use the <a href="http://www.markhneedham.com/blog/2009/01/12/f-partial-function-application-with-the-function-composition-operator/">function composition operator</a> but I couldn't quite see where.</li>
<li><strong>How much context should we put in the names of functions?</strong> Most of my programming has been in OO languages where whenever we have a method its context is defined by the object on which it resides. When naming functions such as 'findOldestStatus' and 'oldestStatusId' I wasn't sure whether or not I was putting too much context into the function name. I took the alternative approach with the 'withLinks' function since I think it reads more clearly like that when it's actually used. </li>
</ul>



~~~ocaml

#light

open Dimebrain.TweetSharp.Fluent
open Dimebrain.TweetSharp.Extensions
open Dimebrain.TweetSharp.Model
open Microsoft.FSharp.Core.Operators 

let getStatusesBefore (statusId:int64) = FluentTwitter
                                            .CreateRequest()
                                            .AuthenticateAs("userName", "password")
                                            .Statuses()
                                            .OnFriendsTimeline()
                                            .Before(statusId)
                                            .AsJson()
                                            .Request()
                                            .AsStatuses()
                                    
let withLinks (statuses:seq<Dimebrain.TweetSharp.Model.TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus -> eachStatus.Text.Contains("http"))

let print (statuses:seq<Dimebrain.TweetSharp.Model.TwitterStatus>) =
    for status in statuses do
        printfn "[%s] %s" status.User.ScreenName status.Text    
 
let getLatestStatuses  = FluentTwitter
                            .CreateRequest()
                            .AuthenticateAs("userName", "password")
                            .Statuses()
                            .OnFriendsTimeline()
                            .AsJson()
                            .Request()
                            .AsStatuses()                                    

let findOldestStatus (statuses:seq<Dimebrain.TweetSharp.Model.TwitterStatus>) = 
    statuses |> Seq.sort_by (fun eachStatus -> eachStatus.Id) |> Seq.hd

let oldestStatusId = (getLatestStatuses |> findOldestStatus).Id  
 
let rec findLinks (args:int64 * int * int) =
    match args with
    | (_, numberProcessed, recordsToSearch) when numberProcessed >= recordsToSearch -> ignore
    | (0L, numberProcessed, recordsToSearch) -> 
        let latestStatuses = getLatestStatuses
        (latestStatuses |> withLinks) |> print
        findLinks(findOldestStatus(latestStatuses).Id, numberProcessed + 20, recordsToSearch)    
    | (lastId, numberProcessed, recordsToSearch) ->  
        let latestStatuses = getStatusesBefore lastId
        (latestStatuses |> withLinks) |> print
        findLinks(findOldestStatus(latestStatuses).Id, numberProcessed + 20, recordsToSearch)


let findStatusesWithLinks recordsToSearch =
    findLinks(0L, 0, recordsToSearch) |> ignore
~~~

And to use it to find the links contained in the most recent 100 statuses of the people I follow:


~~~text

findStatusesWithLinks 100;;
~~~

Any advice on how to improve this will be gratefully received. I'm going to continue working this into a little DSL which can print me up a nice summary of the links that have been posted during the times that I'm not on twitter watching what's going on.
