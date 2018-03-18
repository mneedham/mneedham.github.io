+++
draft = false
date="2008-08-29 00:42:51"
title="Thrift as a message definition layer"
tag=['messaging', 'thrift', 'facebook', 'protocol-buffers']
category=['Messaging']
+++

<a href="http://incubator.apache.org/thrift/">Thrift</a> is a Facebook released open source project for cross language serialisation and RPC communication.

We made use of it for our message definition layer - when it comes to messaging I'm a fan of the event based approach so we left the <a href="http://www.25hoursaday.com/weblog/2008/07/10/TheRevengeOfRPCGoogleProtocolBuffersAndFacebookThrift.aspx">RPC stuff</a> well alone.

<h3>Why Thrift?</h3>

The reason we used Thrift in the first place was because we had a requirement to get interoperability between a Java and .NET application across a message bus and it provided an easy way to do this.

Google's <a href="http://code.google.com/p/protobuf/">protocol buffers</a> offers an alternative solution in this area. I don't think there is much difference between the two approaches - we just happened to come across Thrift first and it seemed to solve our problems so we went with it.

<h3>How it works</h3>

The idea behind it is that you can create Thrift definition files with the elements that you want to include in your message. You then <a href="http://wiki.apache.org/thrift/ThriftInstallationWin32">run a compiler</a> which generates code for Data Transfer Objects (DTO) in Java, C#, Ruby and various other languages.

<h3>Issues we came across</h3>
There were a few issues that we came across when using Thrift. They are not really Thrift specific but would always be the case when taking this approach to message definition:

<h4>Data Mapping</h4>
We wanted to have rich message objects in our code. This meant that we had to write a mapping layer which translated the Thrift DTO messages into our richer objects. This eventually ended up taking up quite a bit of our time - it once took 90 minutes to create the Thrift message, compile the Java/C# DTOs and write the mappers.

<h4>Versioning</h4>
The perennial problem of versioning was still something of an issue although several areas had been addressed.

Each property on a message had a corresponding boolean flag which determined whether or not that property has been set (i.e. whether it had a value). This meant that in theory it was possible to remove a property from the message definition cleanly, although it was still up to the client to check these flags each time they handled a message. 

Using this mechanism would place the responsibility on the client to deal with potential problems - if the flags were ignored then things would break.

Re-ordering of properties was also interesting. In theory as long as the types of the properties are the same then it is possible. For example, if you had:


~~~text

struct FooBarMessageThrift {
1: string Foo
2: string Bar
}
~~~

And you changed it to:


~~~text

struct FooBarMessageThrift {
1: string Bar
2: string Foo
}
~~~

It would still work although you would end up with one client writing in to Foo and the other picking up the value of Bar for Foo. The reading and writing of the messages across the wire completely depends on the order in which they are specified in the thrift file.

If we try and reorder elements with different types even the above is not possible and we end up with corrupt data:


~~~text

struct FooBarMessageThrift {
1: i32 Foo
2: string Bar
}
~~~


~~~text

struct FooBarMessageThrift {
1: string Bar
2: i32 Foo
}
~~~

As you might imagine this can quickly get very confusing so we decided that the way forward was to not re-order and rather than remove a property, simply not assign a value to it if it is no longer in use.

After analysing the potential problems in these areas, a colleague came up with an interesting idea that when versioning messages we should treat it like an API - add but never remove.

There are certainly uses for Thrift and Google Protocol Buffers in the world of messaging but as with everything there are trade offs that we need to be aware of.

Thanks to <a href="http://markthomas.info/blog/">Mark Thomas</a> for working with me to write this.
