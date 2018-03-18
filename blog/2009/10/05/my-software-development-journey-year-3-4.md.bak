+++
draft = false
date="2009-10-05 18:52:14"
title="My Software Development journey: Year 3-4"
tag=['software-development']
category=['Software Development']
+++

Just over a year ago I wrote a blog post about <a href="http://www.markhneedham.com/blog/2008/09/01/my-software-development-journey-so-far/">my software development journey up to that point</a> and I thought it'd be interesting to write a new version for the 13 months or so since then to see what the main things I've learned are.

<h3>Functional programming</h3>
I started playing around with F# about 11 months ago after becoming intrigued about this approach to programming following some conversations with my colleague <a href="http://fragmental.tw">Phil Calcado</a>.

I've only really scratched the surface of what there is to know about functional programming so far but some of the ideas that I've come across seem very intriguing and I think they can help us to write more expressive and easier to understand code.

One of my favourite aspects of the functional programming approach is that it heavily encourages <strong>immutability</strong>. It is still possible to mutate state in F# but the code ends up looking really ugly if you take that approach which encourages you not to!

Mutating of state is much more prevalent in C# code bases but it seems to make it much more difficult to reason about the state that the code is in and we seem to <a href="http://www.markhneedham.com/blog/2009/03/20/coding-reassessing-what-the-debugger-is-for/">turn to the debugger</a> way more frequently as a result. 

In contrast I don't think I've ever tried to debug any F# code I've written. Certainly part of the reason for that is that I haven't written any large systems using the langauge but I think part of it is because it's much easier to reason about code if a value is set once and then doesn't change.

Rich Hickey, the inventor of <a href="http://clojure.org/">Clojure</a>, has <a href="http://www.infoq.com/presentations/Value-Identity-State-Rich-Hickey">a really interesting presentation from QCon London</a> where he describes the need for values to be immutable and for state to be modeled through state transitions instead of by mutating data.

Along those lines <a href="http://www.markhneedham.com/blog/2009/08/29/book-club-unshackle-your-domain-greg-young/">Greg Young also speaks about the need for explicit state transitions</a> and Martin Fowler's <a href="http://martinfowler.com/eaaDev/EventSourcing.html">event sourcing pattern</a> describes the way we can achieve this when using an OO approach.

Learning about functional programming has also encouraged me to see reusable functions in C# code and I think the <strong>ability to use higher order functions effectively removes a lot of the typical design patterns</strong> that we might otherwise look to use.

Jeremy Miller covers these ideas and more in his recent article titled '<a href="http://msdn.microsoft.com/en-us/magazine/ee309512.aspx">Functional Programming for every day .NET development</a>'

More recently <a href="http://lizdouglass.wordpress.com/">Liz</a> and I have been <a href="http://www.markhneedham.com/blog/2009/09/30/scala-99-problems/">playing around with Scala</a> and from trying out some of these exercises I am seeing that when writing recursive functions my thought process has moved towards thinking about how to get the function to exit first and then working back from there to see how to get to that stage.

I'm not sure if that's the distinction between declarative and imperative programming but it certainly seems to be a less imperative thought process than I would typically apply.

I'm currently working my way through Amanda Laucher's '<a href="http://manning.com/laucher/">F# in Action</a>' book and watching the <a href="http://video.google.com/videoplay?docid=5546836985338782440&ei=Vcq9SvmFFZD-wQOFqJjmBg&q=sicp#docid=-1634408017041876836">videos</a> and trying out the exercises from MIT's '<a href="http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_start">Structure and Interpretation of Computer Programs</a>' course from the 1980s so there is still much to learn in this area.

<h3>Context</h3>
It's become more obvious to me over the last year that <strong>there pretty much isn't 'one true solution'</strong> to any problem and that there are different ways of doing things each of which has its own advantages and drawbacks.

I guess the trick is working out which is more suitable in a given situation which I imagine will become easier the more different situations I come across.

While I believe there are <a href="http://www.markhneedham.com/blog/2009/10/04/coding-rules-of-thumb/">rules of thumb</a> that can be useful when developing software it seems like there will always be some constraint which might guide us to a solution which isn't necessarily the perfect one. I think this is inevitable unless we have infinite time and money.

For example we were recently looking at the performance of our code and realised that there are a lot of network calls being made in one particular area. 

One solution to this would be to cache this data but the problem we have is that this data can be changed by the user and our caching mechanism at the moment has time based expiry and we don't want to deal with any other type of cache data invalidation as we are due to release quite soon.

In this case <strong>a time constraint is changing the way that we view our options</strong> so we've had to choose another solution.

I was recently watching a <a href="http://skillsmatter.com/podcast/java-jee/pairing-101">Skills Matter pair programming presentation</a> by my colleagues Christian Blunden and Sarah Taraporewalla and it became clearer to me that the approach I use when pairing now is much more dependent on the situation and doesn't directly correlate with the useful patterns which they suggested.

