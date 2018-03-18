+++
draft = false
date="2008-11-06 21:30:26"
title="Object Calisthenics: First thoughts"
tag=['oop', 'object-calisthenics', 'thoughtworks-anthology', 'coding-dojo']
category=['Software Development', 'Coding Dojo']
+++

We ran an Object Calisthenics variation of <a href="http://codingdojo.org/">Coding Dojo</a> on Wednesday night as part of ThoughtWorks Geek Night in Sydney.

Object Calisthenics is an idea suggest by Jeff Bay in <a href="http://www.amazon.co.uk/ThoughtWorks-Anthology-Technology-Innovation-Programmers/dp/193435614X/ref=sr_1_1?ie=UTF8&s=books&qid=1225966906&sr=8-1">The ThoughtWorks Anthology</a> , and lists 9 rules to writing better Object Oriented code. For those who haven't seen the book, the 9 rules are:

<ol>
<li>Use only one level of indentation per method
</li>
<li>Don't use the else keyword</li>
<li>Wrap all primitives and strings</li>
<li>Use only one dot per line</li>
<li>Don't abbreviate</li>
<li>Keep all entities small</li>
<li>Don't use any classes with more than two instance variables</li>
<li>Use first-class collections</li>
<li>Don't use any getters/setters/properties</li>
</ol>

We decided to try and solve the <a href="http://www.objectmentor.com/resources/articles/xpepisode.htm">Bowling Game Problem</a> while applying these rules. We coded in Java as this was a language everyone in the room was comfortable with. It would have been cool to try out Ruby or another language but I'm not sure if this type of setting is the best place to learn a new language from scratch.

I hadn't arranged a projector so we couldn't adopt the <a href="http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata">Randori</a> approach. Instead we split into three pairs rotating every half an hour, discussing how each pair was approaching the problem at each change.

<h3>Learning from the problem</h3>

I was surprised how difficult the problem was to solve using the Object Calisthenics rules. There were several occasions when it would have been really ease to expose some state by introducing a getter but we had to try another way to attack the problem.

We have been following the approach of wrapping all primitives and strings on my current project as '<strong>micro types</strong>' so this rule wasn't new to me but the general feeling early on was that it was quite annoying to have to do. From my experience on my project it does help to encourage a more object oriented approach of <a href="http://www.dcmanges.com/blog/37">keeping the data with the behaviour</a>.

This approach to object orientation is very extreme but the author suggests giving it a try on some small projects as being able to code like this will result in you seeing problems in a different way. I noticed today that I was always on the lookout for ways to ensure that we didn't expose any state so it's had a slight influence on my approach already.

We had an interesting discussion about mid way through about whether we should <strong>implement equals and hashcode methods on objects just so that we can test their equality</strong>. My general feeling is that this is fine although it has been pointed out to me that doing this is actually adding production code just for a test and should be avoided unless we need to put the object into a HashMap or HashSet when the equals/hashcode methods are actually needed. The only alternative I can think of is to not test object equality and instead only test equality where we have primitives or to test for equality by using reflection.

From seeing the approaches others had taken I realised that the approach we took on my machine was too difficult - we would have been more successful by adopting <a href="http://codingdojo.org/cgi-bin/wiki.pl?BabySteps">baby steps</a>.

<h3>Learning about the format</h3>

We initially started out trying to <strong>design a solution to the problem on a white board</strong> before getting to the coding but this didn't work particularly well so we abandoned this and went straight to the code.

Each machine had three different pairs working on the problem over the duration of the night, with one person always staying on the machine and the others rotating. While we all had slightly different approaches to the problem it would have been interesting to see if we could have progressed further using the Randori approach with everyone having input to the same code base.

None of the pairs managed to complete the problem, and there was concern that the <strong>problem was too big</strong> to fit into the 90 minutes we spent coding. After speaking with <a href="http://www.dtsato.com/blog">Danilo</a> and reading his <a href="http://www.dtsato.com/blog/wp-content/uploads/2008/06/sato-codingdojo.pdf">Coding Dojo paper</a> it seems that this is not necessarily a bad thing and the focus is supposed to be more on the learning than problem completion.

It was certainly an interesting experience and I had the opportunity to work with some people that I haven't worked with before. We are hopefully going to make these Coding Dojos a regular feature and try out some different approaches to see which works best for us.

On this occasion I selected the problem but in the future we would look to make it a group based decision depending on what people are keen to learn. 


