+++
draft = false
date="2008-08-16 23:58:17"
title="Naming the patterns we use in code"
tag=['c', 'patterns', 'collecting-parameter', 'net']
category=['Coding']
+++

I've been playing around with C#'s Xml libraries today and in particular the <a href="http://msdn.microsoft.com/en-us/library/system.xml.xmlwriter(VS.71).aspx">XmlWriter</a> class.

I wanted to use it to create an Xml document so I called the XmlWriter.Create() method. One of the overloads for this methods takes in a StringBuilder which I initially thought the XmlWriter used to create the Xml document.

In fact it actually writes the Xml Document into this StringBuilder. This is actually possible to deduct from the documentation provided on the Create method but I only glanced at the type needed initially and misunderstood how it worked.

Now clearly one response to that could be 'well just read the documentation more closely' but wouldn't it be better if the method was actually XmlWriter.CreateInto(StringBuilder output) for example?

I suppose I could write my own <a href="http://www.developer.com/net/csharp/article.php/3592216">extension method</a> to do this but my initial thought was to name the StringBuilder so that I knew what it was doing:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">var xmlCollectingBuilder = new StringBuilder();<tt>
</tt>var xmlWriter = XmlWriter.Create(xmlCollectingBuilder);~~~
</td>
</tr>
</tbody></table>
That seems more clear to me and I can see at a glance what the code is doing but something about it feels wrong. I am explicitly referencing the <a href="http://c2.com/cgi/wiki?CollectingParameter">collecting parameter pattern</a> in the code to make it easier for me to understand what's going on.

Talking through the problem with a colleague we wondered whether it is actually necessary to explicitly reference the pattern being used in code or whether it can be inferred. In the case of collecting parameter, the following code would be an example where this theory makes sense:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">private void CollectSomeStuff(IList stuff)<tt>
</tt>{<tt>
</tt>   stuff.Add("some value");<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
It's obvious in this example that 'stuff' is being used to collect some data so I don't need to add that information anywhere else - it would be redundant.

However with other patterns it seems that it's considered good practice to explicitly state their use. The strategy and visitor patterns are two examples of these. It's almost like there are implicit rules for when we should or should not explicitly state which pattern we are using in our code.

At the end of the day I think the key to writing code is expressing things in a way that other people who read it can understand. We should do whatever we need to do to make that a possibility.
