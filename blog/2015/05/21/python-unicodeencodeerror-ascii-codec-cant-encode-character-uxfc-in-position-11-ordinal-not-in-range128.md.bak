+++
draft = false
date="2015-05-21 06:14:32"
title="Python: UnicodeEncodeError: 'ascii' codec can't encode character u'\\xfc' in position 11: ordinal not in range(128)"
tag=['python']
category=['Python']
+++

<p>I've been trying to write some Python code to extract the players and the team they represented in the Bayern Munich/Barcelona match into a CSV file and had much more difficulty than I expected.
</p>


<p>
I have some scraping code (which is beyond the scope of this article) which gives me a list of (player, team) pairs that I want to write to disk. The contents of the list is as follows:
</p>



~~~python

$ python extract_players.py
(u'Sergio Busquets', u'Barcelona')
(u'Javier Mascherano', u'Barcelona')
(u'Jordi Alba', u'Barcelona')
(u'Bastian Schweinsteiger', u'FC Bayern M\xfcnchen')
(u'Dani Alves', u'Barcelona')
~~~

<p>
I started with the following script:
</p>



~~~python

with open("data/players.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["player", "team"])

    for player, team in players:
        print player, team, type(player), type(team)
        writer.writerow([player, team])
~~~

<p>
And if I run that I'll see this error:
</p>



~~~bash

$ python extract_players.py
...
Bastian Schweinsteiger FC Bayern München <type 'unicode'> <type 'unicode'>
Traceback (most recent call last):
  File "extract_players.py", line 67, in <module>
    writer.writerow([player, team])
UnicodeEncodeError: 'ascii' codec can't encode character u'\xfc' in position 11: ordinal not in range(128)
~~~

<p>
So it looks like the 'ü' in 'FC Bayern München' is causing us issues. Let's try and encode the teams to avoid this:
</p>



~~~python

with open("data/players.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["player", "team"])

    for player, team in players:
        print player, team, type(player), type(team)
        writer.writerow([player, team.encode("utf-8")])
~~~


~~~bash

$ python extract_players.py
...
Thomas Müller FC Bayern München <type 'unicode'> <type 'unicode'>
Traceback (most recent call last):
  File "extract_players.py", line 70, in <module>
    writer.writerow([player, team.encode("utf-8")])
UnicodeEncodeError: 'ascii' codec can't encode character u'\xfc' in position 8: ordinal not in range(128)
~~~

<p>Now we've got the same issue with the 'ü' in Müller so let's encode the players too:</p>



~~~python

with open("data/players.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["player", "team"])

    for player, team in players:
        print player, team, type(player), type(team)
        writer.writerow([player.encode("utf-8"), team.encode("utf-8")])
~~~


~~~bash

$ python extract_players.py
...
Gerard Piqué Barcelona <type 'str'> <type 'unicode'>
Traceback (most recent call last):
  File "extract_players.py", line 70, in <module>
    writer.writerow([player.encode("utf-8"), team.encode("utf-8")])
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 11: ordinal not in range(128)
~~~

<p>
Now we've got a problem with Gerard Piqué because that value has type string rather than unicode. Let's fix that:
</p>



~~~python

with open("data/players.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["player", "team"])

    for player, team in players:
        if isinstance(player, str):
            player = unicode(player, "utf-8")
        print player, team, type(player), type(team)
        writer.writerow([player.encode("utf-8"), team.encode("utf-8")])
~~~

<p>
Et voila! All the players are now successfully written to the file.
</p>


<p>
An alternative approach is to <a href="http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte">change the default encoding of the whole script</a> to be 'UTF-8', like so:
</p>



~~~python

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open("data/players.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["player", "team"])

    for player, team in players:
        print player, team, type(player), type(team)
        writer.writerow([player, team])
~~~

<p>
It took me a while to figure it out but finally the players are ready to go!
</p>

