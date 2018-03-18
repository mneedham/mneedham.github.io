+++
draft = false
date="2009-06-26 18:15:23"
title="Coding Dojo #18: Groovy Bowling Game"
tag=['oop', 'coding-dojo', 'bowling-game', 'groovy']
category=['Coding Dojo']
+++

This week's dojo involved coding a familiar problem - the <a href="http://www.markhneedham.com/blog/2008/11/06/object-calisthenics-first-thoughts/">bowling</a> <a href="http://www.markhneedham.com/blog/2008/11/13/coding-dojo-2-bowling-game-object-calisthenics-continued/">game</a> - in a different language, Groovy.

The code we wrote is available on <a href="http://bitbucket.org/codingdojosydney/bowling-game-groovy/src/tip/src/">bitbucket</a>.

<h3>The Format</h3>

<a href="http://camswords.wordpress.com/">Cam</a>, <a href="http://twitter.com/deanrcornish">Dean</a> and I took turns pairing with each other with the code projected onto a TV. As there were only a few of us the discussion on where we were taking the code tended to included everyone rather than just the two at the keyboard.

<h3>What We Learnt</h3>

<ul>
<li>I've sometimes wondered about the wisdom of running dojos in newer languages but this one worked quite well because Cam has been learning Groovy and he was able to point us in the right direction when we started writing Java-esque Groovy code. The particular syntax that I didn't know about was that you can define and put items into a list in a much simpler way than in Java:

I was starting to write code like this:

~~~groovy

def frames = new List<Frame>()
frames.Add(frame)
~~~

Which Cam simplified down to:


~~~groovy

def frames = []
frames << frame
~~~

I didn't feel that I missed the static typing you get in Java although IntelliJ wasn't quite as useful when it came to suggesting which methods you could call on a particular object.
</li>
<li>I'm even more convinced that using various languages functional equivalent of the 'for each' loop, in this case 'eachWith' and 'eachWithIndex' is <a href="http://www.markhneedham.com/blog/2009/06/18/functional-collection-parameters-a-different-way-of-thinking-about-collections/">not the way to go</a> and we could see <a href="http://bitbucket.org/codingdojosydney/bowling-game-groovy/src/tip/src/BowlingGame.groovy">our code becoming very complicated</a> when trying to work out how to score strikes thanks to our use of it! </li>
<li>I think we actually got further this time in terms of the implementation although we did slow down when it came to scoring strikes to try and work out exactly how we wanted to do it.

Prior to this we had been following the idea of just getting the tests to pass and driving the design of the code that way but we at this stage it seemed foolish to keep doing that as the code would increased dramatically in complexity by doing so.

The two approaches we were thinking of involved using the state pattern to determine what the current frame outcome was and then work out the cumulative score based on that by looking forward to future frames or an approach that would make use of functional collection parameters (not sure exactly which ones!) to calculate the score in a more function rather than OO way.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>We'll probably keep going with some more Groovy as it's actually more interesting than I thought it would be. I'm also keen to do a coding dojo where we <a href="http://www.antiifcampaign.com/">never make use of the if statement</a>.</li>
</ul>
