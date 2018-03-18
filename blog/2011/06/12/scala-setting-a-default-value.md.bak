+++
draft = false
date="2011-06-12 16:03:30"
title="Scala: Setting a default value"
tag=['scala']
category=['Scala']
+++

We wanted to try and generate a build label to use for the name of the artifacts archive that gets generated each time we run the build but wanted to default it to a hard coded value if the system property representing the build label wasn't available.

In Ruby we would be able to do something like this:


~~~ruby

buildLabel =  ENV["GO_PIPELINE_LABEL"] || "LOCAL" 
~~~

There isn't a function in Scala that does that so we initially ended up with this:


~~~scala

  def buildLabel() = [{ 
    System.getenv("GO_PIPELINE_LABEL") match {
      case null => "LOCAL"
      case label => label
    }                                                                                                                                                                                                     
  } 
~~~

My colleague <a href="http://twitter.com/#!/mushtaqA">Mushtaq</a> suggested passing the initial value into an Option like so... 


~~~scala

def buildLabel() = {
	Option(System.getenv("GO_PIPELINE_LABEL")).getOrElse("LOCAL")
}
~~~

...which I think is pretty neat!

I tried to see what the definition of an operator to do it the Ruby way would look like and ended up with the following:


~~~scala

class RichAny[A](value:A ) {                              
      def || (default:A ) = {  Option(value).getOrElse(default)  }
}
~~~


~~~scala

implicit def any2RichAny[A <: AnyRef](x: A) = new RichAny(x)
~~~

Which we can use like so:


~~~scala

def buildLabel() = {
System.getenv("GO_PIPELINE_LABEL") || "LABEL"
}
~~~

I imagine that's probably not the idiomatic Scala way to do it so I'd be curious to know what is.
