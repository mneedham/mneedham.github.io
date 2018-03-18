+++
draft = false
date="2015-03-27 06:59:02"
title="Neo4j: Generating real time recommendations with Cypher"
tag=['neo4j']
category=['neo4j']
+++

<p>
One of the most common uses of Neo4j is for building real time recommendation engines and a common theme is that they make use of lots of different bits of data to come up with an interesting recommendation.
</p>


<p>
For example <a href="https://vimeo.com/86754045">in this video</a> <a href="https://twitter.com/pandamonial">Amanda</a> shows how dating websites build real time recommendation engines by starting with social connections and then introducing passions, location and a few other things.
</p>


<p>Graph Aware have a <a href="https://github.com/graphaware/neo4j-reco#using-graphaware-neo4j-recommendation-engine">neat framework</a> that helps you to build your own recommendation engine using Java and I was curious what a Cypher version would look like.
</p>


<p>
This is the sample graph:
</p>




~~~cypher

CREATE
    (m:Person:Male {name:'Michal', age:30}),
    (d:Person:Female {name:'Daniela', age:20}),
    (v:Person:Male {name:'Vince', age:40}),
    (a:Person:Male {name:'Adam', age:30}),
    (l:Person:Female {name:'Luanne', age:25}),
    (c:Person:Male {name:'Christophe', age:60}),

    (lon:City {name:'London'}),
    (mum:City {name:'Mumbai'}),

    (m)-[:FRIEND_OF]->(d),
    (m)-[:FRIEND_OF]->(l),
    (m)-[:FRIEND_OF]->(a),
    (m)-[:FRIEND_OF]->(v),
    (d)-[:FRIEND_OF]->(v),
    (c)-[:FRIEND_OF]->(v),
    (d)-[:LIVES_IN]->(lon),
    (v)-[:LIVES_IN]->(lon),
    (m)-[:LIVES_IN]->(lon),
    (l)-[:LIVES_IN]->(mum);
~~~

<p>We want to recommend some potential friends to 'Adam' so the first layer of our query is to find his friends of friends as there are bound to be some potential friends amongst them:
</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)
RETURN me, potentialFriend, COUNT(*) AS friendsInCommon

==> +--------------------------------------------------------------------------------------+
==> | me                             | potentialFriend                   | friendsInCommon |
==> +--------------------------------------------------------------------------------------+
==> | Node[1007]{name:"Adam",age:30} | Node[1006]{name:"Vince",age:40}   | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1005]{name:"Daniela",age:20} | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1008]{name:"Luanne",age:25}  | 1               |
==> +--------------------------------------------------------------------------------------+
==> 3 rows
~~~

<p>This query gives us back a list of potential friends and how many friends we have in common.</p>


<p>
Now that we've got some potential friends let's start building a ranking for each of them. One indicator which could weigh in favour of a potential friend is if they live in the same location as us so let's add that to our query:
</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)

WITH me, potentialFriend, COUNT(*) AS friendsInCommon

RETURN  me,
        potentialFriend,
        SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation

==> +-----------------------------------------------------------------------------------+
==> | me                             | potentialFriend                   | sameLocation |
==> +-----------------------------------------------------------------------------------+
==> | Node[1007]{name:"Adam",age:30} | Node[1006]{name:"Vince",age:40}   | 0            |
==> | Node[1007]{name:"Adam",age:30} | Node[1005]{name:"Daniela",age:20} | 0            |
==> | Node[1007]{name:"Adam",age:30} | Node[1008]{name:"Luanne",age:25}  | 0            |
==> +-----------------------------------------------------------------------------------+
==> 3 rows
~~~

<p>Next we'll check whether Adams' potential friends have the same gender as him by comparing the labels each node has. We've got 'Male' and 'Female' labels which indicate gender.</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)

WITH me, potentialFriend, COUNT(*) AS friendsInCommon

RETURN  me,
        potentialFriend,
        SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation,
        LABELS(me) = LABELS(potentialFriend) AS gender

==> +--------------------------------------------------------------------------------------------+
==> | me                             | potentialFriend                   | sameLocation | gender |
==> +--------------------------------------------------------------------------------------------+
==> | Node[1007]{name:"Adam",age:30} | Node[1006]{name:"Vince",age:40}   | 0            | true   |
==> | Node[1007]{name:"Adam",age:30} | Node[1005]{name:"Daniela",age:20} | 0            | false  |
==> | Node[1007]{name:"Adam",age:30} | Node[1008]{name:"Luanne",age:25}  | 0            | false  |
==> +--------------------------------------------------------------------------------------------+
==> 3 rows
~~~

<p>
Next up let's calculate the age different between Adam and his potential friends:
</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)

WITH me, potentialFriend, COUNT(*) AS friendsInCommon

RETURN me,
       potentialFriend,
       SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation,
       abs( me.age - potentialFriend.age) AS ageDifference,
       LABELS(me) = LABELS(potentialFriend) AS gender,
       friendsInCommon

==> +------------------------------------------------------------------------------------------------------------------------------+
==> | me                             | potentialFriend                   | sameLocation | ageDifference | gender | friendsInCommon |
==> +------------------------------------------------------------------------------------------------------------------------------+
==> | Node[1007]{name:"Adam",age:30} | Node[1006]{name:"Vince",age:40}   | 0            | 10.0          | true   | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1005]{name:"Daniela",age:20} | 0            | 10.0          | false  | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1008]{name:"Luanne",age:25}  | 0            | 5.0           | false  | 1               |
==> +------------------------------------------------------------------------------------------------------------------------------+
==> 3 rows
~~~


