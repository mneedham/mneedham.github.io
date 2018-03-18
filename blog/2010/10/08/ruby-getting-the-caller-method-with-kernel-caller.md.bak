+++
draft = false
date="2010-10-08 13:19:56"
title="Ruby: Getting the caller method with Kernel.caller"
tag=['ruby']
category=['Ruby']
+++

One of the things I've been finding when debugging Cucumber specs is that due to the number of levels of indirection present in those examples it becomes quite difficult to work out exactly how certain pieces of code got called.

In one cuke we were trying to work out how 4 objects of the same type were ending up in the database when it seemed like there should only be two.

Having failed to figure it out just by reading the code we resorted to putting calls to <a href="http://ruby-doc.org/core/classes/Kernel.html#M005929">Kernel.caller</a> inside the <a href="http://github.com/thoughtbot/factory_girl">Factory Girl</a> setup code so we could see how we'd ended up at that code:


~~~ruby

p caller.inspect
~~~

It's not a perfect solution - since the scenarios we write get parsed by Cucumber it's hard to tell exactly which line the call stack started on - but it provided enough information for us to track down the steps which were calling the Factory Girl code in question.
