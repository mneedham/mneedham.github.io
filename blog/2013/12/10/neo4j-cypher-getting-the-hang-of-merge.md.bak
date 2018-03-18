+++
draft = false
date="2013-12-10 23:46:46"
title="Neo4j: Cypher - Getting the hang of MERGE"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>I've been trying to get the hang of cypher's <a href="http://docs.neo4j.org/chunked/milestone/query-merge.html">MERGE function</a> and started out by writing a small file to import some people with random properties using the <a href="https://github.com/DiUS/java-faker">java-faker</a> library.</p>



~~~java

public class Merge {
    private static Label PERSON = DynamicLabel.label("Person");

    public static void main(String[] args) throws IOException {
        File dbFile = new File("/tmp/test-db");
        FileUtils.deleteRecursively(dbFile);

        Faker faker = new Faker();
        Random random = new Random();
        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase(dbFile.getPath());

        Transaction tx = db.beginTx();

        for (int i = 0; i < 100000; i++) {
            Node person = db.createNode(PERSON);

            person.setProperty("name", faker.name());
            person.setProperty("firstName", faker.firstName());
            person.setProperty("lastName", faker.lastName());
            person.setProperty("country", faker.country());
            person.setProperty("age", random.nextInt(50));
        }

        tx.success();
        tx.close();
    }
}
~~~

<p>We can write the following query to get back a sample of the people that have been imported:</p>



~~~cypher

$ MATCH (p:Person) RETURN p LIMIT 5;
==> +------------------------------------------------------------------------------------------------------------------+
==> | p                                                                                                                |
==> +------------------------------------------------------------------------------------------------------------------+
==> | Node[1344]{name:"Benton Swaniawski",firstName:"Rossie",lastName:"Ankunding",country:"Guadeloupe",age:30}         |
==> | Node[1345]{name:"Dagmar Bartell",firstName:"Ashlynn",lastName:"Watsica",country:"French Guiana",age:35}          |
==> | Node[1346]{name:"Ms. Missouri Gaylord",firstName:"Muriel",lastName:"Streich",country:"Chile",age:43}             |
==> | Node[1347]{name:"Melvina Heathcote",firstName:"Geovanni",lastName:"Marks",country:"United Arab Emirates",age:33} |
==> | Node[1348]{name:"Brendan Schaefer",firstName:"Dayne",lastName:"Haley",country:"Tokelau",age:24}                  |
==> +------------------------------------------------------------------------------------------------------------------+
~~~

<p>We can use the MERGE function to ensure that a node with specific properties exists so we might write something like the following:</p>



~~~cypher

MERGE (p:Person {name: "Benton Swaniawski",
                 firstName:"Rossie",
                 lastName:"Ankunding", 
                 country:"Guadeloupe",
                 age:30})
RETURN p
~~~

<p>If we have a look at the <cite>PROFILE</cite> output of the query we'd see something like the following:</p>



~~~bash

UpdateGraph(commands=["
	MergeNodeAction(
		p,
		Map(firstName(1) -> Literal(Rossie), country(3) -> Literal(Guadeloupe), 
		name(0) -> Literal(Benton Swaniawski), 
		lastName(2) -> Literal(Ankunding), 
		age(4) -> Literal(30)),
		List(Person(0)),
		ArrayBuffer(Property(p,lastName(2)) == Literal(Ankunding), 
		Property(p,name(0)) == Literal(Benton Swaniawski), 
		Property(p,age(4)) == Literal(30), 
		Property(p,country(3)) == Literal(Guadeloupe),
		Property(p,firstName(1)) == Literal(Rossie)),
		List(LabelAction(p,LabelSetOp,List(Person(0))), 
		PropertySetAction(Property(p,name),Literal(Benton Swaniawski)), 
		PropertySetAction(Property(p,country),Literal(Guadeloupe)), 
		PropertySetAction(Property(p,age),Literal(30)), 
		PropertySetAction(Property(p,lastName),Literal(Ankunding)), 
		PropertySetAction(Property(p,firstName),
		Literal(Rossie))),
		List(),
		Some(PlainMergeNodeProducer(<function2>)))"], _rows=1, _db_hits=100219)
~~~

<p>The bit that stands out is that there were 100,219 db_hits which slows down the query considerably.</p>
 

<p>If we want to use <cite>MERGE</cite> then we need to make sure that we have an index or constraint on one of the properties e.g.</p>



~~~bash

$ CREATE INDEX ON :Person(name);
==> +-------------------+
==> | No data returned. |
==> +-------------------+
==> Indexes added: 1
~~~

<p>If we look at the profile of that we'll see that the number of db_hits has reduced as it's now using the index to do part of the lookup that the MERGE requires:</p>



~~~bash

UpdateGraph(commands=["
	MergeNodeAction(
		p,
		Map(firstName(1) -> Literal(Rossie), country(3) -> Literal(Guadeloupe), 
		name(0) -> Literal(Benton Swaniawski), 
		... 
		Some(PlainMergeNodeProducer(<function2>)))"], _rows=1, _db_hits=4)
~~~

<p>We can go one step further by only including the property that's acting as our 'key' (i.e. name) in the first part of the statement and setting the other properties only if necessary:</p>



~~~cypher

MERGE (p:Person {name: "Benton Swaniawski"})
ON CREATE SET p.firstName="Rossie", 
              p.lastName="Ankunding", 
              p.country="Guadeloupe",
              p.age=30
RETURN p
~~~

<p>If we profile that query we can see that things have improved:</p>



~~~bash

 UpdateGraph(commands=["MergeNodeAction(
	p,
	Map(name(0) -> Literal(Benton Swaniawski)),
	List(Person(0)),ArrayBuffer(),
	List(LabelAction(p,LabelSetOp,List(Person(0))), 
	PropertySetAction(Property(p,name),Literal(Benton Swaniawski)), 
	PropertySetAction(Property(p,firstName),Literal(Rossie)), 
	PropertySetAction(Property(p,lastName),Literal(Ankunding)), 
	PropertySetAction(Property(p,country),Literal(Guadeloupe)), 
	PropertySetAction(Property(p,age),Literal(30))),
	List(),
	Some(PlainMergeNodeProducer(<function2>)))"], _rows=1, _db_hits=0)
~~~

<p>In some cases we might want to update a property every time that 'key' gets matched in a MERGE statement which we could do like so:</p>



~~~cypher

MERGE (p:Person {name: "Benton Swaniawski"})
ON MATCH SET p.times = COALESCE(p.times, 0) + 1
RETURN p
~~~

<p>You can also use <cite>MERGE</cite> to <a href="http://docs.neo4j.org/chunked/milestone/query-merge.html#merge-merge-on-a-relationship">create relationships</a> but for now I just wanted to explore how it should be used in the context of nodes which I think I've now figured out.</p>
 

<p>Always happy to take tips on how to do things better though!</p>

