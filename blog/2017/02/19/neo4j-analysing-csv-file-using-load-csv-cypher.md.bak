+++
draft = false
date="2017-02-19 22:39:05"
title="Neo4j: Analysing a CSV file using LOAD CSV and Cypher"
tag=['neo4j', 'cypher']
category=['neo4j']
+++

<p>
Last week we ran our <a href="https://www.meetup.com/Neo4j-Online-Meetup/events/237366632/">first online meetup for several years</a> and I wanted to wanted to analyse the stats that YouTube lets you download for an event.
</p>


<p>
The file I downloaded looked like this:
</p>



~~~bash

$ cat ~/Downloads/youtube_stats_pW9boJoUxO0.csv 
Video IDs:, pW9boJoUxO0, Start time:, Wed Feb 15 08:57:55 2017, End time:, Wed Feb 15 10:03:10 2017
Playbacks, Peak concurrent viewers, Total view time (hours), Average session length (minutes)
348, 112, 97.125, 16.7456896552, 

Country code, AR, AT, BE, BR, BY, CA, CH, CL, CR, CZ, DE, DK, EC, EE, ES, FI, FR, GB, HU, IE, IL, IN, IT, LB, LU, LV, MY, NL, NO, NZ, PK, PL, QA, RO, RS, RU, SE, TR, US, VN, ZA
Playbacks, 2, 2, 1, 14, 1, 10, 2, 1, 1, 1, 27, 1, 1, 1, 3, 1, 25, 54, 1, 4, 6, 8, 1, 1, 1, 1, 1, 23, 1, 1, 1, 1, 1, 1, 2, 6, 22, 1, 114, 1, 1
Peak concurrent viewers, 2, 1, 1, 4, 1, 5, 1, 1, 0, 0, 11, 1, 1, 1, 2, 1, 6, 25, 1, 3, 3, 2, 1, 1, 1, 1, 1, 9, 1, 1, 0, 1, 0, 1, 1, 3, 7, 0, 44, 1, 0
Total view time (hours), 1.075, 0.0166666666667, 0.175, 2.58333333333, 0.00833333333333, 3.01666666667, 0.858333333333, 0.0583333333333, 0.0, 0.0, 8.69166666667, 0.8, 0.0166666666667, 0.0583333333333, 0.966666666667, 0.0166666666667, 4.20833333333, 20.8333333333, 0.00833333333333, 1.39166666667, 1.75, 0.766666666667, 0.00833333333333, 0.15, 0.0333333333333, 1.05833333333, 0.0333333333333, 7.36666666667, 0.0583333333333, 0.916666666667, 0.0, 0.00833333333333, 0.0, 0.00833333333333, 0.4, 1.10833333333, 5.28333333333, 0.0, 32.7333333333, 0.658333333333, 0.0
Average session length (minutes), 32.25, 0.5, 10.5, 11.0714285714, 0.5, 18.1, 25.75, 3.5, 0.0, 0.0, 19.3148148148, 48.0, 1.0, 3.5, 19.3333333333, 1.0, 10.1, 23.1481481481, 0.5, 20.875, 17.5, 5.75, 0.5, 9.0, 2.0, 63.5, 2.0, 19.2173913043, 3.5, 55.0, 0.0, 0.5, 0.0, 0.5, 12.0, 11.0833333333, 14.4090909091, 0.0, 17.2280701754, 39.5, 0.0
~~~

<p>
I want to look at the country specific stats so the first 4 lines aren't interesting to me:
</p>



~~~bash

$ tail -n+5 youtube_stats_pW9boJoUxO0.csv > youtube.csv
~~~

<p>
I then put the <cite>youtube.csv</cite> file into the <cite>import</cite> directory of Neo4j and wrote the following query to return a row representing each country and its score for each of the metrics:
</p>



~~~cypher

load csv with headers from "file:///youtube.csv" AS row
WITH [key in keys(row) where key <> "Country code"] AS keys, row, row["Country code"] AS heading
UNWIND keys AS key
RETURN key AS country, heading AS key, row[key] AS value

╒═════════╤═══════════╤═══════╕
│"country"│"key"      │"value"│
╞═════════╪═══════════╪═══════╡
│" SE"    │"Playbacks"│"22"   │
├─────────┼───────────┼───────┤
│" GB"    │"Playbacks"│"54"   │
├─────────┼───────────┼───────┤
│" FR"    │"Playbacks"│"25"   │
├─────────┼───────────┼───────┤
│" RS"    │"Playbacks"│"2"    │
├─────────┼───────────┼───────┤
│" LV"    │"Playbacks"│"1"    │
└─────────┴───────────┴───────┘
~~~


