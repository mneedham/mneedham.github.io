+++
draft = false
date="2013-05-19 22:44:40"
title="Ruby/Python: Constructing a taxonomy from an array using zip"
tag=['ruby', 'python']
category=['Ruby', 'Python']
+++

<p>As I <a href="http://www.markhneedham.com/blog/2013/05/19/neo4jcypher-keep-longest-path-when-finding-taxonomy/">mentioned in my previous blog post</a> I've been hacking on a product taxonomy and I wanted to create a 'CHILD' relationship between a collection of categories.</p>


<p>For example, I had the following array and I wanted to transform it into an array of 'SubCategory, Category' pairs:</p>



~~~python

taxonomy = ["Cat", "SubCat", "SubSubCat"]
# I wanted this to become [("Cat", "SubCat"), ("SubCat", "SubSubCat")
~~~

<p>In order to do this we need to zip the first 2 items with the last which I found reasonably easy to do using Python:</p>



~~~python

>>> zip(taxonomy[:-1], taxonomy[1:])
[('Cat', 'SubCat'), ('SubCat', 'SubSubCat')]
~~~

<p>Here we using the <a href="http://stackoverflow.com/questions/509211/the-python-slice-notation">python array slicing notation</a> to get all but the last item of 'taxonomy' and then all but the first item of 'taxonomy' and zip them together.</p>


<p>I wanted to achieve that effect in Ruby though because my import job was written in that!</p>


<p>We can't achieve the open ended slicing as far as I can tell so the following gives us an error:</p>



~~~ruby

> taxonomy[..-1]
SyntaxError: (irb):10: syntax error, unexpected tDOT2, expecting ']'
taxonomy[..-1]
           ^
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/bin/irb:12:in `<main>'
~~~

<p>The way negative indexing works is a bit different so to remove the last item of the array we use '-2' rather than '-1':</p>



~~~ruby

> taxonomy[0..-2].zip(taxonomy[1..-1])
=> [["Cat", "SubCat"], ["SubCat", "SubSubCat"]]
~~~
