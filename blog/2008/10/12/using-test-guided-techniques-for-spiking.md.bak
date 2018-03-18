+++
draft = false
date="2008-10-12 13:49:35"
title="Using test guided techniques for spiking"
tag=['tdd', 'testing']
category=['Testing']
+++

I think that out of all the <a href="http://www.extremeprogramming.org/rules.html">Extreme Programming practices</a> Test Driven Development is the one which I like the best. I feel it provides a structure for development work and helps me to remain focused on what I am trying to achieve rather than writing code which may not necessarily be needed.

However, there are times when it's difficult to use a TDD approach, and Pat Kua suggested earlier this year that <a href="http://www.thekua.com/atwork/2008/02/05/if-you-do-test-driven-development-all-the-time-youre-doing-something-wrong/">if you're using a TDD approach all the time you're doing something wrong</a>. 

As Pat points out spiking is one time when it can pay off to not to test first, although as was <a href="http://tech.groups.yahoo.com/group/testdrivendevelopment/message/29108">pointed out on the TDD mailing list</a> this doesn't necessarily mean that you can't take a test driven approach to learning new APIs or trying out new things.

Kent Beck speaks of <strong>Learning Tests</strong> - code written using tests to improve our understanding of an API and also guard against changes in future updates of the API - in <a href="http://www.markhneedham.com/blog/2008/10/07/test-driven-development-by-example-book-review/">Test Driven Development by Example</a>, an idea which is referenced in Chapter 8 of Uncle Bob's <a href="http://www.markhneedham.com/blog/2008/09/15/clean-code-book-review/">Clean Code</a>. This is not a new approach.

Tools like the JUnit TestRunner provide a really easy way to try things out and get immediate feedback as to whether or not the API works as you expect. As <a href="http://blog.benhall.me.uk/">Ben Hall</a> writes on twitter it also provides <a href="http://twitter.com/Ben_Hall/statuses/954848393">a level of documentation</a> which you can refer back to later.

Even if we don't want to write an actual test the principles of getting <strong>quick feedback</strong> and <strong>working in small steps</strong> can still be used in our exploration activities.

To give a couple of examples, <a href="http://geekdamana.blogspot.com">Damana</a> and I didn't write unit tests when we were exploring <a href="http://geekdamana.blogspot.com/2008/10/ruby-ldap.html">Ruby</a> <a href="http://www.markhneedham.com/blog/2008/10/05/ruby-ldap-options/">LDAP</a> options but we were only writing a couple of lines at a time then running them using TextMate to see if our understanding was correct. We were then able to keep this code in a 'spikes' directory for future reference.

A couple of years ago a colleague and I were exploring (what was at the time) <a href="http://www.oracle.com/tangosol/index.html">Tangosol Coherence's</a> API. We were using a method on the API to filter some data but for some reason it wasn't returning the data that we expected.

Convinced that we were using the API correctly we decided to code up two JUnit tests - one with a call to the method which we felt had a bug in it, and another achieving the same 'filter' using two other methods on the API. 

This helped us prove that there was a bug in the API and we ended up using the workaround we had discovered to solve our problem.

I'm sure there are other approaches that can achieve the same outcome but if you know how to test drive code then it makes sense to use an approach that is familiar to you.
