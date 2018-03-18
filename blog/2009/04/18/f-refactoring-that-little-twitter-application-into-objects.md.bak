+++
draft = false
date="2009-04-18 08:47:06"
title="F#: Refactoring that little twitter application into objects"
tag=['f', 'refactoring']
category=['F#']
+++

I previously wrote about a <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">little twitter application I've been writing to go through my twitter feed and find only the tweets with links it</a> and while it works I realised that I was finding it quite difficult to add any additional functionality to it.

I've been following the examples in <a href="http://manning.com/petricek/">Real World Functional Programming</a> which has encouraged an approach of creating functions to do everything that you want to do and then mixing them together.

This works quite well for getting a quick development cycle but I found that I ended up mixing different concerns in the same functions, making it really difficult to test the code I've been working on - I decided not to TDD this application because I don't know the syntax well enough. I am now suffering from that decision!

Chatting to <a href="http://pilchardfriendly.wordpress.com/">Nick</a> about the problems I was having he encouraged me to look at the possibility of structuring the code into different objects - this is still the best way that I know for describing intent and managing complexity although it doesn't feel like 'the functional way'.

Luckily Chapter 9 of the book (which I hadn't reached yet!) explains how to restructure your code into a more manageable structure.

I'm a big fan of creating lots of little objects in C# land so I followed the same approach here. I found <a href="http://forum.codecall.net/programming-news/10523-object-oriented-f-creating-classes.html">this post</a> really useful for helping me understand the F# syntax for creating classes and so on.

I started by creating a type to store all the statuses:


~~~ocaml

type Tweets = { TwitterStatuses: seq<TwitterStatus> }  
~~~

F# provides quite a nice way of moving between the quick cycle of writing functions and testing them to structuring objects with behaviour and data together by allowing us to <strong>append members using augmentation</strong>.

From the previous code we have these two functions:


~~~ocaml

let withLinks (statuses:seq<TwitterStatus>) = 
    statuses |> Seq.filter (fun eachStatus -> eachStatus.Text.Contains("http"))

let print (statuses:seq<TwitterStatus>) =
    for status in statuses do
        printfn "[%s] %s" status.User.ScreenName status.Text  
~~~

We can add these two methods to the Tweets type using type augmentations:


~~~ocaml

type Tweets with
    member x.print() = print x.TwitterStatuses
    member x.withLinks() = { TwitterStatuses = withLinks x.TwitterStatuses}
~~~

It looks quite similar to C# extension methods but the methods are actually added to the class rather than being defined as static methods. The type augmentations need to be in the same file as the type is defined.

Next I wanted to put the <a href="http://code.google.com/p/tweetsharp/">tweetsharp</a> API calls into their own class. It was surprisingly tricky working out how to create a class with a no argument constructor but I guess it's fairly obvious in the end.


~~~ocaml

type TwitterService() = 
        static member GetLatestTwitterStatuses(recordsToSearch) =    
            findStatuses(0L, 0, recordsToSearch, [])  
~~~

I managed to simplify the recursive calls to the Twitter API to keep getting the next 20 tweets as well:


~~~ocaml

let friendsTimeLine = FluentTwitter.CreateRequest().AuthenticateAs("userName", "password").Statuses().OnFriendsTimeline()
let getStatusesBefore (statusId:int64) = 
    if(statusId = 0L) then
        friendsTimeLine.AsJson().Request().AsStatuses()  
    else
        friendsTimeLine.Before(statusId).AsJson().Request().AsStatuses()        
        
let rec findStatuses (args:int64 * int * int * seq<TwitterStatus>) =
    let findOldestStatus (statuses:seq<TwitterStatus>) = 
        statuses |> Seq.sort_by (fun eachStatus -> eachStatus.Id) |> Seq.hd
    match args with 
    | (_, numberProcessed, statusesToSearch, soFar) when numberProcessed >= statusesToSearch -> soFar
    | (lastId, numberProcessed, statusesToSearch, soFar) ->  
        let latestStatuses = getStatusesBefore lastId
        findStatuses(findOldestStatus(latestStatuses).Id, numberProcessed + 20, statusesToSearch, Seq.append soFar latestStatuses)
~~~

To get the tweets we can now do the following:


~~~ocaml

let myTweets = { TwitterStatuses = TwitterService.GetLatestTwitterStatuses 100 };;
myTweets.withLinks().print();;
~~~

I still feel that I'm thinking a bit too procedurally when writing this code but hopefully that will get better as I play around with F# more.

One other lesson from this refactoring is that it's so much easier to refactor code when you have tests around them - because I didn't do this I had to change a little bit then run the code manually and check nothing had broken. Painful!
