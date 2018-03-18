+++
draft = false
date="2013-08-31 13:01:16"
title="Elo Rating System: Ranking Champions League teams using Clojure"
tag=['clojure', 'ranking-systems']
category=['Clojure', 'Ranking Systems']
+++

<p>As I mentioned in an earlier blog post <a href="http://www.markhneedham.com/blog/2013/08/24/ranking-systems-what-ive-learnt-so-far/">I've been learning about ranking systems</a> and one of the first ones I came across was the <a href="http://en.wikipedia.org/wiki/Elo_rating_system">Elo rating system</a> which is most famously used to rank chess players.</p>


<p>The Elo rating system uses the following formula to work out a player/team's ranking after they've participated in a match:</p>


<blockquote>
R' = R + K * (S - E)

<ul>
<li>R' is the new rating</li>
<li>R is the old rating</li>
<li>K is a maximum value for increase or decrease of rating (16 or 32 for ELO)</li>
<li>S is the score for a game</li>
<li>E is the expected score for a game</li>
</blockquote>

<p>I converted that formula into the following Clojure functions:</p>



~~~lisp

(defn ranking-after-win
  [{ ranking :ranking opponent-ranking :opponent-ranking importance :importance}]
  (+ ranking (* importance (- 1 (expected ranking opponent-ranking) ))))

(defn ranking-after-loss
  [{ ranking :ranking opponent-ranking :opponent-ranking importance :importance}]
  (+ ranking (* importance (- 0 (expected ranking opponent-ranking) ))))

(defn expected [my-ranking opponent-ranking]
  (/ 1.0
     (+ 1 (math/expt 10 (/ (- opponent-ranking my-ranking) 400)))))
~~~

<p>which would be called like this to work out the new ranking of a team ranked 1200 that beat a team ranked 1500:</p>



~~~lisp

> (ranking-after-win { :ranking 1200 :opponent-ranking 1500 :importance 32 })
1227.1686541692377
~~~

<p>The way it works is that we first work out the likelihood that we should win the match by calling <cite>expected</cite>:</p>



~~~lisp

> (expected 1200 1500)
0.15097955721132328
~~~

<p>This tells us that we have a 15% chance of winning the match so if we do win then our ranking should be increased by a large amount as we aren't expected to win. In this case a win gives us a points increase of '32 * (1-0.15)' which is ~27 points.</p>
 

<p>I kept things simple by always setting the importance/maximum value of increase or decrease to 32. The <a href="http://www.eloratings.net/system.html">World Football Rankings</a> took a different approach where they vary it based on the importance of a match and the margin of victory.</p>


<p>I decided to try out the algorithm on the 2002/2003 Champions League season. I was able to <a href="http://www.rsssf.com/ec/ec200203det.html">grab the data</a> from The Rec Sport Soccer Statistics Foundation and I've written previously about <a href="http://www.markhneedham.com/blog/2013/08/26/clojureenlive-screen-scraping-a-html-file-from-disk/">how I scraped it using Enlive</a>.</p>


<p>With a lot of help from <a href="https://twitter.com/pbostrom">Paul Bostrom</a> I ended up with the following code to run a reduce over the matches while updating team rankings after each match:</p>



~~~lisp

(defn top-teams [number matches]
  (let [teams-with-rankings
    (apply array-map (mapcat (fn [x] [x {:points 1200}]) (extract-teams matches)))]
      (take number
        (sort-by (fn [x] (:points (val x)))
                 >
                 (seq (reduce process-match teams-with-rankings matches))))))

