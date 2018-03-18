+++
draft = false
date="2013-01-02 00:16:50"
title="Haskell: Reading files"
tag=['haskell']
category=['Haskell']
+++

<p>In writing the <a href="https://github.com/mneedham/algorithms2/blob/master/clustering.hs">clustering algorithm</a> which I've mentioned way too many times already I needed to process a text file which contained all the points and my initial approach looked like this:</p>



~~~haskell

import System.IO

main = do    
    withFile "clustering2.txt" ReadMode (\handle -> do  
        contents <- hGetContents handle   
        putStrLn contents) 
~~~

<p>It felt a bit clunky but I didn't realise there was an easier way until I came across <a href="http://stackoverflow.com/questions/7867723/haskell-file-reading">this thread</a>. We can simplify reading a file to the following by using the <cite><a href="http://zvon.org/other/haskell/Outputprelude/readFile_f.html">readFile</a></cite> function:</p>



~~~haskell

main = do    
    contents <- readFile "clustering2.txt" 
    putStrLn contents 
~~~


<p>We need to read the file in the IO monad which explains why we have the 'do' notation on the first line.</p>


<p>Another thing I <a href="http://www.haskell.org/ghc/docs/7.2.2/html/users_guide/interactive-evaluation.html">didn't realise until recently</a> was that you don't actually need to worry about the 'do' notation if you try to read from the IO monad inside GHCI.</p>


<p>In this context we're reading from the IO monad when we bind 'readFile' to the variable 'contents' since 'readFile' returns type 'IO String':</p>



~~~text

> :t readFile
readFile :: FilePath -> IO String
~~~

<p>We can therefore play around with the code pretty easily:</p>



~~~haskell

> contents <- readFile "clustering2.txt"
> let (bits, nodes) = process contents 
> bits
24
> length nodes
19981
> take 10 nodes
[379,1669,5749,6927,7420,9030,9188,9667,11878,12169]
~~~

<p>I think we're able to do this because by being in GHCI we're already in the context of the IO monad but I'm happy to be corrected if I haven't explained that correctly.</p>

