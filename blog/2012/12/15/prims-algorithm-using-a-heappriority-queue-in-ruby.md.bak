+++
draft = false
date="2012-12-15 16:31:05"
title="Prim's algorithm using a heap/priority queue in Ruby"
tag=['algo-class', 'algorithms']
category=['Algorithms']
+++

<p>I recently wrote a blog post describing <a href="http://www.markhneedham.com/blog/2012/12/15/prims-algorithm-in-ruby/">my implementation of Prim's Algorithm</a> for the <a href="https://class.coursera.org/algo2-2012-001">Algorithms 2</a> class and while it comes up with the right answer for the supplied data set it takes almost 30 seconds to do so!</p>

<p>In one of the lectures Tim Roughgarden points out that we're doing the same calculations multiple times to work out the next smallest edge to include in our minimal spanning tree and could use a heap to speed things up.</p>

<p>A heap works well in this situation because one of the reasons we might use a heap is to speed up repeated minimum computations i.e. working out the minimum weighted edge to add to our spanning tree.</p>

<p>The pseudocode for the Prim's algorithm which uses a heap reads like this:</p>

<ul>
<li>Let <cite>X</cite> = nodes covered so far, <cite>V</cite> = all the nodes in the graph, <cite>E</cite> = all the edges in the graph</li>
<li>Pick an arbitrary initial node <cite>s</cite> and put that into <cite>X</cite></li>
<li>for <cite>v</cite> ∈ <cite>V</cite> - <cite>X</cite>
<ul>
<li>key[v] = cheapest edge <cite>(u,v)</cite> with <cite>v</cite> ∈ <cite>X</cite></li>
</ul>
</li>
<li>while <cite>X</cite> ≠ <cite>V</cite>:
<ul>
<li>let <cite>v</cite> = extract-min(heap) <em>(i.e. v is the node which has the minimal edge cost into <cite>X</cite>)</em></li>
<li>Add <cite>v</cite> to <cite>X</cite></li>
<li>for each edge <cite>v, w</cite> ∈ <cite>E</cite>
<ul>
<li>if w ∈ <cite>V</cite> - <cite>X</cite> (<em>i.e. w is a node which hasn't yet been covered)</em>
<ul>
<li>Delete <cite>w</cite> from heap</li>
<li>recompute key[w] = min(key[w], weight(v, w)) <em>(key[w] would only change if the weight of the edge (v,w) is less than the current weight for that key).</em></li>
<li>reinsert <cite>w</cite> into the heap</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>We store the uncovered nodes in the heap and set their priority to be the cheapest edge from that node into the set of nodes which we're already covered.</p>

<p>I came across the <a href="http://rubydoc.info/gems/PriorityQueue/0.1.2/frames">PriorityQueue</a> gem which actually seems to be better than a heap because we can have the node as the key and then set the priority of the key to be the edge weight. When you extract the minimum value from the priority queue it makes use of this priority to return the minimum one.</p>

<p>The outline of my solution to this problem looks like this:</p>


~~~ruby

MAX_VALUE =  (2**(0.size * 8 -2) -1)

adjacency_matrix = create_adjacency_matrix
@nodes_spanned_so_far, spanning_tree_cost = [1], 0

heap = PriorityQueue.new
nodes_left_to_cover.each do |node|
  cheapest_nodes = get_edges(adjacency_matrix, node-1).
                   select { |_, other_node_index| @nodes_spanned_so_far.include?(other_node_index + 1) } || []
  
  cheapest = cheapest_nodes.inject([]) do |all_edges, (weight, index)|
    all_edges << { :start => node, :end => index + 1, :weight => weight }
    all_edges
  end.sort { |x,y| x[:weight]  y[:weight] }.first
  
  weight = !cheapest.nil? ? cheapest[:weight]: MAX_VALUE
  heap[node] = weight
end

while !nodes_left_to_cover.empty?
  cheapest_node, weight = heap.delete_min
  spanning_tree_cost += weight
  @nodes_spanned_so_far << cheapest_node
  
  edges_with_potential_change = get_edges(adjacency_matrix, cheapest_node-1).
                                reject { |_, node_index| @nodes_spanned_so_far.include?(node_index + 1) }
  edges_with_potential_change.each do |weight, node_index|
    heap.change_priority(node_index+1, 
                         [heap.priority(node_index+1), adjacency_matrix[cheapest_node-1][node_index]].min)
  end
end

puts "total spanning tree cost #{spanning_tree_cost}"
~~~

<p>I couldn't see a way to keep track of the edges that comprise the minimal spanning tree so in this version I've created a variable which keeps tracking of the edge weights as we go rather than computing it at the end.</p>


<p>We start off by initialising the priority queue to contain entries for each of the nodes in the graph.</p>


<p>We do this by finding the edges that go from each node to the nodes that we've already covered. In this case the only node we've covered is node 1 so the priorities for most nodes will be MAX_VALUE and for nodes which have an edge to node 1 it'll be the weight of that edge.</p>


<p>While we still have nodes left to cover we take the next node with the cheapest weight from the priority queue and add it to the collection of nodes that we've covered. We then iterate through the nodes which have an edge to the node we just removed and update the priority queue if necessary.</p>


<p>The time taken for this version of the algorithm to run against the data set was 0.3 seconds as compared to the 29 seconds of the naive implementation.</p>



<p>As usual the <a href="https://github.com/mneedham/algorithms2/blob/master/prims_heap.rb">code is on github</a> - I need to figure out how to keep track of the edges so if anyone has any suggestions that'd be cool.</p>

