+++
draft = false
date="2010-03-22 23:42:02"
title="Defensive Programming and the UI"
tag=['defensive-programming']
category=['Software Development']
+++

A few weeks ago I was looking at quite an interesting bug in our system which initially didn't seem possible.

On one of our screens we have some questions that the user fills in which read a bit like this:

<ul>
<li>Do you have a foo?
<ul>
<li>Is your foo an approved foo?</li>
<li>Is your foo special?</li>
</ul>
</li>
</ul>

i.e. you would only see the 2nd and 3rd questions on the screen if you answered yes to the first question.

However, if you went to the next page on the form having answered 'Yes' to the first question and then came back to this page and changed your answer to the first question to 'No' then when the data got submitted to the server the answers to the other two questions would still be posted.

We were therefore ending up with a request with the following values submitted:


~~~text

hasFoo		"No"
approvedFoo 	"Yes"
specialFoo	"Yes"
~~~

Later on in the application we had some logic which decided what to do with the user request and this one was erroneously being approved because we hadn't catered for the condition where the first question was answered 'No' and the other questions had 'Yes' values.

In theory we should have written some client side code to reset the optional questions if the first one was answered 'No' but even then it's still possible to post whatever data you want to the server if you try hard enough.

Given that we need to behave in a somewhat defensive way somewhere on the server.

My initial thinking was that perhaps we should change the logic to handle this scenario but talking through the problem with <a href="http://mikewagg.blogspot.com/">Mike</a> he pointed out that it would make more sense to fix the data earlier in the chain.

I ended up writing some code in the controller to change the latter two fields to 'No' if the answer to the first question was 'No'. We're not really using custom binders on the project otherwise I think it would be the type of logic that would go in there.

Overall I'm no really a fan of defensive programming in general because it often seems to lead to over complicated code but in the case of user input it does make sense and the general guideline seems to be to <strong>fix any logically invalid values as close to the entry point of our application as possible</strong>.
