+++
draft = false
date="2009-08-15 10:53:49"
title="Builders hanging off class vs Builders in same namespace"
tag=['coding', 'communication']
category=['Coding', 'Communication']
+++

I wrote a couple of months ago about an approach we're using to help people find <a href="http://www.natpryce.com/articles/000714.html">test data builders</a> in our code base by <a href="http://www.markhneedham.com/blog/2009/06/02/coding-putting-code-where-people-can-find-it/">hanging those builders off a class called 'GetBuilderFor'</a> and I think it's worked reasonably well.

However, a couple of weeks ago my colleague <a href="http://luning12.blogbus.com/">Lu Ning</a> suggested another way to achieve our goal of allowing people to find the builders easily.

The approach he suggested is to put all of the builders in the same namespace, for example 'Builders', so that if someone wants to find out if a builder already exists they can just type 'Builders.' into the editor and then it will come up with a list of all the builders that exist.

The benefit of this approach is that it means we can make use of the <a href="http://www.markhneedham.com/blog/2009/02/16/c-object-initializer-and-the-horse-shoe/">object initializer</a> to setup test data  - perhaps one of the few occasions when it seems to be reasonably useful.

Lu Ning <a href="http://luning12.blogbus.com/logs/36477752.html">explains in more detail on his blog</a> but the idea is that instead of:


~~~csharp

new FooBuilder().Bar("hello").Build();
~~~

We could do this:


~~~csharp

new FooBuilder { Bar = "hello" }.Build();
~~~

The second approach requires less code since we can just create all public fields and setup a default value for each of them in the class definition and then override the values later if we want to as shown above.

We can't do this with the 'GetBuilderFor' approach since you can only make use of object initializer when you are initialising an object (as the name might suggest!).

Another advantage of this approach is that we don't have to write the boiler plate code to add each builder onto the 'GetBuilderFor' class so that others can find it.

The disadvantage is that once we type 'Builders.' to find the list of builders we then need to delete that text and type in 'new FooBuilder()...' which means the flow of creating test data isn't as smooth as with the 'GetBuilderFor' approach.

I don't feel like there is a really big difference between these approaches and as long as people can find code that's the main thing.

There would probably be less typing required with the namespace approach although I've never really felt that typing is the bottleneck in software development projects so it would be interesting to see if this would give us a gain or not.

We are still using the 'GetBuilderFor' approach on our project since there probably wouldn't be a massive gain by switching to the other approach at this stage.

It does seem like an interesting alternative to solving the same problem though.
