+++
draft = false
date="2013-01-20 19:14:08"
title="Bellman-Ford algorithm in Python using vectorisation/numpy"
tag=['algorithms', 'bellman-ford']
category=['Algorithms']
+++

<p>I recently <a href="http://www.markhneedham.com/blog/2013/01/18/bellman-ford-algorithm-in-python/">wrote about an implementation of the Bellman Ford shortest path algorithm</a> and concluded by saying that it took 27 seconds to calculate the shortest path in the graph for any node.</p>


<p>This seemed a bit slow and while browsing the Coursera forums I came across a suggestion that the algorithm would run much more quickly if we used vectorization with <a href="http://www.numpy.org/">numpy</a> rather than nested for loops.</p>


<p>Vectorisation refers to a problem solving approach where we make use of matrices operations which is what numpy allows us to do.</p>


<p>To refresh, the core of the original algorithm reads like this:</p>



~~~python

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

shortest_path = min(cache)
~~~

<p>We want to try and simplify the first two lines where we have for loops through <cite>i</cite> and <cite>v</cite>.</p>
 

<p>I couldn't see a way to apply matrix operations to the <cite>i</cite> loop since each iteration of <cite>i</cite> makes use of the result of the previous iteration but with the <cite>v</cite> loop the calculation of the shortest path for each vertex is independent of the calculation for other vertices so we can vectorise this bit of code.</p>



<p>We want to try and get to the point where we can use numpy's <cite><a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.minimum.html">minimum</a></cite> function where we'd pass in an array representing the previous iteration of <cite>i</cite> and an array that represents the newly calculated cost for each vertex <cite>v</cite>.</p>



~~~python

# We want to get to this point
previous_cache = cache[:] # here we copy the contents of cache into previous_cache
cache = minimum(previous_cache, new_shortest_paths)
~~~

<p>It was initially a bit tricky to see how we could go about this but after sketching it out on paper it became clear that we needed to add the values in <cite>previous_cache</cite> to the weights of the edges between different vertices and then find the minimum combined value for each vertex.</p>


<p>It seemed much easier to achieve this if we used an adjacency matrix rather than an adjacency list to represent the graph and if we do that then the following example shows how we'd go about vectorising the algorithm.</p>


<p>If our <cite>previous_cache</cite> had the following values:</p>



~~~text

1 2 3 4 5 6 # these are the previous shortest paths for vertex 0,1…,n
~~~

<p>And our adjacency matrix looked like this:</p>



~~~text

inf  inf   4   inf  inf  inf # edges for vertex 0
-2   inf  inf  inf  inf  inf # edges for vertex 1
inf  -1   inf  inf  inf  inf # and so on...
inf  inf   2   inf  inf   1
inf  inf  -3   inf  inf  -4
inf  inf  inf  inf  inf  inf
~~~

<p>where the numeric values represent the edge weights between vertices and those with a value of 'inf' don't have a direct edge we'd except the initial combination of these two data structures to look like this:</p>



~~~text

inf  inf   5   inf  inf  inf # edges for vertex 0
0    inf  inf  inf  inf  inf # edges for vertex 1
inf  2    inf  inf  inf  inf # and so on...
inf  inf   6   inf  inf   5
inf  inf   2   inf  inf   1
inf  inf  inf  inf  inf  inf
~~~

<p>where 1 has been added to every value in the first row, 2 has been added to every value in the second row and so on.</p>


<p>We can achieve that with the following code:</p>



~~~python

>>> previous = arange(1,7).reshape((1,6))
>>> previous
array([[1, 2, 3, 4, 5, 6]])
>>> adjacency_matrix = x = array([[inf,inf,4,inf,inf,inf],[-2,inf,inf,inf,inf,inf],[inf,-1,inf,inf,inf,inf],[inf,inf,2,inf,inf,1],[inf,inf,-3,inf,inf,-4],[inf,inf,inf,inf,inf,inf]])
>>> adjacency_matrix
array([[ inf,  inf,   4.,  inf,  inf,  inf],
       [ -2.,  inf,  inf,  inf,  inf,  inf],
       [ inf,  -1.,  inf,  inf,  inf,  inf],
       [ inf,  inf,   2.,  inf,  inf,   1.],
       [ inf,  inf,  -3.,  inf,  inf,  -4.],
       [ inf,  inf,  inf,  inf,  inf,  inf]])
>>> previous.T + adjacency_matrix
array([[ inf,  inf,   5.,  inf,  inf,  inf],
       [  0.,  inf,  inf,  inf,  inf,  inf],
       [ inf,   2.,  inf,  inf,  inf,  inf],
       [ inf,  inf,   6.,  inf,  inf,   5.],
       [ inf,  inf,   2.,  inf,  inf,   1.],
       [ inf,  inf,  inf,  inf,  inf,  inf]])
~~~

<p>Here we used the <cite><a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html">transpose</a></cite> function to get our <cite>previous</cite> variable in the right shape so we could apply its first value to every item in the first row of <cite>adjacency_matrix</cite> its second value to every item in the second row and so on.</p>


<p>What we actually want is the shortest path for each vertex so we need to take the minimum value from each row for which the <cite><a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.min.html">min</a></cite> function comes in handy.</p>



~~~python

>>> result = previous.T + adjacency_matrix
>>> result.min(axis=1)
array([  5.,   0.,   2.,   5.,   1.,  inf])
~~~

<p>We have to tell it to apply itself to each row by passing 'axis=1' otherwise it will just take the minimum value of the whole matrix.</p>


<p>Now to get our newly calculated cache we just need to combine our <cite>previous</cite> value with this new one:</p>



~~~python

>>> previous
array([[1, 2, 3, 4, 5, 6]])
>>> result.min(axis=1)
array([  5.,   0.,   2.,   5.,   1.,  inf])
>>> minimum(previous, result.min(axis=1))
array([[ 1.,  0.,  2.,  4.,  1.,  6.]])
~~~

<p>Now if we put this into our algorithm it ends up looking like this:</p>



~~~python

adjacency_matrix = zeros((vertices, vertices))
adjacency_matrix[:] = float("inf")
for line in file.readlines():
    tail, head, weight = line.split(" ")
    adjacency_matrix[int(head)-1][int(tail)-1] = int(weight)

def initialise_cache(vertices, s):
    cache = empty(vertices)
    cache[:] = float("inf")
    cache[s] = 0
    return cache    

cache = initialise_cache(vertices, 0)
for i in range(1, vertices):
    previous_cache = cache[:]                
    combined = (previous_cache.T + adjacency_matrix).min(axis=1)
    cache = minimum(previous_cache, combined)
    
# checking for negative cycles
previous_cache = cache[:]
combined = (previous_cache.T + adjacency_matrix).min(axis=1)
cache = minimum(previous_cache, combined)
    
if(not alltrue(cache == previous_cache)):
    raise Exception("negative cycle detected")
~~~

<p>The only numpy function that's new is <cite><a href="http://www.scipy.org/Numpy_Example_List_With_Doc#head-2cddd526f17674432305ae6deeed1f18673ee560">alltrue</a></cite> which is used to check whether every value of two arrays is the same.</p>


<p>The <a href="https://github.com/mneedham/algorithms2/blob/master/shortestpath/shortestpaths-simple.py">code is on github</a> and the running time is now down from 27 seconds to 5 seconds per shortest path which is pretty cool I think!</p>

