+++
draft = false
date="2015-02-22 08:58:57"
title="R/dplyr: Extracting data frame column value for filtering with %in%"
tag=['r-2', 'rstats']
category=['R']
+++

<p>
I've been playing around with <a href="http://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html">dplyr</a> over the weekend and wanted to extract the values from a data frame column to use in a later filtering step.
</p>


<p>
I had a data frame:
</p>



~~~r

library(dplyr)
df = data.frame(userId = c(1,2,3,4,5), score = c(2,3,4,5,5))
~~~

<p>And wanted to extract the userIds of those people who have a score greater than 3. I started with:</p>



~~~r

highScoringPeople = df %>% filter(score > 3) %>% select(userId)
> highScoringPeople
  userId
1      3
2      4
3      5
~~~

<p>
And then filtered the data frame expecting to get back those 3 people:
</p>



~~~r

> df %>% filter(userId %in% highScoringPeople)
[1] userId score 
<0 rows> (or 0-length row.names)
~~~

<p>
No rows! I created vector with the numbers 3-5 to make sure that worked:
</p>



~~~r

> df %>% filter(userId %in% c(3,4,5))
  userId score
1      3     4
2      4     5
3      5     5
~~~

<p>
That works as expected so <cite>highScoringPeople</cite> obviously isn't in the right format to facilitate an 'in lookup'. Let's explore:
</p>



~~~r

> str(c(3,4,5))
 num [1:3] 3 4 5

> str(highScoringPeople)
'data.frame':	3 obs. of  1 variable:
 $ userId: num  3 4 5
~~~

<p>
Now it's even more obvious why it doesn't work - <cite>highScoringPeople</cite> is still a data frame when we need it to be a vector/list.
</p>


<p>One way to fix this is to extract the userIds using the $ syntax instead of the select function:
</p>



~~~r

highScoringPeople = (df %>% filter(score > 3))$userId

> str(highScoringPeople)
 num [1:3] 3 4 5

> df %>% filter(userId %in% highScoringPeople)
  userId score
1      3     4
2      4     5
3      5     5
~~~

<p>
Or if we want to do the column selection using dplyr we can <a href="http://stackoverflow.com/questions/21618423/extract-a-dplyr-tbl-column-as-a-vector">extract the values for the column like this</a>:
</p>



~~~r

highScoringPeople = (df %>% filter(score > 3) %>% select(userId))[[1]]

> str(highScoringPeople)
 num [1:3] 3 4 5
~~~

<p>
Not so difficult after all.
</p>

