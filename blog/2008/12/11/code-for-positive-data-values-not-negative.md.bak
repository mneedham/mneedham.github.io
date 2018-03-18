+++
draft = false
date="2008-12-11 06:48:42"
title="Code for positive data values not negative"
tag=['coding']
category=['Coding']
+++

While reading Pat Kua's latest post about how <a href="http://www.thekua.com/atwork/2008/12/coding-styles-leads-to-or-prevents-certain-classes-of-bugs/">coding a certain way can help you avoid certain classes of bugs</a> I was reminded of a technique taught to me by a colleague with regards to writing functions/methods.

The idea is that it is more effective to <strong>code for positive data values rather than trying to work out all the possible negative combinations</strong>, since there are likely to be cases which we hadn't considered if we do the latter.

For example, given the following method outline:


~~~java

public void someMethod(int someValue) {
		
}	
~~~

We might know that this method should only be allowed to take in non zero values. Therefore it makes more sense to code for this knowledge than to infer which values are not allowed.

The following code snippet...


~~~java

public void someMethod(int someValue) {
	if(someValue != 0) {
		// throw exception
	}		
	// someOtherMethod();
}
~~~

...would therefore be preferable to this code snippet...


~~~java

public void someMethod(int someValue) {
	if(someValue < 0) {
		// throw exception
	}		
	// someOtherMethod();
}
~~~

...since in the latter we are making the assumption that less than 0 is invalid whereas the actual requirement was for non 0 values to be invalid.

I know this is a highly contrived example but in theory this approach should prevent unexpected behaviour in our functions.

I have been following this approach since I was shown it and my first thoughts are that it leads to code which is <strong>more expressive and easier to write</strong> since we are working with what we know rather than trying to infer what we don't know.

I think that following a test driven approach would eventually lead to us writing code similar to this anyway, but it's an interesting idea to keep in mind.
