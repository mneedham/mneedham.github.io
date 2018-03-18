+++
draft = false
date="2012-07-30 22:28:38"
title="London Bus Stops API: Mapping northing/easting values to lat/long"
tag=['software-development']
category=['Software Development']
+++

I started playing around with the <a href="http://www.tfl.gov.uk/businessandpartners/syndication/16493.aspx#17463">TFL Bus stop location and routes API</a> and one of the annoying things about the data is that it uses <a href="http://en.wikipedia.org/wiki/Easting_and_northing">easting/northing</a> values to describe the location of bus stops rather than lat/longs.

The <a href="https://raw.github.com/mneedham/london-buses/master/data/stops.csv">first few lines of the CSV file</a> look like this:


~~~text

1000,91532,490000266G,WESTMINSTER STN <> / PARLIAMENT SQUARE,530171,179738,177,0K08,0
10001,72689,490013793E,TREVOR CLOSE,515781,174783,78,NB16,0
10002,48461,490000108F,HIGHBURY CORNER,531614,184603,5,C902,0
~~~

For each of the stops I wanted to convert from the easting/northing value to the equivalent lat/long value but I couldn't find a simple way of doing it in code although I did <a href="http://www.uk-postcodes.com/eastingnorthing.php?easting=530171&northing=179738">come across an API that would do it for me</a>.

I wrote the following script to save a new CSV file with all the London bus stops and their lat/long location:


~~~ruby

require 'rubygems'
require 'csv'
require 'open-uri'
require 'json'

data_dir = File.expand_path('data') + '/'
file_name = data_dir + "stops.csv"

stops = CSV.read(file_name).drop(1)

out = CSV.open(data_dir + "stops_with_lat_longs.csv","w")

stops.each do |stop|
  code = stop[1]
  easting = stop[4]
  northing = stop[5]
  url  = "http://www.uk-postcodes.com/eastingnorthing.php?easting=#{easting}&northing=#{northing}"
  location = JSON.parse(open(url).read)

  puts "Processing #{stop[3]}: #{location['lat']}, #{location['lng']}"

  out << [code, location['lat'],location['lng']]
end

out.close
~~~

I've uploaded the <a href="https://github.com/mneedham/london-buses/blob/master/data/stops_with_lat_longs.csv">file with mapping from bus stop code to lat/long</a> to github as well.

<a href="http://blog.poggs.com/2010/09/converting-osgb36-eastingsnorthings-to-wgs84-longitudelatitude-in-ruby/">Peter Hicks has a blog post showing another way of doing this using just Ruby code</a> but I couldn't get the 'proj4' gem to install and I didn't fancy shaving that yak when I had another solution which worked.
