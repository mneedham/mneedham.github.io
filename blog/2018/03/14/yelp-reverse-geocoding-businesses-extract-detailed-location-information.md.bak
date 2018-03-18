+++
draft = false
date="2018-03-14 08:53:04"
title="Yelp: Reverse geocoding businesses to extract detailed location information"
tag=['yelp', 'yelp-dataset-challenge', 'geocoding', 'reverse-geocode']
category=['Python']
+++

<p>
I've been playing around with the <a href="https://www.yelp.co.uk/dataset">Yelp Open Dataset</a> and wanted to extract more detailed location information for each business.
</p>


<p>
This is an example of the JSON representation of one business:
</p>



~~~bash

$ cat dataset/business.json | head -n1 | jq
{
  "business_id": "FYWN1wneV18bWNgQjJ2GNg",
  "name": "Dental by Design",
  "neighborhood": "",
  "address": "4855 E Warner Rd, Ste B9",
  "city": "Ahwatukee",
  "state": "AZ",
  "postal_code": "85044",
  "latitude": 33.3306902,
  "longitude": -111.9785992,
  "stars": 4,
  "review_count": 22,
  "is_open": 1,
  "attributes": {
    "AcceptsInsurance": true,
    "ByAppointmentOnly": true,
    "BusinessAcceptsCreditCards": true
  },
  "categories": [
    "Dentists",
    "General Dentistry",
    "Health & Medical",
    "Oral Surgeons",
    "Cosmetic Dentists",
    "Orthodontists"
  ],
  "hours": {
    "Friday": "7:30-17:00",
    "Tuesday": "7:30-17:00",
    "Thursday": "7:30-17:00",
    "Wednesday": "7:30-17:00",
    "Monday": "7:30-17:00"
  }
}
~~~

<p>
The businesses reside in different countries so I wanted to extract the area/county/state and the country for each of them. I found the <a href="https://github.com/thampiman/reverse-geocoder">reverse-geocoder</a> library which is perfect for this problem.
</p>


<p>
You give the library a lat/long or list of lat/longs and it returns you back a list containing the nearest lat/long to your points along with the name of the place, Admin regions, and country code. It's way quicker to pass in a list of lat/longs than to call the function individually for each lat/long so we'll do that.
</p>


<p>
We can write the following code to extract location information for a list of lat/longs:
</p>



~~~python

import reverse_geocoder as rg

lat_longs = {
    "FYWN1wneV18bWNgQjJ2GNg": (33.3306902, -111.9785992),
    "He-G7vWjzVUysIKrfNbPUQ": (40.2916853, -80.1048999),
    "KQPW8lFf1y5BT2MxiSZ3QA": (33.5249025, -112.1153098)
}

business_ids = list(lat_longs.keys())
locations = rg.search(list(lat_longs.values()))

for business_id, location in zip(business_ids, locations):
    print(business_id, lat_longs[business_id], location)
~~~

<p>
This is the output we get from running the script:
</p>



~~~bash

$ python blog.py 
Loading formatted geocoded file...
FYWN1wneV18bWNgQjJ2GNg (33.3306902, -111.9785992) OrderedDict([('lat', '33.37088'), ('lon', '-111.96292'), ('name', 'Guadalupe'), ('admin1', 'Arizona'), ('admin2', 'Maricopa County'), ('cc', 'US')])
He-G7vWjzVUysIKrfNbPUQ (40.2916853, -80.1048999) OrderedDict([('lat', '40.2909'), ('lon', '-80.10811'), ('name', 'Thompsonville'), ('admin1', 'Pennsylvania'), ('admin2', 'Washington County'), ('cc', 'US')])
KQPW8lFf1y5BT2MxiSZ3QA (33.5249025, -112.1153098) OrderedDict([('lat', '33.53865'), ('lon', '-112.18599'), ('name', 'Glendale'), ('admin1', 'Arizona'), ('admin2', 'Maricopa County'), ('cc', 'US')])
~~~

<p>
It seems to work fairly well! Now we just need to tweak our script to read in the values from the Yelp JSON file and generate a new JSON file containing the locations:
</p>



~~~python

import json

import reverse_geocoder as rg

lat_longs = {}

with open("dataset/business.json") as business_json:
    for line in business_json.readlines():
        item = json.loads(line)
        if item["latitude"] and item["longitude"]:
            lat_longs[item["business_id"]] = {
                "lat_long": (item["latitude"], item["longitude"]),
                "city": item["city"]
            }

result = {}

business_ids = list(lat_longs.keys())
locations = rg.search([value["lat_long"] for value in lat_longs.values()])

for business_id, location in zip(business_ids, locations):
    result[business_id] = {
        "country": location["cc"],
        "name": location["name"],
        "admin1": location["admin1"],
        "admin2": location["admin2"],
        "city": lat_longs[business_id]["city"]
    }

with open("dataset/businessLocations.json", "w") as business_locations_json:
    json.dump(result, business_locations_json, indent=4, sort_keys=True)
~~~

<p>
And that's it!
</p>

