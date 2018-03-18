+++
draft = false
date="2015-06-02 06:49:10"
title="R: dplyr - removing empty rows"
tag=['r-2', 'dplyr']
category=['R']
+++

<p>
I'm still working my way through the exercises in Think Bayes and in Chapter 6 needed to do some cleaning of the data in a CSV file containing information about the Price is Right.

</p>


<p>
I downloaded the file using wget:
</p>



~~~bash

wget ￼http://www.greenteapress.com/thinkbayes/showcases.2011.csv￼
~~~

<p>And then loaded it into R and explored the first few rows using dplyr</p>



~~~R

library(dplyr)
df2011 = read.csv("~/projects/rLearning/showcases.2011.csv")

> df2011 %>% head(10)

           X Sep..19 Sep..20 Sep..21 Sep..22 Sep..23 Sep..26 Sep..27 Sep..28 Sep..29 Sep..30 Oct..3
1              5631K   5632K   5633K   5634K   5635K   5641K   5642K   5643K   5644K   5645K  5681K
2                                                                                                  
3 Showcase 1   50969   21901   32815   44432   24273   30554   20963   28941   25851   28800  37703
4 Showcase 2   45429   34061   53186   31428   22320   24337   41373   45437   41125   36319  38752
5                                                                                                  
...
~~~

<p>
As you can see, we have some empty rows which we want to get rid of to ease future processing. I couldn't find an easy way to filter those out but what we can do instead is have empty columns converted to 'NA' and then filter those.
</p>


<p>
First we need to tell <cite>read.csv</cite> to treat empty columns as NA:
</p>



~~~r

df2011 = read.csv("~/projects/rLearning/showcases.2011.csv", na.strings = c("", "NA"))
~~~

<p>And now we can filter them out using <cite>na.omit</cite>:</p>



~~~r

df2011 = df2011 %>% na.omit()

> df2011  %>% head(5)
             X Sep..19 Sep..20 Sep..21 Sep..22 Sep..23 Sep..26 Sep..27 Sep..28 Sep..29 Sep..30 Oct..3
3   Showcase 1   50969   21901   32815   44432   24273   30554   20963   28941   25851   28800  37703
4   Showcase 2   45429   34061   53186   31428   22320   24337   41373   45437   41125   36319  38752
6        Bid 1   42000   14000   32000   27000   18750   27222   25000   35000   22500   21300  21567
7        Bid 2   34000   59900   45000   38000   23000   18525   32000   45000   32000   27500  23800
9 Difference 1    8969    7901     815   17432    5523    3332   -4037   -6059    3351    7500  16136
...
~~~

<p>Much better!</p>

