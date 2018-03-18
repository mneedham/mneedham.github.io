+++
draft = false
date="2011-10-25 20:38:52"
title="Scala: Creating an Xml element with an optional attribute"
tag=['scala']
category=['Scala']
+++

We have a lot of Xml in our application and one of the things that we need to do reasonably frequently in our test code is create elements which have optional attributes on them.

Our simple first approach looked like this:


~~~scala

def createElement(attribute: Option[String]) = if(attribute.isDefined) <p bar={attribute.get} /> else <p />
~~~

That works but it always seemed like we should be able to do it in a simpler way.

Our first attempt was this:


~~~scala

def createElement(attribute: Option[String]) = <p bar={attribute} />
~~~

But that ends up in a compilation error:


~~~text

error: overloaded method constructor UnprefixedAttribute with alternatives:
  (key: String,value: Option[Seq[scala.xml.Node]],next: scala.xml.MetaData)scala.xml.UnprefixedAttribute <and>
  (key: String,value: String,next: scala.xml.MetaData)scala.xml.UnprefixedAttribute <and>
  (key: String,value: Seq[scala.xml.Node],next1: scala.xml.MetaData)scala.xml.UnprefixedAttribute
 cannot be applied to (java.lang.String, Option[String], scala.xml.MetaData)
       def createElement1(attribute: Option[String]) = <p bar={attribute} />
~~~

We really need to extract the string value from the option if there is one and not do anything if there isn't one but with the above approach we try to shove an option in as the attribute value. Unfortunately there isn't an overload of the constructor which lets us do that.

Eventually one of my colleagues suggested we try passing null in as the attribute value if we had a None option:


~~~scala

def createElement(attribute: Option[String]) = <p bar={attribute.getOrElse(null)} />
~~~

Which works pretty well:


~~~text

scala> createElement(Some("mark"))
res0: scala.xml.Elem = <p bar="mark"></p>


scala> createElement(None)
res1: scala.xml.Elem = <p ></p>

~~~
