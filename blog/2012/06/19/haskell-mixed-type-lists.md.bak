+++
draft = false
date="2012-06-19 23:09:39"
title="Haskell: Mixed type lists"
tag=['haskell']
category=['Haskell']
+++

I've been continuing to work through the exercises in <a href="http://www.amazon.co.uk/The-Little-Schemer-Daniel-Friedman/dp/0262560992/ref=sr_1_1?ie=UTF8&qid=1340144213&sr=8-1">The Little Schemer</a> and came across a problem which needed me to write a function to take  a mixed list of Integers and Strings and filter out the Integers.

As I <a href="http://www.markhneedham.com/blog/2012/06/19/the-little-schemer-attempt-2/">mentioned in my previous post</a> I've been doing the exercises in Haskell but I thought I might struggle with that approach here because Haskell collections are homogeneous i.e. all the elements need to be of the same type.

I read about <a href="http://en.wikibooks.org/wiki/Haskell/Existentially_quantified_types#Example%3a_heterogeneous_lists">existentially quantified types</a> but they seemed a bit complicated and instead I decided to use the <a href="http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-Dynamic.html">Dynamic</a> interface.

Using Dynamic we can define a function to strip out the numbers like this:


~~~haskell

import Data.Dynamic
import Data.Maybe

noNums :: [Dynamic] -> [Dynamic]
noNums lat = cond [(null lat, []), 
                   (isNumber (head lat), noNums (tail lat)),
                   (otherwise, head lat : noNums (tail lat))]

justInt :: Dynamic -> Maybe Int
justInt dyn = fromDynamic dyn :: Maybe Int

isNumber :: Dynamic -> Bool
isNumber x = isJust $ justInt x
~~~

We can then call the function like this:


~~~haskell

> map toString $ noNums [toDyn (5 :: Int), toDyn "pears", toDyn (6 :: Int), toDyn "prunes", toDyn (9 :: Int), toDyn "dates"]
[Just "pears",Just "prunes",Just "dates"]
~~~


~~~haskell

toString :: Dynamic -> Maybe String
toString dyn = fromDynamic dyn
~~~

<cite>fromDynamic</cite> eventually makes a call to <cite><a href="http://www.haskell.org/ghc/docs/7.2.2/html/libraries/ghc-prim-0.2.0.0/GHC-Prim.html#v:unsafeCoerce-35-">unSafeCoerce#</a></cite>:

<blockquote>
The function unsafeCoerce# allows you to side-step the typechecker entirely. That is, it allows you to coerce any type into any other type. If you use this function, you had better get it right, otherwise segmentation faults await. It is generally used when you want to write a program that you know is well-typed, but where Haskell's type system is not expressive enough to prove that it is well typed.
</blockquote>


I wanted to try and make the 'isNumber' function handle any numeric type rather than just Ints but I haven't quite worked out how to do that. 

Obviously I'm only using Dynamic here because the exercise requires it but I'm not sure what real life situation would require its use. 

If anyone has used it before or knows a use case I'd be interested to know what it is!
