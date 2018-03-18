+++
draft = false
date="2015-06-19 21:38:47"
title="R: Regex - capturing multiple matches of the same group"
tag=['r-2']
category=['R']
+++

<p>I've been playing around with some web logs using R and I wanted to extract everything that existed in double quotes within a logged entry.
</p>


<p>
This is an example of a log entry that I want to parse:
</p>



~~~r

log = '2015-06-18-22:277:548311224723746831\t2015-06-18T22:00:11\t2015-06-18T22:00:05Z\t93317114\tip-127-0-0-1\t127.0.0.5\tUser\tNotice\tneo4j.com.access.log\t127.0.0.3 - - [18/Jun/2015:22:00:11 +0000] "GET /docs/stable/query-updating.html HTTP/1.1" 304 0 "http://neo4j.com/docs/stable/cypher-introduction.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"'
~~~

<p>And I want to extract these 3 things:</p>


<ul>
	<li>/docs/stable/query-updating.html</li>
	<li>http://neo4j.com/docs/stable/cypher-introduction.html</li>
	<li>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36</li>
</ul>


<p>i.e. the URI, the referrer and  browser details.</p>



<p>I'll be using the <cite>stringr</cite> library which seems to work quite well for this type of work.</p>


<p>
To extract these values we need to find all the occurrences of double quotes and get the text inside those quotes. We might start by using the <cite>str_match</cite> function:
</p>



~~~r

> library(stringr)
> str_match(log, "\"[^\"]*\"")
     [,1]                                               
[1,] "\"GET /docs/stable/query-updating.html HTTP/1.1\""
~~~

<p>Unfortunately that only picked up the first occurrence of the pattern so we've got the URI but not the referrer or browser details. I tried <cite>str_extract</cite> with similar results before I found <cite>str_extract_all</cite> which does the job:
</p>



~~~r

> str_extract_all(log, "\"[^\"]*\"")
[[1]]
[1] "\"GET /docs/stable/query-updating.html HTTP/1.1\""                                                                            
[2] "\"http://neo4j.com/docs/stable/cypher-introduction.html\""                                                                    
[3] "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36\""
~~~

<p>
We still need to do a bit of cleanup to get rid of the 'GET' and 'HTTP/1.1' in the URI and the quotes in all of them:  
</p>



~~~r

parts = str_extract_all(log, "\"[^\"]*\"")[[1]]
uri = str_match(parts[1], "GET (.*) HTTP")[2]
referer = str_match(parts[2], "\"(.*)\"")[2]
browser = str_match(parts[3], "\"(.*)\"")[2]

> uri
[1] "/docs/stable/query-updating.html"

> referer
[1] "https://www.google.com/"

> browser
[1] "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
~~~

<p>We could then go on to split out the browser string into its sub components but that'll do for now!</p>

