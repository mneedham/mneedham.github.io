+++
draft = false
date="2010-01-10 18:52:22"
title="C# Object Initializer: More thoughts"
tag=['c', 'object-initialiser']
category=['.NET']
+++

I wrote previously about <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">my dislike of C#'s object initializer syntax</a> and while I still think those arguments hold I came across an interesting argument for why it is a useful feature in <a href="http://msdn.microsoft.com/en-us/magazine/ee291514.aspx">Jeremy Miller's MSDN article on creating internal DSLs in C#</a>.

In the article Jeremy works through an example where he builds up a 'SendMessageRequest' first by using a fluent interface and then by making use of object initializer syntax.

The fluent interface example reads like this:


~~~csharp

public void SendMessageFluently(FluentMessageSender sender)
 {
     sender
         .SendText("the message body")
         .From("PARTNER001").To("PARTNER002");
 }
~~~

Compared with the object initializer version which looks like this:


~~~csharp

public void SendMessageAsParameter(ParameterObjectMessageSender sender)
 {
     sender.Send(new SendMessageRequest()
     {
         Text = "the message body",
         Receiver = "PARTNER001",
         Sender = "PARTNER002"
     });
 }
~~~

As Jeremy points out:

<blockquote>
this third incarnation of the API reduces errors in usage with much simpler mechanics than the fluent interface version.
</blockquote>

You need much less code to get the second version to work which my colleague Lu Ning pointed out to me when we were discussing <a href="http://www.markhneedham.com/blog/2009/08/15/builders-hanging-off-class-vs-builders-in-same-namespace/">how to use the builder pattern</a> on a project we worked on together.

In general terms the benefit of using object initializer is that we get more expressive code and the intent of that code is clearer than we would be able to achieve by constructing the object using its constructor.

The down side is that it creates a mentality of using setters and the initialisation of the object potentially leaves several fields with null values.

We then end up either getting unexpected null reference exceptions throughout the code or we code defensively and check for nulls whenever we try to access one of the properties. Seeing as one of the goals of the object initializer is to reduce the code we write it's somewhat ironic that we end up writing this extra code to ensure the object has been setup correctly.

One way to solve this is to make use of <a href="http://www.markhneedham.com/blog/2009/03/10/oo-micro-types/">tiny types</a> so that the API is still expressive even though what we want to pass in is a string. That takes more code but it allows us to make use of the constructor to construct the object which is something which seems to have lost favour.

C# 4.0 will introduced <a href="http://geekswithblogs.net/michelotti/archive/2009/01/22/c-4.0-named-parameters-for-better-code-quality.aspx">named parameters</a> into the language which seems like it will help us achieve expressiveness of our code without having to write extra classes and code to achieve this.


* Updated the examples as I had them the wrong way around. Thanks to Corey Haines and Mike Wagg for pointing it out.
