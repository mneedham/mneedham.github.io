+++
draft = false
date="2011-08-13 02:10:53"
title="Scala: Do modifiers on functions really matter?"
tag=['scala']
category=['Scala']
+++

A couple of colleagues and I were having an interesting discussion this afternoon about the visibility of functions which are mixed into an object from a trait.

The trait in question looks like this:


~~~scala

trait Formatting {
  def formatBytes(bytes: Long): Long = {
    math.round(bytes.toDouble / 1024)
  }
}
~~~

And is mixed into various objects which need to display the size of a file in kB like this:


~~~scala

class SomeObject extends Formatting {

}
~~~

By mixing that function into <cite>SomeObject</cite> any of the clients of <cite>SomeObject</cite> would now to be able to call that function and transform a bytes value of their own!

The public API of <cite>SomeObject</cite> is now cluttered with this extra method although it can't actually do any damage to the state of <cite>SomeObject</cite> because it's a pure function whose output depends only on the input given to it.

There are a couple of ways I can think of to solve the modifier 'problem':

<ul>
<li>Make <cite>formatBytes</cite> a private method on <cite>SomeObject</cite></li>
<li>Put <cite>formatBytes</cite> on a singleton object and call it from <cite>SomeObject</cite></li>
</ul>

The problem with the first approach is that it means we have to test the <cite>formatBytes</cite> function within the context of <cite>SomeObject</cite> which makes our test much more difficult than if we can test it on its own.

It also makes the discoverability of that function more difficult for someone else who has the same problem to solve elsewhere.

With the second approach we'll have a dependency on that singleton object in our object which we wouldn't be able to replace in a test context even if we wanted to.

While thinking about this afterwards I realised that it was quite similar to something that I used to notice when i was learning F# - the modifiers on functions don't seem to matter if the data they operate on is immutable. 

I often used to go back over bits of code I'd written and make all the helper functions private before realising that it made more sense to keep them public but group them with similar functions in a module.

I'm moving towards the opinion that if the data is immutable then it doesn't actually matter that much who it's accessible to because they can't change the original version of that data.

<cite>private</cite> only seems to make sense if it's a function mutating a specific bit of data in an object but I'd be interesting in hearing where else my opinion doesn't make sense.
