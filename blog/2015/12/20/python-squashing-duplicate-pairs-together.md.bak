+++
draft = false
date="2015-12-20 12:12:46"
title="Python: Squashing 'duplicate' pairs together"
tag=['python']
category=['Python']
+++

<p>
As part of a data cleaning pipeline I had pairs of ids of duplicate addresses that I wanted to group together.</p>
 

<p>I couldn't work out how to solve the problem immediately so I simplified the problem into pairs of letters i.e.
</p>



~~~text

A	B		(A is the same as B)
B	C		(B is the same as C)
C	D		...
E	F		(E is the same as F)
F	G		...
~~~

<p>
The output that I want to get is:
</p>



~~~text

(A, B, C, D)
(E, F, G)
~~~

<p>
I spent several hours trying to come up with a clever data structure to do this until <a href="https://reshmeeauckloo.wordpress.com/">Reshmee</a> suggested tracking the sets of duplicates using an array of arrays or list of lists since we're going to script this using Python.
</p>


<p>
The actual data is in a CSV file but we'll create a list of tuples to save ourselves some work:
</p>



~~~python

pairs = [ ("A", "B"), ("B", "C"), ("C", "D"), ("E", "F"), ("F", "G") ]
~~~

<p>
We're going to iterate through the list of pairs and on each iteration we'll check if there's an entry in the list containing either of the values. There can be three outcomes from this check:
</p>


<ol>
	<li>No entry - we'll add a new entry with our pair of values.</li>
	<li>One entry - we'll add the other value to that entry.</li>
	<li>Two entries - we'll merge them together replacing the existing entry.</li>
</ol>

<p>
The first step is to write a function to check the list of lists for a matching pair:
</p>



~~~python

def find_matching_index(pair, dups):
    return [index
            for index, dup in enumerate(dups)
            if pair[0] in dup or pair[1] in dup]

print find_matching_index(("A", "B"), [set(["D", "E"])])
[]

print find_matching_index(("B", "C"), [set(["A", "B"])])
[0]

print find_matching_index(("B", "C"), [set(["A", "B"]), set(["C", "D"])])
[0, 1]
~~~

<p>Next we need to write a function which iterates over all our pairs of values and uses <cite>find_matching_index</cite> to work out which decision to make:</p>




~~~python

def extract_groups(items):
    dups = []
    for pair in items:
        matching_index = find_matching_index(pair, dups)

        if len(matching_index) == 0:
            dups.append(set([pair[0], pair[1]]))
        elif len(matching_index) == 1:
            index = matching_index[0]
            matching_dup = dups[index]
            dups.pop(index)
            dups.append(matching_dup.union([pair[0], pair[1]]))
        else:
            index1, index2 = matching_index
            dup1 = dups[index1]
            dup2 = dups[index2]

            dups.pop(index1)
            dups.pop(index2 - 1) # the index decrements since we removed one entry on the previous line
            dups.append(dup1.union(dup2))
    return dups
~~~

<p>
Now let's run this with a few test cases:
</p>



~~~python

test_cases = [
    [ ("A", "B"), ("B", "C"), ("C", "D"), ("E", "F"), ("F", "G") ],
    [ ("A", "B"), ("B", "C"), ("C", "D"), ("E", "F"), ("F", "G"), ("G", "A"), ("G", "Z"), ("B", "D") ],
    [ ("A", "B"), ("B", "C"), ("C", "E"), ("E", "A") ],
    [ ("A", "B"), ("C", "D"), ("F", "G"), ("H", "I"), ("J", "A") ]
]

for test_case in test_cases:
    print extract_groups(test_case)

[set(['A', 'C', 'B', 'D']), set(['E', 'G', 'F'])]
[set(['A', 'C', 'B', 'E', 'D', 'G', 'F', 'Z'])]
[set(['A', 'C', 'B', 'E'])]
[set(['C', 'D']), set(['G', 'F']), set(['I', 'H']), set(['A', 'J', 'B'])]
~~~

<p>This certainly doesn't scale very well but since I only have a few hundred duplicate addresses it does the job for me.</p>
 

<p>It feels like there should be a more functional way to write these functions without mutating all these lists but I haven't figured out what that is yet.</p>

