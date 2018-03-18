+++
draft = false
date="2018-01-23 21:11:49"
title="Asciidoc to Asciidoc: Exploding includes"
tag=['asciidoc', 'asciidoctor']
category=['Software Development']
+++

<p>
One of my favourite features in <a href="http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#include-files">AsciiDoc</a> is the ability to include other files, but when using lots of includes is that it becomes difficult to read the whole document unless you convert it to one of the supported backends.
</p>



~~~bash

$ asciidoctor --help
Usage: asciidoctor [OPTION]... FILE...
Translate the AsciiDoc source FILE or FILE(s) into the backend output format (e.g., HTML 5, DocBook 4.5, etc.)
By default, the output is written to a file with the basename of the source file and the appropriate extension.
Example: asciidoctor -b html5 source.asciidoc

    -b, --backend BACKEND            set output format backend: [html5, xhtml5, docbook5, docbook45, manpage] (default: html5)
                                     additional backends are supported via extensions (e.g., pdf, latex)
~~~

<p>
I don't want to have to convert my code to one of these formats each time - I want to convert asciidoc to asciidoc!
</p>


<p>
For example, given the following files:
</p>



<p><cite>mydoc.adoc</cite></p>



~~~text

= My Blog example

== Heading 1

Some awesome text

== Heading 2

include::blog_include.adoc[]
~~~

<p><cite>blog_include.adoc</cite></p>



~~~text

Some included text
~~~

<p>I want to generate another asciidoc file where the contents of the include file are exploded and displayed inline.
</p>


<p>
After a lot of searching I came across <a href="https://github.com/asciidoctor/asciidoctor-extensions-lab/blob/master/scripts/asciidoc-coalescer.rb">an excellent script</a> written by Dan Allen and put it in a file called <cite>adoc.rb</cite>. We can then call it like this:
</p>



~~~bash

$ ruby adoc.rb mydoc.adoc
= My Blog example

== Heading 1

Some awesome text

== Heading 2

Some included text
~~~

<p>
Problem solved! 
</p>



<p>In my case I actually wanted to explode HTTP includes so I needed to pass the <cite>-a allow-uri-read</cite> flag to the script:
</p>



~~~bash

$ ruby adoc.rb mydoc.adoc -a allow-uri-read 
~~~

<p>
And now I can generate asciidoc files until my heart's content.</p>

</p>

