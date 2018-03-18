+++
draft = false
date="2015-04-18 23:53:20"
title="R: Removing for loops"
tag=['r-2']
category=['R']
+++

<p>In my last blog post I showed <a href="http://www.markhneedham.com/blog/2015/04/16/r-think-bayes-more-posterior-probability-calculations/">the translation of a likelihood function from Think Bayes into R</a> and in my first attempt at this function I used a couple of nested for loops.
</p>



~~~r

likelihoods = function(names, mixes, observations) {
  scores = rep(1, length(names))
  names(scores) = names
  
  for(name in names) {
      for(observation in observations) {
        scores[name] = scores[name] *  mixes[[name]][observation]      
      }
    }  
  return(scores)
}
~~~


~~~r

Names = c("Bowl 1", "Bowl 2")

bowl1Mix = c(0.75, 0.25)
names(bowl1Mix) = c("vanilla", "chocolate")
bowl2Mix = c(0.5, 0.5)
names(bowl2Mix) = c("vanilla", "chocolate")
Mixes = list("Bowl 1" = bowl1Mix, "Bowl 2" = bowl2Mix)
Mixes

Observations = c("vanilla", "vanilla", "vanilla", "chocolate")
l = likelihoods(Names, Mixes, Observations)

> l / sum(l)
  Bowl 1   Bowl 2 
0.627907 0.372093 
~~~

<p>
We pass in a vector of bowls, a nested dictionary describing the mixes of cookies in each bowl and the observations that we've made. The function tells us that there's an almost 2/3 probability of the cookies coming from Bowl 1 and just over 1/3 of being Bowl 2.
</p>


<p>
In this case there probably won't be much of a performance improvement by getting rid of the loops but we should be able to write something that's more concise and hopefully idiomatic.
</p>


<p>
Let's start by getting rid of the inner for loop. That can be replace by a call to the <cite><a href="http://adv-r.had.co.nz/Functionals.html">Reduce</a></cite> function like so:
</p>




~~~r

likelihoods2 = function(names, mixes, observations) {
  scores = rep(0, length(names))
  names(scores) = names
  
  for(name in names) {
    scores[name] = Reduce(function(acc, observation) acc *  mixes[[name]][observation], Observations, 1)
  }  
  return(scores)
}
~~~


~~~r

l2 = likelihoods2(Names, Mixes, Observations)

> l2 / sum(l2)
  Bowl 1   Bowl 2 
0.627907 0.372093 
~~~

<p>
So that's good, we've still got the same probabilities as before. Now to get rid of the outer for loop. The <cite><a href="http://adv-r.had.co.nz/Functionals.html">Map</a></cite> function helps us out here:
</p>



~~~r

likelihoods3 = function(names, mixes, observations) {
  scores = rep(0, length(names))
  names(scores) = names
  
  scores = Map(function(name) 
    Reduce(function(acc, observation) acc *  mixes[[name]][observation], Observations, 1), 
    names)
  
  return(scores)
}

l3 = likelihoods3(Names, Mixes, Observations)
> l3
$`Bowl 1`
  vanilla 
0.1054688 

$`Bowl 2`
vanilla 
 0.0625 
~~~

<p>
We end up with a list instead of a vector which we need to fix by using the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/unlist.html">unlist</a></cite> function:
</p>



~~~r

likelihoods3 = function(names, mixes, observations) {
  scores = rep(0, length(names))
  names(scores) = names
  
  scores = Map(function(name) 
    Reduce(function(acc, observation) acc *  mixes[[name]][observation], Observations, 1), 
    names)
  
  return(unlist(scores))
}

l3 = likelihoods3(Names, Mixes, Observations)

> l3 / sum(l3)
Bowl 1.vanilla Bowl 2.vanilla 
      0.627907       0.372093 
~~~

<p>
Now we just have this annoying 'vanilla' in the name. That's fixed easily enough:
</p>



~~~r

likelihoods3 = function(names, mixes, observations) {
  scores = rep(0, length(names))
  names(scores) = names
  
  scores = Map(function(name) 
    Reduce(function(acc, observation) acc *  mixes[[name]][observation], Observations, 1), 
    names)
  
  result = unlist(scores)
  names(result) = names
  
  return(result)
}

l3 = likelihoods3(Names, Mixes, Observations)

> l3 / sum(l3)
  Bowl 1   Bowl 2 
0.627907 0.372093 
~~~

<P>A slightly cleaner alternative makes use of the <cite><a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/lapply.html">sapply</a></cite> function:</p>



~~~r

likelihoods3 = function(names, mixes, observations) {
  scores = rep(0, length(names))
  names(scores) = names
  
  scores = sapply(names, function(name) 
    Reduce(function(acc, observation) acc *  mixes[[name]][observation], Observations, 1))
  names(scores) = names
    
  return(scores)
}

l3 = likelihoods3(Names, Mixes, Observations)

> l3 / sum(l3)
  Bowl 1   Bowl 2 
0.627907 0.372093 
~~~

<p>That's the best I've got for now but I wonder if we could write a version of this using matrix operations some how - but that's for next time!
</p>

