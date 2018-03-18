+++
draft = false
date="2015-04-22 22:18:00"
title="R: Replacing for loops with data frames"
tag=['r-2']
category=['R']
+++

<p>In my last blog post I showed how to <a href="http://www.markhneedham.com/blog/2015/04/21/r-numeric-keys-in-the-nested-listdictionary/">derive posterior probabilities for the Think Bayes dice problem</a>:
</p>


<blockquote>
Suppose I have a box of dice that contains a 4-sided die, a 6-sided die, an 8-sided die, a 12-sided die, and a 20-sided die. If you have ever played Dungeons & Dragons, you know what I am talking about.

Suppose I select a die from the box at random, roll it, and get a 6. What is the probability that I rolled each die?

</blockquote>

<p>To recap, this was my final solution:</p>



~~~R

likelihoods = function(names, observations) {
  scores = rep(1.0 / length(names), length(names))  
  names(scores) = names
 
  for(name in names) {
      for(observation in observations) {
        if(name < observation) {
          scores[paste(name)]  = 0
        } else {
          scores[paste(name)] = scores[paste(name)] *  (1.0 / name)
        }        
      }
    }  
  return(scores)
}
 
dice = c(4,6,8,12,20)
l1 = likelihoods(dice, c(6))

> l1 / sum(l1)
        4         6         8        12        20 
0.0000000 0.3921569 0.2941176 0.1960784 0.1176471
~~~

<p>Although it works we have nested for loops which aren't very idiomatic R so let's try and get rid of them.</p>


<p>
The first thing we want to do is return a data frame rather than a vector so we tweak the first two lines to read like this:
</p>



~~~r

scores = rep(1.0 / length(names), length(names))  
df = data.frame(score = scores, name = names)
~~~

<p>
Next we can get rid of the inner for loop and replace it with a call to ifelse wrapped inside a dplyr mutate call:
</p>



~~~r

library(dplyr)
likelihoods2 = function(names, observations) {
  scores = rep(1.0 / length(names), length(names))  
  df = data.frame(score = scores, name = names)
  
  for(observation in observations) {
    df = df %>% mutate(score = ifelse(name < observation, 0, score * (1.0 / name)) )
  }
  
  return(df)
}

dice = c(4,6,8,12,20)
l1 = likelihoods2(dice, c(6))

> l1
       score name
1 0.00000000    4
2 0.03333333    6
3 0.02500000    8
4 0.01666667   12
5 0.01000000   20
~~~

<p>Finally we'll tidy up the scores so they're relatively weighted against each other:</p>



~~~r

likelihoods2 = function(names, observations) {
  scores = rep(1.0 / length(names), length(names))  
  df = data.frame(score = scores, name = names)
  
  for(observation in observations) {
    df = df %>% mutate(score = ifelse(name < observation, 0, score * (1.0 / name)) )
  }
  
  return(df %>% mutate(weighted = score / sum(score)) %>% select(name, weighted))
}

dice = c(4,6,8,12,20)
l1 = likelihoods2(dice, c(6))

> l1
  name  weighted
1    4 0.0000000
2    6 0.3921569
3    8 0.2941176
4   12 0.1960784
5   20 0.1176471
~~~

<p>
Now we're down to just the one for loop. Getting rid of that one is a bit trickier. First we'll create a data frame which contains a row for every (observation, dice) pair, simulating the nested for loops:
</p>



~~~r

likelihoods3 = function(names, observations) {
  l = list(observation = observations, roll = names)
  obsDf = do.call(expand.grid,l) %>% 
    mutate(likelihood = 1.0 / roll, 
           score = ifelse(roll < observation, 0, likelihood))   

  return(obsDf)
}

dice = c(4,6,8,12,20)
l1 = likelihoods3(dice, c(6))

> l1
  observation roll likelihood      score
1           6    4 0.25000000 0.00000000
2           6    6 0.16666667 0.16666667
3           6    8 0.12500000 0.12500000
4           6   12 0.08333333 0.08333333
5           6   20 0.05000000 0.05000000

l2 = likelihoods3(dice, c(6, 4, 8, 7, 7, 2))
> l2
   observation roll likelihood      score
1            6    4 0.25000000 0.00000000
2            4    4 0.25000000 0.25000000
3            8    4 0.25000000 0.00000000
4            7    4 0.25000000 0.00000000
5            7    4 0.25000000 0.00000000
6            2    4 0.25000000 0.25000000
7            6    6 0.16666667 0.16666667
8            4    6 0.16666667 0.16666667
9            8    6 0.16666667 0.00000000
10           7    6 0.16666667 0.00000000
11           7    6 0.16666667 0.00000000
12           2    6 0.16666667 0.16666667
13           6    8 0.12500000 0.12500000
14           4    8 0.12500000 0.12500000
15           8    8 0.12500000 0.12500000
16           7    8 0.12500000 0.12500000
17           7    8 0.12500000 0.12500000
18           2    8 0.12500000 0.12500000
19           6   12 0.08333333 0.08333333
20           4   12 0.08333333 0.08333333
21           8   12 0.08333333 0.08333333
22           7   12 0.08333333 0.08333333
23           7   12 0.08333333 0.08333333
24           2   12 0.08333333 0.08333333
25           6   20 0.05000000 0.05000000
26           4   20 0.05000000 0.05000000
27           8   20 0.05000000 0.05000000
28           7   20 0.05000000 0.05000000
29           7   20 0.05000000 0.05000000
30           2   20 0.05000000 0.05000000
~~~

<p>
Now we need to iterate over the data frame, grouping by 'roll' so that we end up with one row for each one.</p>
 

<p>We'll add a new column which stores the posterior probability for each dice. This will be calculated by multiplying the prior probability by the product of the 'score' entries.
</p>


<p>This is what our new likelihood function looks like:</p>



~~~r

likelihoods3 = function(names, observations) {
  l = list(observation = observations, roll = names)
  obsDf = do.call(expand.grid,l) %>% 
    mutate(likelihood = 1.0 / roll, 
           score = ifelse(roll < observation, 0, likelihood))   
  
  return (obsDf %>% 
    group_by(roll) %>% 
    summarise(s = (1.0/length(names)) * prod(score) ) %>%
    ungroup() %>% 
    mutate(weighted = s / sum(s)) %>%
    select(roll, weighted))
}

l1 = likelihoods3(dice, c(6))
> l1
Source: local data frame [5 x 2]

  roll  weighted
1    4 0.0000000
2    6 0.3921569
3    8 0.2941176
4   12 0.1960784
5   20 0.1176471
 
l2 = likelihoods3(dice, c(6, 4, 8, 7, 7, 2))
> l2
Source: local data frame [5 x 2]

  roll    weighted
1    4 0.000000000
2    6 0.000000000
3    8 0.915845272
4   12 0.080403426
5   20 0.003751302
~~~

<p>
We've now got the same result as we did with our nested for loops so I think the refactoring has been a success.
</p>

