+++
draft = false
date="2009-06-11 07:44:41"
title="Coding: Keep method/variable names positive"
tag=['coding']
category=['Coding']
+++

Something which I've come across a few times recently in code is method names which describe the negative aspect of something and for me at least these are very difficult to understand since I need to keep remembering that we are dealing with the negative and not the positive which I think is significantly easier to reason about.

A recent example of this which I came across was in some acceptance test code which among other things was asserting whether or not the policy number that had been created was in a valid format and returning the result of that assertion back to our Fitnesse fixture.

The code to do this was similar to this - we are using the '<a href="http://dannorth.net/introducing-bdd">Given, When, Then</a>' syntax for acceptance testing and this code came under the 'Then' section:


~~~csharp

public bool ThenCustomerShouldSeePageWithPurchasedPolicy()
{
	...
	var policyNumber = GetPolicyNumber();
	if(InvalidPolicyNumber(policyNumber))
	{
		return false;
	}
	...
}
~~~


~~~csharp

private bool InvalidPolicyNumber(string policyNumber) 
{
	string integerPattern = "^[0-9]{7}$";
	return policyNumber.Substring(0,5) != "POLIC" && !Regex.IsMatch(policyNumber.Substring(6,7), integerPattern)  && policyNumber.Length != 12
}
~~~

Originally the lines of code in 'InvalidPolicyNumber' were actually inlined in the 'ThenCustomerShouldSeePageWithPurchasedPolicy' method but we pulled them out to try and understand the code more easily.

I still found it quite difficult to reason about what made an invalid policy since the reasoning of what makes something invalid from reading this code is:

<ul>
<li>The first 5 characters are not 'POLIC'</li>
<li>The next 7 characters are not digits</li>
<li>The total length is not 12</li>
</ul>

The actual rule for a valid policy number are:

<ul>
<li>It should start with the characters 'POLIC'</li>
<li>The next 7 characters should be digits</li>
<li>The total length should be 12</li>
</ul>

So in fact our 'InvalidPolicyNumber' method as well as being quite difficult to read will only tell us that a policy number is invalid if all 3 of those conditions have not been met when in actual fact if any of them are not met the policy number is invalid. A perhaps subtle error has crept in!

We refactored the code to <a href="http://www.markhneedham.com/blog/2008/12/11/code-for-positive-data-values-not-negative/">refer to what we know is valid</a> rather than looking at the reverse which I think is much more difficult to reason about.


~~~csharp

public bool ThenCustomerShouldSeePageWithPurchasedPolicy()
{
	...
	var policyNumber = GetPolicyNumber();
	if(!ValidPolicyNumber(policyNumber))
	{
		return false;
	}
	...
}
~~~


~~~csharp

private bool ValidPolicyNumber(string policyNumber) 
{
	string integerPattern = "^[0-9]{7}$";
	return policyNumber.Substring(0,5) == "POLIC" && Regex.IsMatch(policyNumber.Substring(6,7), integerPattern)  && policyNumber.Length == 12
}
~~~

I've come across a few other examples and the underlying theme is that I find it much easier to reason about code which is written using positive method/variable names and then make use of language constructs if we need to invert that somewhere.

I find it takes me much longer to understand methods which refer to the negative and every time I come back to them in the future I have to reason through each line slowly to make sure I understand what's going on. 
