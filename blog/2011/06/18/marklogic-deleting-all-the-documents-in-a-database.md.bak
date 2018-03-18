+++
draft = false
date="2011-06-18 16:08:47"
title="MarkLogic: Deleting all the documents in a database"
tag=['marklogic']
category=['Mark Logic']
+++

We're using the <a href="http://www.marklogic.com/">MarkLogic</a> database on my current project and something that we wanted to do recently was delete all the documents as part of a deployment script.

Getting all of the documents is reasonably easy - we just need to make a call to the <cite>doc()</cite> function.

We can then iterate through the documents like so:


~~~text

for $doc in doc() return $doc
~~~

We wanted to make use of the <cite><a href="http://docs.marklogic.com/4.2doc/docapp.xqy#search.xqy?start=1&cat=all&query=xdmp:document-delete&button=search">xdmp:document-delete</a></cite> function to tear down all of the modules but that needs a uri representing the location of the document in the database which isn't available in <cite>$doc</cite>:

<blockquote>
<h2>xdmp:document-delete</h2>

<strong>xdmp:document-delete</strong>(
$uri as xs:string
)  as  empty-sequence()

Summary:

Deletes a document from the database.
</blockquote>

A colleague pointed out that what we needed to do was pass the document to <cite><a href="http://docs.marklogic.com/4.2doc/docapp.xqy#search.xqy?start=1&cat=all&query=xdmp:node-uri&button=search">xdmp:node-uri</a></cite> and then our troubles would be over!

The final solution therefore looks like this:


~~~text

for $doc in doc() return xdmp:document-delete(xdmp:node-uri($doc))
~~~

I was expecting that we would delete the documents by some sort of identifier but I guess this approach makes more sense given the way the data is stored. 

It all seems a bit esoteric at the moment!
