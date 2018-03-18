+++
draft = false
date="2015-04-21 05:59:24"
title="R: Numeric keys in the nested list/dictionary"
tag=['r-2']
category=['R']
+++

<p>Last week I described how I've been <a href="http://www.markhneedham.com/blog/2015/04/16/r-think-bayes-more-posterior-probability-calculations/">creating fake dictionaries in R using lists</a> and I found myself using the same structure while solving the <a href="http://www.greenteapress.com/thinkbayes/dice.py">dice problem</a> in <a href="http://www.greenteapress.com/thinkbayes/">Think Bayes</a>.</p>


<p>The dice problem is described as follows:</p>


<blockquote>
Suppose I have a box of dice that contains a 4-sided die, a 6-sided die, an 8-sided die, a 12-sided die, and a 20-sided die. If you have ever played Dungeons & Dragons, you know what I am talking about. 

Suppose I select a die from the box at random, roll it, and get a 6. 
What is the probability that I rolled each die? 
</blockquote>

<p>
Here's a simple example of the nested list that I started with:
</p>



~~~r

dice = c(4,6,8,12,20)
priors = rep(1.0 / length(dice), length(dice))
names(priors) = dice

> priors
  4   6   8  12  20 
0.2 0.2 0.2 0.2 0.2 
~~~

<p>
I wanted to retrieve the prior for the 8 dice which I tried to do like this:
</p>



~~~r

> priors[8]
<NA> 
  NA 
~~~

<p>
That comes back with 'NA' because we're actually looking for the numeric index 8 rather than the item in that column.
</p>


<p>
As far as I understand if we want to look up values by name we have to use a string so I tweaked the code to store names as strings:
</p>



~~~r

dice = c(4,6,8,12,20)
priors = rep(1.0 / length(dice), length(dice))
names(priors) = sapply(dice, paste)

> priors["8"]
  8 
0.2 
~~~

<p>
That works much better but with some experimentation I realised I didn't even need to run 'dice' through the <a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/lapply.html"><cite>sapply</cite></a> function, it already works the way it was:
</p>



~~~r

dice = c(4,6,8,12,20)
priors = rep(1.0 / length(dice), length(dice))
names(priors) = dice

> priors["8"]
  8 
0.2 
~~~

<p>
Now that we've got that working we can write a likelihood function which takes in observed dice rolls and tells us how likely it was that we rolled each type of dice. We start simple by copying the above code into a function:
</p>



~~~r

likelihoods = function(names, observations) {
  scores = rep(1.0 / length(names), length(names))  
  names(scores) = names
  
  return(scores)
}

dice = c(4,6,8,12,20)
l1 = likelihoods(dice, c(6))

> l1
  4   6   8  12  20 
0.2 0.2 0.2 0.2 0.2 
~~~

<p>
Next we'll update the score for a particular dice to 0 if one of the observed rolls is greater than the dice's maximum score:
</p>



~~~r

likelihoods = function(names, observations) {
  scores = rep(1.0 / length(names), length(names))  
  names(scores) = names
  
  for(name in names) {
      for(observation in observations) {
        if(name < observation) {
          scores[paste(name)]  = 0       
        }
      }
    }  
  return(scores)
}

dice = c(4,6,8,12,20)
l1 = likelihoods(dice, c(6))

> l1
  4   6   8  12  20 
0.0 0.2 0.2 0.2 0.2 
~~~

<p>The 4 dice has been ruled out since we've rolled a 6! Now let's put in the else condition which updates our score by the probability that we got the observed roll with each of valid dice. i.e. we have a 1/20 chance of rolling any number with the 20 side dice, a 1/8 chance with the 8 sided dice etc.</p>



~~~r

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

> l1
         4          6          8         12         20 
0.00000000 0.03333333 0.02500000 0.01666667 0.01000000
~~~

<p>And finally let's normalise those scores so they're a bit more readable:</p>



~~~r

> l1 / sum(l1)
        4         6         8        12        20 
0.0000000 0.3921569 0.2941176 0.1960784 0.1176471 
~~~
