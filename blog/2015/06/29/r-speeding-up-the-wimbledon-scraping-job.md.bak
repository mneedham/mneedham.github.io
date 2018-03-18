+++
draft = false
date="2015-06-29 05:36:22"
title="R: Speeding up the Wimbledon scraping job"
tag=['r-2']
category=['R']
+++

<p>
Over the past few days I've written <a href="http://www.markhneedham.com/blog/2015/06/26/r-ggplot-show-discrete-scale-even-with-no-value/">a few</a> <a href="http://www.markhneedham.com/blog/2015/06/25/r-scraping-wimbledon-draw-data/">blog</a> <a href="http://www.markhneedham.com/blog/2015/06/28/r-dplyr-update-rows-with-earlierprevious-rows-values/">posts</a> about a <a href="https://github.com/mneedham/neo4j-wimbledon/blob/master/wimbledon.csv">Wimbledon data set</a> I've been building and after running the scripts a few times I noticed that it was taking much longer to run that I expected.
</p>


<p>
To recap, I started out with the following function which takes in a URI and returns a data frame containing a row for each match:
</p>



~~~r

library(rvest)
library(dplyr)

scrape_matches1 = function(uri) {
  matches = data.frame()
  
  s = html(uri)
  rows = s %>% html_nodes("div#scoresResultsContent tr")
  i = 0
  for(row in rows) {  
    players = row %>% html_nodes("td.day-table-name a")
    seedings = row %>% html_nodes("td.day-table-seed")
    score = row %>% html_node("td.day-table-score a")
    flags = row %>% html_nodes("td.day-table-flag img")
    
    if(!is.null(score)) {
      player1 = players[1] %>% html_text() %>% str_trim()
      seeding1 = ifelse(!is.na(seedings[1]), seedings[1] %>% html_node("span") %>% html_text() %>% str_trim(), NA)
      flag1 = flags[1] %>% html_attr("alt")
      
      player2 = players[2] %>% html_text() %>% str_trim()
      seeding2 = ifelse(!is.na(seedings[2]), seedings[2] %>% html_node("span") %>% html_text() %>% str_trim(), NA)
      flag2 = flags[2] %>% html_attr("alt")
      
      matches = rbind(data.frame(winner = player1, 
                                 winner_seeding = seeding1, 
                                 winner_flag = flag1,
                                 loser = player2, 
                                 loser_seeding = seeding2,
                                 loser_flag = flag2,
                                 score = score %>% html_text() %>% str_trim(),
                                 round = round), matches)      
    } else {
      round = row %>% html_node("th") %>% html_text()
    }
  } 
  return(matches)
}
~~~

<p>Let's run it to get an idea of the data that it returns:</p>



~~~r

matches1 = scrape_matches1("http://www.atpworldtour.com/en/scores/archive/wimbledon/540/2014/results")

> matches1 %>% filter(round %in% c("Finals", "Semi-Finals", "Quarter-Finals"))
           winner winner_seeding winner_flag           loser loser_seeding loser_flag            score          round
1    Milos Raonic            (8)         CAN    Nick Kyrgios          (WC)        AUS    674 62 64 764 Quarter-Finals
2   Roger Federer            (4)         SUI   Stan Wawrinka           (5)        SUI     36 765 64 64 Quarter-Finals
3 Grigor Dimitrov           (11)         BUL     Andy Murray           (3)        GBR        61 764 62 Quarter-Finals
4  Novak Djokovic            (1)         SRB     Marin Cilic          (26)        CRO  61 36 674 62 62 Quarter-Finals
5   Roger Federer            (4)         SUI    Milos Raonic           (8)        CAN         64 64 64    Semi-Finals
6  Novak Djokovic            (1)         SRB Grigor Dimitrov          (11)        BUL    64 36 762 767    Semi-Finals
7  Novak Djokovic            (1)         SRB   Roger Federer           (4)        SUI 677 64 764 57 64         Finals
~~~

<p>As I mentioned, it's quite slow but I thought I'd wrap it in <cite>system.time</cite> so I could see exactly how long it was taking:
</p>



~~~r

> system.time(scrape_matches1("http://www.atpworldtour.com/en/scores/archive/wimbledon/540/2014/results"))
   user  system elapsed 
 25.570   0.111  31.416 
~~~

<p>About 30 seconds! The first thing I tried was downloading the file separately and running the function against the local file:</p>



~~~r

> system.time(scrape_matches1("data/raw/2014.html"))
   user  system elapsed 
 25.662   0.123  25.863
~~~

<p>Hmmm, that's only saved us 5 seconds so the bottleneck must be somewhere else. Still there's no point making a HTTP request every time we run the script so we'll stick with the local file version.
</p>


<p>
While browsing <a href="http://cran.r-project.org/web/packages/rvest/rvest.pdf">rvest's vignette</a> I noticed a function called <cite>html_table</cite> which I was curious about. I decided to try and replace some of my code with a call to that:
</p>



~~~r

