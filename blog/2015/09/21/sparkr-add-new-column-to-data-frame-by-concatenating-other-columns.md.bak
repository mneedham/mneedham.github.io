+++
draft = false
date="2015-09-21 22:30:51"
title="SparkR: Add new column to data frame by concatenating other columns"
tag=['sparkr']
category=['Spark']
+++

<p>
Continuing with my <a href="http://www.markhneedham.com/blog/2015/09/21/sparkr-error-in-invokejavaisstatic-true-classname-methodname-java-lang-classnotfoundexception-failed-to-load-class-for-data-source-csv/">exploration of the Land Registry open data set using SparkR</a> I wanted to see which road in the UK has had the most property sales over the last 20 years.
</p>


<p>To recap, this is what the data frame looks like:</p>



~~~bash

./spark-1.5.0-bin-hadoop2.6/bin/sparkR --packages com.databricks:spark-csv_2.11:1.2.0

> sales <- read.df(sqlContext, "pp-complete.csv", "com.databricks.spark.csv", header="false")

> head(sales)
                                      C0     C1               C2       C3 C4 C5
1 {0C7ADEF5-878D-4066-B785-0000003ED74A} 163000 2003-02-21 00:00  UB5 4PJ  T  N
2 {35F67271-ABD4-40DA-AB09-00000085B9D3} 247500 2005-07-15 00:00 TA19 9DD  D  N
3 {B20B1C74-E8E1-4137-AB3E-0000011DF342} 320000 2010-09-10 00:00   W4 1DZ  F  N
4 {7D6B0915-C56B-4275-AF9B-00000156BCE7} 104000 1997-08-27 00:00 NE61 2BH  D  N
5 {47B60101-B64C-413D-8F60-000002F1692D} 147995 2003-05-02 00:00 PE33 0RU  D  N
6 {51F797CA-7BEB-4958-821F-000003E464AE} 110000 2013-03-22 00:00 NR35 2SF  T  N
  C6  C7 C8              C9         C10         C11
1  F 106       READING ROAD    NORTHOLT    NORTHOLT
2  F  58       ADAMS MEADOW   ILMINSTER   ILMINSTER
3  L  58      WHELLOCK ROAD                  LONDON
4  F  17           WESTGATE     MORPETH     MORPETH
5  F   4      MASON GARDENS  WEST WINCH KING'S LYNN
6  F   5    WILD FLOWER WAY DITCHINGHAM      BUNGAY
                           C12            C13 C14
1                       EALING GREATER LONDON   A
2               SOUTH SOMERSET       SOMERSET   A
3                       EALING GREATER LONDON   A
4               CASTLE MORPETH NORTHUMBERLAND   A
5 KING'S LYNN AND WEST NORFOLK        NORFOLK   A
6                SOUTH NORFOLK        NORFOLK   A
~~~

<p>
<a href="https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd">This document</a> explains the data stored in each field and for this particular query we're interested in fields C9-C12. The plan is to group the data frame by those fields and then sort  by frequency in descending order.
</p>


<p>
When grouping by multiple fields it tends to be easiest to create a new field which concatenates them all and then group by that.
</p>


<p>I started with the following:</p>



~~~bash

> sales$address = paste(sales$C9, sales$C10, sales$C11, sales$C12, sep=", ")
Error in as.character.default(<S4 object of class "Column">) :
  no method for coercing this S4 class to a vector
~~~

<p>
Not so successful! Next I went even more primitive:
</p>



~~~bash

> sales$address = sales$C9 + ", " + sales$C10 + ", " + sales$C11 + ", " + sales$C12

> head(sales)
                                      C0     C1               C2       C3 C4 C5
1 {0C7ADEF5-878D-4066-B785-0000003ED74A} 163000 2003-02-21 00:00  UB5 4PJ  T  N
2 {35F67271-ABD4-40DA-AB09-00000085B9D3} 247500 2005-07-15 00:00 TA19 9DD  D  N
3 {B20B1C74-E8E1-4137-AB3E-0000011DF342} 320000 2010-09-10 00:00   W4 1DZ  F  N
4 {7D6B0915-C56B-4275-AF9B-00000156BCE7} 104000 1997-08-27 00:00 NE61 2BH  D  N
5 {47B60101-B64C-413D-8F60-000002F1692D} 147995 2003-05-02 00:00 PE33 0RU  D  N
6 {51F797CA-7BEB-4958-821F-000003E464AE} 110000 2013-03-22 00:00 NR35 2SF  T  N
  C6  C7 C8              C9         C10         C11
