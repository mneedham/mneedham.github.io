+++
draft = false
date="2015-04-12 07:55:29"
title="R: Creating an object with functions to calculate conditional probability"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been working through Alan Downey's <a href="http://www.greenteapress.com/thinkbayes/">Thinking Bayes</a> and I thought it'd be an interesting exercise to translate some of the code from Python to R.
</p>


<p>
The first example is a simple one about conditional probablity and the author creates a class 'PMF' (Probability Mass Function) to solve the following problem:
</p>


<blockquote>
Suppose there are two bowls of cookies. Bowl 1 contains 30 vanilla cookies and 10 chocolate cookies. Bowl 2 contains 20 of each. 

Now suppose you choose one of the bowls at random and, without looking, select a cookie at random. The cookie is vanilla. 

What is the probability that it came from Bowl 1? 
</blockquote>

<p>
In Python the code looks like this:
</p>



~~~python

pmf = Pmf()
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

pmf.Normalize()

print pmf.Prob('Bowl 1')
~~~

<p>The 'PMF' class is defined <a href="http://www.greenteapress.com/thinkbayes/thinkbayes.py">here</a>.</p>


<ul>
<li>'Set' defines the prior probability of picking a cookie from either bowl i.e. in our case it's random.</li>
<li>'Mult' defines the likelihood of picking a vanilla biscuit from either bowl</li>
<li>'Normalize' applies a normalisation so that our posterior probabilities add up to 1.</li>
</ul>

<p>We want to create something similar in R and the actual calculation is stragiht forward:
</p>



~~~r

pBowl1 = 0.5
pBowl2 = 0.5

pVanillaGivenBowl1 = 0.75
pVanillaGivenBowl2 = 0.5

> (pBowl1 * pVanillaGivenBowl1) / ((pBowl1 * pVanillaGivenBowl1) + (PBowl2 * pVanillaGivenBowl2))
0.6

> (pBowl2 * pVanillaGivenBowl2) / ((pBowl1 * pVanillaGivenBowl1) + (pBowl2 * pVanillaGivenBowl2))
0.4
~~~

<p>
The problem is we have quite a bit of duplication and it doesn't read as cleanly as the Python version.
</p>


<p>
I'm not sure of the idiomatic way of handling this type of problem in R with mutable state in R but it seems like we can achieve this <a href="http://cran.r-project.org/doc/manuals/r-release/R-intro.html#Writing-your-own-functions">using functions</a>.</p>


<p>
I ended up writing the following function which returns a list of other functions to call.
</p>



~~~r

create.pmf = function() {
  priors <<- c()
  likelihoods <<- c()
  list(
    prior = function(option, probability) {
      l = c(probability)  
      names(l) = c(option)
      priors <<- c(priors, l)
    },
    likelihood = function(option, probability) {
      l = c(probability)  
      names(l) = c(option)
      likelihoods <<- c(likelihoods, l)
    },
    posterior = function(option) {
      names = names(priors)
      normalised = 0.0
      for(name in names) {
        normalised = normalised + (priors[name] * likelihoods[name])
      }
      
      (priors[option] * likelihoods[option]) / normalised
    }    
  )
}
~~~

<p>I couldn't work out how to get 'priors' and 'likelihoods' to be lexically scoped so I've currently got those defined as global variables. I'm using a <a href="http://stackoverflow.com/questions/2858014/working-with-dictionaries-lists-in-r">list as a kind of dictionary following a suggestion on Stack Overflow</a>.
</p>


<p>
The code doesn't handle the unhappy path very well but it seems to work for the example from the book:
</p>



~~~r

pmf = create.pmf()

pmf$prior("Bowl 1", 0.5)
pmf$prior("Bowl 2", 0.5)

pmf$likelihood("Bowl 1", 0.75)
pmf$likelihood("Bowl 2", 0.5)

> pmf$posterior("Bowl 1")
Bowl 1 
   0.6 
> pmf$posterior("Bowl 2")
Bowl 2 
   0.4 
~~~

<p>
How would you solve this type of problem? Is there a cleaner/better way?
</p>

