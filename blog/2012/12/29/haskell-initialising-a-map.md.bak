+++
draft = false
date="2012-12-29 19:27:46"
title="Haskell: Initialising a map"
tag=['haskell']
category=['Haskell']
+++

<p>I've been converting a variation of Kruskal's algorithm from <a href="https://github.com/mneedham/algorithms2/blob/master/clustering_big_graph_bitwise.rb">Ruby</a> into <a href="https://github.com/mneedham/algorithms2/blob/master/clustering.hs">Haskell</a> and one thing I needed to do was create a map of binary based values to node ids.</p>


<p>In Ruby I wrote the following code to do this:</p>



~~~ruby

nodes = [1,2,5,7,2,4]
@magical_hash = {}
nodes.each_with_index do |node, index|
  @magical_hash[node] ||= []
  @magical_hash[node] << index
end

=> {1=>[0], 2=>[1, 4], 5=>[2], 7=>[3], 4=>[5]}
~~~

<p>From looking at the documentation it seemed like the easiest way to do this in Haskell would be to convert the nodes into an appropriate list and then call the <cite><a href="http://www.haskell.org/ghc/docs/6.12.2/html/libraries/containers-0.3.0.0/Data-Map.html#v%3AfromList">fromList</a></cite> function to build the map.</p>


<p>I needed to get the data to look like this:</p>



~~~haskell

> let nodesMap = Data.Map.fromList [(1, [0]), (2, [1,4]), (5, [2]), (7, [3]), (4, [5])]
> Data.Map.assocs nodesMap
[(1,[0]),(2,[1,4]),(4,[5]),(5,[2]),(7,[3])]
~~~

<p>The first step was to create a list of tuples with the nodes ids and values:</p>



~~~haskell

> zip [0..] [1,2,5,7,2,4]
[(0,1),(1,2),(2,5),(3,7),(4,2),(5,4)]
~~~

<p>I wanted group the collection by value so that in this instance I could have the 2 nodes with a value of '2' mapping from the same key in the map.</p>


<p>The following code helped do that:</p>



~~~haskell

groupIgnoringIndex = groupBy (\(_,x) (_,y) -> x == y)   
sortIgnoringIndex = sortBy (\(_,x) (_,y) -> x `compare` y)
~~~


~~~haskell

> (groupIgnoringIndex . sortIgnoringIndex) (zip [0..] [1,2,5,7,2,4])
[[(0,1)],[(1,2),(4,2)],[(5,4)],[(2,5)],[(3,7)]]
~~~

<p>I wrote the following function to convert that collection into one that could be passed to <cite>fromList</cite>:</p>



~~~haskell

asMapEntry :: [(Int, Int)] -> (Int, [Int])
asMapEntry nodesWithIndexes = ((snd . head) nodesWithIndexes, 
                              foldl (\acc (x,_) -> acc ++ [x]) [] nodesWithIndexes)
~~~


~~~haskell

> asMapEntry [(1,2),(4,2)]
(2,[1,4])
~~~

<p>We can then put all those functions together into the following top level function:</p>



~~~haskell

toMap :: [Int] -> Map Int [Int]
toMap nodes = Data.Map.fromList $ map asMapEntry $ (groupIgnoringIndex . sortIgnoringIndex) nodesWithIndexes
              where nodesWithIndexes = (zip [0..] nodes)
~~~


~~~haskell

> Data.Map.assocs $ toMap [1,2,5,7,2,4]
[(1,[0]),(2,[4,1]),(4,[5]),(5,[2]),(7,[3])]
~~~

<p>I haven't properly investigated all the functions available in the <cite>Data.Map</cite> package but my gut feeling is there must be a better way to do this - the sort/group combination is ugly in the extreme!</p>

