+++
draft = false
date="2013-10-27 00:33:54"
title="Neo4j: Cypher - Profiling ORDER BY LIMIT vs LIMIT"
tag=['neo4j']
category=['neo4j']
+++

<p>Something I've seen people get confused by when writing queries using Neo4j's cypher query language is the sometimes significant difference in query execution time when using 'LIMIT' on its own compared to using it in combination with 'ORDER BY'.</p>


<p>The confusion is centred around the fact that at first glance it seems like the only thing different between these queries is the sorting of the rows but there's actually more to it.</p>


<p>For example given a small graph with ~ 11,000 nodes...</p>



~~~bash

$ MATCH n RETURN COUNT(n);

==> +----------+
==> | COUNT(n) |
==> +----------+
==> | 11442    |
==> +----------+
==> 1 row
==> 1384 ms
~~~

<p>...we can return 5 random nodes really quickly with the following query:</p>



~~~bash

$ MATCH n RETURN n LIMIT 5;

==> +-------------------------------------------+
==> | n                                         |
==> +-------------------------------------------+
==> | Node[0]{}                                 |
==> | Node[1]{name:"Africa",node_id:"1"}        |
==> | Node[2]{name:"Asia",node_id:"2"}          |
==> | Node[3]{name:"Europe",node_id:"3"}        |
==> | Node[4]{name:"North America",node_id:"4"} |
==> +-------------------------------------------+
==> 5 rows
==> 38 ms
~~~

<p>However, if we order those nodes by ID first then it'll take a bit longer:</p>



~~~bash

$ MATCH n RETURN n ORDER BY ID(n) LIMIT 5;
==> +-------------------------------------------+
==> | n                                         |
==> +-------------------------------------------+
==> | Node[0]{}                                 |
==> | Node[1]{name:"Africa",node_id:"1"}        |
==> | Node[2]{name:"Asia",node_id:"2"}          |
==> | Node[3]{name:"Europe",node_id:"3"}        |
==> | Node[4]{name:"North America",node_id:"4"} |
==> +-------------------------------------------+
==> 5 rows
==> 157 ms
~~~

<p>If we have a look at the profile of the second query we can see why this is:</p>



~~~bash

$ PROFILE MATCH n RETURN n ORDER BY ID(n) LIMIT 5;

==> ColumnFilter(symKeys=["n", "  UNNAMEDS1215244997"], returnItemNames=["n"], _rows=5, _db_hits=0)
==> Top(orderBy=["SortItem(Cached(  UNNAMEDS1215244997 of type Long),true)"], limit="Literal(5)", _rows=5, _db_hits=0)
==>   Extract(symKeys=["n"], exprKeys=["  UNNAMEDS1215244997"], _rows=11442, _db_hits=0)
==>     AllNodes(identifier="n", _rows=11442, _db_hits=11442)
~~~

<p><cite>Top</cite> refers to <cite><a href="https://github.com/neo4j/neo4j/blob/master/community/cypher/src/main/scala/org/neo4j/cypher/internal/compiler/v2_0/pipes/TopPipe.scala">TopPipe</a></cite> and if we look at the <cite><a href="https://github.com/neo4j/neo4j/blob/master/community/cypher/src/main/scala/org/neo4j/cypher/internal/compiler/v2_0/pipes/TopPipe.scala#L34">internalCreateResults</a></cite> function we can see that the entire collection gets evaluated so that we can sort it correctly on line 63.</p>



~~~java

    if (input.isEmpty)
      Iterator.empty
    else {
      val first = input.next()
      val count = countExpression(first).asInstanceOf[Number].intValue()

      val iter = new HeadAndTail(first, input)
      iter.foreach {
        case ctx =>

          if (size < count) {
            result += ctx
            size += 1

            if (largerThanLast(ctx)) {
              last = Some(ctx)
            }
          } else
            if (!largerThanLast(ctx)) {
              result -= last.get
              result += ctx
              result = result.sortWith((a, b) => compareBy(a, b, sortDescription)(state))
              sorted = true
              last = Some(result.last)
            }
      }
    }
~~~

<p>In this case it means that we load the next node but in a more complex query we'd have to evaluate a more complex pattern for every single match.</p>


<p>On the other hand, if we don't have the 'ORDER BY' we use the <cite><a href="https://github.com/neo4j/neo4j/blob/master/community/cypher/src/main/scala/org/neo4j/cypher/internal/compiler/v2_0/pipes/SlicePipe.scala#L47">SlicePipe</a></cite> which does a <cite>take</cite> on the iterator which lazily retrieves the first 5 results in this instance:</p>



~~~bash

$ PROFILE MATCH n RETURN n LIMIT 5;

==> Slice(limit="Literal(5)", _rows=5, _db_hits=0)
==> AllNodes(identifier="n", _rows=5, _db_hits=5)
~~~


~~~java

    (skip, limit) match {
      case (Some(x), None) => sourceIter.drop(asInt(x))
      case (None, Some(x)) => sourceIter.take(asInt(x))

      case (Some(startAt), Some(count)) =>
        val start = asInt(startAt)
        sourceIter.slice(start, start + asInt(count))

      case (None, None) =>
        throw new ThisShouldNotHappenError("Andres Taylor", "A slice pipe that doesn't slice should never exist.")
    }
~~~

<p>Now that we've drilled into the queries a bit more we can see that with the 'ORDER BY LIMIT' query many more paths need to be evaluated to make that possible.</p>


<p>A common anti pattern is to return a result set containing 100s of thousands of rows and then using 'ORDER BY LIMIT' to filter that down to 10.</p>


In that case there might be a better way of modelling the data so that we have less rows coming back from our MATCH clause and <a href="http://blog.neo4j.org/2013/05/reloading-my-beergraph-using-in-graph.html">In graph indexes</a> are one such way of doing that.</p>

