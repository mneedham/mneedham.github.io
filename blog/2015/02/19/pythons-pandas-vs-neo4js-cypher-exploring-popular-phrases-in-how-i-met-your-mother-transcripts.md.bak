+++
draft = false
date="2015-02-19 00:52:10"
title="Python's pandas vs Neo4j's cypher: Exploring popular phrases in How I met your mother transcripts"
tag=['neo4j', 'python']
category=['neo4j']
+++

<p>
I've previously written about <a href="http://www.markhneedham.com/blog/2015/02/15/pythonscikit-learn-calculating-tfidf-on-how-i-met-your-mother-transcripts/">extracting TF/IDF scores for phrases in documents using scikit-learn</a> and the final step in that post involved writing the words into a CSV file for analysis later on.
</p>


<p>
I wasn't sure what the most appropriate tool of choice for that analysis was so I decided to explore the data using Python's pandas library and load it into Neo4j and write some Cypher queries.
</p>


To do anything with Neo4j we need to first load the CSV file into the database. The easiest way to do that is with Cypher's LOAD CSV command. 

First we'll load the phrases in and then we'll connect them to the episodes which were previously loaded:


~~~cypher

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/projects/neo4j-himym/data/import/tfidf_scikit.csv" AS row
MERGE (phrase:Phrase {value: row.Phrase});
~~~


~~~cypher

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/projects/neo4j-himym/data/import/tfidf_scikit.csv" AS row
MATCH (phrase:Phrase {value: row.Phrase})
MATCH (episode:Episode {id: TOINT(row.EpisodeId)})
MERGE (phrase)-[:USED_IN_EPISODE {tfidfScore: TOFLOAT(row.Score)}]->(episode);
~~~

<p>Now we're ready to start writing some queries. To start with we'll write a simple query to find the top 3 phrases for each episode.
</p>


<p>In pandas this is quite easy - we just need to group by the appropriate field and then take the top 3 records in that grouping:</p>



~~~python

top_words_by_episode = df \
    .sort(["EpisodeId", "Score"], ascending = [True, False]) \
    .groupby(["EpisodeId"], sort = False) \
    .head(3)

>>> print(top_words_by_episode.to_string())

        EpisodeId              Phrase     Score
3976            1                 ted  0.262518
2912            1              olives  0.195714
2441            1            marshall  0.155515
8143            2                 ted  0.292184
5197            2              carlos  0.227454
7482            2               robin  0.195150
12551           3                 ted  0.232662
9040            3              barney  0.187255
11254           3              mcneil  0.170619
15641           4             natalie  0.562485
16763           4                 ted  0.191873
16234           4               robin  0.102671
20715           5            subtitle  0.310866
18121           5          coat check  0.181682
20861           5                 ted  0.169973
...
~~~

<p>
The cypher version looks quite similar, the main difference being that we use the <cite>COLLECT</cite> to generate an array of phrases by episode and then take the top 3:
</p>



~~~cypher

MATCH (e:Episode)<-[rel:USED_IN_EPISODE]-(phrase)
WITH e, rel, phrase
ORDER BY e.id, rel.tfidfScore DESC
RETURN e.id, e.title, COLLECT({phrase: phrase.value, score: rel.tfidfScore})[..3]
ORDER BY e.id

