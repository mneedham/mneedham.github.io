+++
draft = false
date="2015-09-25 06:28:29"
title="R: Querying a 20 million line CSV file - data.table vs data frame"
tag=['r-2']
category=['R']
+++

<p>As I mentioned in a couple of blog posts already, I've been exploring the <a href="https://data.gov.uk/dataset/land-registry-monthly-price-paid-data">Land Registry price paid data set</a> and although I've initially been using SparkR I was curious how easy it would be to explore the data set using plain R.
</p>


<p>
I thought I'd start out by loading the data into a data frame and run the same queries using deployer.
</p>


<p>
I've come across Hadley Wickham's <a href="https://github.com/hadley/readr">readr</a> library before but hadn't used it and since I needed to load a 20 million line CSV file this seemed the perfect time to give it a try.
</p>


<blockquote>
The goal of readr is to provide a fast and friendly way to read tabular data into R. 
</blockquote>

<p>Let's' get started:</p>



~~~r

> library(readr)

> system.time(read_csv("pp-complete.csv", col_names = FALSE))
   user  system elapsed 
127.367  21.957 159.963 

> df = read_csv("pp-complete.csv", col_names = FALSE)
~~~

<p>
So it took a little over 2 minutes to process the CSV file into a data frame. Let's take a quick look at its contents:
</p>



~~~r

> head(df)
Source: local data frame [6 x 16]

                                      X1     X2     X3       X4    X5    X6    X7    X8    X9
                                   (chr)  (int) (date)    (chr) (chr) (chr) (chr) (chr) (chr)
1 {0C7ADEF5-878D-4066-B785-0000003ED74A} 163000   <NA>  UB5 4PJ     T     N     F   106      
2 {35F67271-ABD4-40DA-AB09-00000085B9D3} 247500   <NA> TA19 9DD     D     N     F    58      
3 {B20B1C74-E8E1-4137-AB3E-0000011DF342} 320000   <NA>   W4 1DZ     F     N     L    58      
4 {7D6B0915-C56B-4275-AF9B-00000156BCE7} 104000   <NA> NE61 2BH     D     N     F    17      
5 {47B60101-B64C-413D-8F60-000002F1692D} 147995   <NA> PE33 0RU     D     N     F     4      
6 {51F797CA-7BEB-4958-821F-000003E464AE} 110000   <NA> NR35 2SF     T     N     F     5      
Variables not shown: X10 (chr), X11 (chr), X12 (chr), X13 (chr), X14 (chr), X15 (chr), address (chr)
~~~

<p>
Now let's query the data frame to see which postcode has the highest average sale price. We'll need to group by the 'X4' column before applying some aggregate functions:
</p>



~~~R

> library(dplyr)

> system.time(df %>% 
                group_by(X4) %>% 
                summarise(total = sum(as.numeric(X2)), count = n(), ave = total / count) %>%
                arrange(desc(ave)))
   user  system elapsed 
122.557   1.135 124.211 

Source: local data frame [1,164,396 x 4]

         X4     total count      ave
      (chr)     (dbl) (int)    (dbl)
1   SW7 1DW  39000000     1 39000000
2  SW1W 0NH  32477000     1 32477000
3   W1K 7PX  27000000     1 27000000
4  SW1Y 6HD  24750000     1 24750000
5   SW6 1BA  18000000     1 18000000
6  SW1X 7EE 101505645     6 16917608
7    N6 4LA  16850000     1 16850000
8  EC4N 5AE  16500000     1 16500000
9    W8 7EA  82075000     6 13679167
10  W1K 1DP  13500000     1 13500000
~~~

<p>
What about if instead of the average price by post code we want to find the most expensive property ever sold instead?
</p>



~~~R

> system.time(df %>% group_by(X4) %>% summarise(max = max(X2)) %>% arrange(desc(max)))

   user  system elapsed 
 35.438   0.478  36.026 

Source: local data frame [1,164,396 x 2]

         X4      max
      (chr)    (int)
1  SW10 9SU 54959000
2   SW7 1QJ 50000000
3  SW1X 8HG 46013365
4   SW7 1DW 39000000
5  SW1W 0NH 32477000
6  SW1X 7LJ 29350000
7    W8 7EA 27900000
8   SW3 3SR 27750000
9   W1K 7PX 27000000
10 SW1X 7EE 25533000
..      ...      ...
~~~

<P>Interestingly that one was much quicker than the first one even though it seems like we only did slightly less work.</p>


<p>
At this point I mentioned my experiment to <a href="https://twitter.com/a5hok">Ashok</a> who suggested I give <a href="https://github.com/Rdatatable/data.table">data.table</a> a try to see if that fared any better. I'd not used it before but was able to get it <a href="http://stackoverflow.com/questions/1727772/quickly-reading-very-large-tables-as-dataframes-in-r">up and running reasonably quickly</a>:
</p>



~~~r

