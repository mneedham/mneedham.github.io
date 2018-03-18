+++
draft = false
date="2009-05-10 08:58:48"
title="F#: Regular expressions/active patterns"
tag=['f']
category=['F#']
+++

<a href="http://robotoverlords.blogspot.com/">Josh</a> has been <a href="http://twitter.com/markhneedham/status/1723697152">teaching me how to do regular expressions in Javascript this week</a> and intrigued as to how you would do this in F# I came across a couple of blog posts by Chris Smith talking about <a href="http://blogs.msdn.com/chrsmith/archive/2008/02/21/Introduction-to-F_2300_-Active-Patterns.aspx">active patterns</a> and <a href="http://blogs.msdn.com/chrsmith/archive/2008/02/22/regular-expressions-via-active-patterns.aspx">regular expressions via active patterns</a>.

As I understand them active patterns are not that much different to normal functions but we can make use of them as part of a let or match statement which we can't do with a normal function.

I wanted to create an active pattern that would be able to tell me if a <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">Twitter</a> <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">status</a> has a url in it and to return me that url. If there are no urls then it should tell me that as well.

This is therefore a partial active pattern as it does not necessarily describe something. Adapted from Chris Smith's blog I therefore ended up with the following active pattern:


~~~ocaml

open System.Text.RegularExpressions

let (|Match|_|) pattern input =
    let m = Regex.Match(input, pattern) in
    if m.Success then Some (List.tl [ for g in m.Groups -> g.Value ]) else None
~~~

This is a generic active pattern which will take in a string and a regular expression and return an Option containing the matches if there are some and none if there aren't any.

The '_' in the active pattern definition is the partial bit - we don't necessarily have a match.

I quite liked what Chris did on line 4 of this statement whereby the results returned exclude the first item in the group of matches since this contains the entirety of the matched string rather than the individual matches.

I was then able to make use of the active pattern to check whether or not a Tweet contains a url:


~~~ocaml

let ContainsUrl value = 
    match value with
        | Match "(http:\/\/\S+)" result -> Some(result.Head)
        | _ -> None     
~~~

Active patterns seem pretty cool from my limited playing around with them and are something that I came across by chance when looking around for ways to use regular expressions in F#.