==> +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | e.id | e.title                                     | COLLECT({phrase: phrase.value, score: rel.tfidfScore})[..3]                                                                                                               |
==> +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | 1    | "Pilot"                                     | [{phrase -> "ted", score -> 0.2625177493269755},{phrase -> "olives", score -> 0.19571419072701732},{phrase -> "marshall", score -> 0.15551468983363487}]                  |
==> | 2    | "Purple Giraffe"                            | [{phrase -> "ted", score -> 0.292184496766088},{phrase -> "carlos", score -> 0.22745438090499026},{phrase -> "robin", score -> 0.19514993122773566}]                      |
==> | 3    | "Sweet Taste of Liberty"                    | [{phrase -> "ted", score -> 0.23266190616714866},{phrase -> "barney", score -> 0.18725456678444408},{phrase -> "officer mcneil", score -> 0.17061872221616137}]           |
==> | 4    | "Return of the Shirt"                       | [{phrase -> "natalie", score -> 0.5624848345525686},{phrase -> "ted", score -> 0.19187323894701674},{phrase -> "robin", score -> 0.10267067360622682}]                    |
==> | 5    | "Okay Awesome"                              | [{phrase -> "subtitle", score -> 0.310865508347106},{phrase -> "coat check", score -> 0.18168178787561182},{phrase -> "ted", score -> 0.16997258596683185}]               |
==> | 6    | "Slutty Pumpkin"                            | [{phrase -> "mike", score -> 0.2966610054610693},{phrase -> "ted", score -> 0.19333276951599407},{phrase -> "robin", score -> 0.1656172994411056}]                        |
==> | 7    | "Matchmaker"                                | [{phrase -> "ellen", score -> 0.4947912795578686},{phrase -> "sarah", score -> 0.24462913913669443},{phrase -> "ted", score -> 0.23728319597607636}]                      |
==> | 8    | "The Duel"                                  | [{phrase -> "ted", score -> 0.26713931416222847},{phrase -> "marshall", score -> 0.22816702335751904},{phrase -> "swords", score -> 0.17841675237702592}]                 |
==> | 9    | "Belly Full of Turkey"                      | [{phrase -> "ericksen", score -> 0.43145756691027665},{phrase -> "mrs ericksen", score -> 0.1939318283559959},{phrase -> "kendall", score -> 0.1846969793866628}]         |
==> | 10   | "The Pineapple Incident"                    | [{phrase -> "ted", score -> 0.439756993033922},{phrase -> "trudy", score -> 0.36367907631894536},{phrase -> "carl", score -> 0.16413071244131686}]                        |
==> | 11   | "The Limo"                                  | [{phrase -> "moby", score -> 0.48314164479037003},{phrase -> "party number", score -> 0.30458929780262456},{phrase -> "ranjit", score -> 0.1991061739767796}]             |
...
==> +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
~~~

<p>
In the cypher version we get one row per episode whereas with the Python version we get 3 rows. It might be possible to achieve this effect with pandas too but I wasn't sure how to do so.
</p>


<p>
Next let's find the top phrases for a single episode - the type of query that might be part of an episode page on a How I met your mother wiki:
</p>



~~~python

top_words = df[(df["EpisodeId"] == 1)] \
    .sort(["Score"], ascending = False) \
    .head(20)

>>> print(top_words.to_string())

      EpisodeId                Phrase     Score
3976          1                   ted  0.262518
2912          1                olives  0.195714
2441          1              marshall  0.155515
4732          1               yasmine  0.152279
3347          1                 robin  0.130418
209           1                barney  0.124412
2146          1                  lily  0.122925
3637          1                signal  0.103793
1366          1                goanna  0.098138
3524          1                 scene  0.095342
710           1                   cut  0.091734
2720          1              narrator  0.086462
1147          1             flashback  0.078296
1148          1        flashback date  0.070283
3224          1                ranjit  0.069393
4178          1           ted yasmine  0.058569
1149          1  flashback date robin  0.058569
525           1                  carl  0.058210
3714          1           smurf pen1s  0.054365
2048          1              lebanese  0.054365
~~~


~~~cypher

MATCH (e:Episode {title: "Pilot"})<-[rel:USED_IN_EPISODE]-(phrase)
WITH phrase, rel
ORDER BY rel.tfidfScore DESC
RETURN phrase.value AS phrase, rel.tfidfScore AS score
LIMIT 20

