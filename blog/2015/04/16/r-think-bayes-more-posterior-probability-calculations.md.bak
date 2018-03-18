+++
draft = false
date="2015-04-16 20:57:20"
title="R: Think Bayes - More posterior probability calculations"
tag=['r-2']
category=['R']
+++

<p>As I mentioned in a post last week I've been reading through <a href="http://thinkbayes.com">Think Bayes</a> and <a href="http://www.markhneedham.com/blog/2015/04/12/r-creating-an-object-with-functions-to-calculate-conditional-probability/">translating some of the examples form Python to R</a>.
</p>


<p>
After my first post <a href="https://twitter.com/tonkouts">Antonios</a> suggested a more idiomatic way of writing the function in R so I thought I'd give it a try to calculate the probability that combinations of cookies had come from each bowl.
</p>

			
<p>
In the simplest case we have this function which takes in the names of the bowls and the likelihood scores:
</p>



~~~r

f = function(names,likelihoods) {
  # Assume each option has an equal prior
  priors = rep(1, length(names)) / length(names)
  
  # create a data frame with all info you have
  dt = data.frame(names,priors,likelihoods)
  
  # calculate posterior probabilities
  dt$post = dt$priors*dt$likelihoods / sum(dt$priors*dt$likelihoods)
  
  # specify what you want the function to return
  list(names=dt$names, priors=dt$priors, likelihoods=dt$likelihoods, posteriors=dt$post)  
}
~~~

<p>
We assume a prior probability of 0.5 for each bowl.</p>


<p>Given the following probabilities of of different cookies being in each bowl...
</p>



~~~python

mixes = {
  'Bowl 1':dict(vanilla=0.75, chocolate=0.25),
  'Bowl 2':dict(vanilla=0.5, chocolate=0.5),
}
~~~

<p>...we can simulate taking one vanilla cookie with the following parameters:</p>



~~~r

Likelihoods = c(0.75,0.5)
Names = c("Bowl 1", "Bowl 2")
res=f(Names,Likelihoods)

> res$posteriors[res$name == "Bowl 1"]
[1] 0.6
> res$posteriors[res$name == "Bowl 2"]
[1] 0.4
~~~

<p>If we want to simulate taking 3 vanilla cookies and 1 chocolate one we'd have the following:</p>



~~~r

Likelihoods = c((0.75 ** 3) * (0.25 ** 1), (0.5 ** 3) * (0.5 ** 1))
Names = c("Bowl 1", "Bowl 2")
res=f(Names,Likelihoods)

> res$posteriors[res$name == "Bowl 1"]
[1] 0.627907
> res$posteriors[res$name == "Bowl 2"]
[1] 0.372093
~~~

<p>
That's a bit clunky and the intent of '3 vanilla cookies and 1 chocolate' has been lost. I decided to refactor the code to take in a vector of cookies and calculate the likelihoods internally.
</p>


<p>
First we need to create a data structure to store the mixes of cookies in each bowl that we defined above. It turns out we can do this using a <a href="http://stackoverflow.com/questions/22097029/nested-dictionary-in-r">nested list</a>:
</p>



~~~r

bowl1Mix = c(0.75, 0.25)
names(bowl1Mix) = c("vanilla", "chocolate")
bowl2Mix = c(0.5, 0.5)
names(bowl2Mix) = c("vanilla", "chocolate")
Mixes = list("Bowl 1" = bowl1Mix, "Bowl 2" = bowl2Mix)

> Mixes
$`Bowl 1`
  vanilla chocolate 
     0.75      0.25 

$`Bowl 2`
  vanilla chocolate 
      0.5       0.5 
~~~

<p>
Now let's tweak our function to take in observations rather than likelihoods and then calculate those likelihoods internally:
<p>


~~~r

likelihoods = function(names, observations) {
  scores = c(1,1)
  names(scores) = names
  
  for(name in names) {
      for(observation in observations) {
        scores[name] = scores[name] *  mixes[[name]][observation]      
      }
    }  
  return(scores)
}

f = function(names,mixes,observations) {
  # Assume each option has an equal prior
  priors = rep(1, length(names)) / length(names)
  
  # create a data frame with all info you have
  dt = data.frame(names,priors)
  
  dt$likelihoods = likelihoods(Names, Observations)
  
  # calculate posterior probabilities
  dt$post = dt$priors*dt$likelihoods / sum(dt$priors*dt$likelihoods)
  
  # specify what you want the function to return
  list(names=dt$names, priors=dt$priors, likelihoods=dt$likelihoods, posteriors=dt$post)  
}
~~~

<p>And if we call that function:</p>



~~~r

Names = c("Bowl 1", "Bowl 2")

bowl1Mix = c(0.75, 0.25)
names(bowl1Mix) = c("vanilla", "chocolate")
bowl2Mix = c(0.5, 0.5)
names(bowl2Mix) = c("vanilla", "chocolate")
Mixes = list("Bowl 1" = bowl1Mix, "Bowl 2" = bowl2Mix)
Mixes

Observations = c("vanilla", "vanilla", "vanilla", "chocolate")

res=f(Names,Mixes,Observations)

> res$posteriors[res$names == "Bowl 1"]
[1] 0.627907

> res$posteriors[res$names == "Bowl 2"]
[1] 0.372093
~~~

<p>Exactly the same result as before! #win</p>

