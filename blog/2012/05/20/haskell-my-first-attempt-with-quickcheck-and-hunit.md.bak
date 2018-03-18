+++
draft = false
date="2012-05-20 19:09:52"
title="Haskell: My first attempt with QuickCheck and HUnit"
tag=['haskell']
category=['Haskell']
+++

As I <a href="http://www.markhneedham.com/blog/2012/05/16/haskell-writing-a-custom-equality-operator/">mentioned in a blog post a few days</a> I've started learning QuickCheck with the <a href="http://batterseapower.github.com/test-framework/">test-framework</a> package as suggested by David Turner.

I first needed to install test-framework and some dependencies using <cite><a href="http://www.haskell.org/cabal/">cabal</a></cite>:


~~~haskell

> cabal install test-framework
> cabal install test-framework-quickcheck
> cabal install test-framework-hunit
~~~

I thought it'd be interesting to try and write some tests around the <a href="http://www.markhneedham.com/blog/2012/02/28/haskell-creating-a-sliding-window-over-a-collection/">windowed function that I wrote a few months ago</a>:

<cite>Windowed.hs</cite>

~~~haskell

module Windowed (windowed) where

windowed :: Int -> [a] -> [[a]]
windowed size [] = []
windowed size ls@(x:xs) = 
  if length ls >= size then (take size ls) : windowed size xs 
  else windowed size x
~~~

I wrote my first property like so:


~~~haskell

import Windowed

import Test.Framework (defaultMain, testGroup)
import Test.Framework.Providers.QuickCheck (testProperty)
import Test.QuickCheck

main = defaultMain tests

tests = [
  testGroup "windowed" [
    testProperty "should not window if n is bigger than list size" prop_nothing_if_n_too_large
  ]
] 
						  	
prop_nothing_if_n_too_large n xs = n > length xs ==>  windowed n xs == []
~~~

And tried to compile the file:


~~~text

ghc -package test-framework -package test-framework-quickcheck -threaded WindowedQC.hs -o Windowed
~~~

Which resulted in this compilation error:


~~~text

WindowedQC.hs:16:17:
    No instance for (QuickCheck-1.2.0.1:Test.QuickCheck.Testable
                       (Gen Prop))
      arising from a use of `testProperty'
    Possible fix:
      add an instance declaration for
      (QuickCheck-1.2.0.1:Test.QuickCheck.Testable (Gen Prop))
~~~

According to the <a href="http://batterseapower.github.com/test-framework/">test-framework home page</a> this error happens when we have more than one version of QuickCheck installed so we need to tell 'ghc' which one to use: 


~~~text

ghc -package test-framework -package test-framework-quickcheck -package QuickCheck-1.2.0.1 -threaded WindowedQC.hs -o Windowed
~~~

That solved the first compilation problem but I still had another:


~~~text

WindowedQC.hs:16:17:
    Ambiguous type variable `a0' in the constraints:
      (Arbitrary a0) arising from a use of `testProperty'
                     at WindowedQC.hs:12:17-28
      (Show a0) arising from a use of `testProperty'
                at WindowedQC.hs:12:17-28
      (Eq a0) arising from a use of `prop_nothing_if_n_too_large'
              at WindowedQC.hs:12:80-106
    Probable fix: add a type signature that fixes these type variable(s)
~~~

The way to solve this problem is to <a href="https://raw.github.com/batterseapower/test-framework/master/example/Test/Framework/Example.lhs">explicitly state which types will be passed to the property</a> like so:


~~~haskell

prop_nothing_if_n_too_large n xs = n > length xs ==>  windowed n xs == []
    where types = (xs :: [Int], n :: Int)
~~~

I eventually ended up with the following:

<cite>WindowedQC.hs</cite>

~~~haskell

import Windowed

import Test.Framework (defaultMain, testGroup)
import Test.Framework.Providers.QuickCheck (testProperty)
import Test.QuickCheck

import Test.Framework.Providers.HUnit
import Test.HUnit

main = defaultMain tests

tests = [
  testGroup "windowed" [
    testProperty "should not window if n is bigger than list size" prop_nothing_if_n_too_large,
    testProperty "should create sub arrays the size of window" prop_size_of_sub_arrays_is_n,
    testProperty "should group adjacent items into windows" prop_groups_adjacent_items,                
    testCase "should window a simple list" test_should_window_simple_list
  ]
] 

prop_groups_adjacent_items n xs = n < length xs ==>  
                                  not (null xs) ==>
                                  n > 0 ==> (last $  last $ windowed n xs) == last xs
  where types = (xs :: [Int], n :: Int)			
				  	
prop_nothing_if_n_too_large n xs = n > length xs ==>  windowed n xs == []
  where types = (xs :: [Int], n :: Int)

prop_size_of_sub_arrays_is_n n xs =  n > 0 ==> all (\subArray -> length subArray == n)  (windowed n xs)  
  where types = (xs :: [Int], n :: Int)
	
test_should_window_simple_list = 
  windowed 2 [1..10] @?= [[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9], [9,10]]
~~~

I initially only wrote QuickCheck properties but I wasn't satisfied that just passing the properties I've written would guarantee the function is working as expected.

The first property does a simple check that the last item from the windowed function is the same as the last item in the list assuming that the list isn't empty, that we're using a positive n value and our window size is smaller than the list size. 

The second checks that we end up with an empty list if we try to window to a size bigger than the list and the third checks that each of the sub arrays is the correct size.

I wasn't sure how to write a QuickCheck property that would test the values of the individual sub arrays so I ended up writing a <a href="http://hunit.sourceforge.net/">HUnit</a> test instead. 

If you know how I could achieve the same thing using QuickCheck please let me know.

We can then run all the tests like so:


~~~text

> ./Windowed                                                                                                                    
windowed:

  should not window if n is bigger than list size: [OK, passed 100 tests]

  should create sub arrays the size of window: [OK, passed 100 tests]

  should group adjacent items into windows: [OK, passed 100 tests]

  should window a simple list: [OK]

          Properties  Test Cases  Total      
  Passed  3           1           4          
  Failed  0           0           0   
~~~
