+++
draft = false
date="2008-08-15 08:03:09"
title="First thoughts on using var in C# 3.0 with Resharper"
tag=['resharper', 'c', 'net', 'var']
category=['.NET']
+++

One of the first things I noticed when coming into the world of C# 3.0 was the use of the key word 'var' all over our code base.

I had read about it previously and was under the impression that its main use would be when writing code around LINQ or when creating anonymous types.

On getting <a href="http://www.jetbrains.com/resharper/">Resharper</a> to tidy up my code I noticed that just about every variable type declaration had been removed and replaced with var. Very confused I asked one of my colleague's what was going on. It turns out that this is intended and is now <a href="http://resharper.blogspot.com/2007/08/resharper-vs-c-30-implicitly-typed.html">Resharper's default</a>. I quickly found the option and turned it off.

Subsequent discussions have led me to believe that perhaps it is not such a bad thing. When I first saw the use of var I felt that the readability of the code was severely impacted, and I still think that this is the case if method bodies have a lot of code in.

Therefore using var in your code seems to encourage you to keep the methods short so that people can actually understand what's going on. This leads to much easier to understand and maintain code.

Of course the discipline to make this happen is still needed but in the way that the lack of static typing in Ruby encouraged the writing of unit tests (I am led to believe), hopefully the use of var will encourage short compact methods.

The <a href="http://resharper.blogspot.com/">Resharper blog</a> has a <a href="http://resharper.blogspot.com/2008/03/varification-using-implicitly-typed.html">post</a> explaining why they have decided to make var so prevalent in the code refactoring that Resharper does. Included amongst these is better naming of local variables.

Having reading <a href="http://www.xpteam.com/">Jeff Bay's</a> essay in <a href="http://www.pragprog.com/titles/twa/thoughtworks-anthology">The ThoughtWorks Anthology</a> about clean OO design I have become quite fanatical about the naming of variables. I like them to be as descriptive as possible so that I can immediately tell what an object is doing without having to look at the details. Shortcuts such as naming an instance of an Account object as 'acct' are pointless in my opinion and just serve to confuse people.

Any language feature that helps encourage the writing of clear variable names is therefore a very good thing.

<a href="http://www.25hoursaday.com/weblog/2008/05/21/C30ImplicitTypeDeclarationsToVarOrNotToVar.aspx">Dare Obasanjo</a> seems to dislike this new feature while <a href="http://flimflan.com/blog/ToVar.aspx">Joshua Flanaghan</a> is more of a fan so clearly the jury is still out.
