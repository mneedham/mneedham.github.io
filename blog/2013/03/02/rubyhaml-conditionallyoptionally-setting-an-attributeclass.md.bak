+++
draft = false
date="2013-03-02 23:22:50"
title="Ruby/Haml: Conditionally/Optionally setting an attribute/class"
tag=['ruby', 'haml']
category=['Ruby']
+++

<p>One of the things that we want to do reasonably frequently is set an attribute (most often a class) on a HTML element depending on the value of a variable.</p>


<p>I always forget how to do this in Haml so I thought I better write it down so I'll remember next time!</p>


<p>Let's say we want to add a <cite>success</cite> class to a paragraph if the variable <cite>correct</cite> is true and not have any value if it's false.</p>


<p>The following code does what we want:</p>



~~~haml

- correct = true
%p{:class => (correct ? "success" : nil) }
  important text
~~~

<p>This generates the following HTML is <cite>correct</cite> is true:</p>



~~~html4strict

<p class="success">
  important text
</p>

~~~

<p>And the following HTML if it's false</p>



~~~html4strict

<p>
  important text
</p>

~~~

<p>To summarise, <a href="http://stackoverflow.com/questions/3841116/conditionally-set-html-element-id-with-haml">if we set an attribute to nil in Haml it just won't be rendered at all</a> which is exactly what we want in this situation.</p>

