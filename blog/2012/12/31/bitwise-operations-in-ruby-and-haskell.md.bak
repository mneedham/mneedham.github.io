+++
draft = false
date="2012-12-31 13:14:42"
title="Bitwise operations in Ruby and Haskell"
tag=['ruby', 'haskell', 'bitwise']
category=['Ruby', 'Haskell']
+++

<p>Part of one of the most recent problems in the <a href="https://www.coursera.org/course/algo2">Algorithms 2</a> course required us to find the 'neighbours' of binary values.</p>


<p>In this case a neighbour is described as being any other binary value which has an equivalent value or differs in 1 or 2 bits.</p>


<p>e.g. the neighbours of  '10000' would be '00000', '00001', '00010', '00100', ''01000', '10001', '10010', '10011', '10100', '10101', '10110', '11000', '11001', '11010' and '11100'~~~

<p>I initially treated '10000' as an array of 1s and 0s and wrote a function to recursively come up with the above combinations before it was pointed out to me that it'd be much easier to use bit wise logic instead.</p>


<p>I don't remember every having to write any code using bit wise operations since university so I thought I'd document what I learnt.</p>


<p>The first thing to do is convert those binary values into a decimal equivalent which is pretty easy in Ruby:</p>



~~~ruby

> "10000".to_i(2)
=> 16
~~~

<p>In Haskell I <a href="http://pleac.sourceforge.net/pleac_haskell/numbers.html">stole a function from PLEAC</a> to do the job:</p>



~~~haskell

> import Data.Char
> (foldr (\c s -> s * 2 + c) 0 . reverse . map digitToInt) "10000"
16
~~~

<p>I initially worked out the neighbours by hand but I need to work out how to convert that into code so I ran through an example.</p>


<p>We want to get from '10000' (16) to '00000' (0) which we can do by <a href="http://www.tutorialspoint.com/ruby/ruby_operators.htm">using an XOR operation</a>:</p>


<blockquote>
Binary XOR Operator copies the bit if it is set in one operand but not both.
</blockquote>


~~~text

'10000' XOR '10000'
~~~

<p>In Ruby it would read like this:</p>



~~~ruby

> 16 ^ 16
=> 0
~~~

<p>If we do the same XOR operation but changing the other bits instead we end up with all the neighbours of distance 1:</p>



~~~ruby

> [0,1,2,4,16].map { |x| 16 ^ x }
=> [16, 17, 18, 20, 0]
~~~

<p>We can generalise the function that creates that array of values like so:</p>



~~~ruby

> bits = 5
> offsets = (0..(bits - 1)).map { |x| 2 ** x }
=> [1, 2, 4, 8, 16]
~~~

<p>or if we want to use bit shifting:</p>



~~~ruby

> offsets = (0..(bits - 1)).map { |x| 1 << x }
=> [1, 2, 4, 8, 16]
~~~

<p>With that approach we're moving the "left operands value is moved left by the number of bits specified by the right operand." i.e. we move '1' left by 0 bits (from '1'to '1'), then by 1 bit (from '1' to '10'), then by 2 bits (from '1' to '100') and so on.</p>


<p>We still need to get all the neighbours which differ by 2 bits which we can do by getting all the ways that we can combine those <cite>offsets</cite> together. The <cite>combination</cite> function and Bitwise or do the trick here:</p>



~~~ruby

> offsets.combination(2).to_a
=> [[1, 2], [1, 4], [1, 8], [1, 16], [2, 4], [2, 8], [2, 16], [4, 8], [4, 16], [8, 16]]
> offsets.combination(2).to_a.map { |a,b| a|b }
=> [3, 5, 9, 17, 6, 10, 18, 12, 20, 24]
~~~

<p>Now if we put it all together:</p>



~~~ruby

> initial_value = "10000"
=> "10000"
> bits = initial_value.length
=> 5
> value = "10000".to_i(2)
=> 16
> single_bit_offsets = (0..(bits - 1)).map { |x| 1 << x }
=> [1, 2, 4, 8, 16]
> all_the_offsets = offsets + offsets.combination(2).to_a.map { |a,b| a|b }
=> [1, 2, 4, 8, 16, 3, 5, 9, 17, 6, 10, 18, 12, 20, 24]
> all_the_offsets.map { |offset| value ^ offset }.sort 
=> [0, 1, 2, 4, 8, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28]
~~~

<p>The final Haskell version looks like this:</p>



~~~haskell

> import Data.Char
> import Data.Bits
> import Data.List

> let initialValue = "10000"
> let bits = length initialValue
> let value = (foldr (\c s -> s * 2 + c) 0 . reverse . map digitToInt) initialValue
> let singleBitOffsets = map (shiftL 1) [0..(bits - 1)] :: [Int]
> let allTheOffsets = singleBitOffsets ++ map (\(x:y:_) -> (x .|. y)) (combinationsOf 2 singleBitOffsets) :: [Int]
> Data.List.sort $ map (xor value) allTheOffsets 
[0,1,2,4,8,17,18,19,20,21,22,24,25,26,28]
~~~

<p>I took the <cite>combinationsOf</cite> function from <a href="http://www.polyomino.f2s.com/david/haskell/hs/CombinatoricsGeneration.hs.txt">David Amos' Combinatorics Generation library</a> and it reads like so:</p>



~~~haskell

-- subsets of size k
combinationsOf 0 _ = [[]]
combinationsOf _ [] = []
combinationsOf k (x:xs) = map (x:) (combinationsOf (k-1) xs) ++ combinationsOf k xs
~~~


<p>A real life version of this problem occurs in the world of genome analysis where <a href="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC16324/">scientists need to work out whether phylogenetic profiles are functionally linked</a>.</p>