<p>Now let's do some filtering to get rid of people that Adam is already friends with - there wouldn't be much point in recommending those people!</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)

WITH me, potentialFriend, COUNT(*) AS friendsInCommon

WITH me,
     potentialFriend,
     SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation,
     abs( me.age - potentialFriend.age) AS ageDifference,
     LABELS(me) = LABELS(potentialFriend) AS gender,
     friendsInCommon

WHERE NOT (me)-[:FRIEND_OF]-(potentialFriend)

RETURN me,
       potentialFriend,
       SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation,
       abs( me.age - potentialFriend.age) AS ageDifference,
       LABELS(me) = LABELS(potentialFriend) AS gender,
       friendsInCommon

==> +------------------------------------------------------------------------------------------------------------------------------+
==> | me                             | potentialFriend                   | sameLocation | ageDifference | gender | friendsInCommon |
==> +------------------------------------------------------------------------------------------------------------------------------+
==> | Node[1007]{name:"Adam",age:30} | Node[1006]{name:"Vince",age:40}   | 0            | 10.0          | true   | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1005]{name:"Daniela",age:20} | 0            | 10.0          | false  | 1               |
==> | Node[1007]{name:"Adam",age:30} | Node[1008]{name:"Luanne",age:25}  | 0            | 5.0           | false  | 1               |
==> +------------------------------------------------------------------------------------------------------------------------------+
==> 3 rows
~~~

<p>In this case we haven't actually filtered anyone out but for some of the other people we would see a reduction in the number of potential friends.</p>


<p>
Our final step is to come up with a score for each of the features that we've identified as being important for making a friend suggestion. 
</p>


<p>We'll assign a score of 10 if the people live in the same location or have the same gender as Adam and 0 if not. For the ageDifference and friendsInCommon we'll apply apply a log curve so that those values don't have a disproportional effect on our final score. We'll use the formula defined in the <cite><a href="https://github.com/graphaware/neo4j-reco/blob/master/src/main/java/com/graphaware/reco/generic/transform/ParetoScoreTransformer.java#L64">ParetoScoreTransfomer</a></cite> to do this:
</p>



~~~java

    public <OUT> float transform(OUT item, float score) {
        if (score < minimumThreshold) {
            return 0;
        }

        double alpha = Math.log((double) 5) / eightyPercentLevel;
        double exp = Math.exp(-alpha * score);
        return new Double(maxScore * (1 - exp)).floatValue();
    }
~~~

<p>And now for our completed recommendation query:</p>



~~~cypher

MATCH (me:Person {name: "Adam"})
MATCH (me)-[:FRIEND_OF]-()-[:FRIEND_OF]-(potentialFriend)

WITH me, potentialFriend, COUNT(*) AS friendsInCommon

WITH me,
     potentialFriend,
     SIZE((potentialFriend)-[:LIVES_IN]->()<-[:LIVES_IN]-(me)) AS sameLocation,
     abs( me.age - potentialFriend.age) AS ageDifference,
     LABELS(me) = LABELS(potentialFriend) AS gender,
     friendsInCommon

WHERE NOT (me)-[:FRIEND_OF]-(potentialFriend)

WITH potentialFriend,
       // 100 -> maxScore, 10 -> eightyPercentLevel, friendsInCommon -> score (from the formula above)
       100 * (1 - exp((-1.0 * (log(5.0) / 10)) * friendsInCommon)) AS friendsInCommon,
       sameLocation * 10 AS sameLocation,
       -1 * (10 * (1 - exp((-1.0 * (log(5.0) / 20)) * ageDifference))) AS ageDifference,
       CASE WHEN gender THEN 10 ELSE 0 END as sameGender

RETURN potentialFriend,
      {friendsInCommon: friendsInCommon,
       sameLocation: sameLocation,
       ageDifference:ageDifference,
       sameGender: sameGender} AS parts,
     friendsInCommon + sameLocation + ageDifference + sameGender AS score
ORDER BY score DESC

==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | potentialFriend                   | parts                                                                                                           | score             |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
==> | Node[1006]{name:"Vince",age:40}   | {friendsInCommon -> 14.86600774792154, sameLocation -> 0, ageDifference -> -5.52786404500042, sameGender -> 10} | 19.33814370292112 |
==> | Node[1008]{name:"Luanne",age:25}  | {friendsInCommon -> 14.86600774792154, sameLocation -> 0, ageDifference -> -3.312596950235779, sameGender -> 0} | 11.55341079768576 |
==> | Node[1005]{name:"Daniela",age:20} | {friendsInCommon -> 14.86600774792154, sameLocation -> 0, ageDifference -> -5.52786404500042, sameGender -> 0}  | 9.33814370292112  |
==> +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
~~~

<p>
The final query isn't too bad - the only really complex bit is the log curve calculation. This is where user defined functions will come into their own in the future.
</p>


<p>
The nice thing about this approach is that we don't have to step outside of cypher so if you're not comfortable with Java you can still do real time recommendations! On the other hand, the different parts of the recommendation engine all get mixed up so it's not as easy to see the whole pipeline as if you use the graph aware framework.
</p>


<p>
The next step is to apply this to the <a href="http://www.markhneedham.com/blog/2015/03/11/pythonneo4j-finding-interesting-computer-sciency-people-to-follow-on-twitter/">Twitter graph</a> and come up with follower recommendations on there.
</p>

