+++
draft = false
date="2015-03-08 13:24:19"
title="Neo4j: TF/IDF (and variants) with cypher"
tag=['neo4j']
category=['neo4j']
+++

<p>
A few weeks ago I wrote a blog post on <a href="http://www.markhneedham.com/blog/2015/02/15/pythonscikit-learn-calculating-tfidf-on-how-i-met-your-mother-transcripts/">running TF/IDF over HIMYM transcripts using scikit-learn</a> to find the most important phrases by episode and afterwards I was curious how difficult it'd be to do in Neo4j.
</p>


<p>I started by translating one of <a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf#Example_of_tf.E2.80.93idf">wikipedia's TF/IDF examples</a> to cypher to see what the algorithm would look like:</p>



~~~cypher

WITH 3 as termFrequency, 2 AS numberOfDocuments, 1 as numberOfDocumentsWithTerm
WITH termFrequency, log10(numberOfDocuments / numberOfDocumentsWithTerm) AS inverseDocumentFrequency
return termFrequency * inverseDocumentFrequency

0.9030899869919435
~~~

<p>
Next I needed to go over the HIMYM episode transcripts and extract phrases and their corresponding counts in each episode. I used scikit-learn's <cite><a href="http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html">CountVectorizer</a></cite> to do this and wrote the results into a CSV file.
</p>


<p>Here's a preview of that file:</p>



~~~bash

$ head -n 10 data/import/words_scikit.csv
EpisodeId,Phrase,Count
1,2005,1
1,2005 seven,1
1,2005 seven just,1
1,2030,3
1,2030 kids,1
1,2030 kids intently,1
1,2030 narrator,1
1,2030 narrator kids,1
1,2030 son,1
~~~

<p>Now let's import that into Neo4j using the LOAD CSV tool:</p>



~~~cypher

// phrases
USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/projects/neo4j-himym/data/import/words_scikit.csv" AS row
MERGE (phrase:Phrase {value: row.Phrase});
~~~


~~~cypher

// episode -> phrase
USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///Users/markneedham/projects/neo4j-himym/data/import/words_scikit.csv" AS row
MATCH (phrase:Phrase {value: row.Phrase})
MATCH (episode:Episode {id: TOINT(row.EpisodeId)})
MERGE (episode)-[:CONTAINED_PHRASE {times:TOINT(row.Count)}]->(phrase);
~~~

<p>
Now that all the data's in we can translate the TF/IDF query to make use of our graph. We'll start with episode 1:
</p>



~~~cypher

match (e:Episode)
WITH COUNT(e) AS numberOfDocuments
match (p:Phrase)<-[r:CONTAINED_PHRASE]-(e:Episode {id: 1})
WITH numberOfDocuments, p, r.times AS termFrequency
MATCH (p)<-[:CONTAINED_PHRASE]->(otherEpisode)
WITH p, COUNT(otherEpisode) AS numberOfDocumentsWithTerm, numberOfDocuments, termFrequency
WITH p, numberOfDocumentsWithTerm,  log10(numberOfDocuments / numberOfDocumentsWithTerm) AS inverseDocumentFrequency, termFrequency, numberOfDocuments
RETURN p.value, termFrequency, numberOfDocumentsWithTerm, inverseDocumentFrequency, termFrequency * inverseDocumentFrequency AS score
ORDER BY score DESC
LIMIT 10

==> +--------------------------------------------------------------------------------------------------------------------+
==> | p.value                | termFrequency | numberOfDocumentsWithTerm | inverseDocumentFrequency | score              |
==> +--------------------------------------------------------------------------------------------------------------------+
==> | "olives"               | 18            | 2                         | 2.0170333392987803       | 36.306600107378046 |
==> | "yasmine"              | 13            | 1                         | 2.3180633349627615       | 30.1348233545159   |
==> | "signal"               | 11            | 5                         | 1.6127838567197355       | 17.740622423917088 |
==> | "goanna"               | 10            | 4                         | 1.7160033436347992       | 17.16003343634799  |
==> | "flashback date"       | 6             | 1                         | 2.3180633349627615       | 13.908380009776568 |
==> | "scene"                | 17            | 37                        | 0.6989700043360189       | 11.88249007371232  |
==> | "flashback date robin" | 5             | 1                         | 2.3180633349627615       | 11.590316674813808 |
==> | "ted yasmine"          | 5             | 1                         | 2.3180633349627615       | 11.590316674813808 |
==> | "smurf pen1s"          | 5             | 2                         | 2.0170333392987803       | 10.085166696493902 |
==> | "eye patch"            | 5             | 2                         | 2.0170333392987803       | 10.085166696493902 |
==> +--------------------------------------------------------------------------------------------------------------------+
==> 10 rows
~~~

