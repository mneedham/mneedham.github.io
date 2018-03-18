+++
draft = false
date="2008-12-15 23:52:17"
title="C#'s Lambda ForEach: Only on Lists?"
tag=['c', 'lambda', 'foreach', 'functional']
category=['.NET']
+++

One of my favourite things introduced into C# recently is the new <a href="http://blog.jemm.net/2008/01/16/c-comparing-ways-to-iterate-lists-in-c-and-some-lambda-expression-examples/">ForEach</a> method which can be applied to (apparently only!) lists. 

Last week we had a situation where we wanted to make use of the ForEach method on an IDictionary which we were using to store a collection of <a href="http://seleniumhq.org/">Selenium</a> clients.


~~~csharp

IDictionary<string, ISelenium> seleniumClients = new Dictionary<string, ISelenium>();
~~~

We wanted to write a piece of code to exit all of the clients when our tests had completed. We thought the following would do the trick:


~~~csharp

seleniumClients.Values.ForEach(client => client.Stop());
~~~

The problem is that code doesn't actually compile! 

'seleniumClients.Values' returns an ICollection which extends IEnumerable so we thought ForEach should be available. 

We eventually got around the problem by putting the collection into a list and then applying the ForEach method but it seems like there should be a better way to do this.


~~~csharp

new List<ISelenium>(seleniumClients.Values).ForEach(client => client.Stop());
~~~

Is there?
