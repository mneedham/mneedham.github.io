+++
draft = false
date="2013-08-30 12:23:21"
title="Clojure: Handling state by updating a vector inside an atom"
tag=['clojure']
category=['Clojure']
+++

<p>As I mentioned in a <a href="http://www.markhneedham.com/blog/2013/08/24/ranking-systems-what-ive-learnt-so-far/">previous blog post</a>, I've been learning about ranking algorithms and I wanted to apply them to a series of football matches to see who the strongest team was.</p>


<p>Before that, however, I wanted to sketch out the functions that I'd need to do this and I started with the following collections of matches and team rankings:</p>



~~~lisp

(def m
  [{:home "Manchester United", :away "Manchester City", :home_score 1, :away_score 0}
   {:home "Manchester United", :away "Manchester City", :home_score 2, :away_score 0}])

(def teams
  [ {:name "Manchester United" :points 1200}
    {:name "Manchester City" :points 1200} ])
~~~

<p>I wanted to iterate over the matches and make the appropriate updates to the teams' rankings depending on the result of the match. If a team wins their ranking goes up and if they lose it goes down.</p>


<p>I wasn't sure how to iterate over the matches and pass along an updated teams collection so I decided to wrap teams in an <a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/atom">atom</a> that I could update:</p>



~~~lisp

(def t (atom teams))
~~~

<p>The next step was to work out how to update the vector inside the atom <cite>t</cite>. The <cite><a href="http://clojuredocs.org/clojure_core/1.2.0/clojure.core/assoc">assoc</a></cite> function comes in useful here. If we want to update the ranking for Manchester United we could write the following code:</p>



~~~lisp

> (map #(if (= "Manchester United" (:name %))
         (assoc % :points 1500)
         %)
      teams)
[{:name "Manchester United", :points 1500} {:name "Manchester City", :points 1200}]
~~~

<p>We're mapping over the collection of teams and then each time checking whether or not the team is Manchester United. If it is then we update the ':points' value and if not then we leave it alone.</p>


<p>The next step is to update the vector that the atom <cite>t</cite> references which we can do by using the <cite>swap!</cite> function:</p>



~~~lisp

> (swap! t
         (fn [teams]
           (map #(if (= "Manchester United" (:name %)) (assoc % :points 1500) %)
                teams)))
({:name "Manchester United", :points 1500} {:name "Manchester City", :points 1200})
~~~

<p>If we look inside <cite>t</cite> we can see that its reference has changed as well:~~~


~~~lisp

> @t
[{:name "Manchester United", :points 1500} {:name "Manchester City", :points 1200}]
~~~

<p>Our next step is to pull this code into a function that we can call from other code since we'll eventually want to iterate over the matches and update teams appropriately.</p>


<p>Since we know that we'll need to update both the home and away team after each match we'll make sure the function can handle that:</p>



~~~lisp

(defn update-teams
  [teams team1 new-score1 team2 new-score2]
  (vec
   (map #(cond (= team1 (:name %)) (assoc % :points new-score1)
               (= team2 (:name %)) (assoc % :points new-score2)
               :else %)
        teams)))
~~~

<p>We're calling <cite>vec</cite> on the result to get back to a vector like we had initially. We'll handle the updating of the atom reference from elsewhere, this function only handles creating a new instance of the underlying vector.</p>


<p>Now let's call that function while we're iterating over the matches that we defined earlier:</p>



~~~lisp

> (map (fn [match]
       (swap! t (fn [teams]
                  (update-teams teams
                               (:home match)
                               (new-home-score match teams)
                               (:away match)
                               (new-away-score match teams)))))
     m)
([{:name "Manchester United", :points 1201} {:name "Manchester City", :points 1201}] [{:name "Manchester United", :points 1202} {:name "Manchester City", :points 1202}])
~~~

<p>In this case I've stubbed out <cite>new-home-score</cite> and <cite>new-away-score</cite> to increment the existing ranking by one:</p>



~~~lisp

(defn new-home-score
  [match teams]
  (let [home-team (find-team (:home match) teams)]
    (inc (:points home-team))))

(defn new-away-score
  [match teams]
  (let [away-team (find-team (:away match) teams)]
    (inc (:points away-team))))

(defn find-team [team teams]
  (first
   (filter #(= team (:name %)) teams)))
~~~

<p>If we were using a real algorithm we'd assign points to the winner and take them away from the loser of a match.</p>


<p>Although the map over the matches actually returns a collection showing the updated rankings after each match, if we want to access the current rankings we'd deference the atom <cite>t</cite> like we did earlier:</p>



~~~lisp

> @t
[{:name "Manchester United", :points 1202} {:name "Manchester City", :points 1202}]
~~~

<p>This approach works but it feels a bit hacky to have resorted to using an atom so I'd be interested in hearing from any Clojure experts if there's a better way to solve this type of problem and if so what it is.</p>

