+++
draft = false
date="2013-01-07 00:47:34"
title="Knapsack Problem: Python vs Ruby"
tag=['ruby', 'python', 'knapsack']
category=['Algorithms']
+++

<p>The latest algorithm that we had to code in <a href="https://www.coursera.org/course/algo2">Algorithms 2</a> was the <a href="http://en.wikipedia.org/wiki/Knapsack_problem">Knapsack problem</a> which is as follows:</p>


<blockquote>
The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. 
</blockquote>

<p>We did a slight variation on this in that you could only pick each item once, which is known as the 0-1 knapsack problem.</p>


<p>In our case we were given an input file from which you could derive the size of the knapsack, the total number of items and the individual weights & values of each one.</p>


<p>The pseudocode of the version of the algorithm which uses a 2D array as part of a dynamic programming solution is as follows:</p>


<ul>
<li>Let <cite>A</cite> = 2-D array of size <cite>n</cite> (number of items) * <cite>W</cite> (size of the knapsack)</li>
<li>Initialise <cite>A[0,X] = 0</cite> for <cite>X=0,1,..,W</cite></li>
<li>
	for i=1,2,3,…n
	<ul>
		<li>for x=0,1,2,...,w
			<ul>
				<li>A[i,x] = max { A[i-1, x], A[x-1, x-w<sub>i</sub>] + V<sub>i</sub> }</li>
				<li>where V<sub>i</sub> is the value of the i<sup>th</sup> element and W<sub>i</sub> is the weight of the i<sup>th</sup> element</li>
			</ul>
		</li>
	</ul>
</li>
<li>return A[n, W]</li>
</ul>

<p>This version runs in O(nW) time and O(nW) space. This is the main body of <a href="https://github.com/mneedham/algorithms2/blob/master/knapsack/knapsack.rb">my Ruby solution</a> for that:</p>



~~~ruby

number_of_items,knapsack_size = # calculated from file

cache = [].tap { |m| (number_of_items+1).times { m << Array.new(knapsack_size+1) } }
cache[0].each_with_index { |value, weight| cache[0][weight] = 0  }

(1..number_of_items).each do |i|
  value, weight = rows[i-1]
  (0..knapsack_size).each do |x|
    if weight > x
      cache[i][x] = cache[i-1][x] 
    else
      cache[i][x] = [cache[i-1][x], cache[i-1][x-weight] + value].max
    end
  end
end

p cache[number_of_items][knapsack_size]
~~~

<p>This approach works reasonably well when <cite>n</cite> and <cite>W</cite> are small but in the second part of the problem <cite>n</cite> was 500 and <cite>W</cite> was 2,000,000 which means the 2D array would contain 1 billion entries.</p>


<p>If we're storing integers of 4 bytes each in that data structure then the <a href="https://www.google.co.uk/search?q=4+bytes+*+1+billion&oq=4+bytes+*+1+billion&aqs=chrome.0.57j0j62l3.3716&sugexp=chrome,mod=0&sourceid=chrome&ie=UTF-8">amount of memory required is 3.72GB</a> - slightly too much for my machine to handle!</p>


<p>Instead a better data structure would be one where we don't have to allocate everything up front but can just fill it in as we go. In this case we can still use an array for the number of items but instead of storing another array in each slot we'll use a dictionary/hash map instead.</p>


<p>If we take a bottom up approach to this problem it seems like we end up solving a lot of sub problems which aren't relevant to our final solution so I decided to try a top down recursive approach and this is what I ended up with:</p>



~~~ruby

@new_cache = [].tap { |m| (@number_of_items+1).times { m << {} } }

def knapsack_cached(rows, knapsack_size, index)
  return 0 if knapsack_size == 0 || index == 0
  value, weight = rows[index]
  if weight > knapsack_size
    stored_value = @new_cache[index-1][knapsack_size]
            
    return stored_value unless stored_value.nil?  
    return @new_cache[index-1][knapsack_size] = knapsack_cached(rows, knapsack_size, index-1)
  else
    stored_value = @new_cache[index-1][knapsack_size]
    return stored_value unless stored_value.nil?

    option_1  = knapsack_cached(rows, knapsack_size, index-1)
    option_2  = value + knapsack_cached(rows, knapsack_size - weight, index-1)
    return @new_cache[index-1][knapsack_size] = [option_1, option_2].max
  end
end

p knapsack_cached(rows, @knapsack_size, @number_of_items-1)
~~~

<p>The code is pretty similar to the previous version except we're starting from the last item and working our way inwards. We end up storing 2,549,110 items in <cite>@new_array</cite> which we can work out by running this:</p>



~~~ruby

p @new_cache.inject(0) { |acc,x| acc + x.length}
~~~

<p>If we'd used the 2D array that would mean we'd only populated 0.25% of the data structure, truly wasteful!</p>


<p>I wanted to do a little bit of profiling on how fast this algorithm ran in Ruby compared to JRuby and I also recently came across <a href="http://www.martiansoftware.com/nailgun/">nailgun</a> - which allows you to <a href="http://www.tamingthemindmonkey.com/2012/10/15/jruby-faster-feedback-cycle-using-nailgun">start up a persistent JVM and then run your code via that</a> instead of starting a new one up each time - so I thought I could play around with that as well!~~~


~~~ruby

# Ruby
$ time ruby knapsack/knapsack_rec.rb
real	0m18.889s user	0m18.613s sys	0m0.138s

# JRuby
$ time ruby knapsack/knapsack_rec.rb
real	0m6.380s user	0m10.862s sys	0m0.428s

# JRuby with nailgun
$ ruby --ng-server & # start up the nailgun server

$ time ruby --ng knapsack/knapsack_rec.rb
real	0m6.734s user	0m0.023s sys	0m0.021s

$ time ruby --ng knapsack/knapsack_rec.rb
real	0m5.213s user	0m0.022s sys	0m0.021s
~~~

<p>The first run is a bit slow as the JVM gets launched but after that we get a marginal improvement. I thought the JVM startup time would be a bigger proportion of the running time but I guess not!</p>


<p>I thought I'd try it out in Python as well because on one of the previous problems <a href="https://twitter.com/isaiah_p">Isaiah</a> had been able to write much faster versions in Python so I wanted to see if that'd be the case here too.</p>


<p>This was the <a href="https://github.com/mneedham/algorithms2/blob/master/knapsack/knapsack.py">python solution</a>:</p>



~~~python

def knapsack_cached(rows, knapsack_size, index):
    global cache
    if(index is 0 or knapsack_size is 0):
        return 0
    else:
        value, weight = rows[index]
        if(weight > knapsack_size and knapsack_size not in cache[index-1]):
            cache[index-1][knapsack_size] = knapsack_cached(rows, knapsack_size, index-1)                
        else:
            if(knapsack_size not in cache[index-1]):
                option_1  = knapsack_cached(rows, knapsack_size, index-1)
                option_2  = value + knapsack_cached(rows, knapsack_size - weight, index-1)
                cache[index-1][knapsack_size] = max(option_1, option_2)                
            
        return cache[index-1][knapsack_size]

knapsack_size, number_of_items, rows = # worked out from the file

result = knapsack_cached(rows, knapsack_size, number_of_items-1)    
print(result)
~~~

<p>The code is pretty much exactly the same as the Ruby version but interestingly it seems to run more quickly:</p>



~~~python

$ time python knapsack/knapsack.py 
real	0m4.568s user	0m4.480s sys	0m0.078s
~~~

<p>I have no idea why that would be the case but it has been for all the algorithms we've written so far. If anyone has any ideas I'd be intrigued to hear them!</p>

