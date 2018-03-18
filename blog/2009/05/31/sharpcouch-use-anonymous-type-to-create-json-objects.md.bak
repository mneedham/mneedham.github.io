+++
draft = false
date="2009-05-31 20:59:47"
title="SharpCouch: Use anonymous type to create JSON objects"
tag=['sharpcouch', 'couchdb']
category=['.NET', 'CouchDB']
+++

I've been playing around with <a href="http://wiki.apache.org/couchdb/FrontPage">CouchDB</a> a bit today and in particular making use of <a href="http://code.google.com/p/couchbrowse/source/browse/trunk/SharpCouch/SharpCouch.cs">SharpCouch</a>, a library which acts as a wrapper around CouchDB calls. It is included in the <a href="http://code.google.com/p/couchbrowse/">CouchBrowse</a> library which is recommended as a good starting point for interacting with CouchDB from C# code.

I decided to work out how the API worked with by writing an integration test to save a document to the database.

The API is reasonably easy to understand and I ended up with the following test:


~~~csharp

[Test]
public void ShouldAllowMeToSaveADocument()
{
    var server = "http://localhost:5984";
    var databaseName = "sharpcouch";
    var sharpCouchDb = new SharpCouch.DB();

    sharpCouchDb.CreateDocument(server, databaseName, "{ key : \"value\"}");
}
~~~

In theory that should save the JSON object { key = "value" } to the database but it actually throws a 500 internal error in <a href="http://code.google.com/p/couchbrowse/source/browse/trunk/SharpCouch/SharpCouch.cs">SharpCouch.cs</a>:


~~~csharp

HttpWebResponse resp = req.GetResponse() as HttpWebResponse;
~~~

Debugging into that line the Status property is set to 'Protocol Error' and a bit of Googling led me to think that I probably had a <a href="https://issues.apache.org/jira/browse/COUCHDB-335">malformed client request</a>.

I tried the same test but this time created the document to save by creating an anonymous type and then converted it to a JSON object using the <a href="http://litjson.sourceforge.net/">LitJSON</a> library:


~~~csharp

[Test]
public void ShouldAllowMeToSaveADocumentWithAnonymousType()
{
    var server = "http://localhost:5984";
    var databaseName = "sharpcouch";
    var sharpCouchDb = new SharpCouch.DB();

    var savedDocument = new { key = "value"};
    sharpCouchDb.CreateDocument(server, databaseName, JsonMapper.ToJson(savedDocument));
}
~~~ 

That works much better and does actually save the document to the database which I was able to verify by adding a new method to SharpCouch.cs which creates a document and then returns the 'documentID', allowing me to reload it afterwards.


~~~csharp

[Test]
public void ShouldAllowMeToSaveAndRetrieveADocument()
{
    var server = "http://localhost:5984";
    var databaseName = "sharpcouch";
    var sharpCouchDb = new SharpCouch.DB();

    var savedDocument = new {key = "value"};
    var documentId = sharpCouchDb.CreateDocumentAndReturnId(server, databaseName, JsonMapper.ToJson(savedDocument));

    var retrievedDocument = sharpCouchDb.GetDocument(server, databaseName, documentId);

    Assert.AreEqual(savedDocument.key, JsonMapper.ToObject(retrievedDocument)["key"].ToString());
}
~~~


~~~csharp

public string CreateDocumentAndReturnId(string server, string db, string content)
{
    var response = DoRequest(server + "/" + db, "POST", content, "application/json");
    return JsonMapper.ToObject(response)["id"].ToString();
}
~~~

I'm not sure how well anonymous types work for more complicated JSON objects but for the simple cases it seems to do the job.
