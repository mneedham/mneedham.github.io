+++
draft = false
date="2010-03-28 20:02:10"
title="Reading Code: underscore.js"
tag=['reading-code']
category=['Reading Code']
+++

I've been spending a bit of time reading through the source code of <a href="http://documentcloud.github.com/underscore">underscore.js</a>, a JavaScript library that provides lots of functional programming support which my colleague Dave Yeung pointed out to me after reading <a href="http://www.markhneedham.com/blog/2010/03/21/node-js-a-little-application-with-twitter-couchdb/">my post about building a small application with node.js</a>.

I'm still getting used to the way that JavaScript libraries are written but these were some of the interesting things that I got from reading the code:

<ul>
<li>There are a couple of places in the code where the author has some <strong>code which runs conditionally and this is achieved by including that expression on the right hand side of an '&&'</strong>.

For example on line 129 in the 'filter' function:


~~~javascript

  // Return all the elements that pass a truth test.
  // Delegates to JavaScript 1.6's native filter if available.
  _.filter = function(obj, iterator, context) {
    if (nativeFilter && obj.filter === nativeFilter) return obj.filter(iterator, context);
    var results = [];
    each(obj, function(value, index, list) {
      iterator.call(context, value, index, list) && results.push(value);
    });
    return results;
  };
~~~

I would probably have used an if statement to check the result from calling 'iterator' but this way is more concise and pretty neat.

The same type of thing is done on line 150 in the 'every' function:


~~~javascript

  _.every = function(obj, iterator, context) {
    iterator = iterator || _.identity;
    if (nativeEvery && obj.every === nativeEvery) return obj.every(iterator, context);
    var result = true;
    each(obj, function(value, index, list) {
      if (!(result = result && iterator.call(context, value, index, list))) _.breakLoop();
    });
    return result;
  };
~~~

The result is collected and the loop will also exit if the value of 'result' is ever false which is again a cool way to organise code.
</li>
<li>
It's also quite cool that you can <strong>assign a value to a variable from within a conditional</strong> - this isn't possible in any of the other languages that I've used previously as far as I'm aware.

It's even more evident in the 'max' function:


~~~javascript

  _.max = function(obj, iterator, context) {
    if (!iterator && _.isArray(obj)) return Math.max.apply(Math, obj);
    var result = {computed : -Infinity};
    each(obj, function(value, index, list) {
      var computed = iterator ? iterator.call(context, value, index, list) : value;
      computed >= result.computed && (result = {value : value, computed : computed});
    });
    return result.value;
  };
~~~

'result' is conditionally assigned on line 196 but only if the computed value is greater than the current computed value. Again an if statement is avoided.

Another interesting thing about this function is that it specifically checks the type of the 'obj' passed in which reminded me about the <a href="http://blog.obiefernandez.com/content/2009/04/my-reasoned-response-about-scala-at-twitter.html">discussion around Twitter having those sorts of checks in their Ruby code around a year ago</a>. I guess that type of thing would be more prevalent in library code than in an application though.
</li>
<li>I hadn't come across the <strong>!! construct</strong> which is used to turn a JavaScript expression into its boolean equivalent:


~~~javascript

  _.isArray = nativeIsArray || function(obj) {
    return !!(obj && obj.concat && obj.unshift && !obj.callee);
  };
~~~

Without using '!!" the expression would return 'undefined' in the case that one of those functions on 'obj' was not set. '!!' forces the return value to be 'false'.
</li>
<li>Another technique used in this code base is that of <strong>dynamically adding methods to the prototype of an object</strong>:


~~~javascript

  // Add all mutator Array functions to the wrapper.
  each(['pop', 'push', 'reverse', 'shift', 'sort', 'splice', 'unshift'], function(name) {
    var method = ArrayProto[name];
    wrapper.prototype[name] = function() {
      method.apply(this._wrapped, arguments);
      return result(this._wrapped, this._chain);
    };
  });
~~~

This is quite a cool use of meta programming although it isn't initially obvious how those functions end up on the object unless you know what to look for. It does significantly reduce the code needed to add these functions to the 'wrapper' object's prototype, avoiding the '<a href="http://www.ibm.com/developerworks/java/library/j-eaed9/index.html">same whitespace, different values</a>' problem that Neal Ford outlines in his article about harvesting idiomatic patterns in our code.
</li>
</ul>
