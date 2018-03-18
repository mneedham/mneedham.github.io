+++
draft = false
date="2016-10-04 22:33:43"
title="Neo4j: requirement failed"
tag=['neo4j']
category=['neo4j']
+++

<p>
Last week during a hands on Cypher meetup, using Neo4j's built in movie dataset, one of the attendees showed me the following query which wasn't working as expected:
</p>



~~~cypher

MATCH (p:Person)-[:ACTED_IN]->(movie)
RETURN p, COLLECT(movie.title) AS movies
ORDER BY COUNT(movies) DESC
LIMIT 10
~~~


~~~text

requirement failed
~~~

<p>
We can get a full stack trace in <cite>logs/debug.log</cite> if we run the same query from the cypher-shell, which was introduced during one fo the Neo4j 3.1 milestone releases:
</p>



~~~text

2016-10-03 23:25:07.529+0000 ERROR [o.n.b.v.r.ErrorReporter] Client triggered an unexpected error [UnknownError]: requirement failed, reference to. requirement failed
java.lang.IllegalArgumentException: requirement failed
        at scala.Predef$.require(Predef.scala:212)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.steps.sortSkipAndLimit$.apply(sortSkipAndLimit.scala:38)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanEventHorizon$.apply(PlanEventHorizon.scala:43)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanEventHorizon$.apply(PlanEventHorizon.scala:31)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanWithTail.apply(PlanWithTail.scala:46)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanWithTail.apply(PlanWithTail.scala:29)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanSingleQuery.apply(PlanSingleQuery.scala:47)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.PlanSingleQuery.apply(PlanSingleQuery.scala:30)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.DefaultQueryPlanner$$anonfun$2.apply(QueryPlanner.scala:51)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.DefaultQueryPlanner$$anonfun$2.apply(QueryPlanner.scala:51)
        at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
        at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
        at scala.collection.immutable.List.foreach(List.scala:381)
        at scala.collection.TraversableLike$class.map(TraversableLike.scala:234)
        at scala.collection.immutable.List.map(List.scala:285)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.DefaultQueryPlanner.planQueries(QueryPlanner.scala:51)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.logical.DefaultQueryPlanner.plan(QueryPlanner.scala:36)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.CostBasedExecutablePlanBuilder.produceLogicalPlan(CostBasedExecutablePlanBuilder.scala:95)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.CostBasedExecutablePlanBuilder$$anonfun$1.apply(CostBasedExecutablePlanBuilder.scala:71)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.CostBasedExecutablePlanBuilder$$anonfun$1.apply(CostBasedExecutablePlanBuilder.scala:71)
        at org.neo4j.cypher.internal.compiler.v3_1.helpers.package$$anonfun$closing$1.apply(package.scala:29)
        at org.neo4j.cypher.internal.compiler.v3_1.helpers.package$$anonfun$closing$1.apply(package.scala:29)
        at org.neo4j.cypher.internal.compiler.v3_1.helpers.package$.using(package.scala:37)
        at org.neo4j.cypher.internal.compiler.v3_1.helpers.package$.closing(package.scala:29)
        at org.neo4j.cypher.internal.compiler.v3_1.planner.CostBasedExecutablePlanBuilder.producePlan(CostBasedExecutablePlanBuilder.scala:70)
        at org.neo4j.cypher.internal.compiler.v3_1.executionplan.procs.DelegatingProcedureExecutablePlanBuilder.producePlan(DelegatingProcedureExecutablePlanBuilder.scala:99)
        at org.neo4j.cypher.internal.compiler.v3_1.executionplan.FallbackBuilder$class.producePlan(SilentFallbackPlanBuilder.scala:37)
        at org.neo4j.cypher.internal.compiler.v3_1.executionplan.SilentFallbackPlanBuilder.producePlan(SilentFallbackPlanBuilder.scala:56)
        at org.neo4j.cypher.internal.compiler.v3_1.executionplan.ExecutionPlanBuilder.build(ExecutionPlanBuilder.scala:106)
        at org.neo4j.cypher.internal.compiler.v3_1.CypherCompiler$$anonfun$5.apply(CypherCompiler.scala:176)
        at org.neo4j.cypher.internal.compiler.v3_1.CypherCompiler$$anonfun$5.apply(CypherCompiler.scala:176)
        at org.neo4j.cypher.internal.compiler.v3_1.QueryCache$$anonfun$getOrElseUpdate$1$$anonfun$apply$1.apply(CacheAccessor.scala:36)
        at org.neo4j.cypher.internal.compiler.v3_1.MonitoringCacheAccessor$$anonfun$1.apply(CacheAccessor.scala:57)
        at org.neo4j.cypher.internal.compiler.v3_1.LFUCache$$anon$1.apply(LFUCache.scala:31)
~~~

<p>
The problem line seems to be <a href="https://github.com/neo4j/neo4j/blob/0f1c7439d5ba2bf4bfbd2b990bf214b5a28406bf/community/cypher/cypher-compiler-3.1/src/main/scala/org/neo4j/cypher/internal/compiler/v3_1/planner/logical/steps/sortSkipAndLimit.scala#L38">this one</a>:
</p>



~~~scala

require(sortItems.forall(_.expression.isInstanceOf[Variable]))
~~~

<p>
The solution is actually quite simple. We should be using the <cite>SIZE</cite> function to calculate the size of a list rather then the <cite>COUNT</cite> function:
</p>



~~~cypher

MATCH (p:Person)-[:ACTED_IN]->(movie)
RETURN p, COLLECT(movie.title) AS movies
ORDER BY SIZE(movies) DESC
LIMIT 10
~~~
