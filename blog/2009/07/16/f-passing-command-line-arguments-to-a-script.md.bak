+++
draft = false
date="2009-07-16 07:40:18"
title="F#: Passing command line arguments to a script"
tag=['f']
category=['F#']
+++

I've been doing a bit of refactoring of <a href="http://www.markhneedham.com/blog/2009/07/12/f-a-day-writing-a-feedburner-graph-creator/">my FeedBurner application</a> so that I can call it from the command line with the appropriate arguments and one of the problems I came across is working out how to pass arguments from the command line into an <a href="http://www.markhneedham.com/blog/2009/06/09/f-useful-for-scripting/">F# script</a>.

With a compiled application we are able to make use of the '<a href="http://www.markhneedham.com/blog/2009/05/02/f-entry-point-of-an-application/">EntryPointAttribute</a>' to get access to the arguments passed in:


~~~ocaml

[<EntryPointAttribute>]
let main args =
    ShowFeedBurnerStats args
    0
~~~

Sadly this doesn't work with a script but <a href="http://cs.hubfs.net/forums/thread/2911.aspx">it was pointed out on Hub FS</a> that we can get access to all the command line arguments by using 'Sys.argv' or 'System.Environment.GetCommandLineArgs()' which seems to be the preferred choice of the compiler.

The problem is that with that method you get every single argument passed to the command line and there are some that we don't care about given the way you would typically call an F# script:


~~~text

fsi --exec --nologo CreateFeedBurnerGraph.fsx -- "scotthanselman" "2009-03-01" "2009-07-14"
~~~

Results in the following arguments:


~~~text

fsi
--exec
--nologo
CreateFeedBurnerGraph.fsx
--
scotthanselman
2009-03-01
2009-07-14
~~~

We care about everything after the '--' so I wrote a little function to just gather those values:


~~~ocaml

    let GetArgs initialArgs  =
        let rec find args matches =
            match args with
            | hd::_ when hd = "--" -> List.to_array (matches)
            | hd::tl -> find tl (hd::matches) 
            | [] -> Array.empty
        find (List.rev (Array.to_list initialArgs) ) [] 
~~~

I'm not sure this works for every possible case (if you put '--' in as an argument it wouldn't work as expected!) but it's doing the job so far.

An even better way of doing this which I came across while writing this is to use 'fsi.CommandLineArgs' which allows you to just get the arguments passed to the script. Even with this approach though the '--' is still counted as one of the arguments so the function above still makes sense.


~~~ocaml

GetArgs [|"--"; "scotthanselman"; "2009-03-01"; "2009-07-14"|]
~~~


~~~ocaml

val it : string array = [|"scotthanselman"; "2009-03-01"; "2009-07-14"|]
~~~

And from the script I have the following:


~~~ocaml

let programArgs = fsi.CommandLineArgs |> GetArgs
ShowFeedBurnerStats programArgs
~~~

