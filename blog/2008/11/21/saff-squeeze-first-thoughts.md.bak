+++
draft = false
date="2008-11-21 00:58:07"
title="Saff Squeeze: First Thoughts"
tag=['coding', 'kent-beck', 'debugging']
category=['Coding']
+++

While practicing some coding by doing the <a href="http://sites.google.com/site/tddproblems/all-problems-1/Roman-number-conversion">Roman number conversion</a> last weekend I came across an article by Kent Beck which talked of a method he uses to <a href="http://www.threeriversinstitute.org/HitEmHighHitEmLow.html">remove the need to use the debugger</a> to narrow down problems.

He calls the method the '<strong>Saff Squeeze</strong>' and the basic idea as I understand it is to write the original failing test and then inline the pieces of code that it calls, adding assertions earlier on in the code until the actual point of failure is found. 

The thinking behind this is that we will now have another much smaller test which we can add to our test suite although he did point out that it may take longer to solve the problem this way rather than using the debugger.

I'm not a fan of debugging through code and I believe if we are using TDD effectively then it should <a href="http://www.thekua.com/atwork/2007/10/test-driven-development-requires-less-debugging/">reduce the need to use the debugger</a>.

When I got a bit stuck with the parsing of the input for my Roman number conversion I decided this would be a good time to give the approach a trial run.

The actual problem was that I was trying to parse a value such as 'XI' by called String.split("") which looking back of course was ridiculous. This was resulting in an array with 3 values - X,I and "" - which then gave a null pointer exception when I tried to convert it to a numeric value.

Applying the Saff Squeeze allowed me to narrow down this problem and change the implementation when I realised my approach was never going to work.

Although I wasn't able to keep the test which I had created from all the inlining, it did become clear to me from this exercise that my tests around certain areas of the code were not fine grained enough. I find I lose the discipline a bit when I test from the outside in which is something I am trying to improve. This method proved to be a good way of keeping me honest.

Kent suggested that it would take much longer to debug using this approach but I found I was able to solve my problem almost as quickly as if I had debugged through it with the added benefit that I wrote a few extra tests while I was narrowing down the problem.

It is certainly an interesting approach although one which I need more practice with before trying to introduce it into a work environment.
