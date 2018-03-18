+++
draft = false
date="2011-02-12 18:03:53"
title="CouchDB: 'badmatch' when executing view"
tag=['couchdb']
category=['CouchDB']
+++

I've been playing around with <a href="http://couchdb.apache.org/">CouchDB</a> again in my annual attempt to capture the links appearing on my twitter stream and I managed to create the following error for myself:

~~~text

$ curl http://127.0.0.1:5984/twitter_links/_design/cleanup/_view/find_broken_links
{"error":"badmatch","reason":"{\n   \"find_broken_links\": {\n       \"map\": \"function(doc) {   \nvar prefix = doc.actual_link.match(/.*/);            \n  if(true) {                  emit(doc.actual_link, null);                }              }\"\n   }\n}"}
~~~

It turns out this error is because I've managed to create new line characters in the view while editing it inside <a href="http://janl.github.com/couchdbx/">CouchDBX</a>. D'oh!

A better way is to edit the view in a text editor and then send it to CouchDB using curl.

The <a href="http://wiki.apache.org/couchdb/HTTP_Document_API?action=show&redirect=HttpDocumentApi#PUT">proper way</a> to update a view would be to add a '_rev' property to the body of the JSON document but I find it annoying to go and edit the document so I've just been deleting and then recreating my views.


~~~text

$ curl -X GET http://127.0.0.1:5984/twitter_links/_design/cleanup/
{"_id":"_design/cleanup","_rev":"1-8be14d29f183b61f1ade160badef3f75","views"...}
~~~


~~~text

$ curl -X DELETE http://127.0.0.1:5984/twitter_links/_design/cleanup?rev=1-8be14d29f183b61f1ade160badef3f75
{"ok":true,"id":"_design/cleanup","rev":"2-9fa15c1fdbb7cbaa659d623bc897b9da"}
~~~


~~~text

$ curl -X PUT http://127.0.0.1:5984/twitter_links/_design/cleanup -d @cleanup.json
{"ok":true,"id":"_design/cleanup","rev":"17-b0763381b79f3fda843f57a7dcc842e1"}
~~~

I guess there's probably a library somewhere which would encapsulate all that for me but I'm just hacking around at the moment. 

It's interesting to to see how you interact differently with a document database compared to what you'd do with a relational one with respect to optimistic concurrency.
