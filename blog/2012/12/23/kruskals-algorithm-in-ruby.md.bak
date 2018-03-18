+++
draft = false
date="2012-12-23 14:18:53"
title="Kruskal's Algorithm in Ruby"
tag=['ruby', 'algorithms', 'kruskal']
category=['Algorithms']
+++

<p>Last week I wrote a couple of posts showing <a href="http://www.markhneedham.com/blog/2012/12/15/prims-algorithm-using-a-heappriority-queue-in-ruby/">different</a> <a href="http://www.markhneedham.com/blog/2012/12/15/prims-algorithm-in-ruby/">implementations</a> of <a href="http://en.wikipedia.org/wiki/Prim's_algorithm">Prim's algorithm</a> - an algorithm using to find a minimum spanning tree in a graph - and a similar algorithm is <a href="http://en.wikipedia.org/wiki/Kruskal's_algorithm">Kruskal's algorithm</a>.</p>

<p>Kruskal's algorithm also finds a minimum spanning tree but it goes about it in a slightly different way.</p>

<p>Prim's algorithm takes an approach whereby we select nodes and then find connecting edges until we've covered all the nodes. Kruskal's algorithm, on the other hand, drives from the edges of lowest costs and <strong>makes sure that we don't create a cycle</strong> in our spanning tree by adding an edge to it.</p>

<p>The pseudocode for Kruskal's algorithm reads like so:</p>

<ul>
<li>sort edges <cite>E</cite> in order of increasing cost</li>
<li>let <cite>T</cite> = minimum spanning tree, <cite>m</cite> = number of edges</li>
<li>for <cite>i</cite>=1 to <cite>m</cite>:
<ul>
<li>let <cite>e</cite> = selected edge <cite>(u,v)</cite></li>
<li>if there's no way to go between <cite>u</cite> and <cite>v</cite> using edges in <cite>T</cite>:
<ul>
<li>add <cite>e</cite> to <cite>T</cite></li>
</ul>
</li>
</ul>
</li>
<li>return <cite>T</cite></li>
</ul>
<p>The <a href="https://github.com/mneedham/algorithms2/blob/master/kruskals.rb">full code </a>is on github and the outline of the algorithm reads like so:</p>


~~~ruby

@minimum_spanning_tree = []

edges = file.drop(1).
        map { |x| x.gsub(/\n/, "").split(" ").map(&:to_i) }.
        map { |one, two, weight| { :from => one, :to => two, :weight => weight}}.
        sort_by { |x| x[:weight]}
                     
edges.each do |edge|
  @minimum_spanning_tree << edge unless has_cycles edge
end
~~~
<p>The main bit of code is a variation on depth first search to check if adding an edge creates a cycle which would mean we're adding an edge which isn't needed as part of a minimum spanning tree.</p>


~~~ruby

def has_cycles(edge)
  node_one, node_two = edge[:from], edge[:to]
  @minimum_spanning_tree.each { |x| x[:explored] = false }
  cycle_between(node_one, node_two, @minimum_spanning_tree.dup)
end

def cycle_between(one, two, edges)
  adjacent_edges = edges.select { |edge| edge[:to] == one || edge[:from] == one}
  return false if adjacent_edges.empty?
  adjacent_edges.reject {|edge| edge[:explored] }.each do |edge|
    edge[:explored] = true
    other_node = (edge[:from] == one) ? edge[:to] : edge[:from]
    return true if other_node == two || cycle_between(other_node, two, edges)
  end
  false
end
~~~
<p><cite>cycle_between</cite> is the <a href="http://en.wikipedia.org/wiki/Depth-first_search">depth first search</a> but we're using it to tell us whether there's already a path between two nodes in the graph and we exit as soon as we determine that.</p>

<p>I added some code on line 3 to reset the <cite>explored</cite> status of edges each time that <cite>has_cycles</cite> is called but I'm not sure why this is necessary because I am making a copy of <cite>@minimum spanning_tree</cite> (on line 4) before mutating it.</p>

<p>Otherwise I think this is a fairly standard solution. If we wanted to go from node 1 to node 3 and we had the following edges: 1 -> 4 -> 5 -> 3 we'd make these method calls:</p>


~~~ruby

# excluding weights and explored status for brevity
cycle_between(1,3, [{:from => 1, :to => 4}, {:from => 4, :to => 5}, {:from => 5, :to => 3})
cycle_between(4,3, [{:from => 1, :to => 4}, {:from => 4, :to => 5}, {:from =>; 5, :to => 3})
cycle_between(5,3, [{:from => 1, :to => 4}, {:from => 4, :to => 5}, {:from => 5, :to => 3})
~~~
<p>The function would exit on that last iteration because we'd match our target node '3'.</p>

<p>This algorithm wasn't one of the assignments for the class but I used the same data set that was provided for Prim's algorithm and was able to get the same output so I figure it works!</p>

