+++
draft = false
date="2015-09-27 22:02:07"
title="R: data.table - Comparing adjacent rows"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
As part of my exploration of the <a href="https://data.gov.uk/dataset/land-registry-monthly-price-paid-data">Land Registry price paid data set</a> I wanted to compare the difference between consecutive sales of properties.
</p>


<p>
This means we need to group the sales by a property identifier and then get the previous sale price into a column on each row unless it's the first sale in which case we'll have 'NA'. We can do this by creating a <cite><a href="http://stackoverflow.com/questions/26291988/r-how-to-create-a-lag-variable-for-each-by-group">lag</a></cite> variable.
</p>


<p>I'll use a simpler data set which is very similar in structure to the Land Registry's to demonstrate:</p>



~~~r

> blogDT = data.table(name = c("Property 1","Property 1","Property 1","Property 2","Property 2","Property 2"), 
                      price = c(10000, 12500, 18000, 245000, 512000, 1000000))

> blogDT
         name   price
1: Property 1   10000
2: Property 1   12500
3: Property 1   18000
4: Property 2  245000
5: Property 2  512000
6: Property 2 1000000
~~~

<p>
We want to group by the 'name' column and then have the price on row 1 show on row 2, the price on row 2 on row 3, the price on row 4 on row 5 and the price on row 5 on row 6. To do that we'll introduce a 'lag.price' column:
</p>



~~~r

> blogDT[, lag.price := c(NA, price[-.N]), by = name]

> blogDT
         name   price lag.price
1: Property 1   10000        NA
2: Property 1   12500     10000
3: Property 1   18000     12500
4: Property 2  245000        NA
5: Property 2  512000    245000
6: Property 2 1000000    512000
~~~

<p>Next let's calculate the difference between the two prices:</p>



~~~r

> blogDT[, diff := price - lag.price]
> blogDT
         name   price lag.price   diff
1: Property 1   10000        NA     NA
2: Property 1   12500     10000   2500
3: Property 1   18000     12500   5500
4: Property 2  245000        NA     NA
5: Property 2  512000    245000 267000
6: Property 2 1000000    512000 488000
~~~

<p>
Finally let's order the data table by the biggest price gains:
</p>



~~~r

> blogDT[order(-diff)]
         name   price lag.price   diff
1: Property 2 1000000    512000 488000
2: Property 2  512000    245000 267000
3: Property 1   18000     12500   5500
4: Property 1   12500     10000   2500
5: Property 1   10000        NA     NA
6: Property 2  245000        NA     NA
~~~