> library(data.table)

> system.time(fread("pp-complete.csv", header = FALSE))
Read 20075122 rows and 15 (of 15) columns from 3.221 GB file in 00:01:05
   user  system elapsed 
 59.324   5.798  68.956 

> dt = fread("pp-complete.csv", header = FALSE)

> head(dt)
                                       V1     V2               V3       V4 V5 V6 V7  V8 V9
1: {0C7ADEF5-878D-4066-B785-0000003ED74A} 163000 2003-02-21 00:00  UB5 4PJ  T  N  F 106   
2: {35F67271-ABD4-40DA-AB09-00000085B9D3} 247500 2005-07-15 00:00 TA19 9DD  D  N  F  58   
3: {B20B1C74-E8E1-4137-AB3E-0000011DF342} 320000 2010-09-10 00:00   W4 1DZ  F  N  L  58   
4: {7D6B0915-C56B-4275-AF9B-00000156BCE7} 104000 1997-08-27 00:00 NE61 2BH  D  N  F  17   
5: {47B60101-B64C-413D-8F60-000002F1692D} 147995 2003-05-02 00:00 PE33 0RU  D  N  F   4   
6: {51F797CA-7BEB-4958-821F-000003E464AE} 110000 2013-03-22 00:00 NR35 2SF  T  N  F   5   
               V10         V11         V12                          V13            V14 V15
1:    READING ROAD    NORTHOLT    NORTHOLT                       EALING GREATER LONDON   A
2:    ADAMS MEADOW   ILMINSTER   ILMINSTER               SOUTH SOMERSET       SOMERSET   A
3:   WHELLOCK ROAD                  LONDON                       EALING GREATER LONDON   A
4:        WESTGATE     MORPETH     MORPETH               CASTLE MORPETH NORTHUMBERLAND   A
5:   MASON GARDENS  WEST WINCH KING'S LYNN KING'S LYNN AND WEST NORFOLK        NORFOLK   A
6: WILD FLOWER WAY DITCHINGHAM      BUNGAY                SOUTH NORFOLK        NORFOLK   A

~~~

<p>
So we've already gained one minute in the parsing time which is pretty nice. Let's try and find the postcode with the highest average price:
</p>



~~~r

> dt[,list(length(V2), sum(V2)), by=V4][, V2 / V1, by=V4][order(-V1)][1:10]
Error in sum(V2) : invalid 'type' (character) of argument
~~~

<p>
Hmmm, seems like we need to make column 'V2' numeric. Let's do that:
</p>



~~~r

> dt = dt[, V2:= as.numeric(V2)]

> dt[,list(length(V2), sum(V2)), by=V4][, V2 / V1, by=V4][order(-V1)][1:10]
   user  system elapsed 
  5.108   0.670   6.183 

          V4       V1
 1:  SW7 1DW 39000000
 2: SW1W 0NH 32477000
 3:  W1K 7PX 27000000
 4: SW1Y 6HD 24750000
 5:  SW6 1BA 18000000
 6: SW1X 7EE 16917608
 7:   N6 4LA 16850000
 8: EC4N 5AE 16500000
 9:   W8 7EA 13679167
10:  W1K 1DP 13500000
~~~

<P>That's quite a bit faster than our data frame version - ~5 seconds compared to ~2 minutes. We have lost the total sales and number of sales columns but I expect that's just because my data.table foo is weak and we could keep them if we wanted.</p>


<p>
But a good start in terms of execution time. Now let's try the maximum sale price by post code query:
</p>



~~~r

> system.time(dt[,list(max(V2)), by=V4][order(-V1)][1:10])
   user  system elapsed 
  3.684   0.358   4.132 

          V4       V1
 1: SW10 9SU 54959000
 2:  SW7 1QJ 50000000
 3: SW1X 8HG 46013365
 4:  SW7 1DW 39000000
 5: SW1W 0NH 32477000
 6: SW1X 7LJ 29350000
 7:   W8 7EA 27900000
 8:  SW3 3SR 27750000
 9:  W1K 7PX 27000000
10: SW1X 7EE 25533000
~~~

<p>
We've got the same results as before and this time it took ~4 seconds compared to ~35 seconds.
</p>


<p>We can actually do even better if we set the postcode column as a key:</p>



~~~r

> setkey(dt, V4)

> system.time(dt[,list(length(V2), sum(V2)), by=V4][, V2 / V1, by=V4][order(-V1)][1:10])
   user  system elapsed 
  1.500   0.047   1.548 

> system.time(dt[,list(max(V2)), by=V4][order(-V1)][1:10])
   user  system elapsed 
  0.578   0.026   0.604 
~~~

<p>
And that's as far as I've got with my experiment. If there's anything else I can do to make either of the versions quicker do let me know in the comments.
</p>


<p>Oh and for a bit of commentary on what we can learn from the queries...Knightsbridge is a seriously expensive area to live!</p>

