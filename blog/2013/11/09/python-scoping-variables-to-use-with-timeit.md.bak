+++
draft = false
date="2013-11-09 11:01:08"
title="Python: Scoping variables to use with timeit"
tag=['python']
category=['Python']
+++

<p>I've been playing around with Python's <a href="http://docs.python.org/2/library/timeit.html">timeit</a> library to help <a href="http://www.markhneedham.com/blog/2013/11/08/neo4j-2-0-0-m06-applying-wes-freemans-cypher-optimisation-tricks/">benchmark some Neo4j cypher queries</a> but I ran into some problems when trying to give it accessible to variables in my program.</p>


<p>I had the following python script which I would call from the terminal using <cite>python top-away-scorers.py</cite>:</p>



~~~python

import query_profiler as qp

attempts = [
{"query": '''MATCH (player:Player)-[:played]->stats-[:in]->game, stats-[:for]->team
             WHERE game<-[:away_team]-team
             RETURN player.name, SUM(stats.goals) AS goals
             ORDER BY goals DESC
             LIMIT 10'''}
]

qp.profile(attempts, iterations=5, runs=3)
~~~

<p><cite>query_profiler</cite> initially read like this:</p>



~~~python

from py2neo import neo4j
import timeit

graph_db = neo4j.GraphDatabaseService()

def run_query(query, params):
	query = neo4j.CypherQuery(graph_db, query)
	return query.execute(**params).data

def profile(attempts, iterations=10, runs=3):
	print ""

	for attempt in attempts:
		query = attempt["query"]
		potential_params = attempt.get("params")
		
		params = {} if potential_params == None else potential_params
	
		timings = timeit.repeat("run_query(query, params)", setup="from query_profiler import run_query", number=iterations, repeat=runs)

		print re.sub('\n[ \t]', '\n', re.sub('[ \t]+', ' ', query))
		print timings
~~~

<p>but when I ran top-away-scorers.py I got the following exception:</p>



~~~bash

$ python top-away-scorers.py 

Traceback (most recent call last):
  File "top-away-scorers.py", line 11, in <module>
    qp.profile(attempts, iterations=5, runs=3)
  File "/Users/markhneedham/code/cypher-query-tuning/query_profiler.py", line 19, in profile
    timings = timeit.repeat("run_query(query, params)", setup="from query_profiler import run_query", number=iterations, repeat=runs)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 233, in repeat
    return Timer(stmt, setup, timer).repeat(repeat, number)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 221, in repeat
    t = self.timeit(number)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 194, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
NameError: global name 'query' is not defined
~~~

<p>As far as I understand, timeit couldn't understand what 'query' is because we didn't explicitly import it in the setup and it doesn't automatically pick up values from the scope its running in.</p>


<p>I tried adding query and params to the list of imports from query_profiler like so:</p>



~~~python

def profile(attempts, iterations=10, runs=3):
	print ""

	for attempt in attempts:
		query = attempt["query"]
		potential_params = attempt.get("params")
		
		params = {} if potential_params == None else potential_params
	
		timings = timeit.repeat("run_query(query, params)", setup="from query_profiler import run_query, query, params", number=iterations, repeat=runs)

		print re.sub('\n[ \t]', '\n', re.sub('[ \t]+', ' ', query))
		print timings
~~~

<p>Unfortunately that didn't work:</p>



~~~bash

$ python top-away-scorers.py 

Traceback (most recent call last):
  File "top-away-scorers.py", line 11, in <module>
    qp.profile(attempts, iterations=5, runs=3)
  File "/Users/markhneedham/code/cypher-query-tuning/query_profiler.py", line 21, in profile
    timings = timeit.repeat("run_query(query, params)", setup="from query_profiler import run_query, query, params", number=iterations, repeat=runs)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 233, in repeat
    return Timer(stmt, setup, timer).repeat(repeat, number)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 221, in repeat
    t = self.timeit(number)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py", line 194, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 3, in inner
ImportError: cannot import name query
~~~

<p>I eventually came across the <a href="http://docs.python.org/2/reference/simple_stmts.html#grammar-token-global_stmt">global</a> keyword which allows me to scope query and params in a way that we can import them from the query_profiler module:</p>



~~~python

def profile(attempts, iterations=10, runs=3):
	print ""

	for attempt in attempts:
		global query
		query = attempt["query"]
		potential_params = attempt.get("params")
		
		global params
		params = {} if potential_params == None else potential_params
	
		timings = timeit.repeat("run_query(query, params)", setup="from query_profiler import run_query, query, params", number=iterations, repeat=runs)

		print re.sub('\n[ \t]', '\n', re.sub('[ \t]+', ' ', query))
		print timings
~~~

<p>I'm generally wary of using anything global but in this case it seems necessary…or I've completely misunderstood how you're meant to use timeit.</p>
 

<p>Any Pythonistas able to shed some light?</p>

