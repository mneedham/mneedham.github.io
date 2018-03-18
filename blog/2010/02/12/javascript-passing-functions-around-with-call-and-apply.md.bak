+++
draft = false
date="2010-02-12 20:18:02"
title="Javascript: Passing functions around with call and apply"
tag=['javascript']
category=['Javascript']
+++

Having read Douglas Crockford's '<a href="http://www.amazon.com/gp/product/0596517742?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0596517742">Javascript: The Good Parts</a>' I was already aware that making use of the 'this' keyword in Javascript is quite dangerous but we came across what must be a fairly common situation this week where we wanted to pass around a function which made use of 'this' internally.

We were writing some <a href="http://code.google.com/p/js-test-driver/">JSTestDriver</a> tests around a piece of code which looked roughly like this:


~~~javascript

function Common() {
	this.OtherMethod = function(value) {
		// do some manipulation on value
		return someMagicalNewValue;	
	};

	this.Method = function(value) {
		return this.OtherMethod(value);	
	};

};
~~~

In the test we were originally making the following call:


~~~javascript

TestCase("Common", {
    testShouldDoSomeStuff:function(){
		var common = new Common();
		var result = common.Method("some value");
		assertEquals("some value", result);
    }
};
~~~

After writing a couple of tests it became clear that we were pretty much repeating the same few lines of code over and over so we decided to pull out a function:


~~~javascript

function ShouldAssertThatValueIs(f, value, expectedValue) {
    var result = f(value);
    assertEquals(expectedValue, result);
}
~~~


~~~javascript

TestCase("Common", {
    testShouldDoSomeStuff:function(){
		var common = new Common();
		ShouldAssertThatValueIs(common.Method, "some value", "expected value");
    }
};
~~~

When we run that code we get the following error:


~~~javascript

TypeError: this.OtherMethod is not a function
~~~

The scope of 'this' has changed so that 'this' now refers to the 'ShouldAssertThatValueIs' function which doesn't have a 'SomeMethod' defined on it and hence we get the error.

Luckily we can make use of the <a href="http://odetocode.com/Blogs/scott/archive/2007/07/05/function-apply-and-function-call-in-javascript.aspx">call or apply functions</a> to get around this problem and redefine what we want the scope of 'this' to be.

With both 'call' and 'apply' we call either of those methods and pass in the object which we want to be referred to as 'this' as the first argument.

We can then then pass in any other parameters to call on our function as an array in the case of 'apply' or just as a list of arguments for 'call'. 

K Scott Allen covers this in more detail in <a href="http://odetocode.com/Blogs/scott/archive/2007/07/05/function-apply-and-function-call-in-javascript.aspx">his post</a>.

Making use of the 'call' function our assertion function would now look like this:


~~~javascript

function ShouldAssertThatValueIs(common, f, value, expectedValue) {
    var result = f.call(common, value);
    assertEquals(expectedValue, result);
}
~~~


~~~javascript

TestCase("Common", {
    testShouldDoSomeStuff:function(){
		var common = new Common();
		ShouldAssertThatValueIs(common, common.Method, "some value", "expected value");
		ShouldAssertThatValueIs(common, common.Method, "some value", "expected value");
    }
};
~~~

In this case it probably makes more sense to use 'call' since we only have one parameter to pass to the function. If we had an array of values then we could pass that in using 'apply'.

Looking at the test code at the end of the post as compared to the beginning I'm not too convinced that we've actually improved it with this refactoring although it did provide an interesting Javascript lesson for us!

I'm still very much learning Javascript so if I have anything wrong please feel free to point it out or if there's a better way to do what I've described, even better!
