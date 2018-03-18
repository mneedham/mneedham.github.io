+++
draft = false
date="2009-05-24 19:25:07"
title="Real World Functional Programming: Book Review"
tag=['c', 'net', 'books', 'f']
category=['Books']
+++

<h3>The Book</h3>

<a href="http://manning.com/petricek/">Real World Functional Programming</a> by Tomas Petricek with Jon Skeet (<a href="http://www.functional-programming.net/">corresponding website</a>)



<h3>The Review</h3>

I decided to read this book after being somewhat inspired to learn more about functional programming after talking with <a href="http://fragmental.tw/">Phil</a> about his experiences learning <a href="http://clojure.org/">Clojure</a>. I'm currently working on a .NET project so it seemed to make sense that F# was the language I picked to learn.

<h4>What did I learn?</h4>

<ul>
<li>I've worked with C# 3.0 since around July 2008 so I had a bit of experience using some of the functional features in C# before picking up this book. I therefore found it very interesting to read about the history of lambda and the different functional languages and how they came into being. Having this as an opening chapter was a nice way to introduce the functional approach to programming.</li>
<li><strong>Immutable state</strong> is one of the key ideas in functional programming - this reminded me of a <a href="http://channel9.msdn.com/posts/Charles/JAOO-2007-Joe-Armstrong-On-Erlang-OO-Concurrency-Shared-State-and-the-Future-Part-2/">Joe Armstrong video</a> I watched last year where he spoke of his <a href="http://www.markhneedham.com/blog/2009/03/22/coding-making-the-debugger-redundant/">reduced need to use a debugger</a> when coding Erlang due to the fact that there was only one place where state could have been set rather than several as is the case with a more imperative approach. We have been trying to code with immutable state in mind in our <a href="http://www.markhneedham.com/blog/category/coding-dojo/">coding dojos</a> and while it takes a bit more thinking up front, the code is much easier to read when written that way.</li>
<li><strong>Separating the operations from the data</strong> is important for allowing us to write code that can be parallelised, focusing on <strong>what to do to the data rather than how to do it</strong>. <a href="http://sadekdrobi.com/">Sadek Drobi</a> has a nice illustration of what he calls mosquito programming vs functional programming on page 14 of the <a href="http://qconlondon.com/london-2009/file?path=/qcon-london-2009/slides/SadekDrobi_FunctionalProgrammingWithAMainstreamLanguage.pdf">slides of his QCon presentation</a>. It describes this idea quite nicely.</li>
<li>A cool technique that Phil taught me when reading language related books is to have the PDF of the book on one side of the screen and the <a href="http://en.wikipedia.org/wiki/REPL">REPL</a> (in this case F# interactive) on the other side so that you can try out the examples in real time. The book encourages this approach and all the examples follow on from previous ones which I think works quite well for gradually introducing concepts. </li>
<li><strong>Functions are types</strong> in functional programming - I have had a bit of exposure to this idea with Funcs in C# but partial function application is certainly a new concept to me. I can certainly see the value in this although it took me a while to get used to the idea. I am intrigued as to where we should use a functional approach and where an OO approach when working in C#. I think both have a place in well written code. </li>
<li>F#'s <strong>implicit static typing</strong> is one of my favourite things about the language - you get safety at compile time but you don't waste a lot of code writing in type information that the compiler should be able to work out for you. It has the strongest type inference of any language that I've worked with and I thought it was quite nice that it was able to work stuff out for me instead of me having to type it all out.</li>
<li>I really like the idea of <a href="http://www.markhneedham.com/blog/2009/01/02/f-option-types/">option types</a> which I first learnt about from the book. Having the ability to explicitly define when a query hasn't worked is far superior to having to do null checks in our code or the <a href="http://www.markhneedham.com/blog/2008/08/16/null-handling-strategies/">various strategies we use to get around this</a>.</li>
<li>I thought it was cool that in the early chapters the focus with the F# code is to provide <strong>examples that you can just get running straight away</strong> instead of having to worry about the need to structure your code in a maintainable way. After I had a reasonable grasp of this then the chapter about using record types to structure code in an OO way come up. I still prefer the C# style of structuring code in objects - it just feels more natural to me at the moment and manages the complexity more easily. It is quite easy to switch between the two styles <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">using features like member augmentation</a> so I think it's probably possible to mix the two styles quite easily.</li>
<li>We can <strong>use modules to make F# functions which don't fit onto any class available from C# code</strong>. The code is not as clean as if we were writing just for it to be used by other F# code but it's not too bad:


~~~ocaml

module Tests =                                               
    let WithIncome (f:Func<_, _>) client =                  
        { client with Income = f.Invoke(client.Income) }
~~~

We can then call this in our C# code like so:


~~~csharp

Tests.WithIncome(income => income + 5000, client);
~~~
Dave Cameron has <a href="http://intwoplacesatonce.com/?p=9">written more about this</a>.
 </li>
<li>Although I studied <strong>data structures</strong> at university I don't really pay a great deal of attention to them in terms of performance normally so it was interesting to see the massive performance hit that you take when appending a value to the end of an F# list compared to adding it to the beginning. F# uses linked lists so if we want to add something to the end then there is a lot of recursion involved to do that which is quite costly. In terms of <a href="http://en.wikipedia.org/wiki/Big_O_notation">big O notation</a> we go from O(N) where N is the number of elements to append to O(N*M) in terms of performance.</li>
<li>Chapter 13 is about parallel processing of data for which I found I needed to download the <a href="http://www.microsoft.com/downloads/details.aspx?FamilyId=348F73FD-593D-4B3C-B055-694C50D2B0F3&displaylang=en">Microsoft Parallel Extensions to .NET Framework 3.5, June 2008 Community Technology Preview</a> and then add a reference to 'C:\Program Files\Microsoft Parallel Extensions Jun08 CTP\System.Threading.dll' in order to make use of those features. </li>
<li>The author provides a nice introduction to <a href="http://en.wikipedia.org/wiki/Continuation">continuations</a> and how you can make use of them in F# by using <a href="http://blogs.msdn.com/wesdyer/archive/2007/12/22/continuation-passing-style.aspx">continuation passing style</a>. I'm intrigued as to how we can make use of these in our code - we do a bit already by making use of callbacks which get fired at a later point in our code - but <a href="http://www.double.co.nz/pdf/inverting-back-the-inversion.pdf">from what I've read</a> it sounds like we should be able to do even more especially when writing web applications. </li>
<li><a href="http://www.infoq.com/articles/pickering-fsharp-async">Asynchronous workflows</a> are also made very accessible in this book - I had previously struggled a bit with them but the author covers the various API methods available to you and then explains what is going on behind the syntactic sugar that F# provides. I have made some use of these in the <a href="http://www.markhneedham.com/blog/2009/04/13/f-a-day-of-writing-a-little-twitter-application/">little</a> <a href="http://www.markhneedham.com/blog/2009/04/18/f-refactoring-that-little-twitter-application-into-objects/">twitter appication</a> that I've been working on now and again.</li>
</ul>

<h3>In Summary</h3>

I really enjoyed reading this book - it's my first real foray into the world of functional programming since university and I think I understand the functional approach to programming much better than I did back then from reading this book.

It takes an approach of introducing various functional programming concepts before showing examples of where that concept might come in useful when coding. It's also particularly useful that examples are shown in C# and F# as this made it much easier for me to understand what the F# code was doing by comparing it with the code in a more familiar language.

I'd certainly recommend this to any .NET developers curious about learning how to apply ideas derived from functional programming to their C# code and indeed to any developers looking to start out learning about functional programming.
