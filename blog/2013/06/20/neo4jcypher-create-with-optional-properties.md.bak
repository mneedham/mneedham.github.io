+++
draft = false
date="2013-06-20 06:31:11"
title="neo4j/cypher: CREATE with optional properties"
tag=['neo4j']
category=['neo4j']
+++

<p>I've written before about using the <a href="http://docs.neo4j.org/chunked/milestone/query-create.html">cypher CREATE statement</a> to <a href="http://www.markhneedham.com/blog/2013/05/25/neo4jcypher-properties-or-relationships-its-easy-to-switch/">add inferred information to a neo4j graph</a> and sometimes we want to do that but have to deal with optional properties while creating our new relationships.</p>


<p>For example let's say we have the following people in our graph with the 'started' and 'left' properties representing their tenure at a company:</p>



~~~cypher

CREATE (person1 { personId: 1, started: 1361708546 })
CREATE (person2 { personId: 2, started: 1361708546, left: 1371708646 })
CREATE (company { companyId: 1 })
~~~

<p>We want to create a 'TENURE' link from them to the company including the 'started' and 'left' properties when applicable and might start with the following query:</p>



~~~cypher

START person = node:node_auto_index('personId:1 personId:2'), 
      company = node:node_auto_index('companyId:1') 
CREATE person-[:TENURE_AT { started: person.started, left: person.left }]-company 
RETURN person, company
~~~

<p>which throws an exception because not all people have a 'left' property:</p>



~~~text

Error: org.neo4j.cypher.EntityNotFoundException: The property 'left' does not exist on Node[1]
~~~

<p>We tweak our query a bit to make the property optional:</p>



~~~cypher

START person = node:node_auto_index('personId:1 personId:2'), 
      company = node:node_auto_index('companyId:1') 
CREATE person-[:TENURE_AT { started: person.started, left: person.left? }]-company 
RETURN person, company
~~~

<p>which still doesn't work:</p>



~~~text

Error: java.lang.IllegalArgumentException: Null parameter, key=left, value=null
~~~

<p>After looking at this for a while <a href="https://twitter.com/apcj">Alistair</a> pointed out that we should just split the updating of the optional property from the creation of the relationship so we end up with the following:</p>



~~~cypher

START person = node:node_auto_index('personId:1 personId:2'), 
      company = node:node_auto_index('companyId:1') 
CREATE person-[tenure:TENURE_AT { started: person.started }]-company 
WITH person, tenure, company
WHERE HAS(person.left)
SET tenure.left = person.left 
RETURN person, company
~~~

<p>The <a href="http://console.neo4j.org/?id=gdbpuv">code is on the console</a> if you want to see how it works.</p>