matches2= html("data/raw/2014.html") %>% 
  html_node("div#scoresResultsContent table.day-table") %>% html_table(header = FALSE) %>% 
  mutate(X1 = ifelse(X1 == "", NA, X1)) %>%
  mutate(round = ifelse(grepl("\\([0-9]\\)|\\(", X1), NA, X1)) %>% 
  mutate(round = na.locf(round)) %>%
  filter(!is.na(X8)) %>%
  select(winner = X3, winner_seeding = X1, loser = X7, loser_seeding = X5, score = X8, round)

> matches2 %>% filter(round %in% c("Finals", "Semi-Finals", "Quarter-Finals"))
           winner winner_seeding           loser loser_seeding            score          round
1  Novak Djokovic            (1)   Roger Federer           (4) 677 64 764 57 64         Finals
2  Novak Djokovic            (1) Grigor Dimitrov          (11)    64 36 762 767    Semi-Finals
3   Roger Federer            (4)    Milos Raonic           (8)         64 64 64    Semi-Finals
4  Novak Djokovic            (1)     Marin Cilic          (26)  61 36 674 62 62 Quarter-Finals
5 Grigor Dimitrov           (11)     Andy Murray           (3)        61 764 62 Quarter-Finals
6   Roger Federer            (4)   Stan Wawrinka           (5)     36 765 64 64 Quarter-Finals
7    Milos Raonic            (8)    Nick Kyrgios          (WC)    674 62 64 764 Quarter-Finals
~~~

<p>I had to do some slightly clever stuff to get the 'round' column into shape using zoo's <cite>na.locf</cite> function which I <a href="http://www.markhneedham.com/blog/2015/06/28/r-dplyr-update-rows-with-earlierprevious-rows-values/">wrote about previously.</a></p>


<p>
Unfortunately I couldn't work out how to extract the flag with this version - that value is hidden in the 'alt' tag of an img and presumably <cite>html_table</cite> is just grabbing the text value of each cell. This version is much quicker though!
</p>



~~~r

system.time(html("data/raw/2014.html") %>% 
  html_node("div#scoresResultsContent table.day-table") %>% html_table(header = FALSE) %>% 
  mutate(X1 = ifelse(X1 == "", NA, X1)) %>%
  mutate(round = ifelse(grepl("\\([0-9]\\)|\\(", X1), NA, X1)) %>% 
  mutate(round = na.locf(round)) %>%
  filter(!is.na(X8)) %>%
  select(winner = X3, winner_seeding = X1, loser = X7, loser_seeding = X5, score = X8, round))

   user  system elapsed 
  0.545   0.002   0.548 
~~~

<p>
What I realised from writing this version is that I need to match all the columns with one call to <cite>html_nodes</cite> rather than getting the row and then each column in a loop. 
</p>


<p>
I rewrote the function to do that:
</p>



~~~r

scrape_matches3 = function(uri) {
  s = html(uri)
  
  players  = s %>% html_nodes("div#scoresResultsContent tr td.day-table-name a")
  seedings = s %>% html_nodes("div#scoresResultsContent tr td.day-table-seed")
  scores   = s %>% html_nodes("div#scoresResultsContent tr td.day-table-score a")
  flags    = s %>% html_nodes("div#scoresResultsContent tr td.day-table-flag img") %>% html_attr("alt") %>% str_trim()
  
  matches3 = data.frame(
    winner         = sapply(seq(1,length(players),2),  function(idx) players[[idx]] %>% html_text()),
    winner_seeding = sapply(seq(1,length(seedings),2), function(idx) seedings[[idx]] %>% html_text() %>% str_trim()),
    winner_flag    = sapply(seq(1,length(flags),2),    function(idx) flags[[idx]]),  
    loser          = sapply(seq(2,length(players),2),  function(idx) players[[idx]] %>% html_text()),
    loser_seeding  = sapply(seq(2,length(seedings),2), function(idx) seedings[[idx]] %>% html_text() %>% str_trim()),
    loser_flag     = sapply(seq(2,length(flags),2),    function(idx) flags[[idx]]),
    score          = sapply(scores,                    function(score) score %>% html_text() %>% str_trim())
  )
  return(matches3)
}
~~~

<p>Let's run and time that to check we're getting back the right results in a timely manner:</p>



~~~r

> matches3 %>% sample_n(10)
                   winner winner_seeding winner_flag               loser loser_seeding loser_flag         score
70           David Ferrer            (7)         ESP Pablo Carreno Busta                      ESP  60 673 61 61
128        Alex Kuznetsov           (26)         USA         Tim Smyczek           (3)        USA   46 63 63 63
220   Rogerio Dutra Silva                        BRA   Kristijan Mesaros                      CRO         62 63
83         Kevin Anderson           (20)         RSA        Aljaz Bedene          (LL)        GBR      63 75 62
73          Kei Nishikori           (10)         JPN   Kenny De Schepper                      FRA     64 765 75
56  Roberto Bautista Agut           (27)         ESP         Jan Hernych           (Q)        CZE   75 46 62 62
138            Ante Pavic                        CRO        Marc Gicquel          (29)        FRA  46 63 765 64
174             Tim Puetz                        GER     Ruben Bemelmans                      BEL         64 62
103        Lleyton Hewitt                        AUS   Michal Przysiezny                      POL 62 6714 61 64
35          Roger Federer            (4)         SUI       Gilles Muller           (Q)        LUX      63 75 63

