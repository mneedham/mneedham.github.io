+++
draft = false
date="2014-12-04 06:31:02"
title="R: Applying a function to every row of a data frame"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
In my continued exploration of London's meetups I wanted to calculate the distance from meetup venues to a centre point in London.
</p>


<p>
I've created <a href="https://gist.github.com/mneedham/7e926a213bf76febf5ed">a gist containing the coordinates of some of the venues that host NoSQL meetups in London town</a> if you want to follow along:
</p>



~~~r

library(dplyr)

# https://gist.github.com/mneedham/7e926a213bf76febf5ed
venues = read.csv("/tmp/venues.csv")

venues %>% head()
##                        venue      lat       lon
## 1              Skills Matter 51.52482 -0.099109
## 2                   Skinkers 51.50492 -0.083870
## 3          Theodore Bullfrog 51.50878 -0.123749
## 4 The Skills Matter eXchange 51.52452 -0.099231
## 5               The Guardian 51.53373 -0.122340
## 6            White Bear Yard 51.52227 -0.109804
~~~

<p>
Now to do the calculation. I've chosen the Centre Point building in Tottenham Court Road as our centre point. We can use the <cite>distHaversine</cite> function in the <cite>geosphere</cite> library allows us to do the calculation:
</p>



~~~r

options("scipen"=100, "digits"=4)
library(geosphere)

centre = c(-0.129581, 51.516578)
aVenue = venues %>% slice(1)
aVenue
##           venue   lat      lon
## 1 Skills Matter 51.52 -0.09911
~~~

<p>Now we can calculate the distance from Skillsmatter to our centre point:</pr>


~~~r

distHaversine(c(aVenue$lon, aVenue$lat), centre)
## [1] 2302
~~~

<p>That works pretty well so now we want to apply it to every row in the venues data frame and add an extra column containing that value.</p>


<p>This was my first attempt...</p>



~~~r

venues %>% mutate(distHaversine(c(lon,lat),centre))
## Error in .pointsToMatrix(p1): Wrong length for a vector, should be 2
~~~

<p>
...which didn't work quite as I'd imagined!
</p>


<p>
I eventually found my way to the by function which allows you to 'apply a function to a data frame split by factors'. In this case I wouldn't be grouping rows by a factor - I'd apply the function to each row separately.
</p>


<p>
I wired everything up like so:
</p>



~~~r

distanceFromCentre = by(venues, 1:nrow(venues), function(row) { distHaversine(c(row$lon, row$lat), centre)  })

distanceFromCentre %>% head()
## 1:nrow(venues)
##      1      2      3      4      5      6 
## 2301.6 3422.6  957.5 2280.6 1974.1 1509.5
~~~

We can now add the distances to our venues data frame:


~~~r

venuesWithCentre = venues %>% 
  mutate(distanceFromCentre = by(venues, 1:nrow(venues), function(row) { distHaversine(c(row$lon, row$lat), centre)  }))

venuesWithCentre %>% head()
##                        venue   lat      lon distanceFromCentre
## 1              Skills Matter 51.52 -0.09911             2301.6
## 2                   Skinkers 51.50 -0.08387             3422.6
## 3          Theodore Bullfrog 51.51 -0.12375              957.5
## 4 The Skills Matter eXchange 51.52 -0.09923             2280.6
## 5               The Guardian 51.53 -0.12234             1974.1
## 6            White Bear Yard 51.52 -0.10980             1509.5
~~~

<p>
Et voila!
</p>

