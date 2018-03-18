+++
draft = false
date="2015-06-27 22:47:22"
title="R: Command line - Error in GenericTranslator$new : could not find function \"loadMethod\""
tag=['r-2']
category=['R']
+++

<p>
I've been reading <a href="https://pragprog.com/book/rmtpruby/text-processing-with-ruby">Text Processing with Ruby</a> over the last week or so and one of the ideas the author describes is setting up your scripts so you can run them directly from the command line.</p>


<p>
I wanted to do this with my Wimbledon R script and wrote the following script which uses the 'Rscript' executable so that R doesn't launch in interactive mode:
</p>


<em>wimbledon</em>

~~~bash

#!/usr/bin/env Rscript

library(rvest)
library(dplyr)
library(stringr)
library(readr)

# stuff
~~~

<p>
Then I tried to run it:
</p>



~~~bash

$ time ./wimbledon

...

Error in GenericTranslator$new : could not find function "loadMethod"
Calls: write.csv ... html_extract_n -> <Anonymous> -> Map -> mapply -> <Anonymous> -> $
Execution halted

real	0m1.431s
user	0m1.127s
sys	0m0.078s
~~~

<p>
As the error suggests, the script fails when trying to write to a CSV file - it looks like Rscript doesn't load in something from the core library that we need. It turns out <a href="https://groups.google.com/forum/#!topic/shiny-discuss/Gx2P_dhzM38">adding the following line</a> to our script is all we need:
</p>



~~~bash

library(methods)
~~~

<p>So we end up with this:</p>



~~~bash

#!/usr/bin/env Rscript

library(methods)
library(rvest)
library(dplyr)
library(stringr)
library(readr)
~~~

<p>And when we run that all is well!</p>

