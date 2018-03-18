+++
draft = false
date="2012-07-23 22:23:10"
title="neo4j: Graph Global vs Graph Local queries"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

A few weeks ago I did a presentation at the ThoughtWorks EU away day on the graph I've been developing using neo4j and I wanted to show who the most connected people in each of our European offices were.

I started with the following cypher query:


~~~text

START n = node(*)
 
MATCH n-[r:colleagues*1..2]->c, n-[r2:member_of]->office 

WHERE n.type? = 'person'
AND (NOT(HAS(r2.end_date))) 
AND office.name = 'London - UK South' 
AND (NOT(HAS(c.thoughtquitter)))

RETURN n.name, count(distinct(c)) AS connections, office.name 

ORDER BY connections DESC
~~~

The intention is to find all the people who currently work in the London office and find their 1st and 2nd level connections i.e. people they have worked with or people who have worked with people they have worked with. 

That gives a rough idea of their reach in the organisation.

I also wanted to exclude anyone who had left, hence the 'thoughtquitter' check.

When I ran this query it took about 15 minutes to complete which immediately made me realise I was doing something wrong although I wasn't sure exactly what.

I showed the query to Michael Hunger and <a href="https://gist.github.com/2983831">he pointed out</a> that it's a graph global query i.e. it probably touches most of the nodes on the graph even though it doesn't necessarily need to.

Michael suggested restructuring the query to start from the London office and work out from there:


~~~text

START office=node:offices(name='London - UK South')

MATCH office<-[r2:member_of]-n-[r:colleagues*1..2]->c 

WHERE n.type? = 'person' 
AND (NOT(HAS(r2.end_date))) 
AND (NOT(HAS(c.thoughtquitter)))

RETURN n.name, count(distinct(c)) AS connections, office.name 

ORDER BY connections DESC
~~~

Now we are starting at the London office and finding all the people who have been members of it at some stage. We go and find their level 2 colleagues and then do the same filters that we had in the first query.

The query time went down to around 45 seconds, presumably because the number of nodes on the graph that we touch has gone down substantially.

The lesson for me from this is that when doing a graph traversal it makes much more sense to <strong>pick specific starting and/or finishing nodes rather than selecting all of them</strong>.
