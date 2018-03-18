+++
draft = false
date="2009-04-30 06:12:41"
title="Coding Dojo #13: TDD as if you meant it"
tag=['coding-dojo']
category=['Coding Dojo']
+++

We decided to follow Keith Braithwaite's '<a href="http://www.parlezuml.com/softwarecraftsmanship/sessions/tdd_as_if_you_meant_it.htm">TDD as if you meant it</a>' exercise which he led at the <a href="http://www.parlezuml.com/softwarecraftsmanship/index.htm">Software Craftsmanship Conference</a> and which I originally read about on <a href="http://gojko.net/2009/02/27/thought-provoking-tdd-exercise-at-the-software-craftsmanship-conference/">Gojko Adzic's blog</a>.

We worked on implementing a Flash Message interceptor, to hook into the Spring framework, that one of my colleague's has been working on - the idea is to show a flash method to the user, that message being stored in the session on a Post and then removed on a Get in the '<a href="http://en.wikipedia.org/wiki/Post/Redirect/Get">Post-Redirect-Get</a>' cycle. It's similar to the <a href="http://ianpurton.com/helper-to-display-rails-flash-messages/">':flash' messages that get passed around in Rails</a>.

<h3>The Format</h3>

We used the <a href="http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata">Randori</a> approach with five people participating for the whole session.

<h3>What We Learnt</h3>

<ul>
<li>We were following these rules for coding :

<ol>
<li>write exactly ONE failing test</li>
<li>make the test from (1) pass by first writing implementation code IN THE TEST</li>
<li>create a new implementation method/function by:
<ol><li>doing extract method on implementation code created as per (2), or</li>
<li> moving implementation code as per (2) into an existing implementation method</li>
</li>
</ol>
<li>only ever create new methods IN THE TEST CLASS</li>
<li>only ever create implementation classes to provide a destination for extracting a method created as per (4).</li>
<li> populate implementation classes by doing move method from a test class into them</li>
<li>refactor as required</li>
<li>go to (1)</li>
</ol>


Despite having read about Gojko's experiences of this exercise I still found it amazingly frustrating early on taking such small steps and the others pointed out a couple of times that the steps we were taking were too big. The <strong>most difficult thing for me was the idea of writing the implementation in the test</strong> and working out what counts as implementation code and what counts as test setup. The line seemed to be a little bit blurred at times.</li>
<li>We worked out after writing 5 or 6 tests that <strong>we had overcomplicated things</strong> - we originally started out using a map to represent the session and then called the get and put methods on that to represent putting the flash message into and taking it out from the session. We decided to redo these tests so that the flash message was just represented as a string which we manipulated. This second approach guided us towards the idea of having a FlashMessageStore object with a much simpler API than a Map.</li>
<li>We started off <strong>only extracting methods when there was duplication in our tests which forced us to do so</strong>. As a result of doing this I think we ended up having the implementation details in the test for longer than the exercise intended. We didn't introduce a class to hold our methods for quite a while either - the idea we were following was that we wouldn't create a class unless we had three methods to put on it. Once we got the hang of the exercise we started creating those methods and classes much earlier.</li>
<li><a href="http://twitter.com/davcamer/">Dave</a> pointed out an interesting way of writing guard blocks which I hadn't seen before - the idea is that if you want to exit from a method it's fine not to have the {} on the if statement as long as you keep the whole statement on one line. Roughly something like this:


~~~java

public void clearFlashMessageIfRequestTypeIsGet(Request request) {
	if(!"get".equalsIgnoreCase(request.GetType()) return;
	// do other stuff
}
~~~
</li>
<li>It seemed like following these rules guided us towards <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">tiny/micro types</a> in our code and <strong>the methods we extracted were really small</strong> compared to the ones we would have written if we'd started off writing the test and implementation separately.</li>
<li>We had an interesting discussion towards the end of the dojo about the merits of <strong>wrapping framework libraries with our own types</strong>. For example we might choose to wrap the HttpServletRequest in our own Request object so that we can control the API in our code. Although I think this might initially be a bit confusing to people who expect to see a certain set of methods available when they see they are using a Request object, this approach seems to be following Steve McConnell's advice in <a href="http://www.amazon.co.uk/Code-Complete-Practical-Handbook-Construction/dp/0735619670/ref=sr_1_1?ie=UTF8&s=books&qid=1241035816&sr=8-1">Code Complete</a> of 'coding into a language' rather than in a language - we are moulding the framework to our system's needs.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>I really enjoy the dojos where we experiment with an approach which is slightly different than what you do on projects. Although the language (Java) was familiar to everyone it was still challenging to code a very different way than what we're used to. We'll probably try this exercise again the next time with another problem.</li>
</ul>
