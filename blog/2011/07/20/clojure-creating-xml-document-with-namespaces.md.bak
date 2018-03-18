+++
draft = false
date="2011-07-20 20:28:17"
title="Clojure: Creating XML document with namespaces"
tag=['clojure']
category=['Clojure']
+++

As I mentioned in an earlier post we've been <a href="http://www.markhneedham.com/blog/2011/07/16/clojure-extracting-child-elements-from-an-xml-document-with-zip-filter/">parsing XML documents with the Clojure zip-filter API</a> and the next thing we needed to do was create a new XML document containing elements which needed to be inside a namespace.

We wanted to end up with a document which looked something like this:


~~~text

<root>
<mynamespace:foo xmlns:mynamespace="http://www.magicalurlfornamespace.com">
	<mynamespace:bar>baz</mynamespace:bar>
</mynamespace:foo>
</root>
~~~

We can make use of <cite>lazy-xml/emit</cite> to output an XML string from *some sort of input?* by wrapping it inside <cite>with-out-str</cite> like so:


~~~lisp

(require '[clojure.contrib.lazy-xml :as lxml])
(defn xml-string [xml-zip] (with-out-str (lxml/emit xml-zip)))
~~~

I was initially confused about how we'd be able to create a map representing name spaced elements to pass to <cite>xml-string</cite> but it turned out to be reasonably simple.

To create a non namespaced XML string we might pass <cite>xml-string</cite> the following map:


~~~lisp

(xml-string {:tag :root :content [{:tag :foo :content [{:tag :bar :content ["baz"]}]}]})
~~~

Which gives us this:


~~~text

"<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<root>
	<foo>
		<bar>baz</bar>
	</foo>
</root>" 
~~~

Ideally I wanted to prepend <cite>:foo</cite> and <cite>:bar</cite> with ':mynamespace" but I thought that wouldn't work since that type of syntax would be invalid in Ruby and I thought it'd be the same in Clojure.


~~~text

mneedham@Administrators-MacBook-Pro-5.local ~$ irb
>> { :mynamespace:foo "bar" }
SyntaxError: compile error
(irb):1: odd number list for Hash
{ :mynamespace:foo "bar" }
               ^
(irb):1: syntax error, unexpected ':', expecting '}'
{ :mynamespace:foo "bar" }
               ^
(irb):1: syntax error, unexpected '}', expecting $end
	from (irb):1
>> 
~~~

In fact it isn't so we can just do this:


~~~lisp

(xml-string {:tag :root 
  :content [{:tag :mynamespace:foo :attrs {:xmlns:meta "http://www.magicalurlfornamespace.com"} 
              :content [{:tag :mynamespace:bar :content ["baz"]}]}]})
~~~


~~~text

"<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<root>
<mynamespace:foo xmlns:meta=\"http://www.magicalurlfornamespace.com">
	<mynamespace:bar>baz</mynamespace:bar>
</mynamespace:foo>
</root>"  
~~~

As a refactoring step, since I had to append the namespace to a lot of tags, I was able to make use of the <cite>keyword</cite> function to do so:


~~~lisp

(defn tag [name value] {:tag (keyword (str "mynamespace" name)) :content [value]})
~~~


~~~text

> (tag :Foo "hello")  
{:tag :mynamespace:Foo, :content ["hello"]} 
~~~
