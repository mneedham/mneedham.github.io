+++
draft = false
date="2014-06-29 02:56:53"
title="Neo4j's Cypher vs Clojure - Group by and Sorting"
tag=['clojure', 'neo4j', 'cypher']
category=['Clojure', 'neo4j']
+++

<p>One of the points that I emphasised during my talk on <a href="https://skillsmatter.com/skillscasts/5385-analysing-london-s-nosql-meetups-using-clojure-neocons-luminus">building Neo4j backed applications using Clojure</a> last week is understanding when to use Cypher to solve a problem and when to use the programming language.</p>


<p>A good example of this is in the meetup application I've been working on. I have a collection of events and want to display past events in descending order and future events in ascending order.</p>


<p>First let's create some future and some past events based on the current timestamp of 1404006050535:</p>



~~~cypher

CREATE (event1:Event {name: "Future Event 1", timestamp: 1414002772427 })
CREATE (event2:Event {name: "Future Event 2", timestamp: 1424002772427 })
CREATE (event3:Event {name: "Future Event 3", timestamp: 1416002772427 })

CREATE (event4:Event {name: "Past Event 1", timestamp: 1403002772427 })
CREATE (event5:Event {name: "Past Event 2", timestamp: 1402002772427 })
~~~

<p>If we return all the events we see the following:</p>



~~~cypher

$ MATCH (e:Event) RETURN e;
==> +------------------------------------------------------------+
==> | e                                                          |
==> +------------------------------------------------------------+
==> | Node[15414]{name:"Future Event 1",timestamp:1414002772427} |
==> | Node[15415]{name:"Future Event 2",timestamp:1424002772427} |
==> | Node[15416]{name:"Future Event 3",timestamp:1416002772427} |
==> | Node[15417]{name:"Past Event 1",timestamp:1403002772427}   |
==> | Node[15418]{name:"Past Event 2",timestamp:1402002772427}   |
==> +------------------------------------------------------------+
==> 5 rows
==> 13 ms
~~~

<p>We can achieve the desired grouping and sorting with the following cypher query:</p>



~~~lisp

(def sorted-query "MATCH (e:Event)
WITH COLLECT(e) AS events
WITH [e IN events WHERE e.timestamp <= timestamp()] AS pastEvents,
     [e IN events WHERE e.timestamp > timestamp()] AS futureEvents
UNWIND pastEvents AS pastEvent
WITH pastEvent, futureEvents ORDER BY pastEvent.timestamp DESC
WITH COLLECT(pastEvent) as orderedPastEvents, futureEvents
UNWIND futureEvents AS futureEvent
WITH futureEvent, orderedPastEvents ORDER BY futureEvent.timestamp
RETURN COLLECT(futureEvent) AS orderedFutureEvents, orderedPastEvents")
~~~

<p>We then use the following function to call through to the Neo4j server using the excellent <a href="https://github.com/michaelklishin/neocons">neocons</a> library:</p>



~~~lisp

(ns neo4j-meetup.db
  (:require [clojure.walk :as walk])
  (:require [clojurewerkz.neocons.rest.cypher :as cy])
  (:require [clojurewerkz.neocons.rest :as nr]))

(def NEO4J_HOST "http://localhost:7521/db/data/")

(defn cypher
  ([query] (cypher query {}))
  ([query params]
     (let [conn (nr/connect! NEO4J_HOST)]
       (->> (cy/tquery query params)
            walk/keywordize-keys))))

~~~

<p>We call that function and grab the first row since we know there won't be any other rows in the result:</p>



~~~lisp

(def query-result (->> ( db/cypher sorted-query) first))
~~~

<p>Now we need to extract the past and future collections so that we can display them on the page which we can do like so:</p>



~~~lisp

> (map #(% :data) (query-result :orderedPastEvents))
({:timestamp 1403002772427, :name "Past Event 1"} {:timestamp 1402002772427, :name "Past Event 2"})

> (map #(% :data) (query-result :orderedFutureEvents))
({:timestamp 1414002772427, :name "Future Event 1"} {:timestamp 1416002772427, :name "Future Event 3"} {:timestamp 1424002772427, :name "Future Event 2"})
~~~ 

<p>An alternative approach is to return the events from cypher and then handle the grouping and sorting in clojure. In that case our query is much simpler:</p>



~~~lisp

(def unsorted-query "MATCH (e:Event) RETURN e")
~~~

<p>We'll use the <a href="https://github.com/clj-time/clj-time">clj-time</a> library to determine the current time:</p>



~~~lisp

(def now (clj-time.coerce/to-long (clj-time.core/now)))
~~~

<p>First let's split the events into past and future:</p>



~~~lisp

> (def grouped-by-events 
     (->> (db/cypher unsorted-query)
          (map #(->> % :e :data))
          (group-by #(> (->> % :timestamp) now))))

> grouped-by-events
{true [{:timestamp 1414002772427, :name "Future Event 1"} {:timestamp 1424002772427, :name "Future Event 2"} {:timestamp 1416002772427, :name "Future Event 3"}], 
 false [{:timestamp 1403002772427, :name "Past Event 1"} {:timestamp 1402002772427, :name "Past Event 2"}]}
~~~

<p>And finally we sort appropriately using these functions:</p>



~~~lisp

(defn time-descending [row] (* -1 (->> row :timestamp)))
(defn time-ascending [row] (->> row :timestamp))
~~~


~~~lisp

> (sort-by time-descending (get grouped-by-events false))
({:timestamp 1403002772427, :name "Past Event 1"} {:timestamp 1402002772427, :name "Past Event 2"})

> (sort-by time-ascending (get grouped-by-events true))
({:timestamp 1414002772427, :name "Future Event 1"} {:timestamp 1416002772427, :name "Future Event 3"} {:timestamp 1424002772427, :name "Future Event 2"})
~~~

<p>I used Clojure to do the sorting and grouping in my project because the query to get the events was a bit more complicated and became very difficult to read with the sorting and grouping mixed in.</p>


<p>Unfortunately cypher doesn't provide an easy way to sort within a collection so we need our sorting in the row context and then collect the elements back again afterwards.</p>

