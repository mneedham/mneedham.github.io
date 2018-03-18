+++
draft = false
date="2009-06-12 17:35:51"
title="Coding: Single Level of Abstraction Principle"
tag=['coding', 'slap']
category=['Coding']
+++

One of the other useful principles for writing readable code that I've come across in the last year or so is the Single Level of Abstraction Principle.

I first came across the idea of writing code at the same level of abstraction in <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Uncle Bob's Clean Code</a> although I only learnt about the actual term in <a href="http://www.markhneedham.com/blog/2008/09/05/the-productive-programmer-book-review/">Neal Ford's The Productive Programmer</a>.

As the name suggests the idea is that within a certain method we look to keep all the code at the same level of abstraction to help us read it more easily.  It needs to be consistent with stuff around it otherwise it's really confusing as our brain tried to make the mental shift between thinking about higher level concepts and low level implementation details in the code.

While trying to understand the code which I wrote about in a <a href="http://www.markhneedham.com/blog/2009/06/11/coding-keep-methodvariable-names-positive/">previous post about keeping method names positive</a> we decided to extract each of the validation rules so that we could see in English what was going on.


~~~csharp

private bool ValidPolicyNumber(string policyNumber) 
{
	var hasExpectedPrefix = policyNumber.Substring(0,5) == "POLIC";
	var followedBy7Digits = Regex.IsMatch(policyNumber.Substring(6,7), "^[0-9]{7}$");
	var hasLengthOf12 = policyNumber.Length == 12;

	return hasExpectedPrefix && followedBy7Digits && hasLengthOf12;
}
~~~

Although there's more code in that second example I think it makes it more clear what's going on and if we're interested in the how then we can just read the assignments to each of the variables.

After we'd done this refactoring I suggested that perhaps we could inline the 'hasLengthOf12' variable since it didn't seem to be adding value as all it's doing is abstracting away the fact that we're calling the 'Length' properly on string to check the length.

The code would then read like this:


~~~csharp

private bool ValidPolicyNumber(string policyNumber) 
{
	var hasExpectedPrefix = policyNumber.Substring(0,5) == "POLIC";
	var followedBy7Digits = Regex.IsMatch(policyNumber.Substring(6,7), "^[0-9]{7}$");

	return hasExpectedPrefix && followedBy7Digits && policyNumber.Length == 12;
}
~~~

<a href="http://twitter.com/davcamer">Dave</a> rightly pointed out that if we were to do this then we would be mixing code which said <strong>what</strong> made a valid policy with code that determined <strong>how</strong> we did this therefore violating the Single Level of Abstraction Principle.

The whole point of doing this for me is that we can keep less context in our head about the code and we can just read through the code and quickly understand what's going on.

An added benefit is that from my experience it helps to bring out subtle errors that we may have looked over when there was a mixture of levels of abstraction in the code.

I know this is a fairly simple example but it helped me to understand a bit more clearly what it actually means to code to this principle.

* Update *

As Dan points out in the comments the 'followedBy7Digits' variable could never be true. I had the example wrong so I've change it to how it was meant to be.
