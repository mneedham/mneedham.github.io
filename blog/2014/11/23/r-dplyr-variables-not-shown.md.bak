+++
draft = false
date="2014-11-23 01:02:06"
title="R: dplyr - \"Variables not shown\""
tag=['r-2', 'dplyr']
category=['R']
+++

<p>
I recently ran into a problem where the result of applying some operations to a data frame wasn't being output the way I wanted.
</p>


<p>I started with this data frame:</p>



~~~r

words = function(numberOfWords, lengthOfWord) {
  w = c(1:numberOfWords)  
  for(i in 1:numberOfWords) {
    w[i] = paste(sample(letters, lengthOfWord, replace=TRUE), collapse = "")
  }
  w
}

numberOfRows = 100
df = data.frame(a = sample (1:numberOfRows, 10, replace = TRUE),
                b = sample (1:numberOfRows, 10, replace = TRUE),
                name = words(numberOfRows, 10)) 
~~~

<p>I wanted to group the data frame by <cite>a</cite> and <cite>b</cite> and output a comma separated list of the associated names. I started with this:</p>



~~~r

> df %>% 
    group_by(a,b) %>%
    summarise(n = n(), words = paste(name, collapse = ",")) %>%
    arrange(desc(n)) %>%
    head(5)

Source: local data frame [5 x 4]
Groups: a

   a  b  n
1 19 90 10
2 24 36 10
3 29 20 10
4 29 80 10
5 62 54 10
Variables not shown: words (chr)
~~~

<p>Unfortunately the <cite>words</cite> column has been excluded and I came across <a href="http://stackoverflow.com/questions/22471256/overwriting-variables-not-shown-in-dplyr">this Stack Overflow post</a> which suggested that the <cite>print.tbl_df</cite> function was the one responsible for filtering columns.</p>


<p>Browsing the docs I found a couple of ways to overwrite this behaviour:</p>



~~~r

> df %>% 
    group_by(a,b) %>%
    summarise(n = n(), words = paste(name, collapse = ",")) %>%
    arrange(desc(n)) %>%
    head(5) %>%
    print(width = Inf)
~~~

<p>or</p>



~~~r

> options(dplyr.width = Inf)
> df %>% 
    group_by(a,b) %>%
    summarise(n = n(), words = paste(name, collapse = ",")) %>%
    arrange(desc(n)) %>%
    head(5)
~~~

<p>And now we see this output instead:</p>



~~~r

Source: local data frame [5 x 4]
Groups: a

   a  b  n                                                                                                         words
1 19 90 10 dfhtcgymxt,zpemxbpnri,rfmkksuavp,jxaarxzdzd,peydpxjizc,trdzchaxiy,arthnxbaeg,kjbpdvvghm,kpvsddlsua,xmysfcynxw
2 24 36 10 wtokzdfecx,eprsvpsdcp,kzgxtwnqli,jbyuicevrn,klriuenjzu,qzgtmkljoy,bonbhmqfaz,uauoybprrl,rzummfbkbx,icyeorwzxl
3 29 20 10 ebubytlosp,vtligdgvqw,ejlqonhuit,jwidjvtark,kmdzcalblg,qzrlewxcsr,eckfgjnkys,vfdaeqbfqi,rumblliqmn,fvezcdfiaz
4 29 80 10 wputpwgayx,lpawiyhzuh,ufykwguynu,nyqnwjallh,abaxicpixl,uirudflazn,wyynsikwcl,usescualww,bkvsowfaab,gfhyifzepx
5 62 54 10 beuegfzssp,gfmegjtrys,wkubhvnkkk,rkhgprxttb,cwsrzulnpo,hzkvjbiywc,gbmiupnlbw,gffovxwtok,uxadfrjvdn,aojjfhxygs
~~~

<p>Much better!</p>

