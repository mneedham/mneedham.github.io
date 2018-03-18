+++
draft = false
date="2008-08-17 23:05:33"
title="Returning from methods"
tag=['software-development', 'c']
category=['Coding']
+++

When <a href="2008/02/10/pair-programming-introduction/">pair programming</a> there are obviously times when you have different opinions about how things should be done.

One of these is the way that we should return from methods. There seem to be two approaches when it comes to this:
<h3>Exit as quickly as possible</h3>
The goal with this approach is as the title suggests, to get out of the method at the earliest possible moment.

The <a href="http://c2.com/cgi/wiki?GuardClause">Guard Block</a> is the best example of this. It is generally used at the start of methods to stop further execution of the method if the parameters are invalid for example:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public <span class="pt">void</span> DoSomething(SomeObject someObject)<tt>
</tt>{<tt>
</tt>   <span class="r">if</span> (someObject == null) <span class="r">return</span>;<tt>
</tt>   <span class="c">// Do some other stuff</span><tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
When used in this way it is very similar to what would be called a pre condition in the world of <a href="http://archive.eiffel.com/doc/manuals/technology/contract/">Design by Contract</a>. It can also be used in methods which return a result:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public SomeObject GetSomeObject()<tt>
</tt>{<tt>
</tt>   <span class="r">if</span>(ThisConditionHappens()) <span class="r">return</span> new SomeObject(thisParameter);<tt>
</tt>   <span class="r">return</span> new SomeObject(thatParameter);<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
In this example there are only two execution paths so returining early is fine. When there start to become a lot of different branches, however,  the idea of returning in each place becomes counter productive and makes the code harder to read.

If that becomes the case, however, there's probably greater things to worry about with regards to the method than how best to return the result!
<h3>Return everything at the end</h3>
This approach is fairly self explanatory too. If my somewhat contrived example was written to return everything at the end it would look like this:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt><strong>10</strong><tt>
</tt>11<tt>
</tt>12<tt>
</tt>13<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public SomeObject GetSomeObject()<tt>
</tt>{<tt>
</tt>    SomeObject someObject = null;<tt>
</tt>    <span class="r">if</span>(ThisConditionHappens())<tt>
</tt>    {<tt>
</tt>        someObject = new SomeObject(thisParameter);<tt>
</tt>    }<tt>
</tt>    <span class="r">else</span><tt>
</tt>    {<tt>
</tt>        someObject = new SomeObject(thatParameter);<tt>
</tt>    }<tt>
</tt>    <span class="r">return</span> someObject;<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
This idea starts to come into its own when there are more possible paths of execution, although if this becomes the case it might be better to use the <a href="http://c2.com/cgi/wiki?CollectingParameter">collecting parameter</a> idiom to solve the problem.

Just in case it hasn't come across, I am a big advocate of the idea of returning early from methods as it means I don't have to understand the whole internals of a method if I only care about one branch.

If a method gets into such a state that returning early becomes unreadable this would be a clear sign to me that the method is doing too much and should be refactored into smaller chunks.
