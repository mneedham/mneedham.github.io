+++
draft = false
date="2013-01-18 00:40:32"
title="Bellman-Ford algorithm in Python"
tag=['algorithms', 'graphs']
category=['Algorithms']
+++

<p>The latest problem of the <a href="https://www.coursera.org/course/algo2">Algorithms 2</a> class required us to write an algorithm to calculate the <a href="http://en.wikipedia.org/wiki/Shortest_path_problem">shortest path between two nodes on a graph</a> and one algorithm which allows us to do this is <a href="http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm">Bellman-Ford</a>.</p>


<p>Bellman-Ford computes the single source shortest path which means that if we have a 5 vertex graph we'd need to run it 5 times to find the shortest path for each vertex and then find the shortest paths of those shortest paths.</p>


<p>One nice thing about Bellman-Ford compared to <a href="http://en.wikipedia.org/wiki/Dijkstra's_algorithm">Djikstra</a> is that it's able to handle negative edge weights.</p>


<p>The pseudocode of the algorithm is as follows:</p>


<ul>
<li>Let <cite>A</cite> = 2-D array of size <cite>n</cite> * <cite>n</cite> where n is the number of vertices</li>
<li>Initialise <cite>A[0,s] = 0</cite>; A[0,v] = infinity for all v &ne; <cite>s</cite> where <cite>s</cite> is the node we're finding the shortest path for</li>
<li>
	for i=1,2,3,…n-1
	<ul>
		<li>for each v &isin; V
			<ul>
				<li>A[i,v] = min { A[i-1, v], 
				             <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min (w,v) &isin; E { A[k-1, w] + Cost<sub>wv</sub> } <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp}</li>
				<li>where (w,v) are the incoming edges of vertex v</li>
			</ul>
		</li>
	</ul>
</li>
<li>check for negative cycles by running one more time and checking A[n] = A[n-1]</li>
<li>If they are equal then return A[n-1] otherwise report a negative cycle.</li>
</ul>

<p>My first version looked like this:</p>



~~~python

import os
file = open(os.path.dirname(os.path.realpath(__file__)) + "/g_small.txt")
vertices, edges = map(lambda x: int(x), file.readline().replace("\n", "").split(" "))

adjacency_list = [[] for k in xrange(vertices)]
for line in file.readlines():
    tail, head, weight = line.split(" ")
    adjacency_list[int(head)-1].append({"from" : int(tail), "weight" : int(weight)})

s=0
cache = [[0 for k in xrange(vertices+1)] for j in xrange(vertices+1)]
cache[0][s] = 0

for v in range(0, vertices):
  if v != s:
    cache[0][v] = float("inf")

for i in range(1, vertices):
  for v in range(0, vertices):
    least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, cache[i-1])
    cache[i][v] = min(cache[i-1][v], least_adjacent_cost)
    
# detecting negative cycles
for v in range(0, vertices):
  least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, cache[vertices-1])  
  cache[vertices][v] = min(cache[vertices-1][v], least_adjacent_cost)

if(not cache[vertices] == cache[vertices-1]):
    raise Exception("negative cycle detected")
    
shortest_path = min(cache[vertices-1])
print("Shortest Path: " + str(shortest_path))  
~~~

<p>where <cite>calculate_least_adjacent_cost</cite> is defined like so:</p>



~~~python

def calculate_least_adjacent_cost(adjacency_list, i, v, cache):
    adjacent_nodes = adjacency_list[v]
    
    least_adjacent_cost = float("inf")
    for node in adjacent_nodes:
      adjacent_cost = cache[node["from"]-1] + node["weight"]
      if adjacent_cost < least_adjacent_cost:
        least_adjacent_cost = adjacent_cost
    return least_adjacent_cost
~~~

<p>As you can see we're using an adjacency list as our graph representation, mapping from each node to its corresponding edges. We then initialise the cache as per the algorithm and then have two nested for loops which we use to work out the shortest path from <cite>s</cite> to each vertex.</p>
 

<p>The <cite>calculate_least_adjacent_cost</cite> function is used to work out which of the incoming edges to a vertex has the lowest cost, taking into account previous shortest path calculations that we've done up to the source vertices of those incoming edges.</p>


<p>We then have an extra call at the end to check for negative cycles. If there is no change in the values calculated from <cite>s</cite> to each vertex then we know we don't have any negative cycles because otherwise one of them would have come into effect and given us a different result.</p>


<p>This algorithm works but it's inefficient in its use of space - our cache has size n*n when we only ever care about 2 of the rows - the previous and current ones - so we can just use a list instead.</p>


<p>If we do this the code now looks like this:</p>



~~~python

s=0
cache = [[] for j in xrange(vertices+1)]
cache[s] = 0

for v in range(0, vertices):
  if v != s:
    cache[v] = float("inf")

for i in range(1, vertices):
  for v in range(0, vertices):
    previous_cache = cache
    least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, previous_cache)
    cache[v] = min(previous_cache[v], least_adjacent_cost)
    
# detecting negative cycles
for v in range(0, vertices):
  previous_cache = copy.deepcopy(cache)
  least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, previous_cache)
  cache[v] = min(previous_cache[v], least_adjacent_cost)

if(not cache == previous_cache):
    raise Exception("negative cycle detected")
~~~

<p>By doing this we lose the history of the algorithm over the run which means in its current state we wouldn't be able to work our what the shortest path was, we just know its cost.</p>


<p>For a 1000 node, 47978 edge graph it takes 27 seconds to go over the whole graph and detect a negative cycle if there is one.</p>


<p>The <a href="https://github.com/mneedham/algorithms2/blob/master/shortestpath/shortestpaths.py">code for this algorithm</a> is on github as always.</p>

