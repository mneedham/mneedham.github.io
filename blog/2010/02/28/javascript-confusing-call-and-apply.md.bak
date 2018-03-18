+++
draft = false
date="2010-02-28 01:45:49"
title="Javascript: Confusing 'call' and 'apply'"
tag=['javascript']
category=['Javascript']
+++

I wrote a couple of weeks ago about <a href="http://www.markhneedham.com/blog/2010/02/12/javascript-passing-functions-around-with-call-and-apply/">using the 'call' and 'apply' functions in Javascript when passing functions around</a> and while working on <a href="http://www.markhneedham.com/blog/2010/02/28/javascript-isolating-browser-specific-code/">our IE6 specific code</a> I realised that I'd got them mixed up. 

We were writing some code to override one of our functions so that we could call the original function and then do something else after that.

The code was roughly like this:


~~~javascript

Foo = {
    bar : function(duck) {
      console.log("bar " + duck.quack());  
    }
};
~~~

The code that I originally wrote to capture the original function, call it and then do the additional behaviour was like this:


~~~javascript

(function() {
  var originalBar = Foo.bar;

   Foo.bar = function(duck) {
        originalBar.call(this, arguments);
        console.log("new bar");
   };
})();
~~~

When we call the function:


~~~javascript

Foo.bar({ quack : function() { return "quacking" } });
~~~

We get the following error:


~~~text

TypeError: duck.quack is not a function
~~~

'arguments' is a local variable in any Javascript function which contains all the arguments passed to the function stored in an array type structure.

However, I had forgotten that when using the 'call' function we need to pass the full list of parameters individually rather than as an array so in this case we would need to pass 'duck' in specifically:


~~~javascript

(function() {
  var originalBar = Foo.bar;

   Foo.bar = function(duck) {
        originalBar.call(this, duck);
        console.log("new bar");
   };
})();
~~~

Now when we run the function we get the expected behaviour:


~~~javascript

Foo.bar({ quack : function() { return "quacking" } });
~~~


~~~text

bar quacking
new bar
~~~

This is where apply comes in handy because apply allows us to pass in 'arguments' as the second parameter and it will send all the arguments of the function that we're inside to the function that we're calling which is exactly what we want in this case.

Using 'apply' we would end up with the following code:


~~~javascript

(function() {
  var originalBar = Foo.bar;

   Foo.bar = function(duck) {
        originalBar.apply(this, arguments);
        console.log("new bar");
   };
})();
~~~

In this case the function only takes in one argument so there's not much noticeable improvement in the code but when a function takes multiple arguments then using 'apply' is certainly a cleaner approach.
