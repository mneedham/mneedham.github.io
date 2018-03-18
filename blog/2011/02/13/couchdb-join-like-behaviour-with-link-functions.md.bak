+++
draft = false
date="2011-02-13 17:58:54"
title="CouchDB: Join like behaviour with link functions"
tag=['couchdb']
category=['CouchDB']
+++

I've been playing around with the <a href="http://apiwiki.twitter.com/w/page/22554673/Streaming-API-Documentation">Twitter streaming API</a> a bit lately to see which links are being posted most frequently by the people I follow and then storing the appropriate tweets in CouchDB.

I recently came across a problem which I struggled to solve for quite a while.

Based on the following map function:



~~~javascript

{
  "_id" : "_design/query",
  "views" : {
    "by_link" : {
      "map" : "function(doc){ emit(doc.actual_link, { user : doc.user.screen_name, text : doc.text })}"
    }
  }
}
~~~


Which results in the following data set:


~~~text

curl http://127.0.0.1:5984/twitter_links/_design/query/_view/by_link?limit=20
~~~


~~~text

{"total_rows":7035,"offset":0,"rows":[
{"id":"abf54db1d92bfe0e8aaaa9ec51f237bd","key":"http://2dboy.com/2011/02/08/ipad-launch/","value":{"user":"Nash","text":"World of Goo\u2019s iPad Launch http://instapaper.com/zzqrqw32e"}},
{"id":"b8911545ff45438671081260ae0d42b1","key":"http://3.bp.blogspot.com/_T6MpHfZv2qQ/SpKGGjsoQoI/AAAAAAAADIA/Jsa5JDqX9X0/s400/moleskine3.jpg","value":{"user":"oinonio","text":"@stephenfry a Babushka Little My? http://bit.ly/fjPg2a"}},
{"id":"be12d30d1c8b882d8ce0124585fabb19","key":"http://3.bp.blogspot.com/_UAzEooLfuI8/S7aOiCBdAzI/AAAAAAAAF8Y/5W61I9VHxPE/s1600-h/deforestation.jpg","value":{"user":"ironshay","text":"A big problem caused by deforestation http://bit.ly/9qArCg"}}
]}
~~~

What I want to do is go from...

<ul>
<li>Link Url 1 -> Tweet 1</li>
<li>Link Url 1 -> Tweet 2</li>
<li>Link Url 2 -> Tweet 3</li>
</ul>

...to...

<ul>
<li>Link Url 1 -> [Tweet 1, Tweet 2]</li>
<li>Link Url 2 -> [Tweet3]</li>
</ul>

I originally tried to use a reduce function after following <a href="http://chrischandler.name/couchdb/view-collation-for-join-like-behavior-in-couchdb/">Chris Chandler's blog post</a> but that resulted in a 'reduce_overflow_error'.

<a href="http://twitter.com/perrynfowler/status/36372745549774848">Perryn</a> pointed out that what I probably needed was a link function and I came across <a href="http://japhr.blogspot.com/2010/02/collating-not-reducing-with-couchdb.html">Chris Strom's blog</a> while trying to work out how to do that.


~~~javascript

{
  "_id" : "_design/query",
  "views" : {
    "by_link" : {
      "map" : "function(doc){ emit(doc.actual_link, { user : doc.user.screen_name, text : doc.text })}"
    }
  },
  "lists" : {
    "index_tweets" : "function(head, req) {
     var row, last_key, tweets;
     send('{\"rows\" : [');
     while(row = getRow()) {
      if(last_key != row.key ) {
        if(last_key != 'undefined') {
          send(toJSON({key : last_key, values : tweets}));
          send(',');
        }
        tweets = [];
        last_key = row.key;
      } 
      tweets.push(row.value);
     }
     send(toJSON({key : last_key, values : tweets}));
     send(']}');
  }"
  }
}
~~~

We then call the list function with an associated view function following this pattern from <a href="http://dev.twitter.com/pages/streaming_api">CouchDB: The Definitive Guide</a>:

<blockquote>
/db/_design/foo/_list/list-name/view-name
</blockquote>


~~~text

curl http://127.0.0.1:5984/twitter_links/_design/query/_list/index_tweets/by_link
~~~

Which gives the data in the required format:


~~~text

{"rows" : [
{"key":"http://1.bp.blogspot.com/_XdP6Lp2ceqY/TU16NvdT-RI/AAAAAAAAlb8/7QtTN-XxBTM/s400/dcrHk.jpg","values":[{"user":"jhartikainen","text":"RT @codepo8: The dark secret of PacMan: http://bit.ly/exCBDy"}, {"user":"joedevon","text":"RT @codepo8: The dark secret of PacMan: http://bit.ly/exCBDy"}]},
{"key":"http://10poundpom.blogspot.com/","values":[{"user":"10poundpomCL","text":"@andy_murray Help my #£10aWeekCharityChallenge, all it takes is a RT. Read http://10poundpom.blogspot.com/ for more."}]},
{"key":"http://10rem.net/blog/2011/02/09/enhancing-the-wpf-screen-capture-program-with-window-borders","values":[{"user":"brian_henderson","text":"Enhancing the WPF Screen Capture Program with Window Borders: by @Pete_Brown: http://bit.ly/icmXG5 #wpf #win32"},{"user":"SittenSpynne","text":"RT @Pete_Brown: Blogged: Enhancing the WPF Screen Capture Program with Window Borders http://bit.ly/icmXG5 #wpf #win32"}]}]}
~~~

Maybe there's an even better way to solve this problem that I don't know about...let me know if there is!
