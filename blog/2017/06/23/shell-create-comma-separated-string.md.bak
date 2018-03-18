+++
draft = false
date="2017-06-23 12:26:49"
title="Shell: Create a comma separated string"
tag=['shell', 'scripting', 'bash']
category=['Shell Scripting']
+++

<p>
I recently needed to generate a string with comma separated values, based on iterating a range of numbers.
</p>


<p>
e.g. we should get the following output where n = 3
</p>



~~~bash

foo-0,foo-1,foo-2
~~~

<p>I only had the shell available to me so I couldn't shell out into Python or Ruby for example. That means it's bash scripting time!</p>


<p>
If we want to iterate a range of numbers and print them out on the screen we can write the following code:
</p>



~~~bash

n=3
for i in $(seq 0 $(($n > 0? $n-1: 0))); do 
  echo "foo-$i"
done

foo-0
foo-1
foo-2
~~~

<p>
Combining them into a string is a bit more tricky, but luckily I found <a href="http://ajhaupt.blogspot.co.uk/2010/12/create-comma-separated-string-in-shell.html">a great blog post</a> by Andreas Haupt which shows what to do. Andreas is solving a more complicated problem than me but these are the bits of code that we need from the post.
</p>



~~~bash

n=3
combined=""

for i in $(seq 0 $(($n > 0? $n-1: 0))); do 
  token="foo-$i"
  combined="${combined}${combined:+,}$token"
done
echo $combined

foo-0,foo-1,foo-2
~~~

<p>
This won't work if you set <cite>n<0</cite> but that's ok for me! I'll let Andreas explain how it works:
</p>


<ul>
<li>
<cite>${combined:+,}</cite> will return either a comma (if <cite>combined</cite> exists and is set) or nothing at all.
</li>
<li>
In the first invocation of the loop <cite>combined</cite> is not yet set and nothing is put out.
</li>
<li>
In the next rounds <cite>combined</cite> is set and a comma will be put out.
</li>
</ul>

<p>
We can see how it in action by printing out the value of <cite>$combined</cite> after each iteration of the loop:
</p>



~~~bash

n=3
combined=""

for i in $(seq 0 $(($n > 0 ? $n-1: 0))); do 
  token="foo-$i"
  combined="${combined}${combined:+,}$token"
  echo $combined
done

foo-0
foo-0,foo-1
foo-0,foo-1,foo-2
~~~

<p>
Looks good to me!
</p>

