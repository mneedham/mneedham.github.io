+++
draft = false
date="2009-05-02 01:56:09"
title="F#: Entry point of an application"
tag=['f']
category=['F#']
+++

In an attempt to see whether or not the <a href="http://www.markhneedham.com/blog/2009/05/02/f-erlang-style-messaging-passing/">mailboxes I've been working on for my twitter application</a> were actually processing messages on different threads I ran into the problem of defining the entry point of an F# application.

I thought it would be as simple as defining a function called 'main' but I put this function into my code ran the executable and nothing happened!

Googling the problem a bit led me to believe that it is possible to do but that the function needs to be the last thing that happens in the compilation sequence of the project. i.e.  it needs to be on the last line of the last file that gets compiled.

That just seemed wrong to me and a <a href="http://stackoverflow.com/questions/663894?sort=newest">Stack Overflow thread</a> suggested that it should be possible to get around this problem <a href="http://lorgonblog.spaces.live.com/blog/cns!701679AD17B6D310!412.entry">by using the EntryPointAttribute on the main function</a>.

I tried this leading to the following code:


~~~ocaml

[<EntryPoint>]    
let main args = 
    printfn "in main function"
    0
~~~

It seems like if you have the EntryPointAttribute on a function that function needs to be of type 'string array -> int' hence the returning of 0 by this function.

This still didn't solve my problem though and when I tried to build the project it was now failing to compile but no errors were showing up on the Visual Studio error list.

This gave me the chance to try out an F# build tool I came across a couple of weeks ago called <a href="http://code.google.com/p/fake/">Fake</a>.

I setup a build file just to compile the code based on <a href="http://www.navision-blog.de/2009/04/01/getting-started-with-fake-a-f-sharp-make-tool/">Steffen Forkman's blog post</a> and then tried to compile the project, leading to the following error:


~~~text

error FS0191: A function labelled with the 'EntryPointAttribute' atribute must be the last declaration in the last file in the compilation sequence.
~~~

Which suggests that it doesn't actually matter whether or not you have the attribute or not, the main method still needs to be the last step of compilation.

I wanted to get something working so I've just rearranged my fsproj file so that the file with the main function in is the last one listed but it seems a ridiculous fix and I'm sure there must be a better way to do this.

Any ideas?
