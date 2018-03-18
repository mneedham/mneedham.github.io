+++
draft = false
date="2013-03-17 18:56:36"
title="clojure/Java Interop - Importing neo4j spatial data"
tag=['java', 'clojure', 'neo4j']
category=['neo4j']
+++

<p>I wrote a post about a week ago where I described how I'd <a href="http://www.markhneedham.com/blog/2013/03/10/neo4jcypher-finding-football-stadiums-near-a-city-using-spatial/">added football stadiums to my football graph using neo4j spatial</a> and after I'd done that I wanted to put it into my import script along with the rest of the data.</p>


<p>I thought <a href="https://github.com/technomancy/leiningen">leiningen</a> would probably work quite well for this as you can point it at a Java class and have it be executed.</p>


<p>To start with I had to change the import code slightly to link stadiums to teams which have already been added to the graph:</p>



~~~java

package main.java;

// imports excluded

public class StadiumsImport {
    public static void main(String[] args) throws IOException {
        List<String> lines = readFile("data/stadiums.csv");

        EmbeddedGraphDatabase db = new EmbeddedGraphDatabase("neo4j-community-1.9.M04/data/graph.db");
        Index<Node> stadiumsIndex = createSpatialIndex(db, "stadiumsLocation");
        Transaction tx = db.beginTx();

        for (String stadium : lines) {
            String[] columns = stadium.split(",");
            Index<Node> teamsIndex = db.index().forNodes("teams");
            String team = columns[1].replaceAll("\"","");
            Node teamNode = teamsIndex.get("name", team).getSingle();

            if(teamNode != null) {
                Node stadiumNode = db.createNode();
                stadiumNode.setProperty("wkt", String.format("POINT(%s %s)", columns[4], columns[3]));
                stadiumNode.setProperty("name", columns[0].replaceAll("\"",""));
                stadiumsIndex.add(stadiumNode, "dummy", "value");
                teamNode.createRelationshipTo(stadiumNode, DynamicRelationshipType.withName("play_at"));
            }

        }

        tx.success();
        tx.finish();
    }

    private static Index<Node> createSpatialIndex(EmbeddedGraphDatabase db,  String indexName) {
        return db.index().forNodes(indexName, SpatialIndexProvider.SIMPLE_WKT_CONFIG);
    }

    // readFile excluded
}
~~~

<p>I've excluded some bits of the code for brevity but it's on <a href="https://gist.github.com/mneedham/5182948">this gist</a> if you're interested.</p>


<p>The only change from last week's version is that we're now looking up the team that a stadium belongs to and creating a 'play_at' relationship from the team to the stadium.</p>


<p>I was then able to execute that code by calling 'lein run' based on the following project.clj file:</p>



~~~text

(defproject neo4jfootball "1.0.0-SNAPSHOT"
  :description "neo4j football project"
  :main "main.java.StadiumsImport"
  :dependencies [[org.clojure/clojure "1.4.0"] 
                 [org.neo4j/neo4j-spatial "0.11-SNAPSHOT"]
                 [clojure-csv/clojure-csv "2.0.0-alpha1"]]
  :jvm-opts ["-Xmx2g"]
  :plugins [[lein-idea "1.0.1"]]
  :repositories {"local" ~(str (.toURI (java.io.File. "maven_repository")))}
  :java-source-paths ["src/main/java"] )
~~~

<p>I'm using <a href="http://www.markhneedham.com/blog/2011/12/27/leiningen-using-goose-via-a-local-maven-repository/">a local Maven repository</a> to store the neo4j spatial JAR. The Maven entry was created by executed the following command from where I had the <a href="https://github.com/neo4j/spatial">neo4j spatial</a> project checked out:</p>



~~~text

 mvn install:install-file -Dfile=target/neo4j-spatial-0.11-SNAPSHOT.jar -DartifactId=neo4j-spatial -Dversion=0.11-SNAPSHOT -DgroupId=org.neo4j -Dpackaging=jar -DlocalRepositoryPath=/path/to/neo4j-football/maven_repository -DpomFile=pom.xml  
~~~

<p>That worked reasonably well but I thought it'd be interesting to see what the above code would look like if it was written in clojure instead.</p>


<p>This is what I ended up with:</p>



~~~lisp

(ns neo4jfootball.core
  (:require [clojure-csv.core :as csv])
  (:use clojure.java.io)
  (:import (org.neo4j.kernel EmbeddedGraphDatabase) (org.neo4j.gis.spatial.indexprovider SpatialIndexProvider) (org.neo4j.graphdb DynamicRelationshipType)))

(defn take-csv [fname]
  (with-open [file (reader fname)]
    (csv/parse-csv (slurp file))))

(defn transform [line] {:stadium (get line 0) :team (get line 1) :lat (get line 3) :long (get line 4)})

(def not-nil? (comp not nil?))

(defn create-stadium-node [db line]
  (let [stadium-node (.. db createNode)]
    (.. stadium-node (setProperty "wkt" (format "POINT(%s %s)" (:long line) (:lat line))))
    (.. stadium-node (setProperty "name" (:stadium line)))
  stadium-node))

(defn -main []
  (do
    (let [db (new EmbeddedGraphDatabase "neo4j-community-1.9.M04/data/graph.db")
          tx (.beginTx db)
          stadiums-index (.. db index (forNodes "stadiumsLocation" (SpatialIndexProvider/SIMPLE_WKT_CONFIG)))
          teams-index    (.. db index (forNodes "teams"))]
      (doseq [line (drop 1 (map transform (take-csv "data/stadiums.csv")))]
        (let [team-node (.. teams-index (get "name" (:team line)) getSingle)]
          (if (not-nil? team-node)
            (let [stadium-node (create-stadium-node db line)]
              (.. stadiums-index (add stadium-node "dummy" "value"))
              (.. team-node (createRelationshipTo stadium-node (DynamicRelationshipType/withName "play_at")))))))
      (.. tx success)
      (.. tx finish))))
~~~

<p>The code is simplified quite a bit by using the <a href="https://github.com/davidsantiago/clojure-csv">clojure CSV</a> library so I could probably have achieved similar in the Java version by using an equivalent library.</p>


<p>It's a bit easier to see what properties of a row in the CSV file are being used where as a result of the <cite>transform</cite> function where we convert the array into a map.</p>
 

<p>It would have taken quite a bit more code to achieve a similar thing in Java so I didn't bother.</p>


<p>The <a href="http://clojure.org/java_interop">Java Interop page on the clojure website</a> was quite useful for working out how to call the various methods on the Java API.</p>


<p>I'm mainly using the <cite><a href="http://clojure.org/java_interop#Java Interop-The Dot special form-(.. Classname-symbol member+)">..</a></cite> macro which allows us to chain Java method calls together. In a couple of cases we could just as easily have used the <cite><a href="http://clojure.org/java_interop#Java Interop-The Dot special form-(. Classname-symbol (method-symbol args*)) or">.</a></cite> macro instead.</p>


<p>We can then call this code from lein like so:</p>



~~~text

lein run -m neo4jfootball.core
~~~
