+++
draft = false
date="2014-11-07 01:29:09"
title="R: Joining multiple data frames"
tag=['r-2']
category=['R']
+++

<p>I've been looking through the code from Martin Eastwood's excellent talk '<a href="http://pena.lt/y/2014/11/02/predicting-football-using-r/">Predicting Football Using R</a>' and was intrigued by the code which reshaped the data into that expected by <a href="http://stat.ethz.ch/R-manual/R-patched/library/stats/html/glm.html">glm</a>.</p>


<p>The original looks like this:</p>



~~~r

df <- read.csv('http://www.football-data.co.uk/mmz4281/1314/E0.csv')

# munge data into format compatible with glm function
df <- apply(df, 1, function(row){
  data.frame(team=c(row['HomeTeam'], row['AwayTeam']),
             opponent=c(row['AwayTeam'], row['HomeTeam']),
             goals=c(row['FTHG'], row['FTAG']),
             home=c(1, 0))
})
df <- do.call(rbind, df)
~~~

<p>The initial data frame looks like this:</p>



~~~r

> library(dplyr)
> df %>% select(HomeTeam, AwayTeam, FTHG, FTAG) %>% head(1)
  HomeTeam    AwayTeam FTHG FTAG
1  Arsenal Aston Villa    1    3~~~

<p>And we want to get it to look like this:</p>



~~~r

> head(df, 2)
                team    opponent goals home
HomeTeam     Arsenal Aston Villa     1    1
AwayTeam Aston Villa     Arsenal     3    0
~~~

<p>So for each row in the initial data frame we want to have two rows: one representing each team, how many goals they scored in the match and whether they were playing at home or away.</p>


<p>I really like dplyr's pipelining function so I thought I'd try and translate Martin's code to use that and other dplyr functions.</p>


<p>I ended up with the following two sets of function calls:</p>



~~~r

df %>% select(team = HomeTeam, opponent = AwayTeam, goals = FTHG) %>% mutate(home = 1)
df %>% select(team = AwayTeam, opponent = HomeTeam, goals = FTAG) %>% mutate(home = 0)
~~~

<p>I'm doing pretty much the same thing as Martin except I've used dplyr's select and mutate functions to transform the data frame.</p>


<p>The next step was to join those two data frames together and with <a href="https://twitter.com/_nicolemargaret">Nicole's</a> help I realised that there are many ways we can do this.</p>


<p>The functions that will do the job are:</p>


<ul>

<li><a href="http://www.endmemo.com/program/R/rbind.php">rbind</a></li>
<li><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/sets.html">union</a></li>
<li>plyr's <a href="http://www.inside-r.org/packages/cran/plyr/docs/join">join</a> with 'type = "full"'</li>
<li>dplyr's <a href="http://www3.nd.edu/~steve/computing_with_data/24_dplyr/dplyr.html">union</a></li>
<li><a href="http://stat.ethz.ch/R-manual/R-patched/library/base/html/merge.html">merge</a> with 'all = TRUE'</li>

</ul>

<p>We decided to <a href="http://adv-r.had.co.nz/Performance.html">benchmark</a> them to see which was able to transform the data frame the fastest:</p>



~~~r

# load data into data.frame
dfOrig <- read.csv('http://www.football-data.co.uk/mmz4281/1314/E0.csv')

original = function(df) {
  df <- apply(df, 1, function(row){
    data.frame(team=c(row['HomeTeam'], row['AwayTeam']),
               opponent=c(row['AwayTeam'], row['HomeTeam']),
               goals=c(row['FTHG'], row['FTAG']),
               home=c(1, 0))
  })
  do.call(rbind, df)
}

newRBind = function(df) {
  rbind(df %>% select(team = HomeTeam, opponent = AwayTeam, goals = FTHG) %>% mutate(home = 1),
        df %>% select(team = AwayTeam, opponent = HomeTeam, goals = FTAG) %>% mutate(home = 0))  
}

newUnion = function(df) {
  union(df %>% select(team = HomeTeam, opponent = AwayTeam, goals = FTHG) %>% mutate(home = 1),
        df %>% select(team = AwayTeam, opponent = HomeTeam, goals = FTAG) %>% mutate(home = 0))  
}

newJoin = function(df) {
  join(df %>% select(team = HomeTeam, opponent = AwayTeam, goals = FTHG) %>% mutate(home = 1),
       df %>% select(team = AwayTeam, opponent = HomeTeam, goals = FTAG) %>% mutate(home = 0),
      type = "full")  
}

newMerge = function(df) {
  merge(df %>% select(team = HomeTeam, opponent = AwayTeam, goals = FTHG) %>% mutate(home = 1),
       df %>% select(team = AwayTeam, opponent = HomeTeam, goals = FTAG) %>% mutate(home = 0),
       all = TRUE)  
}
~~~


~~~r

> library(microbenchmark)

> microbenchmark(original(dfOrig))
Unit: milliseconds
             expr   min    lq  mean median    uq max neval
 original(dfOrig) 189.4 196.8 202.5    201 205.5 284   100

> microbenchmark(newRBind(dfOrig))
Unit: milliseconds
             expr   min    lq  mean median    uq   max neval
 newRBind(dfOrig) 2.197 2.274 2.396  2.309 2.377 4.526   100

> microbenchmark(newUnion(dfOrig))
Unit: milliseconds
             expr   min    lq  mean median   uq   max neval
 newUnion(dfOrig) 2.156 2.223 2.377  2.264 2.34 4.597   100

> microbenchmark(newJoin(dfOrig))

Unit: milliseconds
            expr   min    lq  mean median   uq   max neval
 newJoin(dfOrig) 5.961 6.132 6.817  6.253 6.65 11.95   100

> microbenchmark(newMerge(dfOrig))
Unit: milliseconds
             expr   min    lq  mean median    uq   max neval
 newMerge(dfOrig) 7.121 7.413 8.037  7.541 7.934 13.32   100
~~~

<p>We actually get a 100 time speed up over the original function if we use rbind or union whereas with merge or join it's around 35 times quicker.</p>


<p>In this case using merge or join is a bit misleading because we're not actually connecting the data frames together based on any particular field - we are just appending one to the other.</p>


<p>The code's <a href="https://gist.github.com/mneedham/98a4e423c1b37f05361c">available as a gist</a> if you want to have a play.</p>

