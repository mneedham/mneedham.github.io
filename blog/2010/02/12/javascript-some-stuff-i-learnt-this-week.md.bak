+++
draft = false
date="2010-02-12 21:11:54"
title="Javascript: Some stuff I learnt this week"
tag=['javascript']
category=['Javascript']
+++

I already wrote about how I've learnt a bit about the 'call' and 'apply' functions in Javascript this week but as I've spent the majority of my time doing front end stuff this week I've also learnt and noticed some other things which I thought were quite interesting.

<h3>Finding character codes</h3>
We were doing some testing early in the week where we needed to restrict the characters that could be entered into a text box.

As a result we needed to know the character codes for the banned characters. While googling to work them out we came across <a href="http://jdstiles.com/java/cct.html">Uncle Jim's CharCode Translator</a> which allows you to type in a character and get its character code and vice versa.

I guess you could easily just call the Javascript functions in FireBug but it's a nice little utility to save the effort.

<h3>Duck typing makes some testing much easier</h3>
Related to that we needed to be able to pass in an event object to a function which only made use of the 'charCode' method.

In a statically language we would have needed to create an event object which had all the properties that an event object needs. In Javascript we could just create the following...


~~~javascript

var event = { eventCode : 57 };
~~~ 

...and then pass that into the function and check that the result was as expected.

I haven't done a lot with languages which support duck typing so this is pretty cool to me and I imagine we'd probably see the same advantages of duck typing when testing in language like Ruby, Python and so on.

<h3>Compressing Javascript files</h3>
One of the requirements for my project is that we need to compress all the javascript files used in our application to allow them to be downloaded more quickly by the user.

On a previous project that I worked on we made use of some Javascript minifying code written by Douglas Crockford but on this one we're making use of the <a href="http://combres.codeplex.com/">Combres</a> library which does all this work for us and compresses CSS files as well.

I haven't done a lot with it but so far it seems to work pretty well.

<h3>Command query separation</h3>
I find it quite intriguing how difficult we've sometimes found it to unit test Javascript on some of the projects I've worked on without ending up with really complicated tests and it seems to me that perhaps the biggest reason for this is that we're often writing functions which violate the idea of command query separation principle.

The idea here is that a function should either be a command i.e. it has some side effect which means DOM manipulation in Javascript code usually or it should be a query i.e. it returns a value probably based on the input.

Typically we might end up writing a function which validates an input in a text box and tells us whether or not it's valid, but then also sets up the display of the error message in the same function.

I don't think this would happen as frequently in Java or C# so perhaps it's down to the fact that it's so easy to reference a global variable (i.e. jQuery) that we end up doing so in our code.

It seems like if we could separate these two types of logic then it would be easier to test the query type code in unit tests and we could rely more on Selenium or manual tests to check that the page is being manipulated correctly.
