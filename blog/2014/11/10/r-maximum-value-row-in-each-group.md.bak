+++
draft = false
date="2014-11-10 22:06:49"
title="R: dplyr - Maximum value row in each group"
tag=['r-2']
category=['R']
+++

<p>In my continued work with R's <a href="http://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html">dplyr</a> I wanted to be able to group a data frame by some columns and then find the maximum value for each group.</p>


<p>We'll continue with my favourite dummy data set:</p>



~~~r

> library(dplyr)

> data = data.frame(
    letter = sample(LETTERS, 50000, replace = TRUE),
    number = sample (1:10, 50000, replace = TRUE)
    )
~~~

<p>I started with the following code to count how many occurrences of each (letter, number) pair there were:</p>



~~~r

> data %>% count(letter, number)
Source: local data frame [260 x 3]
Groups: letter

   letter number   n
1       A      1 184
2       A      2 192
3       A      3 183
4       A      4 193
5       A      5 214
6       A      6 172
7       A      7 196
8       A      8 198
9       A      9 174
10      A     10 196
..    ...    ... ...
~~~

<p>I wanted to find the top number for each letter and with a <a href="http://stackoverflow.com/questions/24558328/how-to-select-the-maximum-value-in-each-group-in-r">bit of help from Stack Overflow</a> I ended up with the following:</p>



~~~r

> data %>% count(letter, number) %>% filter(n == max(n))
Source: local data frame [26 x 3]
Groups: letter

   letter number   n
1       A      5 214
2       B      6 234
3       C      8 213
4       D      6 211
5       E      9 208
6       F      2 219
7       G      1 213
8       H      2 208
9       I      9 220
10      J      7 213
11      K      3 228
12      L      2 206
13      M      3 212
14      N      4 222
15      O      1 211
16      P      7 211
17      Q      9 210
18      R      5 224
19      S      2 211
20      T      9 204
21      U      8 217
22      V      6 220
23      W      2 213
24      X      2 214
25      Y      3 211
26      Z      3 206
~~~

<p>Here we're filtering over a collection of rows grouped by letter and only selecting the row which has the max value. We can see more clearly what's happening if we filter the data frame to only contain one letter:</p>



~~~r

> letterA = data %>% filter(letter == "A") %>% count(letter, number)
> letterA
Source: local data frame [10 x 3]
Groups: letter

   letter number   n
1       A      1 184
2       A      2 192
3       A      3 183
4       A      4 193
5       A      5 214
6       A      6 172
7       A      7 196
8       A      8 198
9       A      9 174
10      A     10 196
~~~

<p>And now let's apply the filter command while also printing out information about each row:</p>



~~~r

> letterA %>% filter(print(n), print(n == max(n)), n == max(n))
 [1] 184 192 183 193 214 172 196 198 174 196
 [1] FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE
Source: local data frame [1 x 3]
Groups: letter

  letter number   n
1      A      5 214
~~~

<p>If instead of getting the top number by letter we wanted to get the top letter by number we just need to reorder the field names in the count method:</p>



~~~r

> data %>% count(number, letter) %>% filter(n == max(n))
Source: local data frame [10 x 3]
Groups: number

   number letter   n
1       1      G 213
2       2      F 219
3       3      K 228
4       4      N 222
5       5      R 224
6       6      B 234
7       7      B 221
8       8      U 217
9       9      I 220
10     10      O 209
~~~

<p>And if we want to see the letter that shows up least frequently we can change the call to 'max' to an equivalent one to 'min':</p>



~~~r

> data %>% count(number, letter) %>% filter(n == min(n))
Source: local data frame [11 x 3]
Groups: number

   number letter   n
1       1      H 166
2       2      O 160
3       3      E 156
4       4      R 169
5       5      L 169
6       6      I 164
7       7      H 170
8       7      I 170
9       8      Q 166
10      9      W 162
11     10      J 168
~~~
