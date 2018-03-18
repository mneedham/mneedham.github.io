+++
draft = false
date="2014-11-26 00:01:12"
title="R: dplyr - Select 'random' rows from a data frame"
tag=['r-2', 'rstats', 'dplyr']
category=['R']
+++

<p>Frequently I find myself wanting to take a sample of the rows in a data frame where just taking the head isn't enough.</p>


<p>Let's say we start with the following data frame:</p>



~~~r

data = data.frame(
    letter = sample(LETTERS, 50000, replace = TRUE),
    number = sample (1:10, 50000, replace = TRUE)
    )
~~~

<p>And we'd like to sample 10 rows to see what it contains. We'll start by <a href="http://blog.revolutionanalytics.com/2009/02/how-to-choose-a-random-number-in-r.html">generating 10 random numbers</a> to represent row numbers using the <cite>runif</cite> function:</p>



~~~r

> randomRows = sample(1:length(data[,1]), 10, replace=T)
> randomRows
 [1]  8723 18772  4964 36134 27467 31890 16313 12841 49214 15621
~~~

<p>
We can then pass that list of row numbers into dplyr's <cite><a href="http://rpackages.ianhowson.com/cran/dplyr/man/slice.html">slice</a></cite> function like so:
</p>



~~~r

> data %>% slice(randomRows)
   letter number
1       Z      4
2       F      1
3       Y      6
4       R      6
5       Y      4
6       V     10
7       R      6
8       D      6
9       J      7
10      E      2
~~~

<p>If we're using that code throughout our code then we might want to pull out a function like so:</p>



~~~r

pickRandomRows = function(df, numberOfRows = 10) {
  df %>% slice(runif(numberOfRows,0, length(df[,1])))
}
~~~

<p>And then call it like so:</p>



~~~r

> data %>% pickRandomRows()
   letter number
1       W      5
2       Y      3
3       E      6
4       Q      8
5       M      9
6       H      9
7       E     10
8       T      2
9       I      5
10      V      4

> data %>% pickRandomRows(7)
  letter number
1      V      7
2      N      4
3      W      1
4      N      8
5      G      7
6      V      1
7      N      7
~~~

<h3>Update</h3>

<p><a href="https://twitter.com/tonkouts">Antonios</a> pointed out via email that we could just make use of the in-built <cite>sample_n</cite> function which I didn't know about until now:</p>



~~~r

> data %>% sample_n(10)
      letter number
29771      U      1
48666      T     10
30635      A      1
34865      X      7
20140      A      3
41715      T     10
43786      E     10
18284      A      7
21406      S      8
35542      J      8
~~~
