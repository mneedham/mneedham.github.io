+++
draft = false
date="2013-09-30 20:26:35"
title="Elo Rating System: Ranking Champions League teams using Clojure Part 2"
tag=['clojure', 'ranking-systems']
category=['Ranking Systems']
+++

<p>A few weeks ago I wrote about <a href="http://www.markhneedham.com/blog/2013/08/31/elo-rating-system-ranking-champions-league-teams-using-clojure/">ranking Champions League teams using the Elo Rating algorithm</a>, and since I wrote that post I've collated data for 10 years worth of matches so I thought an update was in order.</p>


<p>After extracting the details of all those matches I <a href="https://github.com/mneedham/ranking-algorithms/blob/867941c1569075315d0927a842c6adcbb2621e65/data/cl-matches.json">saved them to a JSON file</a> so that I wouldn't have to parse the HTML pages every time I tweaked the algorithm. This should also make it easier for other people to play with the data.</p>


<p>I described the algorithm in the previous post and had analysed the rankings for one season. However, it was difficult to understand why teams has been ranked in a certain order so I drilled into the data to find out.</p>


<p>Since the 2012/2013 season is the freshest in my memory I started with that.<p>

<p>The first thing to do was load <a href="https://github.com/mneedham/ranking-algorithms/blob/27f94ccf1fc6c63663c8b3d512a2470330585803/data/cl-matches-2013.json">the matches</a> from disk:</p>



~~~lisp

(ns ranking-algorithms.uefa
  (:require [clj-time.format :as f])
  (:require [clojure.data.json :as json]))

(defn as-date [date-field] (f/parse (f/formatter "dd MMM YYYY") date-field ))

(defn date-aware-value-reader [key value] (if (= key :date) (as-date value) value))

(defn read-from-file [file]
  (json/read-str (slurp file)
                 :value-fn date-aware-value-reader
                 :key-fn keyword))
~~~

<p>I've written previously about <a href="http://www.markhneedham.com/blog/2013/09/26/clojure-writing-json-to-a-file-exception-dont-know-how-to-write-json-of-class-org-joda-time-datetime/">reifying a date masquerading as a string</a> but for now we want to give those matches a name and then process them.</p>



~~~lisp

> (def the-matches (read-from-file "data/cl-matches-2013.json"))
#'ranking-algorithms.uefa/the-matches

> (count the-matches)
213
~~~

<p>I already had a function <cite><a href="https://github.com/mneedham/ranking-algorithms/blob/27f94ccf1fc6c63663c8b3d512a2470330585803/src/ranking_algorithms/core.clj#L28">top-teams</a></cite> which would apply the Elo algorithm across the matches, but since I wanted to drill into each team's performance I wrapped that function in another one called <cite><a href="https://github.com/mneedham/ranking-algorithms/blob/27f94ccf1fc6c63663c8b3d512a2470330585803/src/ranking_algorithms/core.clj#L121">print-top-teams</a></cite>:</p>



~~~lisp

(comment "other functions excluded for brevity")

(defn format-for-printing [all-matches idx [team ranking & [rd]]]
  (let [team-matches (show-matches team all-matches)]
    (merge  {:rank (inc idx)
             :team team
             :ranking ranking
             :rd rd
             :round (performance team-matches)}
            (match-record team-matches))))

(defn print-top-teams
  ([number all-matches] (print-top-teams number all-matches {}))
  ([number all-matches base-rankings]
      (clojure.pprint/print-table
       [:rank :team :ranking :round :wins :draw :loses]
       (map-indexed
        (partial format-for-printing all-matches)
        (top-teams number all-matches base-rankings)))))
~~~


~~~lisp

> (ranking-algorithms.core/print-top-teams 10 the-matches)
========================================================================
:rank | :team       | :ranking | :round         | :wins | :draw | :loses
========================================================================
1     | Bayern      | 1272.74  | Final          | 10    | 1     | 2     
2     | PSG         | 1230.02  | Quarter-finals | 6     | 3     | 1     
3     | Dortmund    | 1220.96  | Final          | 7     | 4     | 2     
4     | Real Madrid | 1220.33  | Semi-finals    | 6     | 3     | 3     
5     | Porto       | 1216.97  | Round of 16    | 5     | 1     | 2     
6     | CFR Cluj    | 1216.56  | Group stage    | 7     | 1     | 2     
7     | Galatasaray | 1215.56  | Quarter-finals | 5     | 2     | 3     
8     | Juventus    | 1214.0   | Quarter-finals | 5     | 3     | 2     
9     | Málaga      | 1211.53  | Quarter-finals | 5     | 5     | 2     
10    | Valencia    | 1211.0   | Round of 16    | 4     | 2     | 2     
========================================================================
~~~