==> +-----------------------------------------------+
==> | phrase                 | score                |
==> +-----------------------------------------------+
==> | "ted"                  | 0.2625177493269755   |
==> | "olives"               | 0.19571419072701732  |
==> | "marshall"             | 0.15551468983363487  |
==> | "yasmine"              | 0.15227880637176266  |
==> | "robin"                | 0.1304175242341549   |
==> | "barney"               | 0.12441175186690791  |
==> | "lily"                 | 0.12292497785945679  |
==> | "signal"               | 0.1037932464656365   |
==> | "goanna"               | 0.09813798750091524  |
==> | "scene"                | 0.09534236041231685  |
==> | "cut"                  | 0.09173366535740156  |
==> | "narrator"             | 0.08646229819848741  |
==> | "flashback"            | 0.07829592155397117  |
==> | "flashback date"       | 0.07028252601773662  |
==> | "ranjit"               | 0.06939276915589167  |
==> | "ted yasmine"          | 0.05856877168144719  |
==> | "flashback date robin" | 0.05856877168144719  |
==> | "carl"                 | 0.058210117288760355 |
==> | "smurf pen1s"          | 0.05436505297972703  |
==> | "lebanese"             | 0.05436505297972703  |
==> +-----------------------------------------------+
~~~

<p>
Our next query is a negation - find the episodes which don't mention the phrase 'robin'. In python we can do some simple set operations to work this out:
</p>



~~~python

all_episodes = set(range(1, 209))
robin_episodes = set(df[(df["Phrase"] == "robin")]["EpisodeId"])

>>> print(set(all_episodes) - set(robin_episodes))
set([145, 198, 143])
~~~

<p>In cypher land a query will suffice:</p>



~~~cypher

MATCH (episode:Episode), (phrase:Phrase {value: "robin"})
WHERE NOT (episode)<-[:USED_IN_EPISODE]-(phrase)
RETURN episode.id AS id, episode.season AS season, episode.number AS episode
~~~

<p>
And finally a mini recommendation engine type query - how many of the top phrases in Episode 1 were used in other episodes:
</p>



<p>First python:</p>



~~~python

phrases_used = set(df[(df["EpisodeId"] == 1)] \
    .sort(["Score"], ascending = False) \
    .head(10)["Phrase"])

phrases = df[df["Phrase"].isin(phrases_used)]

print (phrases[phrases["EpisodeId"] != 1] \
    .groupby(["Phrase"]) \
    .size() \
    .order(ascending = False))
~~~

<p>
Here we've pulled it out into a few steps - first we identify the top phrases, then we find out where they occur across the whole data set and finally we filter out the occurrences in the first episode and count the other occurrences.
</p>



~~~python

Phrase
marshall    207
barney      207
ted         206
lily        206
robin       204
scene        36
signal        4
goanna        3
olives        1
~~~

<p>
In cypher we can write a query to do this as well:
</p>



~~~cypher

MATCH (episode:Episode {title: "Pilot"})<-[rel:USED_IN_EPISODE]-(phrase)
WITH phrase, rel, episode
ORDER BY rel.tfidfScore DESC
LIMIT 10
MATCH (phrase)-[:USED_IN_EPISODE]->(otherEpisode)
WHERE otherEpisode <> episode
RETURN phrase.value AS phrase, COUNT(*) AS numberOfOtherEpisodes
ORDER BY numberOfOtherEpisodes DESC

==> +------------------------------------+
==> | phrase     | numberOfOtherEpisodes |
==> +------------------------------------+
==> | "barney"   | 207                   |
==> | "marshall" | 207                   |
==> | "ted"      | 206                   |
==> | "lily"     | 206                   |
==> | "robin"    | 204                   |
==> | "scene"    | 36                    |
==> | "signal"   | 4                     |
==> | "goanna"   | 3                     |
==> | "olives"   | 1                     |
==> +------------------------------------+
~~~

<p>
Overall there's not much in it - for some of the queries I found it easier in cypher and for others easier with pandas. It's always useful to have multiple tools in the toolbox!
</p>