<p>
Now I want to create a node representing each country and create a property for each of the metrics. Since the <a href="http://www.markhneedham.com/blog/2016/10/27/neo4j-dynamically-add-property/">property names are going to be dynamic</a> I'll make use of the <a href="https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases">APOC library</a> which I drop into my <cite>plugins</cite> directory. I then tweaked the query to create the nodes:
</p>



~~~cypher

load csv with headers from "https://dl.dropboxusercontent.com/u/14493611/youtube.csv" AS row
WITH [key in keys(row) where key <> "Country code"] AS keys, row, row["Country code"] AS heading
UNWIND keys AS key
WITH key AS country, heading AS key, row[key] AS value
MERGE (c:Country {name: replace(country, " ", "")})
WITH *
CALL apoc.create.setProperty(c, key, toInteger(value))
YIELD node
RETURN COUNT(*)
~~~

<p>
We can now see which country provided the most viewers:
</p>



~~~cypher

MATCH (n:Country) 
RETURN n.name, n.Playbacks AS playbacks, n.`Total view time (hours)` AS viewTimeInHours, n.`Peak concurrent viewers` AS peakConcViewers, n.`Average session length (minutes)` AS aveSessionMins
ORDER BY playbacks DESC
LIMIT 10

╒════════╤═══════════╤═════════════════╤═════════════════╤════════════════╕
│"n.name"│"playbacks"│"viewTimeInHours"│"peakConcViewers"│"aveSessionMins"│
╞════════╪═══════════╪═════════════════╪═════════════════╪════════════════╡
│"US"    │"114"      │"32"             │"44"             │"17"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"GB"    │"54"       │"20"             │"25"             │"23"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"DE"    │"27"       │"8"              │"11"             │"19"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"FR"    │"25"       │"4"              │"6"              │"10"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"NL"    │"23"       │"7"              │"9"              │"19"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"SE"    │"22"       │"5"              │"7"              │"14"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"BR"    │"14"       │"2"              │"4"              │"11"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"CA"    │"10"       │"3"              │"5"              │"18"            │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"IN"    │"8"        │"0"              │"2"              │"5"             │
├────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"IL"    │"6"        │"1"              │"3"              │"17"            │
└────────┴───────────┴─────────────────┴─────────────────┴────────────────┘
~~~

<p>
The United States in first unsurprisingly followed by the UK, Germany, and France. We ran the meetup at 5pm UK time so it was a friendly enough time for this side of the globe but not so friendly for Asia or Australia so it's not too surprising we don't see anybody from there!
</p>


<p>
For my last trick I wanted to see the full names of the countries so I downloaded the <a href="http://data.okfn.org/data/core/country-list">2 digit codes for each country along with their full name</a>. 
</p>


<p>
I then updated my graph:
</p>



~~~cypher

load csv with headers from "file:///countries.csv" AS row
MATCH (c:Country {name: row.Code})
SET c.fullName = row.Name;
~~~

<p>Now let's re-run our query and show the country fullnames instead:</p>



~~~cypher

MATCH (n:Country) 
RETURN n.fullName, n.Playbacks AS playbacks, n.`Total view time (hours)` AS viewTimeInHours, n.`Peak concurrent viewers` AS peakConcViewers, n.`Average session length (minutes)` AS aveSessionMins
ORDER BY playbacks DESC
LIMIT 10

╒════════════════╤═══════════╤═════════════════╤═════════════════╤════════════════╕
│"n.fullName"    │"playbacks"│"viewTimeInHours"│"peakConcViewers"│"aveSessionMins"│
╞════════════════╪═══════════╪═════════════════╪═════════════════╪════════════════╡
│"United States" │"114"      │"32"             │"44"             │"17"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"United Kingdom"│"54"       │"20"             │"25"             │"23"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Germany"       │"27"       │"8"              │"11"             │"19"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"France"        │"25"       │"4"              │"6"              │"10"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Netherlands"   │"23"       │"7"              │"9"              │"19"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Sweden"        │"22"       │"5"              │"7"              │"14"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Brazil"        │"14"       │"2"              │"4"              │"11"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Canada"        │"10"       │"3"              │"5"              │"18"            │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"India"         │"8"        │"0"              │"2"              │"5"             │
├────────────────┼───────────┼─────────────────┼─────────────────┼────────────────┤
│"Israel"        │"6"        │"1"              │"3"              │"17"            │
└────────────────┴───────────┴─────────────────┴─────────────────┴────────────────┘
~~~

<p>
And that's the end of my analysis with no relationships in sight! 
</p>

