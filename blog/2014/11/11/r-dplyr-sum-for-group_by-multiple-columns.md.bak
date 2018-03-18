+++
draft = false
date="2014-11-11 00:17:32"
title="R: dplyr - Sum for group_by multiple columns"
tag=['r-2']
category=['R']
+++

<p>Over the weekend I was playing around with dplyr and had the following data frame grouped by both columns:</p>



~~~r

> library(dplyr)

> data = data.frame(
    letter = sample(LETTERS, 50000, replace = TRUE),
    number = sample (1:10, 50000, replace = TRUE)
    )

> data %>% count(letter, number) %>% head(20)
Source: local data frame [20 x 3]
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
11      B      1 212
12      B      2 198
13      B      3 194
14      B      4 181
15      B      5 203
16      B      6 234
17      B      7 221
18      B      8 179
19      B      9 182
20      B     10 170
~~~

<p>I wanted to add an extra column which would show what percentage of the values for that letter each number had.</p>
 

<p>If we wrote that code standalone we'd have the following:</p>



~~~r

> data %>% count(letter)
Source: local data frame [26 x 2]

   letter    n
1       A 1902
2       B 1974
3       C 1911
4       D 1948
5       E 1888
6       F 1975
7       G 1914
8       H 1886
9       I 1910
10      J 1924
11      K 1974
12      L 1891
13      M 1894
14      N 1946
15      O 1956
16      P 1934
17      Q 1865
18      R 1992
19      S 1946
20      T 1854
21      U 1919
22      V 1913
23      W 1928
24      X 1934
25      Y 1908
26      Z 1914
~~~

<p>We can also get that value by summing up the individual (letter, number) pairs from the previous data frame. The <cite>ungroup</cite> function allows us to do so:</p>



~~~r

> data %>% count(letter, number) %>% ungroup %>% group_by(letter) %>% mutate(sum.n = sum(n)) %>% head(20)
Source: local data frame [20 x 4]
Groups: letter

   letter number   n sum.n
1       A      1 184  1902
2       A      2 192  1902
3       A      3 183  1902
4       A      4 193  1902
5       A      5 214  1902
6       A      6 172  1902
7       A      7 196  1902
8       A      8 198  1902
9       A      9 174  1902
10      A     10 196  1902
11      B      1 212  1974
12      B      2 198  1974
13      B      3 194  1974
14      B      4 181  1974
15      B      5 203  1974
16      B      6 234  1974
17      B      7 221  1974
18      B      8 179  1974
19      B      9 182  1974
20      B     10 170  1974
~~~

<p>Pretty neat!</p>

