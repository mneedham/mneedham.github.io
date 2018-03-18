+++
draft = false
date="2015-10-09 06:34:45"
title="jq: error - Cannot iterate over null (null)"
tag=['jq']
category=['Software Development']
+++

<p>
I've been playing around with the <a href="https://stedolan.github.io/jq/">jq</a> library again over the past couple of days to convert the JSON from the <a href="http://api.stackexchange.com/">Stack Overflow API</a> into CSV and found myself needing to deal with an optional field.
</p>


<p>
I've downloaded 100 or so questions and stored them as an array in a JSON array like so:
</p>



~~~bash

$ head -n 100 so.json
[
    {
        "has_more": true,
        "items": [
            {
                "is_answered": false,
                "delete_vote_count": 0,
                "body_markdown": "...",
                "tags": [
                    "jdbc",
                    "neo4j",
                    "cypher",
                    "spring-data-neo4j"
                ],
                "question_id": 33023306,
                "title": "How to delete multiple nodes by specific ID using Cypher",
                "down_vote_count": 0,
                "view_count": 8,
                "answers": [
                    {
...
]
~~~

<p>
I wrote the following command to try and extract the answer meta data and the corresponding question_id:
</p>




~~~bash

$ jq -r \
 '.[] | .items[] |
 { question_id: .question_id, answer: .answers[] } |
 [.question_id, .answer.answer_id, .answer.title] |
 @csv' so.json

33023306,33024189,"How to delete multiple nodes by specific ID using Cypher"
33020796,33021958,"How do a general search across string properties in my nodes?"
33018818,33020068,"Neo4j match nodes related to all nodes in collection"
33018818,33024273,"Neo4j match nodes related to all nodes in collection"
jq: error (at so.json:134903): Cannot iterate over null (null)
~~~

<p>
Unfortunately this results in an error since some questions haven't been answered yet and therefore don't have the 'answers' property.
</p>


<p>While reading <a href="https://stedolan.github.io/jq/manual/#ConditionalsandComparisons">the docs</a> I came across the alternative operation '//' which can be used to provide defaults - in this case I thought I could plugin an empty array of answers if a question hadn't been answered yet:</p>



~~~bash

$ jq -r \
 '.[] | .items[] |
 { question_id: .question_id, answer: (.answers[] // []) } |
 [.question_id, .answer.answer_id, .answer.title] |
 @csv' so.json

33023306,33024189,"How to delete multiple nodes by specific ID using Cypher"
33020796,33021958,"How do a general search across string properties in my nodes?"
33018818,33020068,"Neo4j match nodes related to all nodes in collection"
33018818,33024273,"Neo4j match nodes related to all nodes in collection"
jq: error (at so.json:134903): Cannot iterate over null (null)
~~~

<p>Still the same error! Reading down the page I noticed the ? operator which provides syntactic sugar for handling/catching errors. I gave it a try:</p>



~~~bash

$ jq -r  '.[] | .items[] |
 { question_id: .question_id, answer: .answers[]? } |
 [.question_id, .answer.answer_id, .answer.title] |
 @csv' so.json | head -n10

33023306,33024189,"How to delete multiple nodes by specific ID using Cypher"
33020796,33021958,"How do a general search across string properties in my nodes?"
33018818,33020068,"Neo4j match nodes related to all nodes in collection"
33018818,33024273,"Neo4j match nodes related to all nodes in collection"
33015714,33021482,"Upgrade of spring data neo4j 3.x to 4.x Relationship Operations"
33011477,33011721,"Why does Neo4j OGM delete method return void?"
33011102,33011565,"Neo4j and algorithms"
33011102,33013260,"Neo4j and algorithms"
33010859,33011505,"Importing data into an existing database in neo4j"
33009673,33010942,"How do I use Spring Data Neo4j to persist a Map (java.util.Map) object inside an NodeEntity?"
~~~

<p>As far as I can tell we are just skipping any records that don't contain 'answers' which is exactly the behaviour I'm after so that's great - just what we need!</p>

