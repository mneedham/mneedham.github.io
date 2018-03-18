+++
draft = false
date="2016-08-22 21:12:54"
title="Neo4j/scikit-learn: Calculating the cosine similarity of Game of Thrones episodes"
tag=['machine-learning-2', 'python']
category=['neo4j', 'Machine Learning', 'Python']
+++

<p>
A couple of months ago <a href="https://twitter.com/praveenasekhar">Praveena</a> and I created a <a href="https://github.com/mneedham/neo4j-got">Game of Thrones dataset</a> to use in a workshop and I thought it'd be fun to run it through some machine learning algorithms and hopefully find some interesting insights.
</p>


<p>
The dataset is <a href="https://github.com/mneedham/neo4j-got/tree/master/data/import">available as CSV files</a> but for this analysis I'm assuming that it's already been imported into neo4j. If you want to import the data you can run the tutorial by typing the following into the query bar of the neo4j browser:
</p>



~~~text

:play http://guides.neo4j.com/got
~~~

<p>
Since we don't have any training data we'll be using unsupervised learning methods, and we'll start simple by calculating the similarity of episodes based character appearances. We'll be using <a href="http://scikit-learn.org/stable/">scitkit-learn</a>'s <a href="http://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html">cosine similarity function</a> to determine episode similarity. 
</p>


<p>
Christian Perone has <a href="http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/">an excellent blog post</a> explaining how to use cosine similarity on text documents which is well worth a read. We'll be using a similar approach here, but instead of building a TF/IDF vector for each document we're going to create a vector indicating whether a character appeared in an episode or not.
</p>


<p>
e.g. imagine that we have 3 characters - A, B, and C - and 2 episodes. A and B appear in the first episode and B and C appear in the second episode. We would represent that with the following vectors:
</p>



~~~text

Episode 1 = [1, 1, 0]
Episode 2 = [0, 1, 1]
~~~

<p>
We could then calculate the cosine similarity between these two episodes like this:
</p>



~~~python

>>> from sklearn.metrics.pairwise import cosine_similarity
>>> one = [1,1,0]
>>> two = [0,1,1]

>>> cosine_similarity([one, two])
array([[ 1. ,  0.5],
       [ 0.5,  1. ]])
~~~

<p>
So this is telling us that Episode 1 is 100% similar to Episode 1, Episode 2 is 100% similar to itself as well, and Episodes 1 and 2 are 50% similar to each other based on the fact that they both have an appearance of Character B. 
</p>


<p>Note that the character names aren't even mentioned at all, they are implicitly a position in the array. This means that when we use our real dataset we need to ensure that the characters are in the same order for each episode, otherwise the calculation will be meaningless!
</p>


<p>
In neo4j land we have an <cite>APPEARED_IN</cite> relationship between a character and each episode that they appeared in. We can therefore write the following code using the Python driver to get all pairs of episodes and characters:
</p>



~~~python

from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

rows = session.run("""
    MATCH (c:Character), (e:Episode)
    OPTIONAL MATCH (c)-[appearance:APPEARED_IN]->(e)
    RETURN e, c, appearance
    ORDER BY e.id, c.id""")
~~~

<p>We can iterate through the rows to see what the output looks like:</p>



~~~python

>>> for row in rows:
        print row

