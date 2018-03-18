+++
draft = false
date="2008-08-08 22:16:02"
title="Ruby: Parameterising with ActiveResource"
tag=['ruby', 'rails', 'rest', 'activeresource']
category=['Ruby']
+++

We've been using Ruby/Rails on my current project to create a <a href="http://ryandaigle.com/articles/2006/06/30/whats-new-in-edge-rails-activeresource-is-here#REST">RESTful</a> web service. One of the problems we wanted to solve was making the data queried by this web service configurable from our build.

We started off with the following bit of code (which makes use of the recently added <a href="http://www.noobkit.com/show/ruby/rails/rails-edge/activeresource-edge/activeresource/base.html">ActiveResource</a> class):
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><span class="r">class</span> <span class="cl">MyClass</span> < <span class="co">ActiveResource</span>::<span class="co">Base</span><tt>
</tt>  <span class="pc">self</span>.site = <span class="s"><span class="dl">"</span><span class="k">http://localhost:3000/</span><span class="dl">"</span></span><tt>
</tt><span class="r">end</span>~~~
</td>
</tr>
</tbody></table>
And then called this class as follows:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><span class="co">MyClass</span>.create(<span class="sy">:param</span> => <span class="s"><span class="dl">"</span><span class="k">param-value</span><span class="dl">"</span></span>)<tt>
</tt>~~~
</td>
</tr>
</tbody></table>
This worked fine for us until we wanted to parameterise the 'site' value so that we could set it to different values depending which build we were running (dev/ci/qa). We tried all the obvious ways - overriding the constructor and passing in the site, trying to set the site by calling MyClass.site but none of them did what we wanted. We eventually ended up creating a new method to create an instance of the class with our configurable site:
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
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }"><span class="r">class</span> <span class="cl">MyClass</span> < <span class="co">ActiveResource</span>::<span class="co">Base</span><tt>
</tt><tt>
</tt><span class="r">def</span> <span class="fu">instance</span>(site, args)<tt>
</tt>  <span class="pc">self</span>.site = site<tt>
</tt>  new(args) <span class="r">unless</span> args.nil?<tt>
</tt><span class="r">end</span><tt>
</tt><tt>
</tt><span class="r">end</span><tt>
</tt>~~~
</td>
</tr>
</tbody></table>
We then call the code like this:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">my_class = <span class="co">MyClass</span>.instance(<span class="s"><span class="dl">"</span><span class="k">http://localhost:3000</span><span class="dl">"</span></span>, <span class="sy">:param</span> => <span class="s"><span class="dl">"</span><span class="k">param-value</span><span class="dl">"</span></span>)<tt>
</tt>my_class.save~~~
</td>
</tr>
</tbody></table>
It seems like a bit of a hack but it got it working!

Out of interest it has taken me ages to try and find a way to put the Ruby code on here in a readable format. I tried to use the TextMate exporter but that wasn't giving me any love. I eventually ended up using <a href="http://spotlight.heroku.com/">Spotlight</a>, a neat little tool written by Tyler Jennings. I found it from Jake Scruggs <a href="http://jakescruggs.blogspot.com/2008/05/syntax-highlighting-for-ruby-made-very.html">blog post</a>.
