+++
draft = false
date="2011-09-11 22:37:15"
title="Learning node.js: Step"
tag=['javascript', 'node-js']
category=['Javascript']
+++

I've been playing around with node.js to generate some graphs from our git repository which effectively meant chaining together a bunch of shell commands to give me the repository data in the format I wanted.

I was able to do this by making use of <cite><a href="http://nodejs.org/docs/v0.4.8/api/all.html#child_process.exec">child_process</a></cite> which comes with the core library.

The first version looked like this:


~~~javascript

var exec = require('child_process').exec, _ = require("underscore");
...
function parseCommitsFromRepository(fn) {
  var gitRepository = "/tmp/core";
  var gitPlayArea = "/tmp/" + new Date().getTime();

  exec('cd ' + gitRepository + ' && git reset HEAD', function() {
    exec('git clone ' + gitRepository + ' ' + gitPlayArea, function() {
      exec('cd ' + gitPlayArea + ' && git log --pretty=format:"%H | %ad | %s%d" --date=raw', function(blank, gitEntries) {
        var commits = _(gitEntries.split("\n")).chain()
                        .filter(function(item) { return item != ""; })
                        .map(function(item) { return item.split("|") })
                        .filter(function(theSplit) { return theSplit !== undefined && theSplit[1] !== undefined && theSplit[2] !== undefined; })
                        .map(function(theSplit) {  
                          var date = new Date(theSplit[1].trim().split(" ")[0]*1000);
                          return {message: theSplit[2].trim(), date: date.toDateString(), time : date.toTimeString()}; })
                        .value();			
        fn(commits);
      });		
    });
  });
}
~~~

node.js has an asynchronous programming model so the majority of the time we have to pass callbacks to other functions which get called when the asynchronous computation has completed.

In this case there's an order dependency in the <cite>parseCommitsFromRepository</cite> function such that we need to nest the second call to <cite>exec</cite>  inside the callback from the first call.

i.e. we don't want to get the log of the repository before we've cloned the repository to the location that we're trying to get that log from.

As you create more and more order dependencies between asynchronous functions the nesting becomes greater and the code moves more and more to the right hand side of the screen.

I came across the <cite><a href="https://github.com/creationix/step">Step</a></cite> library which allows you to stack up functions and have the results from each one get passed on to the next.

I decided to try it in my code and it ended up looking like this:


~~~javascript

function parseCommitsFromRepository(fn) {	
  var gitRepository = "/tmp/core";
  var gitPlayArea = "/tmp/" + new Date().getTime();	
  Step(
    function getRepositoryUpToDate() { exec('cd ' + gitRepository + ' && git reset HEAD', this); },
    function cloneRepository()       { exec('git clone ' + gitRepository + ' ' + gitPlayArea, this); },
    function getGitEntries()         { exec('cd ' + gitPlayArea + ' && git log --pretty=format:"%H | %ad | %s%d" --date=raw', this); },
    function handleResponse(blank, gitEntries) {
      var commits = _(gitEntries.split("\n")).chain()
                      .filter(function(item) { return item != ""; })
                      .map(function(item) { return item.split("|") })
                      .filter(function(theSplit) { return theSplit !== undefined && theSplit[1] !== undefined && theSplit[2] !== undefined; })
                      .map(function(theSplit) {  
                        var date = new Date(theSplit[1].trim().split(" ")[0]*1000);
                        return {message: theSplit[2].trim(), date: date.toDateString(), time : date.toTimeString()}; })
                      .value();			
      fn(commits);
    }
  );	
}
~~~

An interesting side effect of using this approach is that we can describe what each <cite>exec</cite> call is doing in the name of the function that executes it.

Another neat thing about this library is that I can easily wrap those functions inside a logging function if I want to see on the console where the process has got up to:


~~~javascript

function log(message, fn) {
  return function logMe() {
    console.log(new Date().toString() + ": " + message);
     fn.apply(this, arguments);
  }
}
~~~


~~~javascript

function parseCommitsFromRepository(fn) {	
  var gitRepository = "/tmp/core";
  var gitPlayArea = "/tmp/" + new Date().getTime();	
  Step(
    log("Resetting repository", function getRepositoryUpToDate() { exec('cd ' + gitRepository + ' && git reset HEAD', this); }),
    log("Cloning repository", function cloneRepository()         { exec('git clone ' + gitRepository + ' ' + gitPlayArea, this); }),
    log("Getting log", function getGitEntries()                  { exec('cd ' + gitPlayArea + ' && git log --pretty=format:"%H | %ad | %s%d" --date=raw', this); }),
    log("Processing log", function handleResponse(blank, gitEntries) {
      var commits = _(gitEntries.split("\n")).chain()
                      .filter(function(item) { return item != ""; })
                      .map(function(item) { return item.split("|") })
                      .filter(function(theSplit) { return theSplit !== undefined && theSplit[1] !== undefined && theSplit[2] !== undefined; })
                      .map(function(theSplit) {  
                        var date = new Date(theSplit[1].trim().split(" ")[0]*1000);
                        return {message: theSplit[2].trim(), date: date.toDateString(), time : date.toTimeString()}; })
                      .value();			
      fn(commits);
    })
  );	
}
~~~

I then get this output when executing the function:


~~~text

Sun Sep 11 2011 23:33:09 GMT+0100 (BST): Resetting repository
Sun Sep 11 2011 23:33:11 GMT+0100 (BST): Cloning repository
Sun Sep 11 2011 23:33:24 GMT+0100 (BST): Getting log
Sun Sep 11 2011 23:33:24 GMT+0100 (BST): Processing log
~~~

There are more cool ways to use the Step library on the <a href="https://github.com/creationix/step">github page</a> - what I've described here is only a very simple use case.
