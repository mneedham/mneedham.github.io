+++
draft = false
date="2009-06-12 17:07:30"
title="Coding Dojo #17: Refactoring Cruise Control .NET"
tag=['coding-dojo']
category=['Coding Dojo']
+++

After a couple of weeks of <a href="http://www.markhneedham.com/blog/2009/05/21/coding-dojo-15-smalltalk/">more experimental</a> <a href="http://www.markhneedham.com/blog/2009/05/29/coding-dojo-16-reading-sunit-code/">coding dojos</a> this week we decided to get back to some pure coding with the session being focused around doing some refactoring of the continuous integration server <a href="http://confluence.public.thoughtworks.org/display/CCNET/Welcome+to+CruiseControl.NET">Cruise Control .NET</a>.

The overall intention of the refactoring we worked on is to try and introduce the concept of a 'ChangeSet' into the code base to represent the revisions that come in from source control systems that CC.NET integrates with. 

<h3>The Format</h3>

We had 6 people for the majority of the dojo so we resorted to the Randori style with each pair at the keyboard for 10 minutes before rotating. 

<a href="http://twitter.com/davcamer">Dave</a> and I have been reading/trying out the <a href="http://blog.staffannoteberg.com/2008/02/22/pomodoro-technique-in-5-minutes/">Pomodoro technique</a> in our spare time recently so we decided to use Pomodoro's idea of reflecting on our work by stopping every 3 pairing sessions and discussing what we'd done and whether we wanted to vary the approach or keep going the same way.

<h3>What We Learnt</h3>

<ul>
<li>The most obvious place in the code where the 'ChangeSet' concept made sense was in the RssFeedPublisher which was taking a collection of modifications and then converting them back into the same revision format that the data was in when it came from the source control system. 

The <a href="https://bitbucket.org/davcamer/ccnet/src/tip/project/core/sourcecontrol/ISourceControl.cs">ISourceControl</a>.GetModifications() method was the one that we needed to change if we wanted to introduce the changes which we started doing by changing the return type from being a modification array to an IEnumerable&#60;Modificatiion&#62;.

The goal was to <strong>drive towards a place where we could create a ChangeSet</strong> and have that extend an IEnumerable&#60;Modificatiion&#62;  so that we could easily get that into the code before working out how to remove the concept of a Modification. 

We wanted it to extend a more generic type than array since we didn't want to tie the ChangeSet class to something as concrete as an array.

Even with seemingly minor change we still ended up taking around 40 minutes to get the code compiling again - we were very much leaning on the compiler to guide us on what to fix, a technique <a href="http://twitter.com/mfeathers">Michael Feathers</a> talks about in <a href="http://www.amazon.com/Working-Effectively-Legacy-Robert-Martin/dp/0131177052">Working Effectively with Legacy Code</a>. 

It would be interesting to see how a refactoring like this would work in a dynamic language like Ruby where you would lose the compiler support but still have the ability to run your tests to help guide you to the places that need fixing.
</li>

<li>
There were 963 usages of Modification in the code so we didn't have the option of just deleting it straight away! I've not yet worked on a code base this size so it was interesting for me to see how we were forced into a <strong>smaller steps approach</strong> by the code.</li>
<li>After 3 pairing sessions we discussed the approach that we were taking which had led us to a situation where the code still wasn't compiling.

The alternative approach was to <strong>go in even smaller steps and make another method on ISourceControl for 'GetModfications' with a different signature</strong> and then delegate from the new method to the existing one. 

The problem with this was that there were 20 classes which implemented ISourceControl so we would have had to implement the delegation in all of these or create an abstract base class which did the delegation and then get all the existing implementors to extend the case class instead.

We decided to keep going with our original approach for 3 more pairs as it seems like we were quite close and it wasn't clear whether changing the approach would give us significant benefits.</li>
<li>The main compilation errors in the code were actually tests which no longer compiled due to the fact that IEnumerable doesn't have a 'Length' property on it whereas array does. 

CC.NET is a .NET 2.0 code base so we weren't able to introduce <a href="http://msdn.microsoft.com/en-us/library/system.linq.enumerable_members.aspx">LINQ</a> into the code which would have made it really easy to just make use of the 'Count' extension method instead of casting the results from 'GetModification' back to an array in the tests for the time being.

We accidentally came across the <strong>ICollection interface towards the end which perhaps would have been a better choice than IEnumerable</strong> as it would have allowed us to avoid the nasty casting and just make use of the Count property on ICollection instead. </li>
</ul>

<h3>For next time</h3>

<ul>
<li>The pace this week was a bit slower but it definitely seemed to keep people more involved so we're going to try and keep it more focused on the coding rather than experimentation. Possibly a refactoring exercise on some Java code as we have more people using that on their projects.</li>
</ul>
