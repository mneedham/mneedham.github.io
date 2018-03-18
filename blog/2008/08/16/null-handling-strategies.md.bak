+++
draft = false
date="2008-08-16 01:03:03"
title="Null Handling Strategies"
tag=['c', 'null', 'null-object-pattern', 'exceptions']
category=['Coding']
+++

I mentioned in an <a href="2008/07/18/null-checks-everywhere-and-airport-security/">earlier post</a> my dislike of the passing of null around code, and since then there have been a <a href="http://blog.kriskemper.com/2008/08/11/programming-by-contract-considered-excessive/">couple</a> of <a href="http://andyp-tw.blogspot.com/2008/08/returning-null-considered-dishonest.html">posts</a> on the subject on the <a href="http://blogs.thoughtworks.com/">ThoughtWorks blogs</a>.

I had always thought that was a silver bullet for the way that we can handle null objects in our code but it seems from reading other people's opinions and from my own experience that this is not the case (surprise, surprise!). Several ideas of how to handle nulls came out in these posts and the comments posted on them, and it seems to me that there are several strategies for handling nulls in code.
<h3>Return null</h3>
The most common way of handling cases where there is no object to return, the code just returns null instead.

The problem with this approach is that the client now has to handle two different types of results. One if an object is returned and another if nothing is returned. This either results in code like this being scattered throughout the code base:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">Car car = carRepository.RetrieveCar(carId)<tt>
</tt><span class="r">if</span>(car != null)<tt>
</tt>{<tt>
</tt>   car.Drive();<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
Or the client doesn't bother to handle the null and we end up with a Null Pointer/Reference exception at some stage. Neither of these solution is particularly desirable.

Scala actually has an interesting way of getting around this problem by allowing you to define an interface which informs the client that there is the potential for nothing to be returned, therefore effectively designing a contract which allows the client to deal with it appropriately. The Option[T] idea is explained about half way down the page on <a href="http://debasishg.blogspot.com/2008/03/maybe-scala.html">this post</a>.

This can also be done in C# to an extent by making use of the <a href="http://msdn.microsoft.com/en-us/library/1t3y8s4s(VS.80).aspx">nullable operator</a>. In C# it is only useful when you want to make it clear to the client that they may get a null value instead of a primitive.

Overall, this is the simplest solution and probably also the easiest to understand. It just doesn't result in the cleanest code.
<h3>Throw Exception</h3>
The idea here is that if there is no object to return, the code throws a custom exception which describes the reason that no object was found.
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public Car RetrieveCar(Guid carId)<tt>
</tt>{<tt>
</tt>   Car car = FindCarInDatabaseBy(carId);<tt>
</tt>   <span class="r">if</span>(car == null)<tt>
</tt>   {<tt>
</tt>      throw new CarNotFoundException();<tt>
</tt>   }<tt>
</tt>   <span class="r">return</span> car;<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
This is certainly more descriptive in telling you why nothing has been returned, but as with 'Return null' at some stage the alternate result from the method call needs to be handled. If this is being done with Java's checked exceptions then it would either need to be handled by the method which calls RetrieveCar or bubbled up through the car. There are a variety of considerations for why you would would choose each way but that discussion is for another post.

As well as this, in theory you could end up with a method returning different Exceptions depending on the reason for the failure to return an object.

I'm not a big fan of handling state via exceptions as I think that exceptions should only be used where something exceptional has happened and I don't think that failing to find an object can be considered exceptional in most cases.
<h3>Null Object Pattern</h3>
The <a href="http://en.wikipedia.org/wiki/Null_Object_pattern">null object pattern</a> is the most helpful of the null handling strategies as far as the client is concerned. The client will now know that the object it has been returned is a null object, it will just see an object of the type requested. The devil is in the detail:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt><strong>10</strong><tt>
</tt>11<tt>
</tt>12<tt>
</tt>13<tt>
</tt>14<tt>
</tt>15<tt>
</tt>16<tt>
</tt>17<tt>
</tt>18<tt>
</tt>19<tt>
</tt><strong>20</strong><tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public class Car<tt>
</tt>{<tt>
</tt>   public virtual <span class="pt">void</span> Drive()<tt>
</tt>   {<tt>
</tt>      <span class="c">// Do some driving</span><tt>
</tt>   }<tt>
</tt><tt>
</tt>   public <span class="r">static</span> Car <span class="pc">NULL</span><tt>
</tt>   {<tt>
</tt>      get { <span class="r">return</span> new NullCar(); }<tt>
</tt>   }<tt>
</tt><tt>
</tt>   class NullCar : Car<tt>
</tt>   {<tt>
</tt>      public override <span class="pt">void</span> Drive()<tt>
</tt>      {<tt>
</tt>         throw new NotImplementedException();<tt>
</tt>      }<tt>
</tt>   }<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">public Car RetrieveCar(Guid carId)<tt>
</tt>{<tt>
</tt>   Car car = FindCarInDatabaseBy(carId);<tt>
</tt>   <span class="r">if</span>(car == null)<tt>
</tt>   {<tt>
</tt>      <span class="r">return</span> Car.<span class="pc">NULL</span>;<tt>
</tt>   }<tt>
</tt>   <span class="r">return</span> car;<tt>
</tt>}~~~
</td>
</tr>
</tbody></table>
This pattern effectively delays the need to handle the unexpected behaviour exhibited by the RetrieveCar method. Depending on the implementation of the NullCar we might decide to throw a NotImplementedException if a method on it is ever called. Or we can just override every method to do nothing which just hides the problem as far as I'm concerned.

These are the main ways I have come across for handling nulls. I'm sure there are others so if you know of any better ways please let me know.
