+++
draft = false
date="2014-09-29 05:46:43"
title="R: Filtering data frames by column type ('x' must be numeric)"
tag=['r-2', 'rstats']
category=['R']
+++

<p>I've been working through the exercises from <a href="http://www-bcf.usc.edu/~gareth/ISL/">An Introduction to Statistical Learning</a> and one of them required you to create a pair wise correlation matrix of variables in a data frame.</p>


<p>The exercise uses the 'Carseats' data set which can be imported like so:</p>



~~~r

> install.packages("ISLR")
> library(ISLR)
> head(Carseats)
  Sales CompPrice Income Advertising Population Price ShelveLoc Age Education Urban  US
1  9.50       138     73          11        276   120       Bad  42        17   Yes Yes
2 11.22       111     48          16        260    83      Good  65        10   Yes Yes
3 10.06       113     35          10        269    80    Medium  59        12   Yes Yes
4  7.40       117    100           4        466    97    Medium  55        14   Yes Yes
5  4.15       141     64           3        340   128       Bad  38        13   Yes  No
6 10.81       124    113          13        501    72       Bad  78        16    No Yes
~~~

filter the categorical variables from a data frame and

<p>If we try to run the '<a href="http://www.statmethods.net/stats/correlations.html">cor</a>' function on the data frame we'll get the following error:</p>



~~~r

> cor(Carseats)
Error in cor(Carseats) : 'x' must be numeric
~~~

<p>As the error message suggests, we can't pass non numeric variables to this function so we need to remove the categorical variables from our data frame.</p>


<p>But first we need to <a href="http://r.789695.n4.nabble.com/Find-classes-for-each-column-of-a-data-frame-td2339918.html">work out which columns those are</a>:</p>



~~~r

> sapply(Carseats, class)
      Sales   CompPrice      Income Advertising  Population       Price   ShelveLoc         Age   Education 
  "numeric"   "numeric"   "numeric"   "numeric"   "numeric"   "numeric"    "factor"   "numeric"   "numeric" 
      Urban          US 
   "factor"    "factor" 
~~~

<p>We can see a few columns of type 'factor' and luckily for us there's a function which will help us identify those more easily:</p>



~~~r

> sapply(Carseats, is.factor)
      Sales   CompPrice      Income Advertising  Population       Price   ShelveLoc         Age   Education 
      FALSE       FALSE       FALSE       FALSE       FALSE       FALSE        TRUE       FALSE       FALSE 
      Urban          US 
       TRUE        TRUE 
~~~

<p>Now we can remove those columns from our data frame and create the correlation matrix:</p>



~~~r

> cor(Carseats[sapply(Carseats, function(x) !is.factor(x))])
                  Sales   CompPrice       Income  Advertising   Population       Price          Age    Education
Sales        1.00000000  0.06407873  0.151950979  0.269506781  0.050470984 -0.44495073 -0.231815440 -0.051955242
CompPrice    0.06407873  1.00000000 -0.080653423 -0.024198788 -0.094706516  0.58484777 -0.100238817  0.025197050
Income       0.15195098 -0.08065342  1.000000000  0.058994706 -0.007876994 -0.05669820 -0.004670094 -0.056855422
Advertising  0.26950678 -0.02419879  0.058994706  1.000000000  0.265652145  0.04453687 -0.004557497 -0.033594307
Population   0.05047098 -0.09470652 -0.007876994  0.265652145  1.000000000 -0.01214362 -0.042663355 -0.106378231
Price       -0.44495073  0.58484777 -0.056698202  0.044536874 -0.012143620  1.00000000 -0.102176839  0.011746599
Age         -0.23181544 -0.10023882 -0.004670094 -0.004557497 -0.042663355 -0.10217684  1.000000000  0.006488032
Education   -0.05195524  0.02519705 -0.056855422 -0.033594307 -0.106378231  0.01174660  0.006488032  1.000000000
~~~
