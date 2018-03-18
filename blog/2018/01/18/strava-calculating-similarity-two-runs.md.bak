+++
draft = false
date="2018-01-18 23:35:25"
title="Strava: Calculating the similarity of two runs"
tag=['python', 'strava', 'running', 'strava-api', 'dtw', 'dynamic-time-warping', 'google-encoded-polyline-algorithm-format']
category=['Software Development']
description="Learn how to compare runs from the Strava API using the Dynamic Time Warping algorithm."
+++

<p>
I go running several times a week and wanted to compare my runs against each other to see how similar they are.
</p>


<p>
I record my runs with the <a href="https://www.strava.com/">Strava</a> app and it has an <a href="https://strava.github.io/api">API</a> that returns lat/long coordinates for each run in the <a href="https://strava.github.io/api/#polylines">Google encoded polyline algorithm format</a>.
</p>


<p>
We can use the <a href="https://pypi.python.org/pypi/polyline/">polyline</a> library to decode these values into a list of lat/long tuples. For example:
</p>



~~~python

import polyline
polyline.decode('u{~vFvyys@fS]')
[(40.63179, -8.65708), (40.62855, -8.65693)]
~~~

<p>
Once we've got the route defined as a set of coordinates we need to compare them. My Googling led me to an algorithm called <a href="https://en.wikipedia.org/wiki/Dynamic_time_warping">Dynamic Time Warping</a>
</p>


<blockquote>
DTW is a method that calculates an optimal match between two given sequences (e.g. time series) with certain restrictions. 

The sequences are "warped" non-linearly in the time dimension to determine a measure of their similarity independent of certain non-linear variations in the time dimension.
</blockquote>

<p>
The <a href="https://pypi.python.org/pypi/fastdtw">fastdtw</a> library implements an approximation of this library and returns a value indicating the distance between sets of points.
</p>


<p> 
We can see how to apply fastdtw and polyline against Strava data in the following example:
</p>



~~~python

import os
import polyline
import requests
from fastdtw import fastdtw

token = os.environ["TOKEN"]
headers = {'Authorization': "Bearer {0}".format(token)}

def find_points(activity_id):
    r = requests.get("https://www.strava.com/api/v3/activities/{0}".format(activity_id), headers=headers)
    response = r.json()
    line = response["map"]["polyline"]
    return polyline.decode(line)
~~~

<p>
Now let's try it out on two runs, <a href="https://www.strava.com/activities/1361109741">1361109741</a> and <a href="https://www.strava.com/activities/1346460542">1346460542</a>:
</p>



~~~python

from scipy.spatial.distance import euclidean

activity1_id = 1361109741
activity2_id = 1346460542

distance, path = fastdtw(find_points(activity1_id), find_points(activity2_id), dist=euclidean)

>>> print(distance)
2.91985018100644
~~~

<p>
These two runs are both near my house so the value is small. Let's change the second route to be <a href="https://www.strava.com/activities/1246017379">from my trip to New York</a>:
</p>



~~~python

activity1_id = 1361109741
activity2_id = 1246017379

distance, path = fastdtw(find_points(activity1_id), find_points(activity2_id), dist=euclidean)

>>> print(distance)
29383.492965394034
~~~

<p>
Much bigger!
</p>


<p>I'm not really interested in the actual value returned but I am interested in the relative values. I'm building a little application to generate routes that I should run and I want it to come up with a routes that are different to recent ones that I've run. This score can now form part of the criteria.
</p>

