+++
draft = false
date="2008-10-18 19:47:31"
title="Learnings from Code Kata #1"
tag=['code-kata']
category=['Code Katas']
+++

I've been reading <a href="http://www.amazon.co.uk/Job-Went-India-Pragmatic-Programmers/dp/0976694018/ref=sr_1_1?ie=UTF8&s=books&qid=1224258401&sr=8-1">My Job Went To India</a> and one of the chapters midway through the second section talks about the value of practicing coding using <a href="http://codekata.pragprog.com/2007/01/code_katahow_it.html">code katas</a>. 

I've not tried doing these before but I thought it would be an interesting activity to try out.

<h3>The Kata</h3>

<a href="http://codekata.pragprog.com/2007/01/code_kata_one_s.html">Code Kata One - Supermarket Pricing</a>


<h3>What I learnt</h3>

<ul>
<li>
As this kata is not supposed to be a coding exercise I started out just modeling ideas in my head about how I would do it before I realised that this wasn't working as an effective way for me to learn. I decided to try and <strong>test drive some of my ideas</strong> to see whether they would actually work or not.

It also gave me the chance to play around with <a href="http://git.or.cz/">git</a> - I put the code I wrote on <a href="http://github.com/mneedham/code-katas/tree/master/CodeKata1">github</a> - and re-commence my battle with <a href="http://incubator.apache.org/buildr/">buildr</a>.</li>
<li>Having decided to fire up IntelliJ and try out some of my ideas in code I realised that test driving straight away wasn't going to work well - I hadn't spent enough time designing the objects that I wanted to test. I still wanted to try out my ideas in code though so I spent about ten minutes roughly coding out how I expected it to work before using a test driven approach to drive out the (admittedly simple) algorithms.

While Test Driven Development is a very effective technique for driving out object interactions and ensuring code correctness, it was good to have a reminder that there still needs to be <strong>some up front design </strong>work before diving in.</li>
<li>
One of the mistakes I made early on was over engineering my solution - I saw an opportunity to put one of my favourite patterns, the <a href="http://en.wikipedia.org/wiki/Double_dispatch">double dispatch</a> pattern into the code. I did this straight away before stepping back and realising that it wasn't really needed in this instance. 

Speaking to a <a href="http://blog.m.artins.net/">couple</a> of my <a href="http://blog.halvard.skogsrud.com/">colleagues</a> about this the next day they reiterated the need to <strong>keep it simple</strong>. 
</li>
<li>
I consider myself to be reasonably competent when it comes to object modeling - it is certainly something I enjoy doing - so I found it a bit disheartening that I struggled quite a bit to come up with solutions to this problem. I decided to return to the book and re-read the chapter. It had this to say:

<blockquote>
Looking back on it now, I see that the awkward feeling I got from these experiences was a good sign
...
I was stretching my mental muscles and building my coding chops... if I sit down to practice coding and nothing but elegant code comes out, I’m probably sitting somewhere near the center of my current capabilities instead of the edges, where a good practice session should place me. 
</blockquote>
It reminded me about an article I read earlier this year about '<a href="http://www.sciam.com/article.cfm?id=the-expert-mind">the expert mind</a>' which talks of the value of <strong>effortful study</strong>.

<blockquote>
Ericsson argues that what matters is not experience per se but "effortful study," which entails continually tackling challenges that lie just beyond one's competence.
</blockquote>
This makes sense to me - we don't improve that much by doing activities which we already know how to but equally we don't want to be overwhelmed by the difficulty of the activity.

While this task was difficult I think that reading most of <a href="http://www.amazon.co.uk/Object-Design-Responsibilities-Collaborations-Addison-Wesley/dp/0201379430/ref=sr_1_1?ie=UTF8&s=books&qid=1224290769&sr=8-1">Object Design</a> prior to coming across this kata made it a bit easier than it would have otherwise been.</li>
<li>One unusual thing for me while I was trying out this exercise was that I wasn't pairing with someone else. I think this made it more difficult as I didn't have anyone to bounce ideas off and sub optimal solutions weren't getting rejected as quickly due to the I had a <strong>longer feedback cycle</strong>. On the other hand, it provided good practice for <strong>improving my ability to spot unworkable ideas</strong> more quickly.</li>
<li>I really wanted to write the bits of code I wrote in a completely object oriented way. This meant having no getters on any of the classes which forced me to think much more about <strong>the responsibility of each object</strong>. Although I wrote very little code in this instance, this is a practice that will be useful for me when coding in other situations. I had a bit of difficulty trying to keep the code well encapsulated while also allowing it to describe the domain concepts but hopefully this is something that will become easier the more I practice.</li>
</ul>