<p>
The score we've calculated is different to scikit-learn's but the relative order seems fine so that's good. The neat thing about calculating this in Neo4j is that we can now vary the 'inverse document' part of the equation e.g. to find out the most important phrases in a season rather than an episode:
</p>



~~~cypher

match (:Season) 
WITH COUNT(*) AS numberOfDocuments
match (p:Phrase)<-[r:CONTAINED_PHRASE]-(:Episode)-[:IN_SEASON]->(s:Season {number: "1"})
WITH p, SUM(r.times) AS termFrequency, numberOfDocuments
MATCH (p)<-[:CONTAINED_PHRASE]->(otherEpisode)-[:IN_SEASON]->(s:Season)
WITH p, COUNT(DISTINCT s) AS numberOfDocumentsWithTerm, termFrequency, numberOfDocuments
WITH p, numberOfDocumentsWithTerm,  log10(numberOfDocuments / numberOfDocumentsWithTerm) AS inverseDocumentFrequency, termFrequency, numberOfDocuments
RETURN p.value, termFrequency, numberOfDocumentsWithTerm, inverseDocumentFrequency, termFrequency * inverseDocumentFrequency AS score
ORDER BY score DESC
LIMIT 10

==> +-------------------------------------------------------------------------------------------------------------+
==> | p.value         | termFrequency | numberOfDocumentsWithTerm | inverseDocumentFrequency | score              |
==> +-------------------------------------------------------------------------------------------------------------+
==> | "moby"          | 46            | 1                         | 0.9542425094393249       | 43.895155434208945 |
==> | "int"           | 71            | 3                         | 0.47712125471966244      | 33.87560908509603  |
==> | "ellen"         | 53            | 2                         | 0.6020599913279624       | 31.909179540382006 |
==> | "claudia"       | 104           | 4                         | 0.3010299956639812       | 31.307119549054043 |
==> | "ericksen"      | 59            | 3                         | 0.47712125471966244      | 28.150154028460083 |
==> | "party number"  | 29            | 1                         | 0.9542425094393249       | 27.67303277374042  |
==> | "subtitle"      | 27            | 1                         | 0.9542425094393249       | 25.76454775486177  |
==> | "vo"            | 47            | 3                         | 0.47712125471966244      | 22.424698971824135 |
==> | "ted vo"        | 47            | 3                         | 0.47712125471966244      | 22.424698971824135 |
==> | "future ted vo" | 45            | 3                         | 0.47712125471966244      | 21.47045646238481  |
==> +-------------------------------------------------------------------------------------------------------------+
==> 10 rows
~~~

<p>
From this query we learn that 'Moby' was only mentioned once in the whole series and actually all of those mentions were in the <a href="http://en.wikipedia.org/wiki/The_Limo_%28How_I_Met_Your_Mother%29">same episode</a>. The occurrence of 'int' seems to be more of a data issue - in some episodes the transcript describes location but in many it doesn't:
</p>



~~~bash

$ ack -iw "int" data/import/sentences.csv
2361,8,1,8,"INT. LIVING ROOM, YEAR 2030"
2377,8,1,8,INT. CHINESE RESTAURANT
2395,8,1,8,INT. APARTMENT
2412,8,1,8,INT. APARTMENT
2419,8,1,8,INT. BAR
2472,8,1,8,INT. APARTMENT
2489,8,1,8,INT. BAR
2495,8,1,8,INT. APARTMENT
2506,8,1,8,INT. BAR
2584,8,1,8,INT. APARTMENT
2629,8,1,8,INT. RESTAURANT
2654,8,1,8,INT. APARTMENT
2682,8,1,8,INT. RESTAURANT
2689,8,1,8,(Robin gets up and leaves restaurant) INT. HOSPITAL WAITING AREA
~~~