1  F 106       READING ROAD    NORTHOLT    NORTHOLT
2  F  58       ADAMS MEADOW   ILMINSTER   ILMINSTER
3  L  58      WHELLOCK ROAD                  LONDON
4  F  17           WESTGATE     MORPETH     MORPETH
5  F   4      MASON GARDENS  WEST WINCH KING'S LYNN
6  F   5    WILD FLOWER WAY DITCHINGHAM      BUNGAY
                           C12            C13 C14 address
1                       EALING GREATER LONDON   A      NA
2               SOUTH SOMERSET       SOMERSET   A      NA
3                       EALING GREATER LONDON   A      NA
4               CASTLE MORPETH NORTHUMBERLAND   A      NA
5 KING'S LYNN AND WEST NORFOLK        NORFOLK   A      NA
6                SOUTH NORFOLK        NORFOLK   A      NA
~~~

<p>That at least compiled but all addresses were 'NA' which isn't what we want. After a bit of searching I realised that there was a <a href="https://spark.apache.org/docs/latest/api/R/concat_ws.html">concat function</a> that I could use for exactly this task:</p>



~~~bash

> sales$address = concat_ws(sep=", ", sales$C9, sales$C10, sales$C11, sales$C12)

> head(sales)
                                      C0     C1               C2       C3 C4 C5
1 {0C7ADEF5-878D-4066-B785-0000003ED74A} 163000 2003-02-21 00:00  UB5 4PJ  T  N
2 {35F67271-ABD4-40DA-AB09-00000085B9D3} 247500 2005-07-15 00:00 TA19 9DD  D  N
3 {B20B1C74-E8E1-4137-AB3E-0000011DF342} 320000 2010-09-10 00:00   W4 1DZ  F  N
4 {7D6B0915-C56B-4275-AF9B-00000156BCE7} 104000 1997-08-27 00:00 NE61 2BH  D  N
5 {47B60101-B64C-413D-8F60-000002F1692D} 147995 2003-05-02 00:00 PE33 0RU  D  N
6 {51F797CA-7BEB-4958-821F-000003E464AE} 110000 2013-03-22 00:00 NR35 2SF  T  N
  C6  C7 C8              C9         C10         C11
1  F 106       READING ROAD    NORTHOLT    NORTHOLT
2  F  58       ADAMS MEADOW   ILMINSTER   ILMINSTER
3  L  58      WHELLOCK ROAD                  LONDON
4  F  17           WESTGATE     MORPETH     MORPETH
5  F   4      MASON GARDENS  WEST WINCH KING'S LYNN
6  F   5    WILD FLOWER WAY DITCHINGHAM      BUNGAY
                           C12            C13 C14
1                       EALING GREATER LONDON   A
2               SOUTH SOMERSET       SOMERSET   A
3                       EALING GREATER LONDON   A
4               CASTLE MORPETH NORTHUMBERLAND   A
5 KING'S LYNN AND WEST NORFOLK        NORFOLK   A
6                SOUTH NORFOLK        NORFOLK   A
                                                               address
1                             READING ROAD, NORTHOLT, NORTHOLT, EALING
2                   ADAMS MEADOW, ILMINSTER, ILMINSTER, SOUTH SOMERSET
3                                      WHELLOCK ROAD, , LONDON, EALING
4                           WESTGATE, MORPETH, MORPETH, CASTLE MORPETH
5 MASON GARDENS, WEST WINCH, KING'S LYNN, KING'S LYNN AND WEST NORFOLK
6                  WILD FLOWER WAY, DITCHINGHAM, BUNGAY, SOUTH NORFOLK
~~~

<p>That's more like it! Now let's see which streets have sold the most properties:</p>



~~~bash

> byAddress = summarize(groupBy(sales, sales$address), count = n(sales$address))
> head(arrange(byAddress, desc(byAddress$count)), 10)

                                                            address count
1                          BARBICAN, LONDON, LONDON, CITY OF LONDON  1398
2          CHRISTCHURCH ROAD, BOURNEMOUTH, BOURNEMOUTH, BOURNEMOUTH  1313
3                   MAIDA VALE, LONDON, LONDON, CITY OF WESTMINSTER  1305
4                     ROTHERHITHE STREET, LONDON, LONDON, SOUTHWARK  1253
5             SLOANE AVENUE, LONDON, LONDON, KENSINGTON AND CHELSEA  1219
6  THE STRAND, BRIGHTON MARINA VILLAGE, BRIGHTON, BRIGHTON AND HOVE  1218
7                     FAIRFIELD ROAD, LONDON, LONDON, TOWER HAMLETS  1217
8                             QUEENSTOWN ROAD, , LONDON, WANDSWORTH  1153
9                   UPPER RICHMOND ROAD, LONDON, LONDON, WANDSWORTH  1123
10                      QUEENSTOWN ROAD, LONDON, LONDON, WANDSWORTH  1079
~~~

<p>Next we'll drill into the data further but that's for another post.</p>

