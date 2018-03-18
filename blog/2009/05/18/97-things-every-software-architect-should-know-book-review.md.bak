+++
draft = false
date="2009-05-18 01:03:25"
title="97 Things Every Software Architect Should Know: Book Review"
tag=['software-development']
category=['Books']
+++

<h3>The Book</h3>

<a href="http://www.amazon.co.uk/Things-Every-Software-Architect-Should/dp/059652269X/ref=sr_1_1?ie=UTF8&s=books&qid=1242525416&sr=8-1">97 Things Every Software Architect Should Know</a> by Richard Monson-Haefel

<h3>The Review</h3>

My colleague <a href="http://erik.doernenburg.com/">Erik Doernenburg</a> mentioned that he had written a couple of chapters in this book a while ago and there was a copy of the book in the ThoughtWorks office so I thought I'd take a look.

I'm far from being an architect but since their decisions affect what I do I was intrigued to see what they should be doing.

The contributions in the book are <a href="http://97-things.near-time.net/wiki/97-things-every-software-architect-should-know-the-book">also available on the 97 things wiki</a>.

<h4>What did I learn?</h4>

This book contains a series of short essays by software architects, 97 in total, so clearly there is a lot to be learnt from this book. I'll just cover some of the ones I found most interesting.

<ul>
<li>The first chapter in the book talks of the need to not put your resume ahead of the requirements and instead <strong>choose the right technology for the customer</strong> rather than the one that you want to use. Later on Greg Nyberg talks about how <a href="http://97-things.near-time.net/wiki/avoid-good-ideas">good ideas kill projects</a> due to them getting out of hand and taking up much more time than expected to implement and affecting far more of the code than you would think. The suggestion therefore seems to be that we shouldn't upgrade frameworks and should be cautious about introducing technologies into our project. 

At face value this seems to make sense but it somewhat limits our ability to improve in my opinion. If we always choose the technology based on what we currently know then how will we know when something better comes along.