<p>
'vo' stands for voice over which should probably be stripped out in the stop words as it doesn't add much value. It shows up here because the transcripts aren't consistent in the way they represent Future Ted speaking.
</p>


<p>Let's have a look at the final season to see how that fares:</p>



~~~cypher

match (:Season)
WITH COUNT(*) AS numberOfDocuments
match (p:Phrase)<-[r:CONTAINED_PHRASE]-(:Episode)-[:IN_SEASON]->(s:Season {number: "9"})
WITH p, SUM(r.times) AS termFrequency, numberOfDocuments
MATCH (p)<-[:CONTAINED_PHRASE]->(otherEpisode:Episode)-[:IN_SEASON]->(s:Season)
WITH p, COUNT(DISTINCT s) AS numberOfDocumentsWithTerm, termFrequency, numberOfDocuments
WITH p, numberOfDocumentsWithTerm,  log10(numberOfDocuments / numberOfDocumentsWithTerm) AS inverseDocumentFrequency, termFrequency, numberOfDocuments
RETURN p.value, termFrequency, numberOfDocumentsWithTerm, inverseDocumentFrequency, termFrequency * inverseDocumentFrequency AS score
ORDER BY score DESC
LIMIT 10

==> +------------------------------------------------------------------------------------------------------------------+
==> | p.value              | termFrequency | numberOfDocumentsWithTerm | inverseDocumentFrequency | score              |
==> +------------------------------------------------------------------------------------------------------------------+
==> | "ring bear"          | 28            | 1                         | 0.9542425094393249       | 26.718790264301095 |
==> | "click options"      | 26            | 1                         | 0.9542425094393249       | 24.810305245422448 |
==> | "thank linus"        | 26            | 1                         | 0.9542425094393249       | 24.810305245422448 |
==> | "vow"                | 39            | 2                         | 0.6020599913279624       | 23.480339661790534 |
==> | "just click"         | 24            | 1                         | 0.9542425094393249       | 22.901820226543798 |
==> | "rehearsal dinner"   | 23            | 1                         | 0.9542425094393249       | 21.947577717104473 |
==> | "linus"              | 36            | 2                         | 0.6020599913279624       | 21.674159687806647 |
==> | "just click options" | 22            | 1                         | 0.9542425094393249       | 20.993335207665147 |
==> | "locket"             | 32            | 2                         | 0.6020599913279624       | 19.265919722494797 |
==> | "cassie"             | 19            | 1                         | 0.9542425094393249       | 18.13060767934717  |
==> +------------------------------------------------------------------------------------------------------------------+
~~~

<p>
There are several phrases which are specific to Barney & Robin's wedding ('vow', 'ring bear', 'rehearsal dinner') so it makes sense that those come out top. The 'linus' here mostly refers to the server at the bar who interacts with Lily although a quick search over the transcripts reveals that she also had an Uncle Linus!
</p>



~~~bash

$ ack -iw "linus" data/import/sentences.csv  | head -n 5
18649,61,3,17,Lily: Why don't we just call Duluth Mental Hospital and say my Uncle Linus can live with us?
59822,185,9,1,Linus.
59826,185,9,1,"Are you my guy, Linus?"
59832,185,9,1,Thank you Linus.
59985,185,9,1,"Thank you, Linus."
...
~~~

<p>
From doing this exercise I think TF/IDF is an interesting way of exploring unstructured data but for a phrase to be really interesting to us it should appear across multiple episodes/seasons. 
</p>


<p>
One way to achieve that would be to weight those features more so I'll try that out next.
</p>


<p><a href="https://github.com/mneedham/neo4j-himym">All the code in this post is on github</a> if you want to take a look and improve it.</p>

