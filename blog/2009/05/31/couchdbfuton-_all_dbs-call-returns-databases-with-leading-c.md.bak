+++
draft = false
date="2009-05-31 23:28:20"
title="CouchDB/Futon: '_all_dbs' call returns databases with leading 'c/'"
tag=['couchdb', 'futon']
category=['CouchDB']
+++

As I mentioned <a href="http://www.markhneedham.com/blog/2009/05/31/sharpcouch-use-anonymous-type-to-create-json-objects/">in my previous post</a> I've been playing around with <a href="http://wiki.apache.org/couchdb/FrontPage">CouchDB</a> and one of the problems that I've been having is that although I can access my database through the REST API perfectly fine, whenever I went to the <a href="https://forge.process-one.net/browse/~raw,r=811/CouchDB/trunk/share/www/index.html">Futon</a> page ('http://localhost:5984/_utils/' in my case) to view my list of databases I was getting the following javascript error:


~~~text

Database information could not be retrieved: missing
~~~

I thought I'd have a quick look with FireBug to see if I could work out what was going on and saw several requests being made to the following urls and resulting in 404s:

<ul>
<li>http://localhost:5984/c%2Fsharpcouch/</li>
<li>http://localhost:5984/c%2Fmark_erlang/</li>
</ul>

The value 'c/' was being added to the front of each of my database names, therefore meaning that Futon was unable to display the various attributes on the page for each of them.

Tracing this further I realised that the call to 'http://localhost:5984/_all_dbs' was actually the one that was failing, and calling it directly from 'erl' was resulting in the same error:


~~~erlang

> couch_server:all_databases().

{ok,["c/mark_erlang","c/sharpcouch","c/test_suite_db"]}
~~~

I don't know Erlang well enough to try and change the code to fix this problem but I came across a <a href="https://issues.apache.org/jira/browse/COUCHDB-307">bug report</a> on the CouchDB website which described exactly the problem I've been having.

Apparently there is a problem when you use an upper case 'C' for the 'DbRootDir' property in 'couch.ini'. Changing that to a lower case 'c' so that my 'couch.ini' file now looks like this solved the problem:


~~~text

DbRootDir=c:/couchdb/db
~~~
