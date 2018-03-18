+++
draft = false
date="2012-05-10 07:11:17"
title="Haskell: Explicit type declarations in GHCI"
tag=['haskell']
category=['Haskell']
+++

On a few occasions I've wanted to be able to explicitly define the type of something when trying things out in the Haskell REPL (GHCI) but I didn't actually realise this was possible until a couple of days ago.

For example say we want to use the <cite><a href="http://zvon.org/other/haskell/Outputprelude/read_f.html">read</a></cite> function to parse an input string into an integer.

We could do this:


~~~haskell

> read "1" :: Int
1
~~~

But if we just evaluate the function alone and try and assign the result without casting to a type we get an exception:


~~~haskell

> let x  = read "1"

<interactive>:1:10:
    Ambiguous type variable `a0' in the constraint:
      (Read a0) arising from a use of `read'
    Probable fix: add a type signature that fixes these type variable(s)
    In the expression: read "1"
    In an equation for `x': x = read "1"
~~~

sepp2k shows <a href="http://stackoverflow.com/questions/3093133/how-to-provide-explicit-type-declarations-for-functions-when-using-ghci">how we can provide a type declaration in GHCI in his Stack Over Flow answer</a>:


~~~haskell

> let x::Int; x = read "1"
> x
1
~~~

We can also use it when creating a list of integers to ensure they are of type 'Int' rather than 'Integer' for example:


~~~haskell

> let y = [1,2,3]
> :t y
y :: [Integer]

> let y::[Int]; y = [1,2,3]
> :t y
y :: [Int]
~~~

It's a pretty simple thing but I didn't know it was even possible!
