+++
draft = false
date="2008-08-29 01:39:52"
title="C# Thrift Examples"
tag=['c', 'thrift', 'facebook', 'examples']
category=['.NET', 'Messaging']
+++

As I mentioned in my <a href="http://www.markhneedham.com/blog/2008/08/29/thrift-as-a-message-definition-layer/">earlier post</a> I have been working with Facebook's <a href="http://incubator.apache.org/thrift/">Thrift</a> messaging project.

Unfortunately there are not currently any C# examples of how to use the Data Transfer Objects the Thrift compiler generates for us on the <a href="http://wiki.apache.org/thrift/ThriftUsage">official wiki</a>.

We managed to figure out how to do it by following the <a href="http://wiki.apache.org/thrift/ThriftUsageJava">Java instructions</a> and converting them into C# code. Before writing any code we need to import Thrift.dll into our Visual Studio project. 

Assuming that we have the following Thrift definition file:


~~~text

namespace csharp Test.Thrift

struct FooBarMessageThrift {
1: string Foo
2: string Bar
}
~~~

When we run the <a href="http://wiki.apache.org/thrift/ThriftInstallationWin32">Thrift compiler</a> we will end up with the FooBarMessageThrift class. I won't post this class here as it's all codegen.

The easiest way to transport this class around is by converting it to a byte array and transporting that:


~~~csharp

var fooBarMessage = new FooBarMessageThrift {Foo = "foo", Bar = "bar"};
var stream = new MemoryStream();

TProtocol tProtocol = new TBinaryProtocol(new TStreamTransport(stream, stream));

fooBarMessage.Write(tProtocol);

byte[] content = stream.ToArray();
~~~

To read the byte array back into FooBarMessageThrift we do this:


~~~csharp

var stream = new MemoryStream(content);
TProtocol tProtocol = new TBinaryProtocol(new TStreamTransport(stream, stream));

var barFooMessageThrift = new BarFooMessageThrift();
barFooMessageThrift.Read(tProtocol);
~~~
'content' in this example is the byte[] created in the first example, and that's all there is to it!


