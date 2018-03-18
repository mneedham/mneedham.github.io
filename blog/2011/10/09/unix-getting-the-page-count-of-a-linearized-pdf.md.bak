+++
draft = false
date="2011-10-09 11:34:04"
title="Unix: Getting the page count of a linearized PDF"
tag=['unix', 'awk']
category=['Shell Scripting']
+++

We were doing some work last week to rasterize a PDF document into a sequence of images and wanted to get a rough idea of how many pages we'd be dealing with if we created an image per page.

The PDFs we're dealing with are <a href="http://partners.adobe.com/public/developer/en/pdf/PDFReference.pdf">linearized</a> since they're available for viewing on the web:

<blockquote>
A LINEARIZED PDF FILE is one that has been organized in a special way to enable efﬁcient incremental access in a network environment. 

The ﬁle is valid PDF in all respects, and is compatible with all existing viewers and other PDF applications. Enhanced viewer applications can recognize that a PDF ﬁle has been linearized and can take advantage of that organization (as well as added “hint” information) to enhance viewing performance. 
</blockquote>

The neat thing about this is it means that the document has meta data detailing the number of pages it contains:

<blockquote>
Part 2: Linearization parameter dictionary
<br /> 43 0 obj
<br /> << /Linearized 1.0 % Version
<br /> /L 54567 % File length
<br />/H [475 598] % Primary hint stream offset and length (part 5)
<br />/O 45 % Object number of ﬁrst page’s page object (part 6)
<br /> /E 5437 % Offset of end of ﬁrst page
<br /> <strong>/N 11 % Number of pages in document</strong>
<br /> /T 52786 % Offset of ﬁrst entry in main cross-reference table (part 11)
<br /> >>
<br /> endobj
</blockquote>

By making use of the <cite><a href="http://en.wikipedia.org/wiki/Strings_(Unix)">strings</a></cite> command <a href="http://duncan-cragg.org/blog/">Duncan</a> and I hacked together a little script that lets us grab the number of pages in <a href="http://www.rand.org/pubs/commercial_books/CB149-1.html">The Games of Strategy</a> <a href="http://www.rand.org/content/dam/rand/pubs/commercial_books/2007/RAND_CB149-1.pdf">PDF</a> or any other linearized PDF:


~~~text

strings RAND_CB149-1.pdf | 
awk '/Linearized/ { inmeta = 1; } match($0, /\/N [0-9]+/) { if(inmeta) print substr( $0, RSTART, RLENGTH ); exit;}' |
cut -d" " -f2
~~~

It seems much more difficult to find the count if the document hasn't been linearized but we didn't need to solve that problem for the moment!