(defn process-match [ts match]
  (let [{:keys [home away home_score away_score]} match]
    (cond
     (> home_score away_score)
     (-> ts
         (update-in  [home :points]
                     #(ranking-after-win {:ranking % :opponent-ranking (:points (get ts away)) :importance 32}))
         (update-in  [away :points]
                     #(ranking-after-loss {:ranking % :opponent-ranking (:points (get ts home)) :importance 32}))) 
     (> away_score home_score)
     (-> ts
         (update-in  [home :points]
                     #(ranking-after-loss {:ranking % :opponent-ranking (:points  (get ts away)) :importance 32}))
         (update-in  [away :points]
                     #(ranking-after-win {:ranking % :opponent-ranking (:points (get ts home)) :importance 32})))
     (= home_score away_score) ts)))
~~~

<p>The <cite>matches</cite> parameter that we pass into <cite>top-teams</cite> <a href="https://github.com/mneedham/ranking-algorithms/blob/master/src/ranking_algorithms/parse.clj#L20">looks like this</a>:</p>



~~~lisp

> (take 5 all-matches)
({:home "Tampere", :away "Pyunik Erewan", :home_score 0, :away_score 4} {:home "Pyunik Erewan", :away "Tampere", :home_score 2, :away_score 0} {:home "Skonto Riga", :away "Barry Town", :home_score 5, :away_score 0} {:home "Barry Town", :away "Skonto Riga", :home_score 0, :away_score 1} {:home "Portadown", :away "Belshina Bobruisk", :home_score 0, :away_score 0})
~~~

<p>And calling <cite><a href="https://github.com/mneedham/ranking-algorithms/blob/master/src/ranking_algorithms/parse.clj#L22">extract-teams</a></cite> on it gets us a set of all the teams involved:</p>



~~~lisp

> (extract-teams (take 5 all-matches))
#{"Portadown" "Tampere" "Pyunik Erewan" "Barry Town" "Skonto Riga"}
~~~

<p>We then <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/mapcat">mapcat</a></cite> over it to get a vector containing team/default points pairs:</p>



~~~lisp

> (mapcat (fn [x] [x {:points 1200}]) (extract-teams (take 5 all-matches)))
("Portadown" {:points 1200} "Tampere" {:points 1200} "Pyunik Erewan" {:points 1200} "Barry Town" {:points 1200} "Skonto Riga" {:points 1200})
~~~

<p>before calling <cite><a href="http://clojuredocs.org/clojure_core/clojure.core/array-map">array-map</a></cite> to make a hash of the result:</p>



~~~lisp

> (apply array-map (mapcat (fn [x] [x {:points 1200}]) (extract-teams (take 5 all-matches))))
{"Portadown" {:points 1200}, "Tampere" {:points 1200}, "Pyunik Erewan" {:points 1200}, "Barry Town" {:points 1200}, "Skonto Riga" {:points 1200}}
~~~

<p>We then apply a reduce over all the matches and call the function <cite>process-match</cite> on each iteration to update team rankings appropriately. The final step is to sort the teams by their ranking so we can list the top teams:</p>



~~~lisp

> (top-teams 10 all-matches)
(["CF Barcelona" {:points 1343.900393287903}] 
 ["Manchester United" {:points 1292.4731214788262}] 
 ["FC Valencia" {:points 1277.1820905112208}] 
 ["Internazionale Milaan" {:points 1269.8028023141364}] 
 ["AC Milan" {:points 1257.4564374787687}]
 ["Juventus Turijn" {:points 1254.2498432522466}] 
 ["Real Madrid" {:points 1248.0758162475993}] 
 ["Deportivo La Coruna" {:points 1235.7792317210403}] 
 ["Borussia Dortmund" {:points 1231.1671952364256}] 
 ["Sparta Praag" {:points 1229.3249513256828}])
~~~

<p>Interestingly the winners (Juventus) are only in 5th place and the top 2 places are occupied by teams that lost in the Quarter Final. I wrote the following functions to investigate what was going on:</p>



~~~lisp

(defn show-matches [team matches]
  (->> matches
       (filter #(or (= team (:home %)) (= team (:away %))))
       (map #(show-opposition team %))))

(defn show-opposition [team match]
  (if (= team (:home match))
    {:opposition (:away match) :score (str (:home_score match) "-" (:away_score match))}
    {:opposition (:home match) :score (str (:away_score match) "-" (:home_score match))}))
~~~

<p>If we call it with Juventus we can see how they performed in their matches:</p>



~~~lisp

ranking-algorithms.parse> (show-matches "Juventus Turijn" all-matches)
({:opposition "Feyenoord", :score "1-1"} 
 {:opposition "Dynamo Kiev", :score "5-0"} 
 {:opposition "Newcastle United", :score "2-0"} 
 {:opposition "Newcastle United", :score "0-1"} 
 {:opposition "Feyenoord", :score "2-0"} 
 {:opposition "Dynamo Kiev", :score "2-1"} 
 {:opposition "Deportivo La Coruna", :score "2-2"} 
 {:opposition "FC Basel", :score "4-0"} 
 {:opposition "Manchester United", :score "1-2"} 
 {:opposition "Manchester United", :score "0-3"} 
 {:opposition "Deportivo La Coruna", :score "3-2"} 
 {:opposition "FC Basel", :score "1-2"} 
 {:opposition "CF Barcelona", :score "1-1"} 
 {:opposition "CF Barcelona", :score "2-1"} 
 {:opposition "Real Madrid", :score "1-2"} 
 {:opposition "Real Madrid", :score "3-1"})
~~~

<p>Although I'm missing the final - I need to fix the parser to pick that match up and it was a draw anyway - they actually only won 8 of their matches outright. Barcelona, on the other hand, won 13 matches although 2 of those were qualifiers.</p>


<p>The next step is to take into account the importance of the match rather than applying an importance of 32 across the board and adding some value to winning a tie/match even if it's on penalties or away goals.</p>


<p>The <a href="https://github.com/mneedham/ranking-algorithms/tree/master/src/ranking_algorithms">code is on github</a> if you want to play around with it or have suggestions for something else I can try out.</p>

