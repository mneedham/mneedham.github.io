+++
draft = false
date="2009-07-06 00:43:40"
title="Brownfield Application Development in .NET: Book Review"
tag=['net', 'books', 'manning']
category=['Books']
+++

<h3>The Book</h3>

<a href="http://manning.com/baley/">Brownfield Application Development in .NET</a> by Kyle Baley and Donald Belcham



<h3>The Review</h3>

I asked to be sent this book to review by Manning as I was quite intrigued to see how well it would complement Michael Feather's <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1246755805&sr=8-1">Working Effectively with Legacy Code</a>, the other book I'm aware of which covers approaches to dealing with non green field applications.

<h4>What did I learn?</h4>

<ul>
<li>The authors provide a brief description of the two different approaches to unit testing - state based and behaviour based - I'm currently in favour of the latter approach and <a href="http://martinfowler.com/articles/mocksArentStubs.html">Martin Fowler has a well known article</a> which covers pretty much anything you'd want to know about this topic area. </li>
<li>I really like the section of the book which talks about 'Zero Defect Count', whereby the <strong>highest priority should be to fix any defects</strong> that are found in work done previously rather than racing ahead onto the next new piece of functionality:
<blockquote>
Developers are geared towards driving to work on, and complete, new features and tasks. The result is that defect resolution subconsciously takes a back seat in a developer’s mind. </blockquote>
I think this is quite difficult to achieve when the team is getting pressure to complete new features but then again it will take longer to fix defects if we leave them until later since we need to regain the context around them which is more fresh in our mind the earlier we fix them.
</li>
<li>Another cool idea is that of <strong>time boxing efforts at fixing technical debt</strong> in the code base - that way we spend a certain amount of time fixing one area and when the time's up we stop. I think this will work well as an approach as often when trying to fix code we can either get into the mindset of not fixing anything at all because it will take too long to do so or ending up <a href="http://sethgodin.typepad.com/seths_blog/2005/03/dont_shave_that.html">shaving the yak</a> in an attempt to fix a particularly problematic area of code.</li>
<li>I like the definition of abstraction that the authors give:

<blockquote>
From the perspective of object- oriented programming, it is the method in which we simplify a complex “thing”, like an object, a set of objects, or a set of services.</blockquote>

I often end up over complicating code in an attempt to create 'abstractions' but by this definition I'm not really abstracting since I'm not simplifying but complicating! This seems like a useful definition to keep in mind when looking to make changes to code.
</li>
<li>Maintainability of code is something which is seriously undervalued - I think it's very important to write your code in <a href="http://www.markhneedham.com/blog/2009/03/18/coding-make-it-obvious/">such a way that the next person who works with it can actually understand what's going on</a>. The authors have a fantastic quote from Perl Best Practices:

<blockquote>
Always code as if the guy who ends up maintaining your code is a violent psychopath who knows where you live.</blockquote>

Writing code that is easy for the next person to understand is much harder than I would expect it to be although on teams which pair programmed frequently I've found the code easier to understand. I recently read a blog post by Jaibeer Malik where he claims that it is <a href="http://jaibeermalik.wordpress.com/2009/04/12/code-quality-learn-measure-and-organize-awareness/">harder to read code than to write code</a> which I think is certainly true in some cases.
</li>
<li>There is a discussion of some of the design patterns and <a href="http://www.markhneedham.com/blog/2008/08/16/naming-the-patterns-we-use-in-code/">whether or not we should explicitly call out their use in our code</a>, the suggestion being that we should only do so if it makes our intent clearer. </li>
<li>While describing out how to refactor some code to loosen its dependencies it's pointed out that <strong>when the responsibilities of a class are a bit fuzzy the name of the class will probably be quite fuzzy too</strong> - it seems like this would server as quite a useful indicator for refactoring code to the <a href="http://www.objectmentor.com/resources/articles/srp.pdf">single responsibility principle</a>. The authors also suggest trying not to append the suffix 'Service' to classes since it tends to be a very overloaded term and a lot of the time doesn't add much value to our code.</li> 
<li>It is constantly pointed out how important it is to do refactoring in small steps so that we don't break the rest of our code and to allow us to get rapid feedback on whether the refactoring is actually working or not. This is something that we've <a href="http://www.markhneedham.com/blog/2009/05/15/coding-dojo-14-rock-scissors-paper-tdd-as-if-you-meant-it/">practiced in coding dojos</a> and Kent mentions it as being <a href="http://www.infoq.com/presentations/responsive-design">one of his tools when dealing with code</a> - I've certainly found that the overall time is much less when doing small step refactorings than trying to do everything in one go.

I'm quite interested in trying out an idea called '<a href="http://manicprogrammer.com/cs/blogs/heynemann/archive/2008/11/13/bowling-scorecards-great-agile-practice.aspx">Bowling Scorecards</a>' which my former colleague Bernardo Heynemann wrote about - the idea to have a card which has a certain number of squares, each square reprsenting a task that needs to be done. These are then crossed off as members of the team do them.</li>
<li>An interesting point which is made when talking about how to refactor data access code is to try and make sure that we are <strong>getting all the data from a single entry point</strong> - this is something which I noticed on a recent project where we were cluttering the controller with two calls to different repositories to retrieve some data when it probably could have been encapsulated into a single call.</li>
<li>Although they are talking specifically about <strong>poor encapsulation</strong> in data access layers, I think the following section about this applies to anywhere in our code base where we expose the inner workings of classes by failing to encapsulate properly:

<blockquote>
Poor encapsulation will lead to the code changes requiring what is known as the Shotgun Effect. Instead of being able to make one change, the code will require you to make changes in a number of scattered places, similar to how the pellets of a shotgun hit a target. The cost of performing this type of change quickly becomes prohibitive and you will see developers pushing to not have to make changes where this will occur. 
</blockquote>
</li>
<li>The creation of an <a href="http://ibuilthiscage.com/2008/09/21/anatomy-of-an-anti-corruption-layer-part-1/">anti corruption layer</a> to shield us from 3rd party dependency changes is suggested and I think this is absolutely vital otherwise whenever there is a change in the 3rd party code our code breaks all over the place. The authors also adeptly point out:

<blockquote>
The reality is that when you rely on another company's web service, you are ultimately at their mercy. It's the nature of third-party dependencies. You don't have control over them. 
</blockquote>

Even if we do recognise that we are <a href="http://www.markhneedham.com/blog/2009/07/04/domain-driven-design-conformist/">completely reliant on a 3rd party service for our model</a> I think there is still a need for an anti corruption layer even if it is very thin to protect us from changes.

The authors also describe run time and compile time 3rd party dependencies - I think it's <strong>preferable if we can have compile time dependencies since this gives us much quicker feedback</strong> and this is an approach we used on a recent project I worked on by making use of generated classes to interact with a SOAP service rather than using WCF message attributes which only provided us feedback at runtime.
</ul>

<h3>In Summary</h3>

This book starts off with the very basics of any software development project covering things such as version control, continuous integration servers, automated testing and so on but it gets into some quite interesting areas later on which I think are applicable to any project and not necessarily just 'brownfield' ones.

There is a lot of useful advice about making use of abstractions to protect the code against change both from internal and external dependencies and I particularly like the fact that the are code examples showing the progression of the code through each of the refactoring ideas suggested by the authors.

Definitely worth reading although if you've been working on any type of agile projects then you're probably better off skim reading the first half of the book but paying more attention to the second half.
