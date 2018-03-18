+++
draft = false
date="2012-01-13 21:46:58"
title="Oracle: exp -  EXP-00008: ORACLE error 904 encountered/ORA-00904: \"POLTYP\": invalid identifier"
tag=['software-development', 'oracle']
category=['Software Development']
+++

I spent a bit of time this afternoon trying to export an Oracle test database so that we could use it locally using the <cite><a href="http://www.orafaq.com/wiki/Import_Export_FAQ#How_does_one_use_the_import.2Fexport_utilities.3F">exp</a></cite> tool.

I had to connect to exp like this:


~~~text

exp user/password@remote_address
~~~

And then filled in the other parameters interactively.

Unfortunately when I tried to actually export the specified tables I got the following error message:


~~~text

EXP-00008: ORACLE error 904 encountered
ORA-00904: "POLTYP": invalid identifier
EXP-00000: Export terminated unsuccessfully
~~~

I eventually came across <a href="http://oisene.blogspot.com/2010/06/error-when-using-11g-export-client-on.html">Oyvind Isene's blog post which pointed out that you'd get this problem if you tried to export a 10g database using an 11g client</a> which is exactly what I was trying to do!

He explains it like so:

<blockquote>
The export command runs a query against a table called EXU9RLS in the SYS schema. On 11g this table was expanded with the column POLTYP and the export command (exp) expects to find this column. 
</blockquote>

I needed to download the 10g client so that I could use that version of exp instead. I haven't quite got it working yet but at least it's a different error to deal with!
