+++
draft = false
date="2010-03-10 23:06:31"
title="Javascript: Function scoping"
tag=['javascript']
category=['Javascript']
+++

My colleague John Hume wrote <a href="http://elhumidor.blogspot.com/2010/03/actionscript-const-gotcha.html">an interesting post about his experience with the 'const' keyword in ActionScript</a> where he describes the problems with trying to capture a loop variable in a closure and then evaluating it later on in the code.

Since ActionScript and JavaScript are both dialects of <a href="http://en.wikipedia.org/wiki/ECMAScript">ECMAscript</a>, this is a problem in JavaScript as well, and is due to the fact that variables in JavaScript have <a href="http://www.slideshare.net/douglascrockford/crockford-on-javascript-act-iii-function-the-ultimate">function scope rather than block scope</a> which is the case in many other languages.

This problem would tend to reveal itself in code where we try to capture a loop variable in an anonymous function and use it later on, like so:


~~~javascript

function getValues() {
    var x = new Array();
    for(var i=0; i < 10; i++) {
       x[i] = function() { return i; }
    }
    return x;
};

var values = getValues();
for(var j=0; j < values.length; j++) {
    console.log(values[j]());
}
~~~

We might expect that to print the sequence of numbers 0-9 on the screen but what we actually get is '10' printed 10 times.

There are a couple of things that I initially found strange about this:

<ol>
<li>Why doesn't it print out the numbers 0-9?</li>
<li>Given that it doesn't do that why does it print out '10' 10 times instead of '9' 10 times?</li>
</ol>

The answer to the first question is that 'i' gets assigned a new value on each iteration of the loop and we don't evaluate 'i' until we evaluate the anonymous function on line 11.

The value when we do evaluate it would be the last value that it was set to by the loop which in this case that would be '10' because that's the value that 'i' has to be <a href="http://twitter.com/jason_diamond/statuses/10283944438">in order for</a> <a href="http://twitter.com/drunkcod/statuses/10283979588">the loop to terminate</a>.

This is <a href="http://twitter.com/davcamer/statuses/10290979811">actually a problem in C# as well</a> - the following code will output '10' 10 times as well:


~~~csharp

[Test]
public void ClosureOnTheSameValue()
{
    var values = new List<Func<int>>();
    for(int i=0; i < 10; i++)
    {
        values.Add(() => i);
    }

    foreach (var value in values)
    {
        Console.WriteLine(value());
    }
}
~~~

Again we capture 'i' inside a closure and since we only evaluate that value when it's actually used it will always refer to the last value that 'i' was set to which in this case means that it will always output a value of 10.

To fix this in C# we could just create a temporary variable - something which Resharper will actually suggest to us:


~~~csharp

[Test]
public void ClosureOnDifferentValue()
{
    var values = new List<Func<int>>();
    for(int i=0; i < 10; i++)
    {
        var idash = i;
        values.Add(() => idash);
    }

    foreach (var value in values)
    {
        Console.WriteLine(value());
    }
}
~~~

This works in C# because variables have block scope which means that we have a new version of 'idash' for each of the functions that we add to the 'values' collection.

Sadly the same trick doesn't work in JavaScript because variables have function scope in Javascript:


~~~javascript

function getValues() {
    var x = new Array();
    for(var i=0; i < 10; i++) {
       var idash = i;
       x[i] = function() { return idash; }
    }
    return x;
};

var values = getValues();
for(var j=0; j < values.length; j++) {
    console.log(values[j]());
}
~~~

The 'idash' temporary variable that we created to try and solve the problem gets assigned a new value in each iteration of the loop because that variable is only declared once for the whole function. 

The code above could be written like this to make that clearer:


~~~javascript

function getValues() {
    var x = new Array();
    var idash;

    for(var i=0; i < 10; i++) {
       idash = i;
       x[i] = function() { return idash; }
    }
    return x;
};

var values = getValues();
for(var j=0; j < values.length; j++) {
    console.log(values[j]());
}
~~~

As John points out:

<blockquote>
Here's something I either never knew or at some point forgot about JavaScript: variables are lexically scoped, but only function bodies introduce new lexical scopes. 
</blockquote>

In this case we actually end up printing '9' 10 times because that's the maximum value that gets assigned to 'idash'.

One solution is to create a temporary variable inside an anonymous function that we execute immediately, like this:


~~~javascript

function getValues() {
    var x = new Array();
    for(var i=0; i < 10; i++) {
        (function() {
            var idash = i;
            x[i] = function() { return idash; } })();
    }
    return x;
};

var values = getValues();
for(var j=0; j < values.length; j++) {
    console.log(values[j]());
}
~~~

Now 'idash' is scoped inside the anonymous function and we therefore end up with a new value each time like we want.

<a href="http://twitter.com/raphscallion/statuses/10288673700">Raph</a> pointed out that we could achieve the same thing in a simpler way with the following code:


~~~javascript

function getValues() {
    var x = new Array();
    for(var i=0; i < 10; i++) (function(i) {
        x[i] = function() { return i; };
    })(i);
    return x;
};

var values = getValues();
for(var j=0; j < values.length; j++) {
    console.log(values[j]());
}
~~~

Here we define a for loop with just a single statement so we can lose the '{}' and just call an anonymous function passing in 'i'.

Of course this example is truly contrived but I wanted to pick something simple enough that I could try and follow exactly how it worked.

I'm not entirely sure of the terminology around closures and scoping so if I've described anything incorrectly then please correct me!
