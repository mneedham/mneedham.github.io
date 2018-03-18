+++
draft = false
date="2015-08-19 23:27:28"
title="Unix: Stripping first n bytes in a file / Byte Order Mark (BOM)"
tag=['unix']
category=['Shell Scripting']
+++

<p>
I've previously written <a href="http://www.markhneedham.com/blog/2012/10/07/mac-os-x-removing-byte-order-mark-with-an-editor/">a couple</a> <a href="http://www.markhneedham.com/blog/2012/09/03/a-rogue-357273277-utf-8-byte-order-mark/">of blog posts</a> showing how to strip out the byte order mark (BOM) from CSV files to make loading them into Neo4j easier and today I came across another way to clean up the file using tail.
</p>


<p>
The BOM is 3 bytes long at the beginning of the file so if we know that a file contains it then we can strip out those first 3 bytes tail like this:
</p>



~~~bash

$ time tail -c +4 Casualty7904.csv > Casualty7904_stripped.csv

real	0m31.945s
user	0m31.370s
sys	0m0.518s
~~~

<p>
The -c command is described thus;
</p>



~~~bash

-c number
             The location is number bytes.
~~~

<p>
So in this case we start reading at byte 4 (i.e. skipping the first 3 bytes) and then direct the output into a new file. 
</p>


<p>
Although using tail is quite simple, it took 30 seconds to process a 300MB CSV file which might actually be slower than opening the file with a Hex editor and manually deleting the bytes!
</p>