> system.time(scrape_matches3("data/raw/2014.html"))
   user  system elapsed 
  0.815   0.006   0.827 
~~~

<p>It's still quick - a bit slower than <cite>html_table</cite> but we can deal with that. As you can see, I also had to add some logic to separate the values for the winners and losers - the players, seeds, flags come back as as one big list. The odd rows represent the winner; the even rows the loser.</p>


<p>Annoyingly we've now lost the 'round' column because that appears as a table heading so we can't extract it the same way. I ended up cheating a bit to get it to work by working out how many matches each round should contain and generated a vector with that number of entries:</p>



~~~r

raw_rounds = s %>% html_nodes("th") %>% html_text()

> raw_rounds
 [1] "Finals"               "Semi-Finals"          "Quarter-Finals"       "Round of 16"          "Round of 32"         
 [6] "Round of 64"          "Round of 128"         "3rd Round Qualifying" "2nd Round Qualifying" "1st Round Qualifying"

rounds = c( sapply(0:6, function(idx) rep(raw_rounds[[idx + 1]], 2 ** idx)) %>% unlist(),
            sapply(7:9, function(idx) rep(raw_rounds[[idx + 1]], 2 ** (idx - 3))) %>% unlist())

> rounds[1:10]
 [1] "Finals"         "Semi-Finals"    "Semi-Finals"    "Quarter-Finals" "Quarter-Finals" "Quarter-Finals" "Quarter-Finals"
 [8] "Round of 16"    "Round of 16"    "Round of 16"  
~~~

<p>
Let's put that code into the function and see if we end up with the same resulting data frame:
</p>



~~~r

scrape_matches4 = function(uri) {
  s = html(uri)
  
  players  = s %>% html_nodes("div#scoresResultsContent tr td.day-table-name a")
  seedings = s %>% html_nodes("div#scoresResultsContent tr td.day-table-seed")
  scores   = s %>% html_nodes("div#scoresResultsContent tr td.day-table-score a")
  flags    = s %>% html_nodes("div#scoresResultsContent tr td.day-table-flag img") %>% html_attr("alt") %>% str_trim()
  
  raw_rounds = s %>% html_nodes("th") %>% html_text()
  rounds = c( sapply(0:6, function(idx) rep(raw_rounds[[idx + 1]], 2 ** idx)) %>% unlist(),
              sapply(7:9, function(idx) rep(raw_rounds[[idx + 1]], 2 ** (idx - 3))) %>% unlist())
  
  matches4 = data.frame(
    winner         = sapply(seq(1,length(players),2),  function(idx) players[[idx]] %>% html_text()),
    winner_seeding = sapply(seq(1,length(seedings),2), function(idx) seedings[[idx]] %>% html_text() %>% str_trim()),
    winner_flag    = sapply(seq(1,length(flags),2),    function(idx) flags[[idx]]),  
    loser          = sapply(seq(2,length(players),2),  function(idx) players[[idx]] %>% html_text()),
    loser_seeding  = sapply(seq(2,length(seedings),2), function(idx) seedings[[idx]] %>% html_text() %>% str_trim()),
    loser_flag     = sapply(seq(2,length(flags),2),    function(idx) flags[[idx]]),
    score          = sapply(scores,                    function(score) score %>% html_text() %>% str_trim()),
    round          = rounds
  )
  return(matches4)
}

matches4 = scrape_matches4("data/raw/2014.html")

> matches4 %>% filter(round %in% c("Finals", "Semi-Finals", "Quarter-Finals"))
           winner winner_seeding winner_flag           loser loser_seeding loser_flag            score          round
1  Novak Djokovic            (1)         SRB   Roger Federer           (4)        SUI 677 64 764 57 64         Finals
2  Novak Djokovic            (1)         SRB Grigor Dimitrov          (11)        BUL    64 36 762 767    Semi-Finals
3   Roger Federer            (4)         SUI    Milos Raonic           (8)        CAN         64 64 64    Semi-Finals
4  Novak Djokovic            (1)         SRB     Marin Cilic          (26)        CRO  61 36 674 62 62 Quarter-Finals
5 Grigor Dimitrov           (11)         BUL     Andy Murray           (3)        GBR        61 764 62 Quarter-Finals
6   Roger Federer            (4)         SUI   Stan Wawrinka           (5)        SUI     36 765 64 64 Quarter-Finals
7    Milos Raonic            (8)         CAN    Nick Kyrgios          (WC)        AUS    674 62 64 764 Quarter-Finals
~~~

<p>We shouldn't have added much to the time but let's check:</p>



~~~r

> system.time(scrape_matches4("data/raw/2014.html"))
   user  system elapsed 
  0.816   0.004   0.824 
~~~

<p>Sweet. We've saved ourselves 29 seconds per page as long as the number of rounds stayed constant over the years. For the 10 years that I've looked at it has but I expect if you go back further the draw sizes will have been different and our script would break.
</p>


<p>For now though this will do!</p>

