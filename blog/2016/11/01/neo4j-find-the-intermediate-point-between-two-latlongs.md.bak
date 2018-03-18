+++
draft = false
date="2016-11-01 22:10:57"
title="Neo4j: Find the intermediate point between two lat/longs"
tag=['neo4j']
category=['neo4j']
+++

<p>Yesterday I wrote a blog post showing how to find the midpoint between two lat/longs using Cypher which worked well as a first attempt at filling in missing locations, but I realised I could do better.
</p>


<p>
As I mentioned in the last post, when I find a stop that's missing lat/long coordinates I can usually find two nearby stops that allow me to triangulate this stop's location.</p>


<p>I also have train routes which indicate the number of seconds it takes to go from one stop to another, which allows me to indicate whether the location-less stop is closer to one stop than the other.
</p>


<p>
For example, consider stops a, b, and c where b doesn't have a location. If we have these distances between the stops:
</p>



~~~text

(a)-[:NEXT {time: 60}]->(b)-[:NEXT {time: 240}]->(c)
~~~

<p>it tells us that point 'b' is actually 0.2 of the distance from 'a' to 'c' rather than being the midpoint.</p>


<p>
There's <a href="http://www.movable-type.co.uk/scripts/latlong.html#intermediate-point">a formula</a> we can use to work out that point:
</p>



~~~text

a = sin((1−f)⋅δ) / sin δ
b = sin(f⋅δ) / sin δ
x = a ⋅ cos φ1 ⋅ cos λ1 + b ⋅ cos φ2 ⋅ cos λ2
y = a ⋅ cos φ1 ⋅ sin λ1 + b ⋅ cos φ2 ⋅ sin λ2
z = a ⋅ sin φ1 + b ⋅ sin φ2
φi = atan2(z, √x² + y²)
λi = atan2(y, x)

δ is the angular distance d/R between the two points.
φ = latitude
λ = longitude
~~~

<p>Translated to Cypher (with mandatory Greek symbols) it reads like this to find the point 0.2 of the way from one point to another<p>


~~~cypher

with {latitude: 51.4931963543, longitude: -0.0475185810} AS p1, 
     {latitude: 51.47908, longitude: -0.05393950 } AS p2

WITH p1, p2, distance(point(p1), point(p2)) / 6371000 AS δ, 0.2 AS f
WITH p1, p2, δ, 
     sin((1-f) * δ) / sin(δ) AS a,
     sin(f * δ) / sin(δ) AS b
WITH radians(p1.latitude) AS φ1, radians(p1.longitude) AS λ1,
     radians(p2.latitude) AS φ2, radians(p2.longitude) AS λ2,
     a, b
WITH a * cos(φ1) * cos(λ1) + b * cos(φ2) * cos(λ2) AS x,
     a * cos(φ1) * sin(λ1) + b * cos(φ2) * sin(λ2) AS y,
     a * sin(φ1) + b * sin(φ2) AS z
RETURN degrees(atan2(z, sqrt(x^2 + y^2))) AS φi,
       degrees(atan2(y,x)) AS λi
~~~


~~~text

╒═════════════════╤════════════════════╕
│φi               │λi                  │
╞═════════════════╪════════════════════╡
│51.49037311149128│-0.04880308288561931│
└─────────────────┴────────────────────┘
~~~

<p>A quick sanity check plugging in 0.5 instead of 0.2 finds the midpoint which I was able to sanity check against yesterday's post:</p>



~~~text

╒═════════════════╤═════════════════════╕
│φi               │λi                   │
╞═════════════════╪═════════════════════╡
│51.48613822097523│-0.050729537454086385│
└─────────────────┴─────────────────────┘
~~~

<p>
That's all for now!
</p>

