+++
draft = false
date="2012-12-30 23:16:48"
title="Haskell: Using qualified imports to avoid polluting the namespace"
tag=['haskell']
category=['Haskell']
+++

<p>In most of the Haskell code I've read any functions from other modules have been imported directly into the namespace and I reached the stage where I had this list of imports in a file:</p>



~~~haskell

import System.IO
import Data.List.Split
import Data.Char
import Data.Bits
import Control.Monad 
import Data.Map 
import Data.Set 
import Data.List 
import Data.Maybe 
~~~

<p>This becomes a problem when you want to use a function which is defined in multiple modules such as <cite>filter</cite>:</p>



~~~text

clustering.hs:53:43:
    Ambiguous occurrence `filter'
    It could refer to either `Data.List.filter',
                             imported from `Data.List' at clustering.hs:11:1-16
                             (and originally defined in `GHC.List')
                          or `Data.Set.filter',
                             imported from `Data.Set' at clustering.hs:10:1-16
                          or `Data.Map.filter',
                             imported from `Data.Map' at clustering.hs:9:1-16
~~~

<p>One way to solve this is to change occurrences of <cite>filter</cite> to <cite>Data.List.filter</cite> but it's a bit long winded and in this case there is a function in the <cite>Prelude</cite> package which is available without us importing anything.</p>


<p>Unfortunately we'd have to use the prefix <cite>Prelude</cite> to refer to it since all the other versions of the function have made it ambiguous.</p>


<p>We still want to use some of the functions in those other modules though so we can do a qualified import which will make the functions available to us but only if we refer to them by their full name. It won't import them into our namespace.</p>


<p>For example to initialise a map we'd do this:</p>



~~~haskell

> import qualified Data.Map
> Data.Map.assocs $ Data.Map.fromList [(1,2), (3,7)]
[(1,2),(3,7)]
~~~

<p>That's a bit long winded though so we can rename imports with a shorter name to make our life a bit easier:</p>



~~~haskell

import System.IO
import Data.List.Split
import Data.Char
import Data.Bits
import qualified Control.Monad as Monad
import qualified Data.Map as Map
import qualified Data.Set as Set
import qualified Data.List as List
import qualified Data.Maybe as Maybe
~~~

<p>We can then use functions in those packages like so:</p>



~~~haskell

> Maybe.maybeToList (Just 3)
[3]
~~~

<p>For this particular function I haven't come across any with the same name so we might want to import that one into our namespace but require the use of the <cite>Maybe</cite> prefix for any other functions:</p>



~~~haskell

import qualified Data.Maybe as Maybe
import Data.Maybe (maybeToList)
~~~


~~~haskell

> maybeToList (Just 3)
[3]
~~~

<p>There's a wiki entry I came across which <a href="http://en.wikibooks.org/wiki/Haskell/Modules#Renaming_imports">explains Haskell modules this in a bit more detail</a> and is worth a read.</p>

