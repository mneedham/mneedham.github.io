+++
draft = false
date="2009-09-04 00:26:00"
title="Coding Dojo #22: Scala, lamdaj, Project Euler"
tag=['coding-dojo', 'scala', 'lambdaj']
category=['Coding Dojo', 'Scala']
+++

In our latest coding dojo we played around with <a href="http://www.scala-lang.org/">Scala</a> and <a href="http://code.google.com/p/lambdaj/">lambdaj</a> while attempting to solve some of the problems on the <a href="http://projecteuler.net/index.php?section=problems">Project Euler</a> website.

<h3>The Format</h3>

We started off on two different machines with two of us having a look at solving the first Project Euler problem in Scala and the other two trying to solve it in Java while using the lambdaj library.

<h3>What did we learn?</h3>

<ul>
<li><a href="http://fabiopereira.me/blog/">Fabio</a> and I worked on the Scala solution to the problem and we were pretty much playing around with different ways to aggregate all the values in the list:


~~~scala

1.to(999).filter(x => x%3 == 0 || x%5 == 0).foldLeft(0)((acc,x) => acc + x)
1.to(999).filter(x => x%3 == 0 || x%5 == 0)./:(0)((x,y) => x+y)
1.to(999).filter(x => x%3 == 0 || x%5 == 0).foldRight(0)(_+_)
1.to(999).filter(x => x%3 == 0 || x%5 == 0).reduceLeft(_+_)
1.to(999).filter(x => x%3 == 0 || x%5 == 0)./:(0)(_+_)
~~~

We decided to work through how 'foldLeft' and 'foldRight' work for summing a simpler collection of data, the numbers 1-5, which goes something like this:

fold_left

~~~text

(((((0 + 1) + 2) + 3) + 4) + 5) = 15
~~~

fold_right

~~~right

(1 + (2 + (3 + (4 + (5 + 0))))) = 15
~~~

When adding the numbers together it doesn't make any different whether we fold the collection from the left or from the right.

If we do subtraction we do get different answers though:

fold_left

~~~text

(((((0 - 1) - 2) - 3) - 4) - 5) = -15
~~~

fold_right

~~~text

(1 - (2 - (3 - (4 - (5 - 0))))) = 3

-> 5 - 0 = 5
-> 4 - 5 = -1
-> 3 - -1 = 4
-> 2 - 4 = -2
-> 1 - -2 = 3
~~~


The other way of doing fold_left, '/:', is quite interesting although perhaps unintuitive when you first come across it. <a href="http://lizdouglass.wordpress.com/">Liz</a> showed me an <a href="http://rickyclarkson.blogspot.com/2008/01/in-defence-of-0l-in-scala.html">interesting post by Ricky Clarkson where he talks about this method and the reason why it's in the language</a>. 

Liz and Dave Yeung worked on doing a solution to lambdaj to the problem but it ended up being quite verbose so we decided to play around with Scala for the rest of the session.</li>
<li>We spent a bit of time playing around with traits via a <a href="http://www.artima.com/scalazine/articles/steps.html">nice introductory article</a> which effectively acts as a a cut down version of the <a href="http://www.artima.com/shop/programming_in_scala">Programming in Scala</a> book.

I particularly like the way that you can add a trait to an instance of an object and you get access to all the methods defined on that trait which seems quite similar to Ruby mixins.

<a href="http://lizdouglass.wordpress.com/">Liz</a> and I were discussing <a href="http://docondev.blogspot.com/2009/08/messy-code-is-not-technical-debt.html">an article written by Michael Norton comparing  technical debt and making a mess</a> so that's where the trait name came from!


~~~scala

trait Mess  {
  def makeMess = print("tech debt is so funny")
}

class Liz {

}
~~~

If you try to make use of the trait like this:


~~~scala

val liz : Liz = new Liz with Mess
~~~

You don't have access to the 'makeMess' method since you explicitly defined the type to be 'Liz' which doesn't have the method:


~~~scala

liz.makeMess
> error: value makeMess is not a member of Liz
       liz.makeMess
~~~

If we let the compiler do its thing without trying to explicitly type the value it works much better:


~~~scala

val liz = new Liz with Mess
> Liz with Mess
~~~


~~~scala

liz.makeMess
> tech debt is so funny
~~~

I really like having the ability to do this although I think I need to code a bit more Scala before I'll appreciate where we really gain by having this feature.

The conciseness of the language and the lack of '{}' while keeping the same expressiveness in the code is something which reminds me a lot of F# and from what I've seen so far I imagine it would be much more fun to code in Scala than in Java. 

It also seems more clear to me that when a static language has really good type inference then one of the main reasons that people prefer dynamic languages - you get to write less code for the same amount of features - is actually much less valid.</li>
<li>This was a very experimental dojo in nature although Liz has been playing around with Scala a bit so she was able to guide us a bit when we got stuck. 

I'm finding that sessions where everyone is fairly new to the language or technology aren't necessarily as fruitless as I had previously imagined that they would be - I find that <a href="http://www.markhneedham.com/blog/2009/01/25/learning-alone-or-learning-together/">learning something together</a> makes it more interesting as you can then draw on other people's ideas and understanding of the language as well as your own.

I think in the cases where everyone is a novice people need to be prepared to get involved and write some code despite that. If that's the case then I think it's certainly possible to gain a lot from these sessions.</li>
</ul>

