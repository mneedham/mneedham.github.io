+++
draft = false
date="2008-08-28 10:15:45"
title="Querying Xml with LINQ - Don't forget the namespace"
tag=['c', 'net', 'linq', 'xml', 'namespace']
category=['.NET']
+++

I've been working with a colleague on parsing a Visual Studio project file <a href="http://weblogs.asp.net/scottgu/archive/2007/08/07/using-linq-to-xml-and-how-to-build-a-custom-rss-feed-reader-with-it.aspx">using LINQ</a> to effectively create a DOM of the file.

The first thing we tried to do was get a list of all the references from the file. It seemed like a fairly easy problem to solve but for some reason nothing was getting returned:


~~~csharp

XDocument projectFile = XDocument.Load(projectFilePath.Path);

var references = from itemGroupElement in projectFile.Descendants("ItemGroup").First().Elements()
                 select itemGroupElement.Attribute("Include").Value;
~~~

We are selecting all the occurrences of 'ItemGroup', taking the first occurrence, getting all the elements inside it (i.e. all the Reference elements) and then selecting the value of the 'Include' attribute. A fragment of the csproj file is as follows:


~~~xml

<ItemGroup>
	<Reference Include="System" />
	<Reference Include="System.Core">
		<RequiredTargetFramework>3.5</RequiredTargetFramework>
	 </Reference>
...
</ItemGroup>
~~~

After several hours of trial and error it turned out that we just needed to include the namespace of the file when querying. The new and now working code looks like this:


~~~csharp

XNamespace projectFileNamespace = "http://schemas.microsoft.com/developer/msbuild/2003";
XDocument projectFile = XDocument.Load(projectFilePath.Path);

var references = from itemGroupElement in projectFile.Descendants(projectFileNamespace + "ItemGroup").First().Elements()
                 select itemGroupElement.Attribute("Include").Value;
~~~

There are two quite clever things going on with the way this is done

1) There is an <a href="http://msdn.microsoft.com/en-us/library/z5z9kes2(VS.71).aspx">implicit type conversion</a> defined on XNamespace which allows us instatiate it using a string.
2) The addition(+) operator has been overloaded on XNamespace so that it can combine the namespace with the local name ('ItemGroup'). This is described in more detail <a href="http://msdn.microsoft.com/en-us/library/bb669152.aspx">here</a>.
