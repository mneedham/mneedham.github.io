+++
draft = false
date="2008-09-25 23:18:09"
title="Easily misused language features"
tag=['coding', 'software-development']
category=['Coding', 'Software Development']
+++

In the comments of my <a href="http://www.markhneedham.com/blog/2008/09/24/my-dislike-of-javas-static-import/">previous post about my bad experiences with Java's import static</a> my colleague <a href="http://www.lixo.org/">Carlos</a> and several others pointed out that it is actually a useful feature when used properly. 

The code base where I initially came across the feature misused it quite severely but it got me thinking about other language features I have come across which can add great value when used effectively but lead to horrific problems when misused.

Apart from import static some other features which I can see easy potential for misuse are:

<ul>
<li>
 C#'s <a href="http://www.dotnetjunkies.com/WebLog/richardslade/archive/2007/03/26/218656.aspx">automatic properties</a> which seem to make it even easier to expose object's internals than it already is but perhaps could be useful for something like Xml serialisation and deserialisation. </li>
<li>C#'s <a href="http://www.markhneedham.com/blog/2008/08/15/first-thoughts-on-using-var-in-c-30-with-resharper/">var keyword</a> which 
helps to remove unnecessary type information and can lead to shorter methods when used well but completely unreadable code when misused.
</li>
<li>
Ruby's  open classes which give great flexibility when working effectively with 3rd party libraries for example but can lead to <a href="http://avdi.org/devblog/2008/02/23/why-monkeypatching-is-destroying-ruby/">difficult debugging problems</a> if overused. The same probably also applies to C#'s <a href="http://msdn.microsoft.com/en-us/library/bb383977.aspx">extension methods</a>.
</li>
</ul>

I have no doubt there are other features in other languages and probably more in the languages I listed but those are some of the ones that stood out to me when I first saw them.

I like this quote from Nate in the comments about import static, referring to being able to being able to tell what the code is doing just from looking at it:

<blockquote>
The rule is simple (and somewhat subjective… if you aren't sure, just ask me what I prefer. :) ) — if it helps the code to communicate better (especially contextually!) then use it.
</blockquote>

Maybe a similar type of rule is applicable when using other language features as well and there is no feature that we should be using all the time - only if it makes our code easier to read and understand.
