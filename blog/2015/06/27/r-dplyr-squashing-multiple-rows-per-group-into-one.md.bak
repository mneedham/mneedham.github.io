+++
draft = false
date="2015-06-27 22:36:50"
title="R: dplyr - squashing multiple rows per group into one"
tag=['r-2']
category=['R']
+++

<p>
I spent a bit of the day working on my <a href="http://www.markhneedham.com/blog/2015/06/25/r-scraping-wimbledon-draw-data/">Wimbledon</a> <a href="http://www.markhneedham.com/blog/2015/06/26/r-ggplot-show-discrete-scale-even-with-no-value/">data set</a> and the next thing I explored is all the people that have beaten Andy Murray in the tournament.
</p>


<p>The following dplyr query gives us the names of those people and the year the match took place:</p>



~~~r

library(dplyr)

> main_matches %>% filter(loser == "Andy Murray") %>% select(winner, year)

            winner year
1  Grigor Dimitrov 2014
2    Roger Federer 2012
3     Rafael Nadal 2011
4     Rafael Nadal 2010
5     Andy Roddick 2009
6     Rafael Nadal 2008
7 Marcos Baghdatis 2006
8 David Nalbandian 2005
~~~

<p>As you can see, Rafael Nadal shows up multiple times. I wanted to get one row per player and list all the years in a single column.
</p>


<p>This was my initial attempt:</p>



~~~r

> main_matches %>% filter(loser == "Andy Murray") %>% 
     group_by(winner) %>% summarise(years = paste(year))
Source: local data frame [6 x 2]

            winner years
1     Andy Roddick  2009
2 David Nalbandian  2005
3  Grigor Dimitrov  2014
4 Marcos Baghdatis  2006
5     Rafael Nadal  2011
6    Roger Federer  2012
~~~

<p>
Unfortunately it just gives you the last matching row per group which isn't quite what we want.. I realised my mistake while trying to pass a vector into paste and noticing that a vector came back when I'd expected a string:
</p>



~~~r

> paste(c(2008,2009,2010))
[1] "2008" "2009" "2010"
~~~

<p>
The missing argument was 'collapse' - <a href="http://www.markhneedham.com/blog/2014/08/11/r-grouping-by-two-variables/">something I'd come across when using plyr</a> last year:
</p>



~~~r

> paste(c(2008,2009,2010), collapse=", ")
[1] "2008, 2009, 2010"
~~~

<p>
Now, if we apply that to our original function:
</p>



~~~r

> main_matches %>% filter(loser == "Andy Murray") %>% 
     group_by(winner) %>% summarise(years = paste(year, collapse=", "))
Source: local data frame [6 x 2]

            winner            years
1     Andy Roddick             2009
2 David Nalbandian             2005
3  Grigor Dimitrov             2014
4 Marcos Baghdatis             2006
5     Rafael Nadal 2011, 2010, 2008
6    Roger Federer             2012
~~~

<p>That's exactly what we want. Let's tidy that up a bit:
</p>



~~~r

> main_matches %>% filter(loser == "Andy Murray") %>% 
     group_by(winner) %>% arrange(year) %>%
     summarise(years  = paste(year, collapse =","), times = length(year))  %>%
     arrange(desc(times), years)
Source: local data frame [6 x 3]

            winner          years times
1     Rafael Nadal 2008,2010,2011     3
2 David Nalbandian           2005     1
3 Marcos Baghdatis           2006     1
4     Andy Roddick           2009     1
5    Roger Federer           2012     1
6  Grigor Dimitrov           2014     1
~~~
