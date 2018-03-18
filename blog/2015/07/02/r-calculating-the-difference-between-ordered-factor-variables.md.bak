+++
draft = false
date="2015-07-02 22:55:01"
title="R: Calculating the difference between ordered factor variables"
tag=['r-2']
category=['R']
+++

<p>
In my continued exploration of <a href="https://github.com/mneedham/neo4j-wimbledon/blob/master/wimbledon.csv">Wimbledon data</a> I wanted to work out whether a player had done as well as their seeding suggested they should.

</p>


<p>I therefore wanted to work out the difference between the round they reached and the round they were expected to reach. A 'round' in the dataset is an ordered factor variable.
</p>


<p>
These are all the possible values:
</p>



~~~r

rounds = c("Did not enter", "Round of 128", "Round of 64", "Round of 32", "Round of 16", "Quarter-Finals", "Semi-Finals", "Finals", "Winner")
~~~

<p>And if we want to factorise a couple of strings into this factor we would do it like this:</p>



~~~r

round = factor("Finals", levels = rounds, ordered = TRUE)
expected = factor("Winner", levels = rounds, ordered = TRUE)  

> round
[1] Finals
9 Levels: Did not enter < Round of 128 < Round of 64 < Round of 32 < Round of 16 < Quarter-Finals < ... < Winner

> expected
[1] Winner
9 Levels: Did not enter < Round of 128 < Round of 64 < Round of 32 < Round of 16 < Quarter-Finals < ... < Winner
~~~

<p>
In this case the difference between the actual round and expected round should be -1 - the player was expected to win the tournament but lost in the final. We can calculate that differnce by <a href="http://stackoverflow.com/questions/7611810/converting-a-factor-to-numeric-without-losing-information-r-as-numeric-doesn">calling the <cite>unclass</cite> function on each variable</a>:
</p>



~~~r


> unclass(round) - unclass(expected)
[1] -1
attr(,"levels")
[1] "Did not enter"  "Round of 128"   "Round of 64"    "Round of 32"    "Round of 16"    "Quarter-Finals"
[7] "Semi-Finals"    "Finals"         "Winner" 
~~~

<p>
That still seems to have some remnants of the factor variable so to get rid of that we can cast it to a numeric value:
</p>



~~~r

> as.numeric(unclass(round) - unclass(expected))
[1] -1
~~~

<p>
And that's it! We can now go and apply this calculation to all seeds to see how they got on.
</p>

