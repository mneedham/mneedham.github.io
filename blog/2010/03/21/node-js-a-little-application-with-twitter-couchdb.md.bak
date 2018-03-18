+++
draft = false
date="2010-03-21 22:13:27"
title="node.js: A little application with Twitter & CouchDB"
tag=['javascript', 'node-js']
category=['Javascript']
+++

I've been continuing to play around with <a href="http://nodejs.org/api.html">node.js</a> and I thought it would be interesting to write a little application to poll Twitter every minute and save any new Tweets into a <a href="http://wiki.apache.org/couchdb/">CouchDB</a> database.

I first played around with CouchDB in May last year and initially spent a lot of time trying to work out how to install it before coming across <a href="http://janl.github.com/couchdbx/">CouchDBX</a> which gives you one click installation for Mac OS X.

I'm using sixtus' <a href="http://github.com/sixtus/node-couch">node-couch</a> library to communicate with CouchDB and I've written a little bit of code that allows me to call the Twitter API.

<h4>What did I learn?</h4>

<ul>
<li>I've been reading through Brian Guthrie's slides from his '<a href="http://www.slideshare.net/btguthrie/advanced-ruby-idioms-so-clean-you-can-eat-off-of-them">Advanced Ruby Idioms So Clean You Can Eat Off Of Them</a>' talk from <a href="http://rubyconfindia.org/">RubyConfIndia</a> and one of the suggestions he makes is that in Ruby there are only 6 acceptable types of signatures for functions:

<ul>
<li>0 parameters</li>
<li>1 parameter</li> 
<li>2 parameters </li>
<li>A hash</li>
<li>1 parameter and a hash</li>
<li>A variable number of arguments passed in as an array</li>
</ul>
It seems to me that the same guidelines would be applicable in JavaScript as well except <strong>instead of a Hash we can pass in an object with properties and values to serve the same purpose</strong>. A lot of the jQuery libraries I've used actually do this anyway so it's an idiom that's in both languages.

I originally wrote my twitter function it so that it would take in several of the arguments individually:


~~~javascript

export.query = function(username, password, method) { ... }
~~~

After reading Brian's slides I realised that this was quickly going to become a mess so I've changed the signature to only take in the most important parameter ('method') on its own with the other parameters passed in an 'options' object:


~~~javascript

export.query = function(method, options) { ... }
~~~

I've not written functions that take in parameters like this before but I really like it so far. It <strong>really helps simplify signatures</strong> while allowing you to pass in extra values if necessary.

</li>
<li><strong>I find myself porting higher order functions from C#/F# into JavaScript</strong> whenever I can't find a function to do what I want - it's fun writing them but I'm not sure how idiomatic the code I'm writing is.

For example I wanted to write a function to take query parameters out of an options object and create a query string out of them. I adapted the code from node-couch and ended up with the following:


~~~javascript

Object.prototype.filter = function(fn) {
    var result = {};
    for (var name in this) {
        if (this.hasOwnProperty(name)) {
            if (fn.call(this[name], name, this[name])) {
                result[name] = this[name];
            }
        }
    }
    return result;
};

Object.prototype.into = function(theArray, fn) {
    for (var name in this) {
        if (this.hasOwnProperty(name)) {
            theArray.push(fn.call(this[name], name, this[name]));
        }
    }
    return theArray;
};

function encodeOptions(options) {
    var parameters = [];
    if (typeof(options) === "object" && options !== null) {
        parameters = options
                        .filter(function(name) {
                            return !(name === "username" || name === "password" || name === "callback");})
                        .into([], function(name, value) {
                            return encodeURIComponent(name) + "=" + encodeURIComponent(value); });
    }
    return parameters.length ? ("?" + parameters.join("&")) : "";
}
~~~

I'm not sure how wise it is adding these functions to the object prototype - I haven't had any problems so far but I guess if other libraries I'm using changed the prototype of these built in types in the same way as I am then I might get unexpected behaviour. 

Would the typical way to defend against this be to check if a function is defined before trying to define one and throwing an exception if so? Or is adding to the prototype just a dangerous thing to do altogether?

Either way I'm not altogether convinced that the code with these higher order functions actually reads better than it would without them.
</li>
<li>I'm finding it quite interesting that a lot of the code I write around node.js depends on callbacks which means that if you have 3 operations that depend on each other then you end up with nested callbacks which almost reads like code written in a <a href="http://www.markhneedham.com/blog/2010/03/19/functional-c-continuation-passing-style/">continuation passing style</a>.

For example I have some code which needs to do the following:

<ul>
<li>Query CouchDB to get the ID of the most recently saved tweet</li>
<li>Query Twitter with that ID to get any tweets since that one</li>
<li>Save those tweets to CouchDB</li>
</ul>


~~~javascript

var server = http.createServer(function (req, res) {
    couchDB.view("application/sort-by-id", {
        descending : true,
        success : function(response) {
            twitter.query("friends_timeline", {
                ...
                since_id : response.rows[0].value.id,
                callback : function(tweets) {
                    tweets.each(function(tweet) {
                        couchDB.saveDoc(tweet, {
                            success : function(doc) {
                                sys.log("Document " + doc._id + " successfully saved")
                            },
                            error : function() {
                                sys.log("Document failed to save");
                            }
                        });
                    }); 

                }
            });
        },
        error : function() {
            sys.log("Failed to retrieve documents");
        }
    });

    ...
});
~~~

There's a 'success' callback for calling 'couchDB.view' and then a 'callback' callback for calling 'twitter.query' and finally a 'success' callback from calling 'couchDB.saveDoc'. 

To me it's not that obvious what the code is doing at first glance - perhaps because I'm not that used to this style of programming - but I'm intrigued if there's a way to write the code to make it more readable.
</li>
<li>I haven't yet worked out a good way to test drive code in a node.js module. As I understand it all the functions we define except for ones added to the 'exports' object are private to the module so there's no way to test against that code directly unless you pull it out into another module.

At the moment I'm just changing the code and then restarting the server and checking if it's working or not. It's probably not the most effective feedback cycle but it's working reasonably well so far.
</ul>

I've put the code that I've written so far as gists on github:

<ul>
<li><a href="http://gist.github.com/339579">twitter-server.js</a></li>
<li><a href="http://gist.github.com/339583">twitter.js</a></li>
<li><a href="http://gist.github.com/339591">encoding.js</a></li>
</ul>

That can be run with the following command from the terminal:


~~~text

node twitter-server.js
~~~


