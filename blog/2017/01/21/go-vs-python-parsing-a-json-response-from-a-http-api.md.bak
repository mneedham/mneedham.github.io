+++
draft = false
date="2017-01-21 10:49:46"
title="Go vs Python: Parsing a JSON response from a HTTP API"
tag=['go', 'golang']
category=['Python']
description="Parsing meetup.com's HTTP API using Go and Python."
+++

As part of a <a href="https://www.meetup.com/graphdb-london/events/236256437/">recommendations with Neo4j talk</a> that I've presented a few times over the last year I have a set of scripts that download some data from the <a href="https://www.meetup.com/meetup_api/">meetup.com API</a>.

They're all written in Python but I thought it'd be a fun exercise to see what they'd look like in Go. My eventual goal is to try and parallelise the API calls.

This is the Python version of the script:

~~~python

import requests
import os
import json

key =  os.environ['MEETUP_API_KEY']
lat = "51.5072"
lon = "0.1275"

seed_topic = "nosql"
uri = "https://api.meetup.com/2/groups?&topic={0}&lat={1}&lon={2}&key={3}".format(seed_topic, lat, lon, key)

r = requests.get(uri)
all_topics = [topic["urlkey"]  for result in r.json()["results"] for topic in result["topics"]]

for topic in all_topics:
    print topic
~~~
We're using the <a href="http://docs.python-requests.org/en/master/">requests</a> library to send a request to the meetup API to get the groups which have the topic 'nosql' in the London area. We then parse the response and print out the topics.

Now to do the same thing in Go! The first bit of the script is almost identical:

~~~go

import (
	"fmt"
	"os"
	"net/http"
	"log"
	"time"
)

func handleError(err error) {
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
	}
}

func main() {
	var httpClient = &http.Client{Timeout: 10 * time.Second}

	seedTopic := "nosql"
	lat := "51.5072"
	lon := "0.1275"
	key := os.Getenv("MEETUP_API_KEY")

	uri := fmt.Sprintf("https://api.meetup.com/2/groups?&topic=%s&lat=%s&lon=%s&key=%s", seedTopic, lat, lon, key)

	response, err := httpClient.Get(uri)
	handleError(err)
	defer response.Body.Close()
	fmt.Println(response)
}
~~~
If we run that this is the output we see:

~~~bash

$ go cmd/blog/main.go

&{200 OK 200 HTTP/2.0 2 0 map[X-Meetup-Request-Id:[2d3be3c7-a393-4127-b7aa-076f150499e6] X-Ratelimit-Reset:[10] Cf-Ray:[324093a73f1135d2-LHR] X-Oauth-Scopes:[basic] Etag:["35a941c5ea3df9df4204d8a4a2d60150"] Server:[cloudflare-nginx] Set-Cookie:[__cfduid=d54db475299a62af4bb963039787e2e3d1484894864; expires=Sat, 20-Jan-18 06:47:44 GMT; path=/; domain=.meetup.com; HttpOnly] X-Meetup-Server:[api7] X-Ratelimit-Limit:[30] X-Ratelimit-Remaining:[29] X-Accepted-Oauth-Scopes:[basic] Vary:[Accept-Encoding,User-Agent,Accept-Language] Date:[Fri, 20 Jan 2017 06:47:45 GMT] Content-Type:[application/json;charset=utf-8]] 0xc420442260 -1 [] false true map[] 0xc4200d01e0 0xc4202b2420}
~~~
So far so good. Now we need to parse the response that comes back.

Most of the examples that I came across <a href="http://stackoverflow.com/questions/17156371/how-to-get-json-response-in-golang">suggest creating a struct with all the fields</a> that you want to extract from the JSON document but that feels a bit over kill for such a simple script.

Instead we can just create maps of (string -> interface{}) and then apply type conversions where appropriate. I ended up with the following code to extract the topics:

~~~go

import "encoding/json"

var target map[string]interface{}
decoder := json.NewDecoder(response.Body)
decoder.Decode(&target)

for _, rawGroup := range target["results"].([]interface{}) {
    group := rawGroup.(map[string]interface{})
    for _, rawTopic := range group["topics"].([]interface{}) {
        topic := rawTopic.(map[string]interface{})
        fmt.Println(topic["urlkey"])
    }
}
~~~
It's more verbose that the Python version because we have to explicitly type each thing we take out of the map at every stage, but it's not too bad. This is the full script:

~~~go

package main

import (
	"fmt"
	"os"
	"net/http"
	"log"
	"time"
	"encoding/json"
)

func handleError(err error) {
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
	}
}

func main() {
	var httpClient = &http.Client{Timeout: 10 * time.Second}

	seedTopic := "nosql"
	lat := "51.5072"
	lon := "0.1275"
	key := os.Getenv("MEETUP_API_KEY")

	uri := fmt.Sprintf("https://api.meetup.com/2/groups?&topic=%s&lat=%s&lon=%s&key=%s", seedTopic, lat, lon, key)

	response, err := httpClient.Get(uri)
	handleError(err)
	defer response.Body.Close()

	var target map[string]interface{}
	decoder := json.NewDecoder(response.Body)
	decoder.Decode(&target)

	for _, rawGroup := range target["results"].([]interface{}) {
		group := rawGroup.(map[string]interface{})
		for _, rawTopic := range group["topics"].([]interface{}) {
			topic := rawTopic.(map[string]interface{})
			fmt.Println(topic["urlkey"])
		}
	}
}
~~~
Once I've got these topics the next step is to make more API calls to get the groups for those topics.

I want to make those API calls in parallel while making sure I don't exceed the rate limit restrictions on the API and I think I can make use of go routines, channels, and timers to do that. But that's for another post!
