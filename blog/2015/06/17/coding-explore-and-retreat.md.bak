+++
draft = false
date="2015-06-17 17:23:10"
title="Coding: Explore and retreat"
tag=['coding']
category=['Coding']
+++

<p>When refactoring code or looking for the best way to integrate a new piece of functionality I generally favour a small steps/incremental approach but recent experiences have led me to believe that this isn't always the quickest approach.
</p>


<p>
Sometimes it seems to make more sense to go on little discovery missions in the code, make some bigger steps and then if necessary retreat and  revert our changes and apply the lessons learnt on our next discovery mission. This technique which isn't anything novel but I think is quite effective.
</p>


<p>
<a href="https://twitter.com/mesirii">Michael</a> and I were recently looking at the <a href="http://www.ludowaltman.nl/slm/">Smart Local Moving algorithm</a> which is used for community detection in large networks and decided to refactor the code to make sure we understood how it worked. When we started the outline of the main class was <a href="https://github.com/mneedham/slm/blob/3e8468f3598ce9f61b2be32e2953890d1d497a4b/src/main/java/Network.java">like this</a>:
</p>



~~~java

public class Network implements Cloneable, Serializable
{
    private static final long serialVersionUID = 1;

    private int numberOfNodes;
    private int[] firstNeighborIndex;
    private int[] neighbor;
    private double[] edgeWeight;
    private double totalEdgeWeightSelfLinks;
    private double[] nodeWeight;
    private int nClusters;
    private int[] cluster;

    private double[] clusterWeight;
    private int[] numberNodesPerCluster;
    private int[][] nodePerCluster;
    private boolean clusteringStatsAvailable;
...
}
~~~

<p>
My initial approach was to put methods around things to make it a bit easier to understand and then step by step replace each of those fields with nodes and relationships. I spent the first couple of hours doing this and while it was making the code more readable it wasn't progressing very quickly and I wasn't much wiser about how the code worked.
</p>


<p>
Michael and I paired on it for a few hours and he adopted a slightly different but more successful approach where we looked at slightly bigger chunks of code e.g. all the loops that used the <cite>firstNeighborIndex</cite> field and then created a hypothesis of what that code was doing.
</p>


<p>
In this case <cite>firstNeighborIndex</cite> acts as an offset into <cite>neighbor</cite> and is used to iterate through a node's relationships. We thought we could probably replace that with something more similar to the <a href="http://neo4j.com/">Neo4j</a> model where you have classes for nodes and relationships and a node has a method which returns a collection of relationships.
</p>


<p>
We tried tearing out everywhere that used those two fields and replacing them with our new nodes/relationships code but that didn't work because we hadn't realised that <cite>edgeWeight</cite> and <cite>nodeWeight</cite> are also tied to the contents of the original fields.
</p>


<p>
We therefore needed to retreat and try again. This time I put the new approach alongside the existing approach and then slowly replaced existing bits of code. 
</p>


<p>
Along the way I came up with other ideas about how to restructure the code, tried some more bigger leaps to validate my ideas and then moved back into incremental mode again.
</p>


<p>In summary I've found the combination of incrementally changing code and going on bigger exploratory missions works quite well.
</p>
 

<p>
Now I'm trying to work out when each approach is appropriate and I'll write that up when I learn more! You can see my progress <a href="https://github.com/mneedham/slm/commits/master">via the github commits</a>.
</p>

