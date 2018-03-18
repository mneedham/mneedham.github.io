+++
draft = false
date="2014-10-18 10:49:07"
title="Neo4j: LOAD CSV - The sneaky null character"
tag=['software-development']
category=['Software Development']
+++

<p>I spent some time earlier in the week trying to import a CSV file extracted from Hadoop into Neo4j using Cypher's <a href="http://docs.neo4j.org/chunked/stable/query-load-csv.html">LOAD CSV</a> command and initially struggled due to some rogue characters.</p>


<p>The CSV file looked like this:</p>



~~~bash

$ cat foo.csv
foo,bar,baz
1,2,3
~~~

<p>I wrote the following LOAD CSV query to extract some of the fields and compare others:</p>



~~~cypher

load csv with headers from "file:/Users/markneedham/Downloads/foo.csv" AS line
RETURN line.foo, line.bar, line.bar = "2"
~~~


~~~text

==> +--------------------------------------+
==> | line.foo | line.bar | line.bar = "2" |
==> +--------------------------------------+
==> | <null>   | "2"     | false          |
==> +--------------------------------------+
==> 1 row
~~~

<p>I had expect to see a "1" in the first column and a 'true' in the third column, neither of which happened.</p>


<p>I initially didn't have a text editor with hexcode mode available so I tried checking the length of the entry in the 'bar' field:</p>



~~~cypher

load csv with headers from "file:/Users/markneedham/Downloads/foo.csv" AS line
RETURN line.foo, line.bar, line.bar = "2", length(line.bar)
~~~


~~~text

==> +---------------------------------------------------------+
==> | line.foo | line.bar | line.bar = "2" | length(line.bar) |
==> +---------------------------------------------------------+
==> | <null>   | "2"     | false          | 2                |
==> +---------------------------------------------------------+
==> 1 row
~~~

<p>The length of that value is 2 when we'd expect it to be 1 given it's a single character.</p>


<p>I tried trimming the field to see if that made any difference...</p>



~~~cypher

load csv with headers from "file:/Users/markneedham/Downloads/foo.csv" AS line
RETURN line.foo, trim(line.bar), trim(line.bar) = "2", length(line.bar)
~~~


~~~text

==> +---------------------------------------------------------------------+
==> | line.foo | trim(line.bar) | trim(line.bar) = "2" | length(line.bar) |
==> +---------------------------------------------------------------------+
==> | <null>   | "2"            | true                 | 2                |
==> +---------------------------------------------------------------------+
==> 1 row
~~~

<p>...and it did! I thought there was probably a trailing whitespace character after the "2" which trim had removed and that 'foo' column in the header row had the same issue.</p>


<p>I was able to see that this was the case by extracting the JSON dump of the query via the Neo4j browser:</p>



~~~javascript

{  
   "table":{  
      "_response":{  
         "columns":[  
            "line"
         ],
         "data":[  
            {  
               "row":[  
                  {  
                     "foo\u0000":"1\u0000",
                     "bar":"2\u0000",
                     "baz":"3"
                  }
               ],
               "graph":{  
                  "nodes":[  

                  ],
                  "relationships":[  

                  ]
               }
            }
         ],
      ...
}
~~~

<p>It turns out there were null characters scattered around the file so I needed to <a href="http://stackoverflow.com/questions/2398393/identifying-and-removing-null-characters-in-unix">pre process the file to get rid of them</a>:</p>



~~~bash

$ tr < foo.csv -d '\000' > bar.csv
~~~

<p>Now if we process bar.csv it's a much smoother process:</p>



~~~cypher

load csv with headers from "file:/Users/markneedham/Downloads/bar.csv" AS line
RETURN line.foo, line.bar, line.bar = "2", length(line.bar)
~~~


~~~text

==> +---------------------------------------------------------+
==> | line.foo | line.bar | line.bar = "2" | length(line.bar) |
==> +---------------------------------------------------------+
==> | "1"      | "2"      | true           | 1                |
==> +---------------------------------------------------------+
==> 1 row

~~~

<p>Note to self: <strong>don't expect data to be clean, inspect it first!</strong></p>

