+++
draft = false
date="2011-07-19 06:39:44"
title="Scala: Rolling with implicit"
tag=['scala']
category=['Scala']
+++

We've been coding in Scala on my project for around 6 weeks now and are getting to the stage where we're probably becoming a big dangerous with our desire to try out some of the language features.

One that we're trying out at the moment is the <a href="http://www.scala-lang.org/node/114">implicit</a> key word which allows you to pass arguments to objects and methods without explicitly defining them in the parameter list.

The website we're working on needs to be accessible in multiple languages and therefore we need to be able to translate some words before they get displayed on the page.

Most of the time it's just static labels which need to be internationalised but there are a few words which are retrieved from the database and aren't as easy to deal with.

We introduced the idea of the <cite>LanguageAwareString</cite> which acts as a wrapper around a <cite>String</cite> and has its own <cite>toString</cite> method which delegates to a <cite>Language</cite> class which contains a dictionary 

It's defined like this:


~~~scala

case class LanguageAwareString(ignorantValue:String)(implicit val language : Language) {
  def toString = language.translate(ignorantValue)
}
~~~

We didn't want to have to pass <cite>Language</cite> to the <cite>LanguageAwareString</cite> factory method every time we're going to be calling it in quite a few places.

We therefore create an implicit val at the beginning of our application in the Scalatra entry code


~~~scala

class Controllers extends ScalatraFilter with ScalateSupport {
	...
	implicit def currentLanguage : Language = // work out the current language
}
~~~

As I understand it, whenever the Scala compiler encounters an implicit it looks in its execution scope for any value defined as implicit with the expected type.

As long as there's only one such value in the scope it make use of that value but if there's more than one we'd see a compilation error since it wouldn't know which one to use.

We therefore needed to define <cite>Language</cite> as an implicit on all the classes/methods which the code follows on its way down to <cite>LanguageAwareStrong</cite>.

The problem we've had is that it's not immediately obvious what's going on to someone who hasn't come across  <cite>implicit</cite> before and we therefore end up having to go the above each time!

We've decided that to ease that transition we'd explicitly pass <cite>Language</cite> down through the first few classes so that it's more obvious what's going on.

We therefore have code like this in a few places:


~~~scala

new ObjectThatTakesLanguageImplicitly(someArg)(currentLanguage)
~~~

Maybe we can phase that out as people get used to <cite>implicit</cite> or maybe we'll just get rid of <cite>implicit</cite> and decide it's not worth the hassle!
