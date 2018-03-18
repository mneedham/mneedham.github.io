+++
draft = false
date="2011-02-11 20:34:53"
title="Sed: Extended regular expressions"
tag=['software-development', 'sed']
category=['Software Development']
+++

<a href="http://twitter.com/irfn">Irfan</a> and I were looking at how to do some text substitution in a text file this afternoon and turned to sed to help us in our quest.

He had originally used grep to find what he wanted to replace on each line, using a grep regular expression to match one or more numbers:


~~~text

cat the_file.txt | grep "[0-9]\+"
~~~

That works pretty well but since I knew how to do the substitution in sed we needed to convert the regular expression to work with sed.

We started off with just trying to print the lines which matched the regular expression:


~~~text

cat the_file.txt | sed -n '/[0-9]\+/p'
~~~

Which prints nothing because sed uses basic regular expressions by default which means we can't use '+' to match 1 or more numbers.

grep on the other hand...

<blockquote>
Grep understands two different versions of regular expression syntax: "basic" and "extended."  In GNU grep, there is no difference in available functionality using either  syntax.   In  other  implementations, basic regular expressions are less powerful.
</blockquote>

To get sed to allow us to use extended metacharacters we need to pass the '-E' flag to sed which also means that we no longer to escape the '+':


~~~text

cat the_file.txt | sed -nE '/[0-9]+/p'
~~~

From <a href="http://www.amazon.com/sed-awk-2nd-Dale-Dougherty/dp/1565922255/ref=sr_1_1?ie=UTF8&qid=1297456109&sr=8-1">what I understand</a> you can also only use the following metacharacters in extended mode as well:

<ul>
<li>? - for matching zero or one occurrence of a regular expression</li>
<li>| - for matching either the preceding or following regular expression</li>
<li>() - grouping regular expressions</li>
<li>{n,m} - for matching a range of occurrences of the single preceding character</li>
</ul>

I'm told that you can use grep to do substitution as well but I haven't figured out how exactly you do that yet.
