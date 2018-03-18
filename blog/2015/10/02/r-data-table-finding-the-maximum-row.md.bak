+++
draft = false
date="2015-10-02 18:42:47"
title="R: data.table - Finding the maximum row"
tag=['r-2', 'rstats', 'data-table']
category=['R']
+++

<p>
In my continued playing around with the R <a href="https://cran.r-project.org/web/packages/data.table/index.html">data.table</a> package I wanted to find the maximum row based on one of the columns, grouped by another column, and then return back the whole row.
</p>


<p>We'll use the following data table to illustrate:</p>




~~~r

> blogDT = data.table(name = c("Property 1","Property 1","Property 1","Property 2","Property 2","Property 2"), 
                    price = c(10000, 12500, 18000, 245000, 512000, 1000000),
                    date = c("Day 1", "Day 7", "Day 10", "Day 3", "Day 5", "Day 12"))

> blogDT[, lag.price := c(NA, price[-.N]), by = name]

> blogDT[, diff := price - lag.price]

> blogDT
         name   price   date lag.price   diff
1: Property 1   10000  Day 1        NA     NA
2: Property 1   12500  Day 7     10000   2500
3: Property 1   18000 Day 10     12500   5500
4: Property 2  245000  Day 3        NA     NA
5: Property 2  512000  Day 5    245000 267000
6: Property 2 1000000 Day 12    512000 488000
~~~

<p>I wanted to find the biggest difference in 'price' and 'lag.price' grouped by the 'name' column.
</p>


<p>
If we just want to get the max 'diff' grouped by 'name' it's quite easy:
</p>



~~~r

> blogDT[!is.na(diff), .(max = max(diff)), keyby = name]
         name    max
1: Property 1   5500
2: Property 2 488000
~~~

<p>
However now we've lost the information about which 'date' that was on and what the 'price' and 'lag.price' were which is a bit annoying.
</p>


<p>
If we only want to keep the rows which have the highest 'diff' grouped by 'name', one way to go about this is to add a 'max.diff' column to each row and then filter appropriately. e.g.
</p>



~~~r

> maxDT = blogDT[!is.na(diff)][, max := max(diff), by = name]

> maxDT
         name   price   date lag.price   diff    max
1: Property 1   12500  Day 7     10000   2500   5500
2: Property 1   18000 Day 10     12500   5500   5500
3: Property 2  512000  Day 5    245000 267000 488000
4: Property 2 1000000 Day 12    512000 488000 488000

> maxDT[diff == max]
         name   price   date lag.price   diff    max
1: Property 1   18000 Day 10     12500   5500   5500
2: Property 2 1000000 Day 12    512000 488000 488000
~~~

<p>
I've only been playing with data.table for a few days so if there's a better way do let me know in the comments.
</p>

