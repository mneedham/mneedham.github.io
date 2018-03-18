+++
draft = false
date="2012-12-29 17:49:46"
title="Sed: Replacing characters with a new line"
tag=['sed']
category=['Shell Scripting']
+++

<p>I've been playing around with writing some algorithms in both Ruby and Haskell and the latter wasn't giving the correct result so I wanted to output an intermediate state of the two programs and compare them.</p>


<p>I didn't do any fancy formatting of the output from either program so I had the raw data structures in text files which I needed to transform so that they were comparable.</p>


<p>The main thing I wanted to do was get each of the elements of the collection onto their own line. The output of one of the programs looked like this:</p>



~~~text

[(1,2), (3,4)…] 
~~~

<p>To get each of the elements onto a new line my first step was to replace every occurrence of ', (' with '\n('. I initially tried using <cite>sed</cite> to do that:</p>



~~~text

sed -E -e 's/, \(/\\n(/g' ruby_union.txt
~~~

<p>All that did was insert the string value '\n' rather than the new line character.</p>


<p>I've come across similar problems before and I usually just use <cite>tr</cite> but in this case it doesn't work very well because we're replacing more than just a single character.</p>


<p>I came across <a href="http://www.linuxquestions.org/questions/linux-software-2/sed-insert-a-newline-why-does-not-it-work-158806/">this thread</a> on Linux Questions which gives a couple of ways that we can get see to do what we want.</p>


<p>The first suggestion is that we should use a back slash followed by the enter key while writing our sed expression where we want the new line to be and then continue writing the rest of the expression.</p>
 

<p>We therefore end up with the following:</p>



~~~text

sed -E -e "s/,\(/\
/g" ruby_union.txt
~~~

<p>This approach works but it's a bit annoying as you need to delete the rest of the expression so that the enter works correctly.</p>


<p>An alternative is to make use of <cite>echo</cite> with the '-e' flag which allows us to output a new line. Usually <a href="http://linux.about.com/library/cmd/blcmdl1_echo.htm">backslashed characters aren't interpreted</a> and so you end up with a literal representation. e.g.</p>



~~~text

$ echo "mark\r\nneedham"
mark\r\nneedham

$ echo -e "mark\r\nneedham"
mark
needham
~~~

<p>We therefore end up with this:~~~


~~~text

sed -E -e "s/, \(/\\`echo -e '\n\r'`/g" ruby_union.txt
~~~

<p>** Update **</p>


<p>It was pointed out in the comments that this final version of the sed statement doesn't actually lead to a very nice output which is because I left out the other commands I passed to it which get rid of extra brackets.</p>


<p>The following gives a cleaner output:</p>



~~~text

$ echo "[(1,2), (3,4), (5,6)]" | sed -E -e "s/, \(/\\`echo -e '\n\r'`/g" -e 's/\[|]|\)|\(//g'
1,2
3,4
5,6
~~~
