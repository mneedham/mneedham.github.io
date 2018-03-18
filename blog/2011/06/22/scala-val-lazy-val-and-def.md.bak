+++
draft = false
date="2011-06-22 23:04:44"
title="Scala: val, lazy val and def"
tag=['scala']
category=['Scala']
+++

We have a variety of <cite>val</cite>, </cite>lazy val</cite> and <cite>def</cite> definitions across our code base but have been led to believe that idiomatic Scala would have us using <cite>lazy val</cite> as frequently as possible.

As far as I understand so far this is what the different things do:

<ul>
<li><cite>val</cite> evaluates as soon as you initialise the object and stores the result.</li>
<li><cite>lazy</cite> val evaluates the first time that it's accessed and stores the result.</li>
<li><cite>def</cite> executes the piece of code every time - pretty much like a Java method would.</li>
</ul>

In Java, C# or Ruby I would definitely favour the 3rd option because it <a href="http://www.markhneedham.com/blog/2009/09/02/coding-reduce-fields-delay-calculations/">reduces the amount of state that an object has to hold</a>.

I'm not sure that having that state matters so much in Scala because all the default data structures we use are immutable so you can't do any harm by having access to them.

I recently read <a href="http://www.codequarterly.com/2011/rich-hickey/">an interesting quote from Rich Hickey</a> which seems applicable here:

<blockquote>
To the extent the data is immutable, there is little harm that can come of providing access, other than that someone could come to depend upon something that might change. Well, okay, people do that all the time in real life, and when things change, they adapt.
</blockquote>	

If the data was mutable then it would be possible to change it from any other place in the class which would make it difficult to reason about the object because the data might be in an unexpected state.

If we define something as a <cite>val</cite> in Scala then it's not even possible to change the reference to that value so it doesn't seem problematic.

Perhaps I just require a bit of a mind shift to not worry so much about state if it's immutable.

It's only been a few weeks so I'd be interested to hear the opinions of more seasoned Scala users.

---

I've read that there are various performance gains to be had from making use of <cite>lazy val</cite> or <cite>def</cite> depending on the usage of the properties but that would seem to be a premature optimisation so we haven't been considering it so far.