<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5415 labels=set([u'Character']) properties={u'name': u'Addam Marbrand', u'id': u'/wiki/Addam_Marbrand'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5882 labels=set([u'Character']) properties={u'name': u'Adrack Humble', u'id': u'/wiki/Adrack_Humble'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=6747 labels=set([u'Character']) properties={u'name': u'Aegon V Targaryen', u'id': u'/wiki/Aegon_V_Targaryen'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5750 labels=set([u'Character']) properties={u'name': u'Aemon', u'id': u'/wiki/Aemon'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5928 labels=set([u'Character']) properties={u'name': u'Aeron Greyjoy', u'id': u'/wiki/Aeron_Greyjoy'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5503 labels=set([u'Character']) properties={u'name': u'Aerys II Targaryen', u'id': u'/wiki/Aerys_II_Targaryen'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=6753 labels=set([u'Character']) properties={u'name': u'Alannys Greyjoy', u'id': u'/wiki/Alannys_Greyjoy'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=6750 labels=set([u'Character']) properties={u'name': u'Alerie Tyrell', u'id': u'/wiki/Alerie_Tyrell'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5753 labels=set([u'Character']) properties={u'name': u'Alliser Thorne', u'id': u'/wiki/Alliser_Thorne'}> appearance=None>
<Record e=<Node id=6780 labels=set([u'Episode']) properties={u'season': 1, u'number': 1, u'id': 1, u'title': u'Winter Is Coming'}> c=<Node id=5858 labels=set([u'Character']) properties={u'name': u'Alton Lannister', u'id': u'/wiki/Alton_Lannister'}> appearance=None>
~~~

<p>
Next we'll build a 'matrix' of episodes/characters. If a character appears in an episode then we'll put a '1' in the matrix, if not we'll put a '0':
</p>



~~~python

episodes = {}
for row in rows:
    if episodes.get(row["e"]["id"]) is None:
        if row["appearance"] is None:
            episodes[row["e"]["id"]] = [0]
        else:
            episodes[row["e"]["id"]] = [1]
    else:
        if row["appearance"] is None:
            episodes[row["e"]["id"]].append(0)
        else:
            episodes[row["e"]["id"]].append(1)
~~~

<p>Here's an example of one entry in the matrix:</p>



~~~python

>>> len(episodes)
60

>>> len(episodes[1])
638

>>> episodes[1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
~~~

<p>
From this output we learn that there are 60 episodes and 638 characters in Game of Thrones so far. We can also see which characters appeared in the first episode, although it's a bit tricky to work out which index in the array corresponds to each character.
</p>


<p>
The next thing we're going to do is calculate the cosine similarity between episodes. Let's start by seeing how similar the first episode is to all the others:
</p>



~~~python

>>> all = episodes.values()

>>> cosine_similarity(all[0:1], all)[0]
array([ 1.        ,  0.69637306,  0.48196269,  0.54671752,  0.48196269,
        0.44733753,  0.31707317,  0.42340087,  0.34989921,  0.43314808,
        0.36597766,  0.18421252,  0.30961158,  0.2328101 ,  0.30616181,
        0.41905818,  0.36842504,  0.35338088,  0.18376917,  0.3569686 ,
        0.2328101 ,  0.34539847,  0.25043516,  0.31707317,  0.25329221,
        0.33342786,  0.34921515,  0.2174909 ,  0.2533473 ,  0.28429311,
        0.23026565,  0.22310537,  0.22365301,  0.23816275,  0.28242289,
        0.16070148,  0.24847093,  0.21434648,  0.03582872,  0.21189672,
        0.15460414,  0.17161693,  0.15460414,  0.17494961,  0.1234662 ,
        0.21426863,  0.21434648,  0.18748505,  0.15308091,  0.20161946,
        0.19877675,  0.30920827,  0.21058466,  0.19127301,  0.24607943,
        0.18033393,  0.17734311,  0.16296707,  0.18740851,  0.23995201])
~~~

<p>
The first entry in the array indicates that episode 1 is 100% similar to episode 1 which is a good start. It's 69% similar to episode 2 and 48% similar to episode 3. We can sort that array to work out which episodes it's most similar to:
</p>



~~~python

>>> for idx, score in sorted(enumerate(cosine_similarity(all[0:1], all)[0]), key = lambda x: x[1], reverse = True)[:5]:
        print idx, score

0 1.0
1 0.696373059207
3 0.546717521051
2 0.481962692712
4 0.481962692712
~~~

<p>
Or we can see how similar the last episode of season 6 is compared to the others:
</p>



~~~python

>>> for idx, score in sorted(enumerate(cosine_similarity(all[59:60], all)[0]), key = lambda x: x[1], reverse = True)[:5]:
        print idx, score

59 1.0
52 0.500670191678
46 0.449085146211
43 0.448218732478
49 0.446296233312
~~~

<p>
I found it a bit painful exploring similarities like this so I decided to write them into neo4j instead and then write a query to find the most similar episodes. The following query creates a <cite>SIMILAR_TO</cite> relationship between episodes and sets a <cite>score</cite> property on that relationship:
</p>



~~~python

>>> episode_mapping = {}
>>> for idx, episode_id in enumerate(episodes):
        episode_mapping[idx] = episode_id

>>> for idx, episode_id in enumerate(episodes):
        similarity_matrix = cosine_similarity(all[idx:idx+1], all)[0]
        for other_idx, similarity_score in enumerate(similarity_matrix):
            other_episode_id = episode_mapping[other_idx]
            print episode_id, other_episode_id, similarity_score
            if episode_id != other_episode_id:
                session.run("""
                    MATCH (episode1:Episode {id: {episode1}}), (episode2:Episode {id: {episode2}})
                    MERGE (episode1)-[similarity:SIMILAR_TO]-(episode2)
                    ON CREATE SET similarity.score = {similarityScore}
                    """, {'episode1': episode_id, 'episode2': other_episode_id, 'similarityScore': similarity_score})

    session.close()
~~~

<p>
The <cite>episode_mapping</cite> dictionary is needed to map from episode ids to indices e.g. episode 1 is at index 0. 
</p>


<p>
If we want to find the most similar pair of episodes in Game of Thrones we can execute the following query:
</p>



~~~cypher

MATCH (episode1:Episode)-[similarity:SIMILAR_TO]-(episode2:Episode)
WHERE ID(episode1) > ID(episode2)
RETURN "S" + episode1.season + "E" + episode1.number AS ep1, 
       "S" + episode2.season + "E" + episode2.number AS ep2, 
       similarity.score AS score
ORDER BY similarity.score DESC
LIMIT 10

╒═════╤════╤══════════════════╕
│ep1  │ep2 │score             │
╞═════╪════╪══════════════════╡
│S1E2 │S1E1│0.6963730592072543│
├─────┼────┼──────────────────┤
│S1E4 │S1E3│0.6914173051223086│
├─────┼────┼──────────────────┤
│S1E9 │S1E8│0.6869464497590777│
├─────┼────┼──────────────────┤
│S2E10│S2E8│0.6869037302955034│
├─────┼────┼──────────────────┤
│S3E7 │S3E6│0.6819943394704735│
├─────┼────┼──────────────────┤
│S2E7 │S2E6│0.6813598225089799│
├─────┼────┼──────────────────┤
│S1E10│S1E9│0.6796436827080401│
├─────┼────┼──────────────────┤
│S1E5 │S1E4│0.6698105143372364│
├─────┼────┼──────────────────┤
│S1E10│S1E8│0.6624062584864754│
├─────┼────┼──────────────────┤
│S4E5 │S4E4│0.6518358737330705│
└─────┴────┴──────────────────┘
~~~

<p>And the least popular?</p>



~~~cypher

MATCH (episode1:Episode)-[similarity:SIMILAR_TO]-(episode2:Episode)
WHERE ID(episode1) > ID(episode2)
RETURN "S" + episode1.season + "E" + episode1.number AS ep1, 
       "S" + episode2.season + "E" + episode2.number AS ep2, 
       similarity.score AS score
ORDER BY similarity.score
LIMIT 10

╒════╤════╤═══════════════════╕
│ep1 │ep2 │score              │
╞════╪════╪═══════════════════╡
│S4E9│S1E5│0                  │
├────┼────┼───────────────────┤
│S4E9│S1E6│0                  │
├────┼────┼───────────────────┤
│S4E9│S4E2│0                  │
├────┼────┼───────────────────┤
│S4E9│S2E9│0                  │
├────┼────┼───────────────────┤
│S4E9│S2E4│0                  │
├────┼────┼───────────────────┤
│S5E6│S4E9│0                  │
├────┼────┼───────────────────┤
│S6E8│S4E9│0                  │
├────┼────┼───────────────────┤
│S4E9│S4E6│0                  │
├────┼────┼───────────────────┤
│S3E9│S2E9│0.03181423814878889│
├────┼────┼───────────────────┤
│S4E9│S1E1│0.03582871819500093│
└────┴────┴───────────────────┘
~~~

<p>The output of this query suggests that there are no common characters between 8 pairs of episodes which at first glance sounds surprising. Let's write a query to check that finding:
</p>



~~~cypher

MATCH (episode1:Episode)<-[:APPEARED_IN]-(character)-[:APPEARED_IN]->(episode2:Episode)
WHERE episode1.season = 4 AND episode1.number = 9 AND episode2.season = 1 AND episode2.number = 5
return episode1, episode2

(no changes, no rows)
~~~

<p>
It's possible I made a mistake with the scraping of the data but from a quick look over <a href="http://gameofthrones.wikia.com/wiki/The_Watchers_on_the_Wall">the Wiki page</a> I don't think I have. I found it interesting that Season 4 Episode 9 shows up on 9 of the top 10 least similar pairs of episodes.
</p>


<p>
Next I'm going to cluster the episodes based on character appearances, but this post is long enough already so that'll have to wait for another post another day. 
</p>

