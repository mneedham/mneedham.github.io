+++
draft = false
date="2012-06-24 22:55:39"
title="Why you shouldn't use name as a key a.k.a. I am an idiot"
tag=['software-development']
category=['Software Development']
+++

I think one of the first things that I learnt about dealing with users in a data store is that you should never use name as a primary key because their might be two people with the same name.

Despite knowing that I foolishly chose to ignore this knowledge when building my neo4j graph and used name as the key for the Lucene index. 

I thought I'd got away with it but NO!

Earlier today I was trying to work out who the most connected person at ThoughtWorks is and the graph was suggesting that 'Rahul Singh' was the most connected, having worked with 540 people.

I mentioned this to <a href="https://twitter.com/#!/jennifersmithco">Jen</a> who felt something was probably wrong since he'd only started working at ThoughtWorks a couple of years ago.

Amusingly Jen found an email from 18 months ago sent by Rahul #1 explaining that there were in fact two people with exactly the same name and he was getting emails intended for the other one and vice versa.

I now have first hand knowledge of what can happen if you ignore one of the most basic rules of software development!

My gamble that there probably wouldn't be two people with the same name in such a small dataset has totally failed and from now on I'll be sure to use a unique key!
