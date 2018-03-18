+++
draft = false
date="2013-06-15 13:04:53"
title="neo4j/cypher: Finding single hop paths"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>The neo4j docs have a few examples explaining how to to write <a href="http://docs.neo4j.org/chunked/snapshot/cypher-cookbook-path-tree.html#cookbook-return-partly-shared-path-ranges">cypher queries dealing with path ranges</a> but an interesting variation that I came across recently is where we want to find the individual hops in a path.</p>


<p>I thought <a href="http://en.wikipedia.org/wiki/List_of_Chelsea_F.C._managers">the managers that Chelsea have had</a> since Roman Abramovich took over would serve as a useful data set to show how this works.</p>


<p>So we create all the managers and a 'SUCCEEDED_BY' relationship between them as follows:</p>



~~~cypher

CREATE (ranieri {name: "Claudio Ranieri"})
CREATE (mourinho {name: "Jose Mourinho"})
CREATE (grant {name: "Avram Grant"})
CREATE (scolari {name: "Luiz Felipe Scolari"})
CREATE (wilkins {name: "Ray Wilkins"})
CREATE (hiddink {name: "Guus Hiddink"})
CREATE (ancelotti {name: "Carlo Ancelotti"})
CREATE (villasBoas {name: "Andre Villas Boas"})
CREATE (diMatteo {name: "Roberto Di Matteo"})
CREATE (benitez {name: "Rafael Benitez"})

CREATE (ranieri)-[:SUCCEEDED_BY]->(mourinho)
CREATE (mourinho)-[:SUCCEEDED_BY]->(grant)
CREATE (grant)-[:SUCCEEDED_BY]->(scolari)
CREATE (scolari)-[:SUCCEEDED_BY]->(wilkins)
CREATE (wilkins)-[:SUCCEEDED_BY]->(hiddink)
CREATE (hiddink)-[:SUCCEEDED_BY]->(ancelotti)
CREATE (ancelotti)-[:SUCCEEDED_BY]->(villasBoas)
CREATE (villasBoas)-[:SUCCEEDED_BY]->(diMatteo)
CREATE (diMatteo)-[:SUCCEEDED_BY]->(benitez)
CREATE (benitez)-[:SUCCEEDED_BY]->(mourinho)
~~~

<p>We want to write a query which will return the 'SUCCEEDED_BY' pairs starting from Claudio Ranieri and working down.</p>


<p>We might start out with this query which starts from Ranieri and goes all the way down the tree finding the next successor:</p>



~~~cypher

START m = node:node_auto_index(name="Claudio Ranieri") 
MATCH path = (m)-[rel:SUCCEEDED_BY*]->(successor) 
RETURN EXTRACT(n IN NODES(path): n.name)
~~~


~~~text

==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | EXTRACT(n IN NODES(path): n.name)                                                                                                                                                               |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | ["Claudio Ranieri","Jose Mourinho"]                                                                                                                                                             |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant"]                                                                                                                                               |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari"]                                                                                                                         |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins"]                                                                                                           |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink"]                                                                                            |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink","Carlo Ancelotti"]                                                                          |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink","Carlo Ancelotti","Andre Villas Boas"]                                                      |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink","Carlo Ancelotti","Andre Villas Boas","Roberto Di Matteo"]                                  |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink","Carlo Ancelotti","Andre Villas Boas","Roberto Di Matteo","Rafael Benitez"]                 |
==> | ["Claudio Ranieri","Jose Mourinho","Avram Grant","Luiz Felipe Scolari","Ray Wilkins","Guus Hiddink","Carlo Ancelotti","Andre Villas Boas","Roberto Di Matteo","Rafael Benitez","Jose Mourinho"] |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> 10 rows
~~~

<p>That gives us all the combinations but unfortunately it includes all the previous successors as well so it's not quite what we want.</p>


<p>We need to manipulate the query such that we have a list of all the managers and can then follow a single 'SUCCEEDED_BY' relationship to find their successor.</p>


<p>We could easily get that list of managers by following the 'SUCCEEDED_BY' relationship and getting the nodes on the other side but that would lead to Claudio Ranieri being excluded since he doesn't have an incoming relationship.</p>


<p>To keep Ranieri we can make use of the 0 length path like so:</p>



~~~cypher

START m = node:node_auto_index(name="Claudio Ranieri") 
MATCH path = (m)-[rel:SUCCEEDED_BY*0..]->(mm) 
RETURN mm
~~~


~~~text

==> +--------------------------------------+
==> | mm                                   |
==> +--------------------------------------+
==> | Node[8]{name:"Claudio Ranieri"}      |
==> | Node[9]{name:"Jose Mourinho"}        |
==> | Node[10]{name:"Avram Grant"}         |
==> | Node[11]{name:"Luiz Felipe Scolari"} |
==> | Node[12]{name:"Ray Wilkins"}         |
==> | Node[13]{name:"Guus Hiddink"}        |
==> | Node[14]{name:"Carlo Ancelotti"}     |
==> | Node[15]{name:"Andre Villas Boas"}   |
==> | Node[16]{name:"Roberto Di Matteo"}   |
==> | Node[17]{name:"Rafael Benitez"}      |
==> | Node[9]{name:"Jose Mourinho"}        |
==> +--------------------------------------+
==> 11 rows
~~~

<p>If we now follow the 'SUCCEEDED_BY' relationship from our list of managers we end up with pairs of managers:</p>



~~~cypher

START m = node:node_auto_index(name="Claudio Ranieri")  
MATCH path = (m)-[rel:SUCCEEDED_BY*0..]->(mm)-[:SUCCEEDED_BY]->(successor)
RETURN DISTINCT mm.name, successor.name
~~~


~~~text

==> +-----------------------------------------------+
==> | mm.name               | successor.name        |
==> +-----------------------------------------------+
==> | "Claudio Ranieri"     | "Jose Mourinho"       |
==> | "Jose Mourinho"       | "Avram Grant"         |
==> | "Avram Grant"         | "Luiz Felipe Scolari" |
==> | "Luiz Felipe Scolari" | "Ray Wilkins"         |
==> | "Ray Wilkins"         | "Guus Hiddink"        |
==> | "Guus Hiddink"        | "Carlo Ancelotti"     |
==> | "Carlo Ancelotti"     | "Andre Villas Boas"   |
==> | "Andre Villas Boas"   | "Roberto Di Matteo"   |
==> | "Roberto Di Matteo"   | "Rafael Benitez"      |
==> | "Rafael Benitez"      | "Jose Mourinho"       |
==> +-----------------------------------------------+
==> 10 rows
~~~

<p>The code for this is available on the <a href="http://console.neo4j.org/?id=dzs5bn">neo4j console</a> if you're interested in playing with it further.</p>

