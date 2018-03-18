+++
draft = false
date="2015-05-23 10:14:38"
title="Python: Refactoring to iterator"
tag=['python']
category=['Python']
+++

<p>Over the last week I've been building a set of scripts to scrape the events from the <a href="http://www.bbc.co.uk/sport/0/football/32683310">Bayern Munich/Barcelona game</a> and I've ended up with a few hundred lines of nested for statements, if statements and mutated lists. I thought it was about time I did a bit of refactoring.
</p>


<p>The following is a function which takes in a match file and spits out a collection of maps containing times & events.</p>



~~~python

import bs4
import re
from bs4 import BeautifulSoup
from soupselect import select

def extract_events(file):
    match = open(file, 'r')
    soup = BeautifulSoup(match.read())

    all_events = []
    for event in select(soup, 'div#live-text-commentary-wrapper div#live-text'):
        for child in event.children:
            if type(child) is bs4.element.Tag:
                all_events.append(child.getText().strip())

    for event in select(soup, 'div#live-text-commentary-wrapper div#more-live-text'):
        for child in event.children:
            if type(child) is bs4.element.Tag:
                all_events.append(child.getText().strip())

    timed_events = []
    for i in range(0, len(all_events)):
        event = all_events[i]
        time =  re.findall("\d{1,2}:\d{2}", event)
        formatted_time = " +".join(time)
        if time:
            timed_events.append({'time': formatted_time, 'event': all_events[i+1]})
    return timed_events
~~~

<p>
We call it like this:
</p>



~~~python

match_id = "32683310"
for event in extract_events("data/%s" % (match_id))[:10]:
    print event
~~~

<p>
The file we're loading is the <a href="http://www.bbc.co.uk/sport/0/football/32683310">Bayern Munich vs Barcelona match</a> HTML file which I have saved locally. After we've got that read into beautiful soup we locate the two divs on the page which contain the match events.
</p>


<p>
We then iterate over that list and create a new list containing (time, event) pairs which we return.
</p>


<p>
I think we should be able to get to our resulting collection without persisting an intermediate list, but first things first - let's remove the duplicated for loops:
</p>



~~~python

def extract_events(file):
    match = open(file, 'r')
    soup = BeautifulSoup(match.read())

    all_events = []
    events = select(soup, 'div#live-text-commentary-wrapper div#live-text')
    more_events = select(soup, 'div#live-text-commentary-wrapper div#more-live-text')

    for event in events + more_events:
        for child in event.children:
            if type(child) is bs4.element.Tag:
                all_events.append(child.getText().strip())

    timed_events = []
    for i in range(0, len(all_events)):
        event = all_events[i]
        time =  re.findall("\d{1,2}:\d{2}", event)
        formatted_time = " +".join(time)
        if time:
            timed_events.append({'time': formatted_time, 'event': all_events[i+1]})
    return timed_events
~~~

<p>The next step is to refactor towards using an iterator. After <a href="http://anandology.com/python-practice-book/iterators.html#generators">a bit of reading</a> I realised a generator would make life even easier.
</p>


<p>
I created a function which returned an iterator of the raw events and plugged that into the original function:
</p>



~~~python

def raw_events(file):
    match = open(file, 'r')
    soup = BeautifulSoup(match.read())
    events = select(soup, 'div#live-text-commentary-wrapper div#live-text')
    more_events = select(soup, 'div#live-text-commentary-wrapper div#more-live-text')
    for event in events + more_events:
        for child in event.children:
            if type(child) is bs4.element.Tag:
                yield child.getText().strip()

def extract_events(file):
    all_events = list(raw_events(file))

    timed_events = []
    for i in range(0, len(all_events)):
        event = all_events[i]
        time =  re.findall("\d{1,2}:\d{2}", event)
        formatted_time = " +".join(time)
        if time:
            timed_events.append({'time': formatted_time, 'event': all_events[i+1]})
    return timed_events
~~~

<p>If we run that function we still get the same output as before which is good. Now we need to work out how to clean up the second bit of the code which groups the appropriate rows together. 
</p>


<p>
The goal is that 'extract_events' returns an iterator rather than a list - we need to figure out how to iterate over the output of 'raw_events' in such a way that when we find a 'time row' we can yield that and the row immediately after.
</p>


<p>
Luckily I found <a href="http://stackoverflow.com/questions/16789776/iterating-over-two-values-of-a-list-at-a-time-in-python">a Stack Overflow post</a> explaining that you can use the 'next' function inside an iterator to achieve this:
</p>



~~~python

def extract_events(file):
    events = raw_events(file)
    for event in events:
        time =  re.findall("\d{1,2}:\d{2}", event)
        formatted_time = " +".join(time)
        if time:
            yield {'time': formatted_time, 'event': next(events)}
~~~

<p>
It's not that much less code than the original function but I think it's an improvement. Any thoughts/tips to simplify it further are always welcome.
</p>

