+++
draft = false
date="2014-11-09 09:30:09"
title="R: dplyr - Ordering by count after multiple column group_by"
tag=['r-2']
category=['R']
+++

<p>
I was recently trying to group a data frame by two columns and then sort by the count using dplyr but it wasn't sorting in the way I expecting which was initially very confusing.
</p>


<p>I started with this data frame:</p>



~~~r

library(dplyr)

data = data.frame(
  letter = sample(LETTERS, 50000, replace = TRUE),
  number = sample (1:10, 50000, replace = TRUE)
  )
~~~

<p>And I wanted to find out how many occurrences of each (letter, number) pair exist in the data set. I started with the following code:</p>



~~~r

> data %>% count(letter, number, sort = TRUE)
Source: local data frame [260 x 3]
Groups: letter

   letter number   n
1       A      4 205
2       A      9 201
3       A      3 197
4       A      1 195
5       A     10 191
6       A      2 189
7       A      8 184
8       A      7 183
9       A      5 181
10      A      6 173
..    ...    ... ...
~~~

<p>
As you can see it's only showing A's which is interesting as I wouldn't expect there to be a bias towards that letter. Let's filter out the A's:
</p>



~~~r

> data %>% filter(letter != "A") %>% count(letter, number, sort = TRUE)
Source: local data frame [250 x 3]
Groups: letter

   letter number   n
1       B      8 222
2       B      9 212
3       B      5 207
4       B      6 201
5       B     10 200
6       B      7 192
7       B      2 189
8       B      3 189
9       B      1 187
10      B      4 181
..    ...    ... ...
~~~

<p>Now all we see are B's and we can see that both (B,8) and (B,9) have a higher 'n' value than any of the A's.</p>


<p>I put the code back into the more verbose form to see if it was the <cite>count</cite> function that behaved unexpectedly:</p>



~~~r

> data %>% group_by(letter, number) %>% summarise(n = n()) %>% arrange(desc(n))
Source: local data frame [260 x 3]
Groups: letter

   letter number   n
1       A      4 205
2       A      9 201
3       A      3 197
4       A      1 195
5       A     10 191
6       A      2 189
7       A      8 184
8       A      7 183
9       A      5 181
10      A      6 173
..    ...    ... ...
~~~

<p>Nope, still the same behaviour.</p>


<p>At this point I vaguely remembered there being a function called <cite>ungroup</cite> which I hadn't used and wondered if now was the time.</p>



~~~r

> data %>% group_by(letter, number) %>% summarise(n = n()) %>% ungroup() %>% arrange(desc(n))
Source: local data frame [260 x 3]

   letter number   n
1       L      2 236
2       V      1 231
3       Y      8 226
4       J      4 225
5       J     10 223
6       Q      7 223
7       B      8 222
8       O      9 222
9       Q     10 221
10      Z      9 221
..    ...    ... ...
~~~

<p>Indeed it was and now we can go back to our original version of the code using <cite>count</cite> and handle the sorting afterwards:</p>



~~~r

> data %>% count(letter, number) %>% ungroup() %>% arrange(desc(n))
Source: local data frame [260 x 3]

   letter number   n
1       L      2 236
2       V      1 231
3       Y      8 226
4       J      4 225
5       J     10 223
6       Q      7 223
7       B      8 222
8       O      9 222
9       Q     10 221
10      Z      9 221
..    ...    ... ...
~~~
