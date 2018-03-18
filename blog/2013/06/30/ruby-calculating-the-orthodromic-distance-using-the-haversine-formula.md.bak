+++
draft = false
date="2013-06-30 22:53:14"
title="Ruby: Calculating the orthodromic distance using the Haversine formula"
tag=['ruby', 'orthodromicdistance']
category=['Ruby']
+++

<p>As part of the <a href="http://www.markhneedham.com/blog/2013/06/30/leaflet-js-resizing-a-map-to-keep-a-circle-diameter-inside-it/">UI I'm building around my football stadiums data set</a> I wanted to calculate the distance from a football stadium to a point on the map in Ruby since <a href="http://docs.neo4j.org/chunked/milestone/cypher-query-lang.html">cypher</a> doesn't currently return this value.</p>


<p>I had the following cypher query to return the football stadiums near Westminster along with their lat/long values:</p>



~~~ruby

lat, long, distance = ["51.55786291569685", "0.144195556640625", 10]
query =  " START node = node:geom('withinDistance:[#{lat}, #{long}, #{distance}]')"
query << " RETURN node.name, node.team, node.lat, node.lon"

rows = result["data"].map do |row| 
         { :team => row[1], 
           :stadium => row[0],            
           :lat => row[2],
           :lon => row[3]
         } 
p rows
~~~

<p>which returns the following:</p>



~~~ruby

[{:team=>"Millwall", :stadium=>"The Den", :lat=>51.4859, :lon=>-0.050743},
 {:team=>"Arsenal", :stadium=>"Emirates Stadium", :lat=>51.5549, :lon=>-0.108436}, 
 {:team=>"Chelsea", :stadium=>"Stamford Bridge", :lat=>51.4816, :lon=>-0.191034},
 {:team=>"Fulham", :stadium=>"Craven Cottage", :lat=>51.4749, :lon=>-0.221619}, 
 {:team=>"Queens Park Rangers", :stadium=>"Loftus Road", :lat=>51.5093, :lon=>-0.232204}, 
 {:team=>"Leyton Orient", :stadium=>"Brisbane Road", :lat=>51.5601, :lon=>-0.012551}]
~~~

<p>In the neo4j spatial code the distance between two points is referred to as the 'orthodromic distance' but searching for that didn't come up with anything. However, I did eventually come across <a href="http://codingandweb.blogspot.co.uk/2012/04/calculating-distance-between-two-points.html">the following post</a> which referred to the <a href="http://en.wikipedia.org/wiki/Haversine_formula">Haversine formula</a> which is exactly what we want.</p>


<p>There is a <a href="http://mathforum.org/library/drmath/view/51879.html">good explanation of the formula on the Ask Dr Math forum</a> which defines the formula like so:</p>



~~~text

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
c = 2 * atan2(sqrt(a), sqrt(1-a)) 
d = R * c
~~~

<p>where:</p>


<ul>
<li>R - the radius of the Earth</li>
<li>c - the great circle distance in radians</li>
<li>c - the great circle distance in the same units as R</li>
<li>lat1, lat2, lon1, lon2 - latitude and longitudes in radians</li>
</ul>

<p>To convert decimal degrees to radians we need to multiply the number of degrees by <cite>pi/180</cite> radians/degree.</p>


<p>The Ruby translation of that formula looks like this:</p>



~~~ruby

def haversine(lat1, long1, lat2, long2)  
  radius_of_earth = 6378.14 
  rlat1, rlong1, rlat2, rlong2 = [lat1, long1, lat2, long2].map { |d| as_radians(d)}
 
  dlon = rlong1 - rlong2
  dlat = rlat1 - rlat2
 
  a = power(Math::sin(dlat/2), 2) + Math::cos(rlat1) * Math::cos(rlat2) * power(Math::sin(dlon/2), 2)
  great_circle_distance = 2 * Math::atan2(Math::sqrt(a), Math::sqrt(1-a))
  radius_of_earth * great_circle_distance
end

def as_radians(degrees)
  degrees * Math::PI/180
end

def power(num, pow)
  num ** pow
end
~~~

<p>And if we change our initial code to use it:</p>



~~~ruby

lat, long, distance = ["51.55786291569685", "0.144195556640625", 10]
query =  " START node = node:geom('withinDistance:[#{lat}, #{long}, #{distance}]')"
query << " RETURN node.name, node.team, node.lat, node.lon"

rows = result["data"].map do |row| 
         { :team => row[1], 
           :stadium => row[0], 
           :distance => haversine(lat, long, row[2], row[3]).round(2),           
           :lat => row[2],
           :lon => row[3]
         } 
p rows
~~~

<p>which gives us the output we want:</p>



~~~ruby

[{:team=>"Millwall", :stadium=>"The Den", :distance=>4.87, :lat=>51.4859, :lon=>-0.050743}, 
 {:team=>"Arsenal", :stadium=>"Emirates Stadium", :distance=>5.57, :lat=>51.5549, :lon=>-0.108436}, 
 {:team=>"Chelsea", :stadium=>"Stamford Bridge", :distance=>5.94, :lat=>51.4816, :lon=>-0.191034}, 
 {:team=>"Fulham", :stadium=>"Craven Cottage", :distance=>8.18, :lat=>51.4749, :lon=>-0.221619}, 
 {:team=>"Queens Park Rangers", :stadium=>"Loftus Road", :distance=>8.21, :lat=>51.5093, :lon=>-0.232204}, 
 {:team=>"Leyton Orient", :stadium=>"Brisbane Road", :distance=>9.33, :lat=>51.5601, :lon=>-0.012551}]~~~