<p><em>I've excluded most of the functions but you can find the source in <a href="https://github.com/mneedham/ranking-algorithms/blob/27f94ccf1fc6c63663c8b3d512a2470330585803/src/ranking_algorithms/core.clj">core.clj</a> on github.</em></p>


<p>Clojure-wise I learnt about the <cite><a href="http://clojuredocs.org/clojure_core/clojure.pprint/print-table">print-table</a></cite> function which came in handy and Elo-wise I realised that the ranking places a heavy emphasis on winning matches.</p>


<p>If you follow the Champions League closely you'll have noticed that Barcelona are missing from the top 10 despite reaching the Semi Final. The Elo algorithm actually ranks them in 65th position:</p>



~~~lisp

=========================================================================================
:rank | :team               | :ranking | :round                  | :wins | :draw | :loses
=========================================================================================
63    | Motherwell          | 1195.04  | Third qualifying round  | 0     | 0     | 2     
64    | Feyenoord           | 1195.04  | Third qualifying round  | 0     | 0     | 2     
65    | Barcelona           | 1194.68  | Semi-finals             | 5     | 3     | 4     
66    | BATE                | 1194.36  | Group stage             | 5     | 3     | 4     
67    | Anderlecht          | 1193.41  | Group stage             | 4     | 2     | 4 
=========================================================================================
~~~

<h4>It's all about winning</h4>

<p>I thought there might be a bug in my implementation but having looked through it multiple times, Barcelona's low ranking results from losing multiple games - to Celtic, AC Milan and twice to Bayern Munich - and progressing from their Quarter Final tie against PSG without winning either match.</p>


<p>I did apply a higher weighting to matches won later on in the competition but otherwise the Elo algorithm doesn't take into account progress in a tournament.</p>


<h4>Low variation in rankings</h4>

<p>The initial ranking of each team was 1200, so I was surprised to see that the top ranked team had only achieved a ranking of 1272 - I expected it to be higher.</p>


<p>I read a bit more about the algorithm and learnt that a 200 points gap in ranking signifies that the higher ranked team should win 75% of the time.</p>
 

<p>For this data set the top ranked team has 1272 points and the lowest ranked team has 1171 points so we probably need to tweak the algorithm to make it more accurate.</p>


<h4>Accuracy of the Elo algorithm</h4>

<p>My understanding of the Elo algorithm is that it becomes more accurate as teams play more matches so I decided to try it out on all the matches from 2004 - 2012.</p>


<p>I adapted the <cite>print-top-teams</cite> function to exclude ':round' since it doesn't make sense in this context:</p>



~~~lisp

(comment "I really need to pull out the printing stuff into a function but I'm lazy so I haven't...yet")

(defn print-top-teams-without-round
  ([number all-matches] (print-top-teams-without-round number all-matches {}))
  ([number all-matches base-rankings]
      (clojure.pprint/print-table
       [:rank :team :ranking :wins :draw :loses]
       (map-indexed
        (partial format-for-printing all-matches)
        (top-teams number all-matches base-rankings)))))
~~~

<p>If we evaluate that function we see the following rankings:</p>



~~~lisp

> (def the-matches (read-from-file "data/cl-matches-2004-2012.json"))
#'ranking-algorithms.uefa/the-matches

> (ranking-algorithms.core/print-top-teams-without-round 10 the-matches)
==========================================================
:rank | :team          | :ranking | :wins | :draw | :loses
==========================================================
1     | Barcelona      | 1383.85  | 55    | 25    | 12    
2     | Man. United    | 1343.54  | 49    | 21    | 14    
3     | Chelsea        | 1322.0   | 44    | 27    | 17    
4     | Real Madrid    | 1317.68  | 42    | 14    | 18    
5     | Bayern         | 1306.18  | 42    | 13    | 19    
6     | Arsenal        | 1276.83  | 47    | 21    | 18    
7     | Liverpool      | 1272.52  | 41    | 17    | 17    
8     | Internazionale | 1260.27  | 36    | 18    | 21    
9     | Milan          | 1257.63  | 34    | 22    | 18    
10    | Bordeaux       | 1243.04  | 12    | 3     | 7     
==========================================================
~~~

<p>The only finalists missing from this list are Monaco and Porto who contested the final in 2004 but haven't reached that level of performance since.</p>
 

<p>Bordeaux are the only unlikely entry in this list and have played ~60 games less than the other teams which suggests that we might not have as much confidence in their ranking. It was at this stage that I started looking at the <a href="http://glicko.net/glicko/glicko.pdf">Glicko algorithm</a> which calculates a rating reliability as well as the rating itself.</p>


<p>I've <a href="https://github.com/mneedham/ranking-algorithms">added instructions to the github README</a> showing some examples but if you have any questions feel free to ping me on here or <a href="https://twitter.com/markhneedham">twitter</a>.</p>

