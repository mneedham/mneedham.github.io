+++
draft = false
date="2016-08-25 22:07:25"
title="scikit-learn: Trying to find clusters of Game of Thrones episodes"
tag=['scikit-learn']
category=['Machine Learning', 'Python']
+++

<p>
In my last post I showed how to <a href="http://www.markhneedham.com/blog/2016/08/22/neo4jscikit-learn-calculating-the-cosine-similarity-of-game-of-thrones-episodes/">find similar Game of Thrones episodes based on the characters that appear in different episodes</a>. This allowed us to find similar episodes on an episode by episode basis, but I was curious whether there were <strong>groups of similar episodes</strong> that we could identify.
</p>


<p>scikit-learn provides several clustering algorithms that can run over our episode vectors and hopefully find clusters of similar episodes. A clustering algorithm groups similar documents together, where similarity is based on calculating a 'distance' between documents. Documents separated by a small distance would be in the same cluster, whereas if there's a large distance between episodes then they'd probably be in different clusters.</p>
 

<p>The simplest variant is <a href="http://scikit-learn.org/stable/modules/clustering.html#k-means">K-means</a> clustering:
</p>


<blockquote>
The KMeans algorithm clusters data by trying to separate samples in n groups of equal variance, minimizing a criterion known as the inertia or within-cluster sum-of-squares. This algorithm requires the number of clusters to be specified.
</blockquote>

<p>
The output from the algorithm is a list of labels which correspond to the cluster assigned to each episode.
</p>


<p>
Let's give it a try on the Game of Thrones episodes. We'll start from the 2 dimensional array of episodes/character appearances that we created in the <a href="http://www.markhneedham.com/blog/2016/08/22/neo4jscikit-learn-calculating-the-cosine-similarity-of-game-of-thrones-episodes/">previous post</a>. 
</p>



~~~python

>>> all.shape
(60, 638)

>>> all
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ..., 
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]])
~~~

<p>
We have a 60 (episodes) x 638 (characters) array which we can now plug into the K-means clustering algorithm:
</p>



~~~python

>>> from sklearn.cluster import KMeans

>>> n_clusters = 3
>>> km = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, n_init=1)
>>> cluster_labels = km.fit_predict(all)

>>> cluster_labels
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], dtype=int32)
~~~

<p><cite>cluster_labels</cite> is an array containing a label for each episode in the <cite>all</cite> array. The spread of these labels is as follows:
</p>



~~~python

>>> import numpy as np
>>> np.bincount(cluster_labels)
array([19, 12, 29])
~~~

<p>
i.e. 19 episodes in cluster 0, 12 in cluster 1, and 29 in cluster 2.
</p>


<h3>How do we know if the clustering is any good?</h3>

<p>
Ideally we'd have some labelled training data which we could compare our labels against, but since we don't we can measure the effectiveness of our clustering by calculating <a href="http://stackoverflow.com/questions/8102515/selecting-an-appropriate-similarity-metric-assessing-the-validity-of-a-k-means">inter-centroidal separation and intra-cluster variance</a>. 
</p>


<p>i.e. how close are the episodes to other episodes in the same cluster vs how close are they to episodes in the closest different cluster.
</p>


<p>
scikit-learn gives us a function that we can use to calculate this score - the <a href="http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#example-cluster-plot-kmeans-silhouette-analysis-py">silhouette coefficient</a>.
</p>


<p>The output of this function is a score between -1 and 1.</p>


<ul>
<li>A score of 1 means that our clustering has worked well and a document is far away from the boundary of another cluster.</li>
<li>A score of -1 means that our document should have been placed in another cluster.</li>
<li>A score of 0 means that the document is very close to the decision boundary between two clusters.</li>
</ul>

<p>I tried calculating this coefficient for some different values of K. This is what I found:</p>



~~~python

from sklearn import metrics

for n_clusters in range(2, 10):
    km = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=100, n_init=1)
    cluster_labels = km.fit_predict(all)

    silhouette_avg = metrics.silhouette_score(all, cluster_labels, sample_size=1000)
    sample_silhouette_values = metrics.silhouette_samples(all, cluster_labels)

    print n_clusters, silhouette_avg

2 0.0798610142955
3 0.0648416081725
4 0.0390877994786
5 0.020165277756
6 0.030557856406
7 0.0389677156458
8 0.0590721834989
9 0.0466170527996
~~~

<p>
The best score we manage here is 0.07 when we set the number of clusters to 2. Even our highest score is much lower than the <a href="http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#example-cluster-plot-kmeans-silhouette-analysis-py">lowest score on the documentation page</a>!
</p>


<p>
I tried it out with some higher values of K but only saw a score over 0.5 once I put the number of clusters to 40 which would mean 1 or 2 episodes per cluster at most. 
</p>


<p>
At the moment our episode arrays contain 638 elements so they're too long to visualise on a 2D silhouette plot. We'd need to apply a dimensionality reduction algorithm before doing that.
</p>


<p>
In summary it looks like character co-occurrence isn't a good way to cluster episodes. I'm curious what would happen if we flip the array on its head and try and cluster the characters instead, but that's for another day.</p>


<p>
If anyone spots anything that I've missed when reading the output of the algorithm let me know in the comments. I'm just learning by experimentation at the moment.</p>

