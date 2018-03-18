+++
draft = false
date="2013-05-31 00:37:57"
title="neo4j/cypher: 400 response - Paths can't be created inside of foreach"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>In the neo4j 1.9 milestone releases if we wanted to create multiple relationships from a node we could use the following cypher syntax:</p>



~~~ruby

require 'neography'

neo = Neography::Rest.new

neo.execute_query("create (me {name: 'Mark'})")

query =  " START n=node:node_auto_index(name={name})"
query << " FOREACH (friend in {friends} : CREATE f=friend, n-[:FRIEND]->f)"

neo.execute_query(query, {"name" => "Mark", 
                          "friends" => [{ "name" => "Will"}, {"name" => "Paul"}]})
~~~

<p>To check that the 'FRIEND' relationships have been created we'd write the following query:</p>



~~~cypher

START p = node:node_auto_index(name="Mark") 
MATCH p-[:FRIEND]-f 
RETURN f
~~~


~~~text

==> +----------------------+
==> | f                    |
==> +----------------------+
==> | Node[2]{name:"Will"} |
==> | Node[3]{name:"Paul"} |
==> +----------------------+
==> 2 rows
==> 37 ms
~~~

<p>In between the M04 and RC2 releases there was a change in the cypher parser which meant that this approach doesn't work anymore:</p>



~~~text

/Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/connection.rb:168:in `handle_4xx_500_response': 
Paths can't be created inside of foreach (Neography::SyntaxException)
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/connection.rb:143:in `return_result'
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/connection.rb:126:in `evaluate_response'
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/connection.rb:45:in `post'
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/rest/cypher.rb:19:in `query'
	from /Users/markhneedham/.rbenv/versions/1.9.3-p327/lib/ruby/gems/1.9.1/gems/neography-1.0.10/lib/neography/rest.rb:335:in `execute_query'
	from create.rb:12:in `<main>'
~~~

<p>Instead we can just use <cite><a href="http://docs.neo4j.org/chunked/stable/query-create.html#create-create-multiple-nodes-from-map">CREATE</a></cite> to achieve the same thing:</p>



~~~ruby

require 'neography'

neo = Neography::Rest.new

neo.execute_query("create (me {name: 'Mark'})")

query =  " START n = node:node_auto_index(name={name})"
query << " CREATE friend = {friends} "
query << " CREATE n-[:FRIEND]->friend"

neo.execute_query(query, {"name" => "Mark", 
                          "friends" => [{ "name" => "Will"}, { "name" => "Paul" }]})
~~~
