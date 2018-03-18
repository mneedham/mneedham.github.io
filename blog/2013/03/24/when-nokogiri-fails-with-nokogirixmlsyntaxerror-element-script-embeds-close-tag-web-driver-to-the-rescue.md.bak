+++
draft = false
date="2013-03-24 21:20:35"
title="When nokogiri fails with 'Nokogiri::XML::SyntaxError: Element script embeds close tag' Web Driver to the rescue"
tag=['software-development']
category=['Software Development']
+++

<p>As I mentioned in <a href="http://www.markhneedham.com/blog/2013/03/24/neo4jcypher-cyphertypeexception-failed-merging-number-with-relationship/">my previous post</a> I wanted to add televised games to my football graph and the <a href="http://www.premierleague.com/en-gb/matchday/broadcast-schedules.tv.html?rangeType=.dateSeason&country=GB&clubId=ALL&season=2012-2013&isLive=true">Premier League website</a> seemed like the best case to find out which games those were.</p>


<p>I initially tried to use <a href="http://nokogiri.org/">Nokogiri</a> to grab the data that I wanted...</p>



~~~ruby

> require 'nokogiri'
> require 'open-air'
> tv_times = Nokogiri::HTML(open('http://www.premierleague.com/en-gb/matchday/broadcast-schedules.tv.html?rangeType=.dateSeason&country=GB&clubId=ALL&season=2012-2013&isLive=true'))
~~~

<p>...but when I tried to query by CSS selector for all the matches nothing came back:</p>



~~~ruby

> tv_times.css(".broadcastschedule table.contentTable tbody tr")
=> []
~~~

<p>I was a bit surprised but read somewhere that I should check if there were any errors while parsing the document. In fact there were quite a few!</p>



~~~ruby

> tv_times.errors
=> [#<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, #<Nokogiri::XML::SyntaxError: Element script embeds close tag>, ...]
~~~

<p>I ran the document through the <a href="http://validator.w3.org/">W3C markup validation service</a> and it didn't seem to find any problem with it.</p>


<p>Next I tried stripping out all the script tags using <a href="https://github.com/flavorjones/loofah">loofah</a> before manually removing them but neither of those approaches helped.</p>


<p>I've previously used <a href="https://code.google.com/p/selenium/wiki/RubyBindings">Web Driver</a> to scrape web pages but I'd found that Nokogiri was much faster so I stopped using it.</p>
 

<p>Since my new library wasn't playing ball I thought I'd quickly see if Web Driver was up to the challenge and indeed it was:</p>



~~~ruby

require "selenium-webdriver"

driver = Selenium::WebDriver.for :chrome
driver.navigate.to "http://www.premierleague.com/en-gb/matchday/broadcast-schedules.tv.html?rangeType=.dateSeason&country=GB&clubId=ALL&season=2012-2013&isLive=true"

matches = driver.find_elements(:css, '.broadcastschedule table.contentTable tbody tr')
matches.each do|tr| 	
  match = tr.find_element(:css, "td.show a").text
  broadcaster = tr.find_element(:css, "td.broadcaster img").attribute("src")
  tv_channel = broadcaster.include?("sky-sports") ? "Sky" : "ESPN"

  puts "#{match},#{tv_channel}"
end

driver.quit
~~~


~~~ruby

$ ruby tv_games.rb 
Newcastle United vs Tottenham Hotspur,ESPN
Wigan Athletic vs Chelsea,Sky
Manchester City vs Southampton,Sky
Everton vs Manchester United,Sky
Swansea City vs West Ham United,Sky
Chelsea vs Newcastle United,ESPN
...
~~~

<p>Ideally I'd like to use Nokogiri to do this job but it's decided that the document is invalid and it can't parse it properly so Web Driver is a pretty decent replacement I reckon!</p>

