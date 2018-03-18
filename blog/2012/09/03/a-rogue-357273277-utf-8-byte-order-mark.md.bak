+++
draft = false
date="2012-09-03 06:31:54"
title="A rogue \"\\357\\273\\277\" (UTF-8 byte order mark)"
tag=['software-development']
category=['Software Development']
+++

We've been loading some data into neo4j from a CSV file - creating one node per row and using the value in the first column as the index lookup for the node.

Unfortunately the index lookup wasn't working for the first row but was for every other row.

By coincidence we started saving each row into a hash map and were then able to see what was going wrong:


~~~ruby

require 'rubygems'
require 'fastercsv'

things = FasterCSV.read("things.csv", :col_sep => "|")

saved_things = {}
things do |row|
  saved_things[row[0]] = row[1]
end

p saved_things
~~~

This is what we saw when we ran the script:


~~~text

{"\357\273\2771"=>"Thing1", "2" => "Thing2"}
~~~

A bit of googling suggests that "\357\273\277" <a href="http://www.highdots.com/forums/macromedia-dreamweaver/357-273-277-characters-placed-154281.html">represents a UTF-8 byte order mark</a> which apparently <a href="http://en.wikipedia.org/wiki/Byte_order_mark">isn't actually needed anyway</a>:

<blockquote>
The Unicode Standard does permit the BOM in UTF-8, but does not require or recommend its use. Byte order has no meaning in UTF-8 so in UTF-8 the BOM serves only to identify a text stream or file as UTF-8.
</blockquote>

We're not converting the CSV file back into any other format so the following awk command can be used to cleanup it up:


~~~text

awk '{if(NR==1)sub(/^\xef\xbb\xbf/,"");print}' things.csv > things.nobom.csv
~~~ 

If we use the hexdump tool we can see that the BOM has been removed:

Before:

~~~text

$ hexdump things.csv
0000000 ef bb bf 31 7c 50 72 69 6d 61 72 69 65 73 0d 0a
...
~~~

After:

~~~text

hexdump things.nobom.csv
0000000 31 7c 50 72 69 6d 61 72 69 65 73 0d 0a 31 30 7c
~~~

I was initially curious why Ruby and the hexdump were printing out different values but it's just a case of Ruby showing the Octal version of the BOM as compared to the Hexidecimal version. The values translate like so:


~~~text

Octal | Hexadecimal | Decimal
357   | EF          | 239
273   | BB          | 187
277   | BF          | 191
~~~
