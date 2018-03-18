+++
draft = false
date="2015-06-20 22:18:55"
title="R: dplyr - segfault cause 'memory not mapped'"
tag=['r-2', 'dplyr']
category=['R']
+++

<p>
In my <a href="http://www.markhneedham.com/blog/2015/06/19/r-regex-capturing-multiple-matches-of-the-same-group/">continued playing around with web logs in R</a> I wanted to process the logs for a day and see what the most popular URIs were.
</p>


<p>
I first read in all the lines using the <cite>read_lines</cite> function in readr and put the vector it produced into a data frame so I could process it using dplyr.
</p>



~~~r

library(readr)
dlines = data.frame(column = read_lines("~/projects/logs/2015-06-18-22-docs"))
~~~

<p>
In the previous post I showed some code to extract the URI from a log line. I extracted this code out into a function and adapted it so that I could pass in a list of values instead of a single value:
</p>



~~~r

extract_uri = function(log) {
  parts = str_extract_all(log, "\"[^\"]*\"")
  return(lapply(parts, function(p) str_match(p[1], "GET (.*) HTTP")[2] %>% as.character))
}
~~~

<p>
Next I ran the following function to count the number of times each URI appeared in the logs:
</p>



~~~r

library(dplyr)
pages_viewed = dlines %>%
  mutate(uri  = extract_uri(column)) %>% 
  count(uri) %>%
  arrange(desc(n))
~~~

<p>This crashed my R process with the following error message:</p>



~~~r

segfault cause 'memory not mapped' 
~~~

<p>I narrowed it down to a problem when doing a group by operation on the 'uri' field and came across <a href="https://github.com/hadley/dplyr/issues/322">this post</a> which suggested that it was handled more cleanly in more recently version of dplyr.</p>


<p>I upgraded to 0.4.2 and tried again:</p>




~~~R

## Error in eval(expr, envir, enclos): cannot group column uri, of class 'list'
~~~

<p>
That makes more sense. We're probably returning a list from <cite>extract_uri</cite> rather than a vector which would fit nicely back into the data frame. That's fixed easily enough by unlisting the result:
</p>



~~~r

extract_uri = function(log) {
  parts = str_extract_all(log, "\"[^\"]*\"")
  return(unlist(lapply(parts, function(p) str_match(p[1], "GET (.*) HTTP")[2] %>% as.character)))
}
~~~


<p>And now when we run the count function it's happy again, good times!</p>

