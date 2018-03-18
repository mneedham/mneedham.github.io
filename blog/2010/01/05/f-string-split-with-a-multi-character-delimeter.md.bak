+++
draft = false
date="2010-01-05 23:10:56"
title="F#: String.Split with a multi character delimeter"
tag=['f']
category=['F#']
+++

In my continued efforts at <a href="http://osherove.com/tdd-kata-1/">Roy Osherove's TDD Kata</a> I've been trying to work out how to split a string based on a delimeter which contains more than one character.

My original thinking was that it should be possible to do so like this:


~~~ocaml

"1***2".Split("***".ToCharArray());;
~~~

I didn't realise that splitting the string like that splits on each of the stars individually which means that we end up getting 2 empty values in the result:


~~~text

val it : string [] = [|"1"; ""; ""; "2"|]
~~~

If we want to split on '***' then we have to pass it in as a value in a string array:


~~~ocaml

"1***2".Split([| "***" |], StringSplitOptions.None);;
~~~

That way we only get the 1 and 2 which is what we want:


~~~text

val it : string [] = [|"1"; "2"|]
~~~

I'd expected there to be an overload which takes in a string and then just splits on that but since there isn't this isn't a bad alternative.

Sam Allen has <a href="http://dotnetperls.com/string-split">a very interesting article which covers all sorts of way to split different types of strings</a>.
