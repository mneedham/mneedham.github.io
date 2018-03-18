+++
draft = false
date="2008-08-30 03:03:58"
title="Getting a strongly typed collection using LINQ to Xml"
tag=['c', 'net', 'linq']
category=['.NET']
+++

I <a href="http://www.markhneedham.com/blog/2008/08/28/querying-xml-with-linq-dont-forget-the-namespace/">mentioned earlier</a> that I have been playing around with LINQ to Xml for parsing a Visual Studio csproj file. 

While having namespace issues I decided to try and parse a simpler Xml file to try and work out what I was doing wrong. 

Given this fragment of Xml:


~~~xml

<Node>
  <InnerNode>mark</InnerNode>
  <InnerNode>needham</InnerNode>
</Node>
~~~

I wanted to get a collection(IEnumerable<string>) of InnerNode values.

Unfortunately my over enthusiasm to use <a href="http://weblogs.asp.net/scottgu/archive/2007/05/15/new-orcas-language-feature-anonymous-types.aspx?CommentPosted=true">anonymous types</a> meant that I caused myself more problems than I needed to. This was my original (failed) effort at doing so:


~~~csharp

var innerNodes = from node in projectFile.Descendants("Node").Elements()
                 select new {InnerNode = node.Value};

IList<string> innerNodesAsCollection = new List<string>();
foreach (var innerNode in innerNodes)
{
    innerNodesAsCollection.Add(innerNode.InnerNode);
}
~~~

A very round about way of solving the problem I'm sure you'll agree. I was sure this should be easy to do but I was making it very complicated indeed. A bit more googling revealed that I could put items straight into the collection from the LINQ query by not using anonymous types:


~~~csharp

IEnumerable<string> innerNodes = from node in projectFile.Descendants("Node").Elements()
                                 select node.Value;
~~~

Much less code, much simpler, and a lesson in the art of not over complicating things.
