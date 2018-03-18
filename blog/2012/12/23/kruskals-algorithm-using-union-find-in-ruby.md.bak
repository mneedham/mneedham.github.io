+++
draft = false
date="2012-12-23 21:43:42"
title="Kruskal's Algorithm using union find in Ruby"
tag=['ruby', 'algorithms', 'kruskal']
category=['Algorithms']
+++

<p>I recently wrote a blog post describing <a href="http://www.markhneedham.com/blog/2012/12/23/kruskals-algorithm-in-ruby/">my implementation</a> of <a href="http://en.wikipedia.org/wiki/Kruskal's_algorithm">Kruskal's algorithm</a> - a greedy algorithm using to find a minimum spanning tree (MST) of a graph - and while it does the job it's not particularly quick.</p>
 

<p>It takes 20 seconds to calculate the MST for a 500 node, ~2000 edge graph.</p>


<p>One way that we can improve the performance of the algorithm is by storing the MST in a union find/<a href="http://en.wikipedia.org/wiki/Disjoint-set_data_structure">disjoint set</a> data structure.</p>


<p>To refresh, Kruskal's algorithm does the following:</p>


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

<p>In the first version of the algorithm we stored the MST in an array and then we did a depth first search to check that adding an edge to the array wasn't going to create a cycle which would mean we no longer had an MST.</p>


<p>As I understand it the way that we use the union find data structure is that we start out with <cite>n</cite> connected components i.e. every node is in its own connected component.</p>


<p>We then merge these components together as we come across new edges which connect nodes in different components until we only have one component left at which point we should have our MST.</p>


<ul>
<li>sort edges <cite>E</cite> in order of increasing cost</li>
<li>initialise union-find <cite>uf</cite> with <cite>n</cite> connected components</li>
<li>let <cite>T</cite> = minimum spanning tree, <cite>m</cite> = number of edges</li>
<li>for <cite>i</cite>=1 to <cite>m</cite>:
<ul>
<li>let <cite>e</cite> = selected edge <cite>(u,v)</cite></li>
<li>if <cite>u</cite> and <cite>v</cite> not in same connected component in <cite>uf</cite>:
<ul>
<li>merge <cite>u</cite> and <cite>v</cite> into same connected component in <cite>uf</cite></li>
<li>add <cite>e</cite> to <cite>T</cite></li>
</ul>
</li>
</ul>
</li>
<li>return <cite>T</cite></li>
</ul>

<p>I came across <a href="https://github.com/mluckeneder/Union-Find-Ruby">this bit of code</a> written by Michael Luckeneder which implements the union find data structure in Ruby and adapted that slightly to fit the nomenclature used in the <a href="https://class.coursera.org/algo2-2012-001/class">Algorithms 2</a> videos.</p>


<p>The union find data structure looks like this:</p>



~~~ruby

class UnionFind
  def initialize(n)
    @leaders = 1.upto(n).inject([]) { |leaders, i| leaders[i] = i; leaders }
  end
  
  def connected?(id1,id2)
    @leaders[id1] == @leaders[id2]
  end
  
  def union(id1,id2)
    leader_1, leader_2 = @leaders[id1], @leaders[id2]
    @leaders.map! {|i| (i == leader_1) ? leader_2 : i }
  end
end
~~~

<p>We have two methods:</p>


<ul>
<li><cite>connected?</cite> which we use to check whether or not two nodes are in the same connected component.</li>
<li><cite>union</cite> which we use to put two nodes into the same connected component.</li>
</ul>

<p>The way it's implemented is that we have a collection of 'leaders' and initially each node is its own leader. As we find edges which belong in the MST we call <cite>union</cite> passing the two nodes as arguments. After this method executes every node which has the same leader as the first node will now instead have the same leader as the second node.</p>


<p>For example if we have a simple graph with edges 1 -> 2 -> 3 -> 4 -> 5 our initial union find data structure would look like this:</p>



~~~ruby

> uf = UnionFind.new 5
=> #<UnionFind:0x45e5a9b3 @leaders=[nil, 1, 2, 3, 4, 5]>
~~~

<p>At this stage each node is in its own connected component but if we process the edge 1 -> 2 we'd first check if those two nodes were already in the same connected component:</p>



~~~ruby

> uf.connected?(1,2)
=> false
~~~

<p>Given that they aren't we can call <cite>union</cite>:</p>



~~~ruby

> uf.union(1,2)
=> [nil, 2, 2, 3, 4, 5]
~~~

<p>As we can see from the output nodes 1 & 2 now both have the same leader since they are in the same connected component while  the other nodes still remain on their own.</p>


<p>We could then process the 2 -> 3 edge which would put nodes 1, 2 & 3 together:</p>



~~~ruby

> uf.union(2,3)
=> [nil, 3, 3, 3, 4, 5]
~~~

<p>The outline for Kruskal's algorithm which makes use of this data structure is like so:</p>



~~~ruby

set = UnionFind.new number_of_nodes

@minimum_spanning_tree = []

edges = file.drop(1).
        map { |x| x.gsub(/\n/, "").split(" ").map(&:to_i) }.
        map { |one, two, weight| { :from => one, :to => two, :weight => weight}}.
        sort_by { |x| x[:weight]}
                     
edges.each do |edge|
  if !set.connected?(edge[:from], edge[:to])
    @minimum_spanning_tree << edge 
    set.union(edge[:from], edge[:to])
  end  
end

puts "MST: #{@minimum_spanning_tree}"
puts "Cost: #{@minimum_spanning_tree.inject(0) { |acc, x| acc + x[:weight]}}"
~~~

<p>This version of the algorithm runs in 1.9 seconds, a significant improvement on the initial version. The <a href="https://github.com/mneedham/algorithms2/blob/master/kruskals_union_set.rb">full code is on github</a> as usual!</p>

