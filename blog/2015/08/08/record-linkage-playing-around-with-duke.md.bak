+++
draft = false
date="2015-08-08 22:50:41"
title="Record Linkage: Playing around with Duke"
tag=['software-development']
category=['Software Development']
+++

<p>
I've become quite interesting in <a href="https://en.wikipedia.org/wiki/Record_linkage">record linkage</a> recently and came across the <a href="https://github.com/larsga/Duke">Duke</a> project which provides some tools to help solve this problem. I thought I'd give it a try.</p>


<p>
The typical problem when doing record linkage is that we have two records from different data sets which represent the same entity but don't have a common key that we can use to merge them together. We therefore need to come up with a heuristic that will allow us to do so.
</p>


<p>
Duke has a few examples showing it in action and I decided to go with the <a href="https://github.com/larsga/Duke/wiki/LinkingCountries">linking countries</a> one. Here we have countries from Dbpedia and the Mondial database and we want to link them together.
</p>


<p>The first thing we need to do is build the project:</p>



~~~bash

export JAVA_HOME=`/usr/libexec/java_home`
mvn clean package -DskipTests
~~~

<p>
At the time of writing this will put a zip fail containing everything we need at <cite>duke-dist/target/</cite>. Let's unpack that:
</p>



~~~bash

unzip duke-dist/target/duke-dist-1.3-SNAPSHOT-bin.zip
~~~

<p>Next we need to download the data files and Duke configuration file:</p>



~~~bash

wget https://raw.githubusercontent.com/larsga/Duke/master/doc/example-data/countries-dbpedia.csv
wget https://raw.githubusercontent.com/larsga/Duke/master/doc/example-data/countries.xml
wget https://raw.githubusercontent.com/larsga/Duke/master/doc/example-data/countries-mondial.csv
wget https://raw.githubusercontent.com/larsga/Duke/master/doc/example-data/countries-test.txt
~~~

<p>Now we're ready to give it a go:</p>



~~~bash

java -cp "duke-dist-1.3-SNAPSHOT/lib/*" no.priv.garshol.duke.Duke --testfile=countries-test.txt --testdebug --showmatches countries.xml

...

NO MATCH FOR:
ID: '7706', NAME: 'guatemala', AREA: '108890', CAPITAL: 'guatemala city',

MATCH 0.9825124555160142
ID: '10052', NAME: 'pitcairn islands', AREA: '47', CAPITAL: 'adamstown',
ID: 'http://dbpedia.org/resource/Pitcairn_Islands', NAME: 'pitcairn islands', AREA: '47', CAPITAL: 'adamstown',

Correct links found: 200 / 218 (91.7%)
Wrong links found: 0 / 24 (0.0%)
Unknown links found: 0
Percent of links correct 100.0%, wrong 0.0%, unknown 0.0%
Records with no link: 18
Precision 100.0%, recall 91.74311926605505%, f-number 0.9569377990430622
~~~

<p>
We can look in <cite>countries.xml</cite> to see how the similarity between records is being calculated:
</p>



~~~xml

  <schema>
    <threshold>0.7</threshold>
...
    <property>
      <name>NAME</name>
      <comparator>no.priv.garshol.duke.comparators.Levenshtein</comparator>
      <low>0.09</low>
      <high>0.93</high>
    </property>
    <property>
      <name>AREA</name>
      <comparator>no.priv.garshol.duke.comparators.NumericComparator</comparator>
      <low>0.04</low>
      <high>0.73</high>
    </property>
    <property>
      <name>CAPITAL</name>
      <comparator>no.priv.garshol.duke.comparators.Levenshtein</comparator>
      <low>0.12</low>
      <high>0.61</high>
    </property>
  </schema>
~~~

<p>
So we're working out similarity of the capital city and country by calculating their Levenshtein distance i.e. the minimum number of single-character edits required to change one word into the other
</p>


<p>
This works very well if there is a typo or difference in spelling in one of the data sets. However, I was curious what would happen if the country had two completely different names e.g Cote d'Ivoire is sometimes know as Ivory Coast. Let's try changing the country name in one of the files:
</p>



~~~text

"19147","Cote dIvoire","Yamoussoukro","322460"
~~~



~~~bash

java -cp "duke-dist-1.3-SNAPSHOT/lib/*" no.priv.garshol.duke.Duke --testfile=countries-test.txt --testdebug --showmatches countries.xml

NO MATCH FOR:
ID: '19147', NAME: 'ivory coast', AREA: '322460', CAPITAL: 'yamoussoukro',
~~~

<p>
I also tried it out with the <a href="http://www.bbc.co.uk/sport/0/football/33744640">BBC</a> and <a href="http://www.espnfc.co.uk/gamecast/statistics/id/422662/statistics.html">ESPN</a> match reports of the Man Utd vs Tottenham match - the BBC references players by surname, while ESPN has their full names.
</p>


<p>
When I compared the full name against surname using the Levenshtein comparator there were no matches as you'd expect. I had to split the ESPN names up into first name and surname to get the linking to work. 
</p>


<p>Equally when I varied the team name's to be 'Man Utd' rather than 'Manchester United' and 'Tottenham' rather than 'Tottenham Hotspur' that didn't work either.
</p>


<p>I think I probably need to write a domain specific comparator but I'm also curious whether I could come up with a bunch of training examples and then train a model to detect what makes two records similar. It'd be less deterministic but perhaps more robust.</p>

