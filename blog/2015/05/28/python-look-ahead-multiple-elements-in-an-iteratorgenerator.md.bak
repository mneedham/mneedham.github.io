+++
draft = false
date="2015-05-28 20:56:08"
title="Python: Look ahead multiple elements in an iterator/generator"
tag=['python']
category=['Python']
+++

<p>
As part of the BBC live text scraping code I've been working on I needed to take an iterator of raw events created by a generator and transform this into an iterator of cards shown in a match.
</p>


<p>
The structure of the raw events I'm interested in is as follows:
</p>


<ul>
<li>Line 1: Player booked</li>
<li>Line 2: Player fouled</li>
<li>Line 3: Information about the foul</li>
</ul>

<p>
e.g.
</p>



~~~text

events = [
  {'event': u'Booking     Pedro (Barcelona) is shown the yellow card for a bad foul.', 'sortable_time': 5083, 'match_id': '32683310', 'formatted_time': u'84:43'}, 
  {'event': u'Rafinha (FC Bayern M\xfcnchen) wins a free kick on the right wing.', 'sortable_time': 5078, 'match_id': '32683310', 'formatted_time': u'84:38'}, 
  {'event': u'Foul by Pedro (Barcelona).', 'sortable_time': 5078, 'match_id': '32683310', 'formatted_time': u'84:38'}
]
~~~

<p>
We want to take these 3 raw events and create one 'booking event'. We therefore need to have access to all 3 lines at the same time.
</p>


<p>
I started with the following function:
</p>



~~~python

def cards(events):
    events = iter(events)

    item = events.next()
    next = events.next()
    event_id = 0

    for next_next in events:
        event = item["event"]
        booking = re.findall("Booking.*", event)
        if booking:
            player = re.findall("Booking([^(]*)", event)[0].strip()
            team = re.findall("Booking([^(]*) \((.*)\)", event)[0][1]

            associated_foul = [x for x in [(next, event_id+1), (next_next, event_id+2)]
                                 if re.findall("Foul by.*", x[0]["event"])]

            if associated_foul:
                associated_foul = associated_foul[0]
                yield event_id, associated_foul[1], player, team, item, "yellow"
            else:
                yield event_id, "", player, team, item, "yellow"

        item = next
        next = next_next
        event_id += 1
~~~

<p>If we run the sample events through it we'd see this output:
</p>



~~~python

>>> for card_id, associated_foul, player, team, item, card_type in cards(iter(events)):
      print card_id, associated_foul, player, team, item, card_type
  
0 2 Pedro Barcelona {'match_id': '32683310', 'event': u'Booking     Pedro (Barcelona) is shown the yellow card for a bad foul.', 'formatted_time': u'84:43', 'sortable_time': 5083} yellow
~~~


<p>In retrospect, it's a bit of a hacky way of moving a window of 3 items over the iterator of raw events and yielding a 'booking' event if the regex matches.</p>


<p>
I thought there was probably a better way of doing this using <a href="https://docs.python.org/2/library/itertools.html">itertools</a> and <a href="http://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator-in-python">indeed there is</a>!
</p>


<p>First we need to create a window function which will return us an iterator of tuples containing consecutive events:</p>



~~~python

from itertools import tee, izip

def window(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)
~~~

<p>Now let's have a look at how it works using a simple example:</p>



~~~python

>>> numbers = iter(range(0,10))
>>> for triple in window(numbers, 3):
      print triple

(0, 1, 2)
(1, 2, 3)
(2, 3, 4)
(3, 4, 5)
(4, 5, 6)
(5, 6, 7)
(6, 7, 8)
(7, 8, 9)
~~~

<p>Exactly what we need. Now let's plug the windows function into our cards function:</p>



~~~python

def cards(events):
    events = iter(events)
    for event_id, triple in enumerate(window(events, 3)):
        item = triple[0]
        event = triple[0]["event"]

        booking = re.findall("Booking.*", event)
        if booking:
            player = re.findall("Booking([^(]*)", event)[0].strip()
            team = re.findall("Booking([^(]*) \((.*)\)", event)[0][1]

            associated_foul = [x for x in [(triple[1], event_id+1), (triple[2], event_id+2)]
                                 if re.findall("Foul by.*", x[0]["event"])]

            if associated_foul:
                associated_foul = associated_foul[0]
                yield event_id, associated_foul[1], player, team, item, "yellow"
            else:
                yield event_id, "", player, team, item, "yellow"
~~~

<p>
And finally check it still processes events correctly:
</p>



~~~python

>>> for card_id, associated_foul, player, team, item, card_type in cards(iter(events)):
      print card_id, associated_foul, player, team, item, card_type

0 2 Pedro Barcelona {'match_id': '32683310', 'event': u'Booking     Pedro (Barcelona) is shown the yellow card for a bad foul.', 'formatted_time': u'84:43', 'sortable_time': 5083} yellow
~~~
