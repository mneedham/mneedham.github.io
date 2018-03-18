+++
draft = false
date="2009-06-02 22:01:52"
title="F#: Tuples don't seem to express intent well"
tag=['f']
category=['F#']
+++

Tuples are one of the data types that I learnt about at university but never actually got to use for anything until I started playing around with F# which has this type in the language.

A <a href="http://diditwith.net/2008/01/18/WhyILoveFTuples.aspx">tuple</a> describes an ordered group of values and in that sense is similar to a C# anonymous type except an anonymous type's values are named whereas a tuple's are not.

In F# we can create one by separating a sequence of values with a comma in a value assignment:


~~~ocaml

> let myTuple = "mark", 7;;

val myTuple : string * int
~~~

As we can see the type of myTuple is 'string * int' and there are some functions such as 'fst' and 'snd' which allow us to extract the individual values from the tuple.

They're also quite nice to work with in terms of pattern matching which is why I decided to make use of a tuple in my twitter application to represent the running state of the retrieval of tweets.


~~~ocaml

type TwitterService() = 
        static member GetLatestTwitterStatuses(recordsToSearch) =    
            findStatuses(0L, 0, recordsToSearch)
~~~


~~~ocaml

    let rec findStatuses (args:int64 * int * int) =
        let findOldestStatus (statuses:seq<TwitterStatus>) = 
            statuses |> Seq.sortBy (fun eachStatus -> eachStatus.Id) |> Seq.hd
        match args with 
        | (_, numberProcessed, statusesToSearch) when numberProcessed >= statusesToSearch -> centralProcessor.Stop()
        | (lastId, numberProcessed, statusesToSearch) ->  
            let latestStatuses = getStatusesBefore lastId
            centralProcessor.Send(latestStatuses)
            findStatuses(findOldestStatus(latestStatuses).Id, numberProcessed + 20, statusesToSearch)
~~~

The pattern matching is evident here and has allowed me to easily separate each of the values and give it a meaningful name inside the findStatuses function.

The problem I had is that looking at the 'GetLatestTwitterStatuses' method after a few weeks of not working with this code I didn't really have any idea what the first two 0's being passed to 'findStatuses' mean - I'm not expressing intent very well at all.

I decided to refactor this code to make it a bit more explicit by introducing a type to describe the search parameters.


~~~ocaml

    type TwitterService() = 
            static member GetLatestTwitterStatuses(recordsToSearch) =    
                findStatuses(new TwitterBackwardsSearch(startingTweetId = 0L,tweetsSoFar = 0 , tweetsToTraverse =  recordsToSearch))  
~~~


~~~ocaml

    type TwitterBackwardsSearch(startingTweetId:int64, tweetsSoFar:int, tweetsToTraverse:int) =
        member x.ShouldKeepSearching() = tweetsSoFar < tweetsToTraverse
        member x.LastId = startingTweetId
        member x.NextSearch(newStartingTweetId: int64) = 
            new TwitterBackwardsSearch( startingTweetId = newStartingTweetId, tweetsSoFar = tweetsSoFar+20, tweetsToTraverse = tweetsToTraverse)


    let rec findStatuses(twitterBackwardsSearch:TwitterBackwardsSearch) =
        if(twitterBackwardsSearch.ShouldKeepSearching()) then
            let findOldestStatus (statuses:seq<TwitterStatus>) = statuses |> Seq.sortBy (fun eachStatus -> eachStatus.Id) |> Seq.hd
            let latestStatuses = getStatusesBefore twitterBackwardsSearch.LastId
            centralProcessor.Send(latestStatuses)
            findStatuses(twitterBackwardsSearch.NextSearch(findOldestStatus(latestStatuses).Id))
        else
            centralProcessor.Stop()  
~~~

There's more code there than there was in the original solution but I think it is easier to work out what's going on from reading that than from reading the original code because it's more explicit.

Another advantage I found from doing this refactoring was that I could write tests describing whether or not we should keep on processing more tweets or not:


~~~ocaml

    [<Fact>]
    let should_not_keep_processing_if_number_processed_is_equal_or_higher_than_number_to_search () =
        let twitterBackwardsSearch = new TwitterBackwardsSearch(startingTweetId = 0L, tweetsSoFar = 20, tweetsToTraverse = 20)
        Assert.False(twitterBackwardsSearch.ShouldKeepSearching())    
        
    [<Fact>]
    let should_keep_processing_if_number_processed_is_less_than_number_to_search () =
        let twitterBackwardsSearch = new TwitterBackwardsSearch(startingTweetId = 0L, tweetsSoFar = 20, tweetsToTraverse = 40)
        Assert.True(twitterBackwardsSearch.ShouldKeepSearching())    
~~~

I've definitely refactored the code into a more object oriented style although I don't think that what I had before was necessarily the functional style - it felt more like a mix of different concerns in the same function.

I don't think a tuple was the correct choice of data type for what I wanted to do although I could certainly see their value when doing mathematical calculations which require x and y values for example.

I'm intrigued to see what usages people will come up with for <a href="http://weblogs.asp.net/podwysocki/archive/2008/11/16/functional-net-4-0-tuples-and-zip.aspx">using tuples in C# 4.0</a> - I'm not really convinced that they are beneficial for use when describing most types although I can certainly see some value from the way we can make use of them in active patterns to do pattern matching against certain parts of an instance of a stronger type as Matt Podwysocki explains about half way down the page of <a href="http://weblogs.asp.net/podwysocki/archive/2008/11/16/functional-net-4-0-tuples-and-zip.aspx">his post</a>.
