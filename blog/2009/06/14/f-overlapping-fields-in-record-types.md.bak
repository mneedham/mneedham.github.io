+++
draft = false
date="2009-06-14 00:37:01"
title="F#: Overlapping fields in record types"
tag=['f', 'records']
category=['F#']
+++

A problem which has confused me for a while is how to create instances of record types whose fields overlap with another record defined further down in an F# file.

The most recently defined record seems to take precedence even if it has more fields than a record defined earlier and you don't specify all of those fields in your record creation attempt.

For example, if I have the following two record types:


~~~ocaml

type Mark = { Value : string }
type SpecificMark = { Value: string; AnotherValue : int }
~~~

I thought it would be possible to create an instance of 'Mark' by doing this:


~~~ocaml

let mark = { Value = "mark" }
~~~

But what I actually got is the following compilation error:


~~~text

No assignment given for field 'AnotherValue'
~~~

It turns out that you need to be more explicit about the fact that you want to create the 'Mark' record type. 

Using the pre F# 1.9.16 syntax we would use the following <a href="http://www.markhneedham.com/blog/2009/05/19/f-object-expressions/">object expression</a>:


~~~ocaml

let mark = { new Mark with Value = "mark" }
~~~

But versions after that indicate that this syntax is deprecated and we need to do something more like this:


~~~ocaml

let mark = { new Mark with member self.Value = "mark" }
~~~

Which leads to the following error:


~~~text

error FS0191: Only simple bindings of the form 'id = expr' can be used in construction expressions
~~~

This has <a href="http://cs.hubfs.net/forums/thread/10412.aspx">also been mentioned on the hubfs forums</a> although there is no suggestion as for why this syntax would be invalid - it seems like it should work to me. 

Luckily there are a couple of other ways to get an instance of the 'Mark' type:


~~~ocaml

let (m:Mark) = { Value = "mark" }
~~~


~~~ocaml

let mark = {Value = "mark" } : Mark
~~~

Both of which require less typing anyway!
