+++
draft = false
date="2015-11-14 22:51:38"
title="jq: Filtering missing keys"
tag=['jq']
category=['Software Development']
+++

<p>
I've been playing around with the <a href="http://www.meetup.com/meetup_api/docs/2/events/">meetup.com API</a> again over the last few days and having saved a set of events to disk I wanted to extract the venues using <a href="https://stedolan.github.io/jq/">jq</a>.
</p>


<p>
This is what a single event record looks like:
</p>



~~~bash

$ jq -r ".[0]" data/events/0.json
{
  "status": "past",
  "rating": {
    "count": 1,
    "average": 1
  },
  "utc_offset": 3600000,
  "event_url": "http://www.meetup.com/londonweb/events/3261890/",
  "group": {
    "who": "Web Peeps",
    "name": "London Web",
    "group_lat": 51.52000045776367,
    "created": 1034097743000,
    "join_mode": "approval",
    "group_lon": -0.12999999523162842,
    "urlname": "londonweb",
    "id": 163876
  },
  "name": "London Web Design October Meetup",
  "created": 1094756756000,
  "venue": {
    "city": "London",
    "name": "Roadhouse Live Music Restaurant , Bar & Club",
    "country": "GB",
    "lon": -0.1,
    "phone": "44-020-7240-6001",
    "address_1": "The Piazza",
    "address_2": "Covent Garden",
    "repinned": false,
    "lat": 51.52,
    "id": 11725
  },
  "updated": 1273536337000,
  "visibility": "public",
  "yes_rsvp_count": 2,
  "time": 1097776800000,
  "waitlist_count": 0,
  "headcount": 0,
  "maybe_rsvp_count": 5,
  "id": "3261890"
}
~~~

<p>
We want to extract the keys underneath 'venue'. 
I started with the following:
</p>



~~~bash

$ jq -r ".[] | .venue" data/events/0.json
...
{
  "city": "London",
  "name": "Counting House Pub",
  "country": "gb",
  "lon": -0.085022,
  "phone": "020 7283 7123",
  "address_1": "50 Cornhill Rd",
  "address_2": "EC3V 3PD",
  "repinned": false,
  "lat": 51.513407,
  "id": 835790
}
null
{
  "city": "Paris",
  "name": "Mozilla Paris",
  "country": "fr",
  "lon": 2.341002,
  "address_1": "16 Bis Boulevard Montmartre",
  "repinned": false,
  "lat": 48.871834,
  "id": 23591845
}
...
~~~

<p>
This is close to what I want but it includes 'null' values which means when you extract the keys inside 'venue' they are all empty as well:
</p>



~~~bash

jq -r ".[] | .venue | [.id, .name, .city, .address_1, .address_2, .lat, .lon] | @csv" data/events/0.json
...
101958,"The Green Man and French Horn,  -","London","54, St. Martins Lane - Covent Garden","WC2N 4EA",51.52,-0.1
,,,,,,
107295,"The Yorkshire Grey Pub","London","46 Langham Street","W1W 7AX",51.52,-0.1
...
,,,,,,
~~~

<p>
If functional programming lingo we want to filter out any JSON documents which don't have the 'venue' key. 
'filter' has a different meaning in jq so it took me a while to realise that the 'select' function was what I needed to get rid of the null values:
</p>



~~~bash

$ jq -r ".[] | select(.venue != null) | .venue | [.id, .name, .city, .address_1, .address_2, .lat, .lon] | @csv" data/events/0.json | head
11725,"Roadhouse Live Music Restaurant , Bar & Club","London","The Piazza","Covent Garden",51.52,-0.1
11725,"Roadhouse Live Music Restaurant , Bar & Club","London","The Piazza","Covent Garden",51.52,-0.1
11725,"Roadhouse Live Music Restaurant , Bar & Club","London","The Piazza","Covent Garden",51.52,-0.1
11725,"Roadhouse Live Music Restaurant , Bar & Club","London","The Piazza","Covent Garden",51.52,-0.1
76192,"Pied Bull Court","London","Galen Place, London, WC1A 2JR",,51.516747,-0.12719
76192,"Pied Bull Court","London","Galen Place, London, WC1A 2JR",,51.516747,-0.12719
85217,"Earl's Court Exhibition Centre","London","Warwick Road","SW5 9TA",51.49233,-0.199735
96579,"Olympia 2","London","Near Olympia tube station",,51.52,-0.1
76192,"Pied Bull Court","London","Galen Place, London, WC1A 2JR",,51.516747,-0.12719
101958,"The Green Man and French Horn,  -","London","54, St. Martins Lane - Covent Garden","WC2N 4EA",51.52,-0.1
~~~

<p>
And we're done.
</p>