I much prefer the idea of trying out several solution early on (an idea that Erik Doernenburg mentions in '<a href="http://97-things.near-time.net/wiki/Try%20before%20choosing">Try before choosing</a>' using lean's idea of <a href="http://xp123.com/xplor/xp0611/index.shtml">concurrent set based engineering</a>. Experimentation is very important early on in a project although of course we must eventually be looking to choose the best solution and go with that at the <a href="http://www.codinghorror.com/blog/archives/000705.html">last responsible moment</a>.</li>
<li>Another one that really stood out for me is '<a href="http://97-things.near-time.net/wiki/Simplicity%20before%20generality,%20use%20before%20reuse">Simplicity Before Generality, Use Before Reuse</a>' written by Kevin Hennery. He speaks of how we <strong>often use general purpose infrastructure code/class libraries which don't actually help us solve our specific problem</strong>.

It's better to derive the generality of a solution later on having originally designed for what we need them for in the first place. Joe Walnes' <a href="http://xstream.codehaus.org/">XStream</a> framework is often pointed out as being a library which was developed in this way - he only put in the features that he needed rather than trying to think how people might want to use it and by doing so actually did cover the way that most people would use it.</li>
<li>I think my favourite essay in the book is '<a href="http://97-things.near-time.net/wiki/dont-be-clever">Don't Be Clever</a>' by Eben Hewitt where he talks of the importance of being '<strong>as dumb as you possibly can and still create the appropriate design</strong>'. He goes on to add:

<blockquote>
More developers can implement and maintain dumb solutions. In dumb solutions, each component can only do one thing. They will take less time to create, and less time to change later.
</blockquote>
It's so easy to make clever design decisions but when there are other people on a team that need to work with these designs it is in fact pointless to be clever and creating something simple that everyone will be able to work with is a much better approach.

<a href="http://97-things.near-time.net/wiki/your-system-is-legacy-design-for-it">Dave Anderson also talks about the importance of designing our code so that it's easy for someone from a different team to work</a> with especially if they have to make production fixes. The need for the code to be <a href="http://www.markhneedham.com/blog/2009/03/18/coding-make-it-obvious/">obvious</a>, testable, correct and traceable are pointed out as being key.	
</li>
<li>Another one which I really liked is '<a href="http://97-things.near-time.net/wiki/the-business-vs-the-angry-architect">The Business vs The Angry Architect</a>' which talks about <strong>the need to listen to what the business are saying instead of always waiting to have our say and display our superior knowledge</strong>. My favourite quote from this chapter is:

<blockquote>
Remember; when you’re talking you can only hear something you already know. Don’t ever start thinking you’re so smart that no one else has something valuable to say.
...
Don’t allow yourself to become a disgruntled genius that spends all of your time trying to impress others by making witty, condescending statements about how poorly the company is run. They won’t be impressed.
</blockquote>

This is certainly something that anyone in a software team can apply not only architects. Certainly I have learnt that it's important to accept some decisions instead of constantly pointing out how wrong they are, something which Dan North also points out in his '<a href="http://www.markhneedham.com/blog/2009/04/25/pimp-my-architecture-dan-north/">Pimp My Architecture</a>' talk.</li>
<li>I really like Timothy High's idea of '<a href="http://97-things.near-time.net/wiki/record-your-rationale">Recording Your Rationale</a>' where he suggests keeping track of all the <a href="http://www.markhneedham.com/blog/2009/03/02/trade-offs-some-thoughts/">trade offs</a> being made so that we know in the future why certain decisions were made. This ties in quite nicely with Dan North's idea of the project shaman who tells the stories of the project and why different decisions were made. <a href="http://97-things.near-time.net/wiki/communication-is-king">Mark Richards also talks about the need to communicate clearly</a> with the developers on the team and keep them informed about the big picture and the like and Timothy High goes on to talk about the importance of recording any assumptions that we make.

On every project I've worked on we have recorded assumptions related to the order of stories and the approach we are likely to take during estimation sessions and it certainly makes it easier to explain decisions in the future.

Dave Quick suggests that we could also <a href="http://97-things.near-time.net/wiki/warning-problems-in-mirror-may-be-larger-than-they-appear">record potential risks</a> on projects until they are no longer a risk. They can be prioritised and reviewed when there is new information. I quite like this idea as it puts the information out in the open rather than sweeping it under the carpet. 
</li>
<li>Paul W. Homer talks of the benefit of <a href="http://97-things.near-time.net/wiki/share-your-knowledge-and-experiences">sharing our knowledge and experiences</a>, an idea that I absolutely agree with and I think can be valuable within teams as well as within the industry. He points out that <strong>explaining our ideas to others helps us find the weaknesses in what we are saying</strong> - I agree, I find I learn most when <a href="http://www.markhneedham.com/blog/2009/04/21/learning-through-teaching/">trying to teach things to other people</a>.</li>
<li>Einar Landre's essay about how the <a href="http://www.markhneedham.com/blog/2009/04/21/learning-through-teaching/">architect's focus is around the boundaries and interfaces</a> is another interesting one - I think this is the place where the messiest code ends up being so it makes sense that you would have the strongest person technically in the team involved. Creating these boundaries is certainly essential from my experience.

The author talks about making use of <a href="http://domaindrivendesign.org">Domain Driven Design</a> concepts such as <a href="http://www.markhneedham.com/blog/2009/03/07/ddd-bounded-contexts/">bounded contexts</a> and <a href="http://dddstepbystep.com/wikis/ddd/context-map.aspx">context mapping</a> to handle the complexity around these areas.

Keith Braithwaite also talks about the value of <a href="http://97-things.near-time.net/wiki/There%20Can%20be%20More%20than%20One">having multiple overlapping representations instead of trying to have one representation for the whole system</a> which seems along the same lines as the DDD approach.</li>
<li><a href="http://97-things.near-time.net/wiki/shortcuts-now-are-paid-back-with-interest-later">Scott Mcphee</a> and <a href="http://97-things.near-time.net/wiki/pay-down-your-technical-debt">Burkhardt Hufnagel</a> both talk about the importance of <strong>paying back technical debt before it causes us problems</strong>. Scott covers it more from the angle of correcting incorrect decisions as soon as we can while Burk comes at this more from the angle of making changes the correct way later on if we can't do the first time we make them. I think this is something that we often forget to do and it's not immediately painful so we think we've got away with it until a few months later we notice how truly difficult it is to make any changes at all and then it's really hard to recover the code to a good state. </li>
<li><a href="http://97-things.near-time.net/wiki/Reuse%20is%20about%20people%20and%20education,%20not%20just%20architecture">Jeremey Mayer</a> makes a very astute observation about reuse of code - <strong>developers need to know that code is there to reuse</strong> otherwise they will just write the functionality that they need themselves. He also notes that developers tend to prefer to solve problems themselves rather than ask for help.

<a href="http://www.markhneedham.com/blog/2009/03/15/qcon-london-2009-the-power-of-value-power-use-of-value-objects-in-domain-driven-design-dan-bergh-johnsson/">Dan Bergh Johnsson also noted at QCon</a> that developers will only wait 30 seconds to try and find a piece of code that they need before writing it themselves.</li>
</ul>

<h3>In Summary</h3>
I enjoyed reading this book and there is plenty more in this book than just what I've mentioned - I was mainly interested in the architecture advice which affects me as a developer but there's also advice which doesn't apply so much to me at the moment which is probably more interesting to architects.