For example when working with someone who's new to a code base it makes sense to take a back seat role more of the time and allow them to get used to working out where things are whereas when you've both been working on the code for a while then a more even distribution of the keyboard time will probably happen more naturally.

If we can work out which context we're in and what constraints we have then I think it makes it much easier to choose an approach that will work for us.

<h3>Reason for everything</h3>
This first became more obvious to me when listening to a talk by my colleague Dan North titled '<a href="http://www.markhneedham.com/blog/2009/04/25/pimp-my-architecture-dan-north/">Pimp my architecture</a>' where he describes approaches that can be useful when confronted with an existing code that you want to make some improvements to.

Liz Keogh described this in such a way that made it really obvious to me in <a href="http://docondev.blogspot.com/2009/08/messy-code-is-not-technical-debt.html?showComment=1251883929431#c3911511509905214349">a comment on Michael Norton's post on technical debt</a>:

<blockquote>
The other reason that messy code happens is because people are learning.

Unless you start with a team of developers born to produce beautiful, clean code, the chances are that someone on that team will be learning. In that respect, messy code _is_ a normal part of the development cycle, as is having it left around.
</blockquote>

Until I read this <strong>I had pretty much decided that if someone wrote what I considered 'stupid code' then they just didn't care about what they were doing</strong>.

However, since then I've actually come across some pretty terrible code that I wrote a few months ago which I realised I'd written because I didn't know of a better way to solve the problem. 

Quite often the reason for something seems to be because the person didn't know another way to do it.

We've had a few new people join my project recently and it's always interesting to see the types of things they point out as having been done quite poorly. 

In just about every situation there's a (sometimes crazy) reason for the code being like that and I think the important thing in these conversations is to try and work out whether that reason still holds valid today and if not then perhaps we can make some changes to the code.

<h3>Mercilessly changing code</h3>
As it's pretty much impossible to come to a perfect solution the first time around I think <strong>it's quite vital that we have the confidence to make changes to the code we're working with</strong>. 

Ideally this is done by coding with a test driven approach so that we have some unit tests providing a safety net to allow us to make changes to the code but if we don't have this then we should still look to <a href="http://www.markhneedham.com/blog/2008/11/28/tdd-suffering-from-testing-last/">put some tests around the code</a> by using some of the techniques from <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1254731863&sr=8-1">Working Effectively With Legacy Code</a>.

I've been working on the same project for the majority of the last year and I think a lot of the problems we've created for ourselves have been from a fear of changing the code. I think this is the worst mindset to end up in because it means that you feel like you can't improve the situation.

In some areas of our code base we've been converting C# objects into a JSON representation which we can then parse on the client side and while this works quite nicely for allowing us to write logic for this type of code on the client side, we have pretty much stopped changing anything to do with those C# objects as even changing the names would possibly lead to the javascript code breaking.

This is where my worry of how well the <a href="http://memeagora.blogspot.com/2006/12/polyglot-programming.html">polyglot programming</a> approach originally coined by Neal Ford and <a href="http://www.infoq.com/presentations/polyglot-polyparadigm-programming">presented at QCon by Dean Wampler</a> will actually work.

I think if we don't want to sacrifice the ability to change code mercilessly then our IDE tools will need to get to the stage that if we make a change to code in one language then any references made to that code in another language should be changed too.

I'm told that this is what happens if you mix Scala and Java but I'm not sure if that's the case with other combinations just yet although I'm sure it will be.

In general though I think we need to keep a focus on putting the safety nets in place and designing our systems in such a way that we can change code mercilessly. 

If we can achieve that then it doesn't matter if we make a mistake because we can easily fix it.

<h3>In summary</h3>
These are the areas that I feel I've learnt the mos over the last year and the common threads running through seem to be that I've learnt that there's more than one approach to problems and we rarely get it right the first time.

More recently I've found myself drifting towards an interest in how things work under the hood and where some of the original ideas we use today come from.

As a result I've found myself reading '<a href="http://www.amazon.co.uk/CLR-Via-Applied-Framework-Programming/dp/0735621632/ref=sr_1_1?ie=UTF8&s=books&qid=1254732415&sr=8-1">CLR via C#</a>' and '<a href="http://www.amazon.co.uk/Fundamentals-Object-oriented-Design-Object-Technology/dp/020169946X/ref=sr_1_1?ie=UTF8&s=books&qid=1254732474&sr=1-1">Fundamentals of Object-Oriented Design in UML</a>' as well as SICP as I mentioned previously.

It will be interesting to see where that will take me to and I'd be interested to see if my experiences at this stage are in anyway similar to what others experienced.
