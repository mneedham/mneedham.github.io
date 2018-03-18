+++
draft = false
date="2011-02-27 20:10:50"
title="Ruby: Refactoring from hash to object"
tag=['ruby']
category=['Ruby', 'Incremental Refactoring']
+++

Something I've noticed when I play around with Ruby in my own time is that I nearly always end up with the situation where I'm passing hashes all over my code and to start with it's not a big deal.

Unfortunately I eventually get to the stage where I'm effectively modelling an object inside a hash and it all gets very difficult to understand.

I've written a few times before about <a href="http://www.markhneedham.com/blog/category/coding/incremental-refactoring/">incrementally refactoring</a> code so this seemed like a pretty good chance for me to try that out.

The code in the view looked something like this:


~~~html

<% @tweets.each do |tweet| %>
  <%= tweet[:key] %>  <%= tweet[:value][:something_else] %>
<% end %>
~~~

<cite>@tweets</cite> was being populated directly from a call to CouchDB so to start with I needed to change it from being a collection of hashes to a collection of objects:

I changed the Sinatra calling code from: 


~~~ruby

get '/' do
  @tweets = get_the_couchdb_tweets_hash
end
~~~

to:


~~~ruby

get '/' do
  tweets_hash = get_the_couchdb_tweets_hash
  @tweets = tweets_hash.map { |tweet| TweetViewModel.new(tweet) }
end
~~~

where <cite>TweetViewModel</cite> is defined like so:


~~~ruby

class TweetViewModel
  attr_accessor :key, :value

  def initialize(tweet_hash)
    @key = tweet_hash[:key]
    @value = tweet_hash[:value]
  end

  def get(lookup)
    if lookup == :key
      key
    else
      value
    end
  end

  alias_method :[], :get
end
~~~

The next step was to get rid of the <cite>get</cite> method and rename those <cite>attr_accessor</cite> methods to something more intention revealing.


~~~ruby

class TweetViewModel
  attr_accessor :url, :messages

  def initialize(tweet_hash)
    @url = tweet_hash[:key]
    @messages = tweet_hash[:value]
  end
end
~~~


~~~html

<% @tweets.each do |tweet| %>
  <%= tweet.url %>  <%= tweet.messages[:something_else] %>
<% end %>
~~~

I originally didn't realise how easy it would be to make the <cite>TweetViewModel</cite> pretend to temporarily be a <cite>Hash</cite> but it actually made it really easy for me to change the code and know that it was working the whole way.

For someone with more Ruby experience perhaps it wouldn't be necessary to break out the refactoring like this because they could fairly confidently do it in one go.
