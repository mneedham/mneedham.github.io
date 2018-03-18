+++
draft = false
date="2016-04-11 05:40:06"
title="R: tm - Unique words/terms per document"
tag=['r-2']
category=['R']
+++

<p>
I've been doing a bit of text mining over the weekend using the R <a href="https://cran.r-project.org/web/packages/tm/index.html">tm package</a> and I wanted to only count a term once per document which isn't how it works out the box.
</p>


<p>For example let's say we're writing a bit of code to calculate the frequency of terms across some documents. We might write the following code:</p>



~~~r

library(tm)
text = c("I am Mark I am Mark", "Neo4j is cool Neo4j is cool")
corpus = VCorpus(VectorSource(text))
tdm = as.matrix(TermDocumentMatrix(corpus, control = list(wordLengths = c(1, Inf))))

> tdm
       Docs
Terms   1 2
  am    2 0
  cool  0 2
  i     2 0
  is    0 2
  mark  2 0
  neo4j 0 2

> rowSums(tdm)
   am  cool     i    is  mark neo4j 
    2     2     2     2     2     2 
~~~

<p>
We've created a small corpus over a vector which contains two bits of text. On the last line we output a TermDocumentMatrix which shows how frequently each term shows up across the corpus. I had to tweak the default word length of 3 to make sure we could see 'am' and 'cool'.
</p>


<p>
But we've actually got some duplicate terms in each of our documents so we want to get rid of those and only count unique terms per document.
</p>


<p>
We can achieve that by mapping over the corpus using the <cite>tm_map</cite> function and then applying a function which returns unique terms. I wrote the following function:
</p>



~~~r

uniqueWords = function(d) {
  return(paste(unique(strsplit(d, " ")[[1]]), collapse = ' '))
}
~~~

<p>We can then apply the function like so:</p>



~~~r

corpus = tm_map(corpus, content_transformer(uniqueWords))
tdm = as.matrix(TermDocumentMatrix(corpus, control = list(wordLengths = c(1, Inf))))

> tdm
       Docs
Terms   1 2
  am    1 0
  cool  0 1
  i     1 0
  is    0 1
  mark  1 0
  neo4j 0 1

> rowSums(tdm)
   am  cool     i    is  mark neo4j 
    1     1     1     1     1     1 
~~~

<p>And now each term is only counted once. Success!</p>

