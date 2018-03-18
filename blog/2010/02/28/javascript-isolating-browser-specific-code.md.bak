+++
draft = false
date="2010-02-28 00:11:20"
title="Javascript: Isolating browser specific code"
tag=['javascript']
category=['Javascript']
+++

One thing we've found on my current project is that despite our best efforts we've still ended up with some javascript code which we only want to run if the user is using Internet Explorer 6 and the question then becomes how to write that code so that it doesn't end up being spread all over the application.

jQuery has some functions which allow you to work out which browser's being used but I've noticed that when we use those you tend to end up with if statements dotted all around the code which isn't so good. 

An approach which I was shown recently involves using <a href="http://www.quirksmode.org/css/condcom.html">CSS conditionals</a> to identify when we're using Internet Explorer instead.

We can then include an IE6 specific javascript file like so:


~~~text

<!--[if lt IE 7]>
	<script type="text/javascript" src="/path/to/ie6.js") %>"></script>
<![endif]-->    
~~~

Since we're building an ASP.NET MVC application we include this bit of code in our master page so that it gets picked up by all the web pages. 

We've either needed to override existing functions or call the existing function but then do some extra work afterwards as well. 

In order to do this we have to make sure that the IE6 specific file is included after our other javascript files since the interpreter will use the last definition of a function that it finds.

Given an existing function defined like so:


~~~javascript

Foo = {
    Bar : function() {
            console.log("original bar call");
    }
};
~~~

If we want to override this function to do something else we could include the following code in our IE6 specific file:


~~~javascript

Foo.bar = function() {
    console.log("overriding bar call");
}
~~~

When we call 'Foo.bar()' we'd only see the second 'console.log' statement.

It becomes a bit more interesting if we want to call the original function and then do some other functionality.

We can make use of the <a href="http://docs.jquery.com/Types#Proxy_Pattern">proxy pattern</a> to allow us to do this cleanly.


~~~javascript

Foo = {
    bar : function() {
            console.log("original bar call");
    }
};

(function() {
    var originalBar = Foo.bar;
    Foo.bar = function() {
        originalBar.apply(this, arguments);
        console.log("overriding bar call");
    };
})();
~~~

If we call 'Foo.bar()' in IE6 we'd now see both of those 'console.log' statements.

The reason that we wrap the reassignment in a function is so that we can hide the 'originalBar' function from the rest of our code. We save 'Foo.bar' in a closure and then override it and delegate calls to the original before logging the extra message.

I quite like this approach although I'm not sure if it's the most intention revealing code because it's not necessarily obvious that the function is being rewritten unless you happen to know about the IE6 only file.

Is there a better way to do this than the approach I've described?
