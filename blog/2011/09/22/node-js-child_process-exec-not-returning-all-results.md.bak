+++
draft = false
date="2011-09-22 19:55:45"
title="node.js: child_process.exec not returning all results"
tag=['javascript', 'node-js']
category=['Javascript']
+++

I've been playing around with some node.js code to get each of the commits from our git repository but noticed that it didn't seem to be returning me all the results.

I had the following code:


~~~javascript

var exec = require('child_process').exec;

var gitRepository = '/some/local/path';

exec('cd ' + gitRepository + ' && git log --pretty=format:"%H | %ad | %s%d" --date=raw ', function(error, stdout, stderror) {
  var commits = stdout.split("\n");

  // do some stuff with commits
});
~~~

We have around 2000 commits in the repository but I was only getting back 1600 of them when I checked the <cite>length</cite> of <cite>commits</cite>.

Eventually I decided to print out what was in <cite>error</cite> and got the following message:


~~~text

error: Error: maxBuffer exceeded.
~~~

Going back to <a href="http://nodejs.org/docs/v0.4.8/api/all.html#child_process.exec">the documentation</a> revealed my mistake:

<blockquote>
maxBuffer specifies the largest amount of data allowed on stdout or stderr - if this value is exceeded then the child process is killed.

The default options are

{ encoding: 'utf8',
  timeout: 0,
  maxBuffer: 200*1024,
  killSignal: 'SIGTERM',
  cwd: null,
  env: null }

</blockquote>

The limit is 2048000 which is around about the number of bytes being returned when I get to 1600 commits. 

Changing the code to increase the buffer sorts it out: 


~~~javascript

var exec = require('child_process').exec;

var gitRepository = '/some/local/path';

exec('cd ' + gitRepository + ' && git log --pretty=format:"%H | %ad | %s%d" --date=raw ', {maxBuffer: 500*1024}, function(error, stdout, stderror) {
  var commits = stdout.split("\n");

  // do some stuff with commits
});
~~~
