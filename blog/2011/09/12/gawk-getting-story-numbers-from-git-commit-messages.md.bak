+++
draft = false
date="2011-09-12 07:05:13"
title="gawk: Getting story numbers from git commit messages"
tag=['software-development']
category=['Software Development']
+++

As I mentioned in my previous post I've been writing a little application to create graphs based on our git repository history and in one of them we wanted to try and create a graph showing which people had been working on which stories. 

I needed a way to extract a story number from the git commit message and then store them all in a text file.

A typical commit with a story number in might look like this:


~~~text

Mark/Uday #689 some awesome scala refactoring
~~~

I couldn't think of an easy way to do this with my current knowledge of sed or the Mac version of awk but the <cite><a href="http://www.gnu.org/software/gawk/manual/gawk.html#index-g_t_0040code_007bmatch_0028_0029_007d-function-1373">match</a></cite> function of gawk (GNU awk) makes this really easy.

<blockquote>
match(string, regexp [, array])

Search string for the longest, leftmost substring matched by the regular expression, regexp and return the character position, or index, at which that substring begins (one, if it starts at the beginning of string). If no match is found, return zero.

...

If array is present, it is cleared, and then the zeroth element of array is set to the entire portion of string matched by regexp. 
</blockquote>

The <cite>array</cite> argument is what I needed and it's only available as a gawk extension according to the documentation.

I ended up with the following command to strip the story numbers:


~~~text

git log --no-merges --pretty="format:%s" | 
gawk '{ match($0, /#([0-9]+)/, arr); if(arr[1] != "") print arr[1] }'
~~~

I had to install gawk using ports on my Mac but on Fedora the default installation of awk is gawk.
