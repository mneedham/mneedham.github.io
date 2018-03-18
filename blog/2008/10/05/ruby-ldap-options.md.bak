+++
draft = false
date="2008-10-05 16:29:32"
title="Ruby LDAP Options"
tag=['activeldap', 'ruby-ldap', 'rjb']
category=['Ruby']
+++

As I <a href="http://www.markhneedham.com/blog/2008/09/29/connecting-to-ldap-server-using-opends-in-java/">mentioned in an earlier post</a> a colleague and I spent a few days looking at how to connect to an <a href="http://www.opends.org/">OpenDS</a> LDAP server using Ruby.

We ended up analysing four different solutions for solving the problem. 

<h3>Active LDAP</h3>
This approach involved using the <a href="http://rubyforge.org/projects/ruby-activeldap/">Active LDAP Ruby</a> which "provides an object oriented interface to LDAP. It maps LDAP entries to Ruby objects with LDAP attribute accessors based on your LDAP server's schema and each object's objectClasses".

We had real problems trying to even connect to our OpenDS server using this library. We eventually found out that OpenDS is not actually listed as one of the supported interfaces.

The real benefit of this approach was that the library is written in Ruby meaning that getting permission to install it would be easier.

The fact that we couldn't actually get it to work didn't help!

<h3>Java LDAP libraries + RJB</h3>
This approach involved interacting with <a href="http://www.markhneedham.com/blog/2008/09/29/connecting-to-ldap-server-using-opends-in-java/">LDAP with Java libraries</a> and then using the <a href="http://rjb.rubyforge.org/">Ruby Java Bridge</a> to connect to these from our Ruby code.

We were able to solve the problem quite easily using this approach but the Ruby code we ended up writing was very Javaesque in style and it didn't feel like we were utilising the power of Ruby by using Java for such a fundamental part of the problem we were attempting to solve.

On the positive side RJB is easily installable via a gem and we were able to connect to OpenDS and execute the operations that were required.

<h3>Ruby-LDAP</h3>
The third option we looked at was <a href="http://ruby-ldap.sourceforge.net/">Ruby-LDAP</a>, a Ruby extension library written in C.

The disadvantage of this was that we needed to have make available to install it onto our machine. Seeing as we were using a Mac this meant downloading XCode to make use of the GCC compiler.

Interacting with the different libraries was tricky initially but we eventually got the hang of it and were able to connect to OpenDS despite it not being listed as one of the supported libraries.

<h3>ruby-net-ldap</h3>

<a href="http://rubyfurnace.com/docs/ruby-net-ldap-0.0.4/">ruby-net-ldap</a> is a pure Ruby LDAP library, installable via a gem.

This had by far the best examples and most intuitive interface of the options that we analysed and worked for us first time without too much fuss. Connecting to our Open DS server was seamless.

<h3>Overall</h3>

Our original selection, despite the slightly more complicated installation was Ruby-LDAP. 

However, <a href="http://olabini.com/">Ola Bini</a> pointed out ruby-net-ldap which actually proved to meet our criteria even more closely than Ruby-LDAP did and as such was the option we went with.

For those that are interested, <a href="http://geekdamana.blogspot.com/">Damana</a> has posted more of the <a href="http://geekdamana.blogspot.com/2008/10/ruby-ldap.html">technical details</a> behind the approaches we took.
