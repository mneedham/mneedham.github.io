+++
draft = false
date="2012-12-15 02:51:14"
title="Prim's Algorithm in Ruby"
tag=['algorithms']
category=['Algorithms']
+++

<p>One of the first programming assignments of the <a href="https://class.coursera.org/algo2-2012-001/class">Algorithms 2</a> course was to code <a href="http://en.wikipedia.org/wiki/Prim's_algorithm">Prim's algorithm</a> - a greedy algorithm used to find the minimum spanning tree of a connected weighted undirected graph.</p>

<p>In simpler terms we need to find the path of least cost which connects all of the nodes together and there can't be any cycles in that path.</p>

<p>Wikipedia has a neat diagram which <a href="http://en.wikipedia.org/wiki/Minimum_spanning_tree">shows this more clearly</a>:</p>

<div align="center"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Minimum_spanning_tree.svg/300px-Minimum_spanning_tree.svg.png" alt="" /></div>
<p>The pseudocode for the algorithm is as follows:</p>

<ul>
<li>Let <cite>X</cite> = nodes covered so far, <cite>T</cite> = edges covered so far, <cite>V</cite> = all the nodes in the graph</li>
<li>Pick an initial arbitrary node <cite>s</cite> - it doesn't matter which one it is</li>
<li>while <cite>X</cite> ≠ <cite>V</cite>:
<ul>
<li>let <cite>e</cite> = <cite>(u,v)</cite> be the cheapest edge of the graph where <cite>u</cite> ∈ <cite>X</cite> and v ∉ <cite>X</cite> <br />i.e. <cite>u</cite> is a node that has been covered and <cite>v</cite> a node that has not yet been covered</li>
<li>Add <cite>e</cite> to <cite>T</cite></li>
<li>Add <cite>v</cite> to <cite>X</cite></li>
</ul>
</li>
</ul>
<p>At the end of the algorithm we'll have a collection of all the nodes in the graph and a collection of the edges we need to follow in order to create a minimal spanning tree. If we sum the weights of those edges we get the cost of the tree.</p>

<p>I used an <a href="http://en.wikipedia.org/wiki/Adjacency_matrix">adjacency matrix</a> to represent the graph i.e. a 2 dimensional array of size n*n (where n = number of nodes in the graph).</p>

<p>If node 0 had an edge to node 3 of weight 4 then we'd put this entry into the matrix:</p>


~~~ruby

~~~
<p>I tried to get my implementation of the algorithm to look as close to the pseudocode as possible and I ended up with the following:</p>


~~~ruby

adjacency_matrix = create_adjacency_matrix
first_edge = select_first_edge(adjacency_matrix)
@nodes_spanned_so_far, @edges = [first_edge[:start], first_edge[:end]], [first_edge]

while !nodes_left_to_cover.empty?
  cheapest_edge = find_cheapest_edge(adjacency_matrix, @nodes_spanned_so_far, number_of_nodes)
  @edges << cheapest_edge
  @nodes_spanned_so_far << cheapest_edge[:start]
end
~~~
<p>The code became a bit messy in parts because it relies on a 0 indexed array yet the names of the nodes start at 1. There's therefore loads of +1s and -1s dotted around the place.</p>

<p>The method to work out the next cheapest node looks like this:</p>


~~~ruby

def find_cheapest_edge(adjacency_matrix, nodes_spanned_so_far, number_of_nodes)
  available_nodes = (0..number_of_nodes-1).to_a.reject { |node_index| nodes_spanned_so_far.include?(node_index + 1) }
  
  cheapest_edges = available_nodes.inject([]) do |acc, node_index|
    get_edges(adjacency_matrix, node_index).select { |_, other_node_index| nodes_spanned_so_far.include?(other_node_index + 1) }.each do |weight, other_node_index|
      acc << { :start => node_index + 1, :end => other_node_index + 1, :weight => weight }
    end
    acc
  end
    
  cheapest_edges.sort { |x,y| x[:weight]  y[:weight] }.first
end

def get_edges(adjacency_matrix, node_index)
  adjacency_matrix[node_index].each_with_index.reject { |edge, index| edge.nil? }
end
~~~
<p>We first get all the nodes which haven't already been spanned and then build up a collection of the edges between nodes we've already spanned and ones that we haven't.</p>

<p>The other bit of interesting code is the creation of the adjacency matrix at the beginning:</p>


~~~ruby

def create_adjacency_matrix
  adjacency_matrix = [].tap { |m| number_of_nodes.times { m << Array.new(number_of_nodes) } }
  file.drop(1).map { |x| x.gsub(/\n/, "").split(" ").map(&:to_i) }.each do |(node1, node2, weight)|
    adjacency_matrix[node1 - 1][node2 - 1] = weight
    adjacency_matrix[node2 - 1][node1 - 1] = weight
  end
  adjacency_matrix
end
~~~
<p>Here we are first parsing the file which involves skipping the first header line and the converting it into a collection of integer arrays representing the two nodes and their corresponding edge weight.</p>

<p>We then put two entries into the adjacency matrix, one entry from node A to node B and one entry from node B to node A. The reason we do this is that this is an undirected graph so we can go either way between the nodes.</p>

<p>To work out the cost of the minimum spanning tree I use this line of code at the end:</p>


~~~ruby

puts "edges: #{@edges}, total spanning tree cost #{@edges.inject(0) {|acc, edge| acc + edge[:weight]}}"
~~~
<p>My full solution is on <a href="https://github.com/mneedham/algorithms2/blob/master/prims.rb">github</a> so if anyone has any suggestions/improvements they're always welcome.</p>

