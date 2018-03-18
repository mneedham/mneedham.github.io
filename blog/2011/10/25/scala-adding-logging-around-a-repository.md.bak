+++
draft = false
date="2011-10-25 21:19:22"
title="Scala: Adding logging around a repository"
tag=['scala']
category=['Scala']
+++

We wanted to add some logging around one of our repositories to track how many times users were trying to do various things on the application and came across <a href="http://yacode.blogspot.com/2011/07/dynamic-proxy-using-scala-implicit.html">a cool blog post explaining how we might be able to do this</a>.

We ended up with the following code:


~~~scala

class BarRepository {
  def all: Seq[Bar] = Seq()
  def find(barId:String) : Bar = Bar("myBar")
}
~~~


~~~scala

class TrackService(barRepository:BarRepository) {
  def all : Seq[Bar] = { 
    var bars = barRepository.all; 
    println("tracking all bars"); 
    bars 
  }
}
~~~


~~~scala

implicit def trackServiceToBarRepository(t:TrackService) : BarRepository = t.barRepository
~~~

We can then use it like this:


~~~scala

scala> val service = new TrackService(new BarRepository())
service: TrackService = TrackService@4e5394c

scala> service.all
tracking all bars
res6: Seq[Bar] = List()
~~~

If a method doesn't exist on <cite>TrackService</cite> then the implicit conversion ensures that the appropriate method will be called on <cite>BarRepository</cite> directly:


~~~scala

scala> service.find("mark")
res7: Bar = Bar(myBar)
~~~

I came across another way to achieve the same results by <a href="http://java.dzone.com/articles/real-world-scala-managing-cros">making use of traits</a> although we'd need to change our design a little bit to achieve this pattern:


~~~scala

trait IProvideBars {
  def all : Seq[Bar]
  def find(barId:String) : Bar
}
~~~


~~~scala

class BarRepository extends IProvideBars {
  def all: Seq[Bar] = Seq()
  def find(barId:String) : Bar = Bar("myBar")
}
~~~


~~~scala

trait Tracking extends IProvideBars {
  abstract override def all : Seq[Bar] = { 
    val bars = super.all;
    println("tracking all bars"); 
    bars 
  }
}
~~~


~~~scala

scala> val b = new BarRepository() with Tracking
b: BarRepository with Tracking = $anon$1@ddc652f

scala> b.all
tracking all bars
res8: Seq[Bar] = List()
~~~
