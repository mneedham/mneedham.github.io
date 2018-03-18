+++
draft = false
date="2013-06-15 09:53:15"
title="neo4j/cypher/Lucene: Dealing with special characters"
tag=['neo4j', 'lucene', 'cypher']
category=['neo4j']
+++

<p>neo4j uses <a href="http://lucene.apache.org/core/">Lucene</a> to handle indexing of nodes and relationships in the graph but something that can be a bit confusing at first is how to handle special characters in Lucene queries.</p>


<p>For example let's say we set up a database with the following data:</p>



~~~cypher

CREATE ({name: "-one"})
CREATE ({name: "-two"})
CREATE ({name: "-three"})
CREATE ({name: "four"})
~~~

<p>And for whatever reason we only wanted to return the nodes that begin with a hyphen.</p>


<p>A hyphen is a special character in Lucene so if we forget to escape it we'll end up with an impressive stack trace:</p>



~~~cypher

START p = node:node_auto_index("name:-*") RETURN p;
~~~


~~~text

==> RuntimeException: org.apache.lucene.queryParser.ParseException: Cannot parse 'name:-*': Encountered " "-" "- "" at line 1, column 5.
==> Was expecting one of:
==>     <BAREOPER> ...
==>     "(" ...
==>     "*" ...
==>     <QUOTED> ...
==>     <TERM> ...
==>     <PREFIXTERM> ...
==>     <WILDTERM> ...
==>     "[" ...
==>     "{" ...
==>     <NUMBER> ...
==>
~~~

<p>So we change our query to escape the hyphen:</p>



~~~cypher

START p = node:node_auto_index("name:\-*") RETURN p;
~~~

<p>which results in the following exception:</p>



~~~text

==> SyntaxException: invalid escape sequence
==> 
==> Think we should have better error message here? Help us by sending this query to cypher@neo4j.org.
==> 
==> Thank you, the Neo4j Team.
==> 
==> "START p = node:node_auto_index("name:\-*") RETURN p"
==>
~~~

<p>The problem is that the cypher parser also treats '\' as an escape character so we need to use two of them to make our query do what we want:</p>



~~~cypher

START p = node:node_auto_index("name:\\-*") RETURN p;
~~~


~~~text

==> +------------------------+
==> | p                      |
==> +------------------------+
==> | Node[4]{name:"-one"}   |
==> | Node[5]{name:"-two"}   |
==> | Node[6]{name:"-three"} |
==> +------------------------+
==> 3 rows
~~~

<p>Alternatively, as <a href="https://twitter.com/cleishm">Chris</a> pointed out, we could make use of parameters in which case we don't need to worry about how the cypher parser handles escaping:</p>



~~~ruby

require 'neography'

neo = Neography::Rest.new
query = "START p = node:node_auto_index({query}) RETURN p"
result = neo.execute_query(query, { :query => 'name:\-*'})

p result["data"].map { |x| x[0]["data"] }
~~~


~~~text

$ bundle exec ruby params.rb
[{"name"=>"-one"}, {"name"=>"-two"}, {"name"=>"-three"}]
~~~
