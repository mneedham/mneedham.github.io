+++
draft = false
date="2014-02-26 07:32:14"
title="Java 8: Lambda Expressions vs Auto Closeable"
tag=['java']
category=['Java']
+++

<p>If you used earlier versions of Neo4j via its Java API with Java 6 you probably have code similar to the following to ensure write operations happen within a transaction:</p>



~~~java

public class StylesOfTx
{
    public static void main( String[] args ) throws IOException
    {
        String path = "/tmp/tx-style-test";
        FileUtils.deleteRecursively(new File(path));

        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( path );

        Transaction tx = db.beginTx();
        try 
        {
            db.createNode();
            tx.success();
        } 
        finally 
        {
            tx.close();
        }
    }
}
~~~

<p>In Neo4j 2.0 Transaction started extending <a href="http://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html">AutoCloseable</a> which meant that you could use 'try with resources' and the 'close' method would be automatically called when the block finished:</p>



~~~java

public class StylesOfTx
{
    public static void main( String[] args ) throws IOException
    {
        String path = "/tmp/tx-style-test";
        FileUtils.deleteRecursively(new File(path));

        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( path );

        try ( Transaction tx = db.beginTx() )
        {
            Node node = db.createNode();
            tx.success();
        }
    }
}
~~~

<p>This works quite well although it's still possible to have transactions hanging around in an application when people don't use this syntax - the old style is still permissible.</p>


<p>In <a href="http://pragprog.com/book/vsjava8/functional-programming-in-java">Venkat Subramaniam's Java 8 book</a> he suggests an alternative approach where we use a lambda based approach:</p>



~~~java

public class StylesOfTx
{
    public static void main( String[] args ) throws IOException
    {
        String path = "/tmp/tx-style-test";
        FileUtils.deleteRecursively(new File(path));

        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( path );

        Db.withinTransaction(db, neo4jDb -> {
            Node node = neo4jDb.createNode();
        });
    }

    static class Db {
        public static void withinTransaction(GraphDatabaseService db, Consumer<GraphDatabaseService> fn) {
            try ( Transaction tx = db.beginTx() )
            {
                fn.accept(db);
                tx.success();
            }
        }
    }
}
~~~

<p>The 'withinTransaction' function would actually go on GraphDatabaseService or similar rather than being on that Db class but it was easier to put it on there for this example.</p>


<p>A disadvantage of this style is that you don't have explicit control over the transaction for handling the failure case - it's assumed that if 'tx.success()' isn't called then the transaction failed and it's rolled back. I'm not sure what % of use cases actually need such fine grained control though.</p>


<p>Brian Hurt refers to this as the '<a href="http://www.markhneedham.com/blog/2009/04/04/functional-c-the-hole-in-the-middle-pattern/">hole in the middle pattern</a>' and I imagine we'll start seeing more code of this ilk once Java 8 is released and becomes more widely used.</p>

