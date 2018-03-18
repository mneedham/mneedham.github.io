+++
draft = false
date="2016-06-18 07:38:04"
title="Python: Regex - matching foreign characters/unicode letters"
tag=['python']
category=['Python']
+++

<p>
I've been back in the land of screen scrapping this week extracting data from the <a href="http://gameofthrones.wikia.com/wiki">Game of Thrones wiki</a> and needed to write a regular expression to pull out characters and actors.
<p>

<p>Here are some examples of the format of the data:</p>



~~~text

Peter Dinklage as Tyrion Lannister
Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)
Filip Lozić as Young Nobleman
Morgan C. Jones as a Braavosi captain
Adewale Akinnuoye-Agbaje as Malko
~~~

<p>So the pattern is:</p>



~~~text

<actor> as <character> 
~~~

<p>optionally followed by some other text that we're not interested in.</p>


<p>The output I want to get is:</p>



~~~text

Peter Dinklage, Tyrion Lannister
Daniel Naprous, Oznak zo Pahl
Filip Lozić, Young Nobleman
Morgan C. Jones, a Braavosi captain
Adewale Akinnuoye-Agbaje, Malko
~~~

<p>I started using the 'split' command on the word 'as' but that broke down when I realised some of the characters had the letters 'as' in the middle of their name. So regex it is!</p>


<p>
This was my first attempt:
</p>



~~~python

import re

strings = [
    "Peter Dinklage as Tyrion Lannister",
    "Filip Lozić as Young Nobleman",
    "Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)",
    "Morgan C. Jones as a Braavosi captain",
    "Adewale Akinnuoye-Agbaje as Malko"
]

regex = "([A-Za-z\-'\. ]*) as ([A-Za-z\-'\. ]*)"

for string in strings:
    print string
    match = re.match( regex, string)
    if match is not None:
        print match.groups()
    else:
        print "FAIL"
	print ""
~~~


~~~text

Peter Dinklage as Tyrion Lannister
('Peter Dinklage', 'Tyrion Lannister')

Filip Lozić as Young Nobleman
FAIL

Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)
('Daniel Naprous', 'Oznak zo Pahl')

Morgan C. Jones as a Braavosi captain
('Morgan C. Jones', 'a Braavosi captain')

Adewale Akinnuoye-Agbaje as Malko
('Adewale Akinnuoye-Agbaje', 'Malko')
~~~

<p>
It works for 4 of the 5 scenarios but now for Filip Lozić. The 'ć' character causes the issue so we need to be able to match foreign characters which the current charset I defined in the regex doesn't capture.</p>


<p>I came across <a href="http://stackoverflow.com/questions/3009993/regex-what-would-be-regex-for-matching-foreign-characters">this Stack Overflow post</a> which said that in some regex libraries you can use '\p{L}' to match all letters. I gave that a try:
</p>



~~~python

regex = "([\p{L}\-'\. ]*) as ([\p{L}\-'\. ]*)"
~~~

<p>And then re-ran the script:</p>



~~~text

Peter Dinklage as Tyrion Lannister
FAIL

Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)
FAIL

Filip Lozić as Young Nobleman
FAIL

Morgan C. Jones as a Braavosi captain
FAIL

Adewale Akinnuoye-Agbaje as Malko
FAIL
~~~

<p>Hmmm, not sure if I did it wrong or if that isn't available in Python. I'll assume the latter but feel free to correct me in the comments and I'll update the post.</p>


<p>
I went search again and found <a href="http://stackoverflow.com/questions/8923949/matching-only-a-unicode-letter-in-python-re">this post</a> which suggested another approach:
</p>


<blockquote>
You can construct a new character class:

[^\W\d_]

instead of \w. Translated into English, it means "Any character that is not a non-alphanumeric character ([^\W] is the same as \w), but that is also not a digit and not an underscore".
</blockquote>

<p>Let's try plugging that in:</p>



~~~python

regex = "([A-Za-z\-'\.^\W\d_ ]*) as ([A-Za-z\-'\.^\W\d_ ]*)"
~~~


~~~text

Peter Dinklage as Tyrion Lannister
('Peter Dinklage', 'Tyrion Lannister')

Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)
('Daniel Naprous as Oznak zo Pahl(credited', 'Stunt Performer)')

Filip Lozić as Young Nobleman
('Filip Lozi\xc4\x87', 'Young Nobleman')

Morgan C. Jones as a Braavosi captain
('Morgan C. Jones', 'a Braavosi captain')

Adewale Akinnuoye-Agbaje as Malko
('Adewale Akinnuoye-Agbaje', 'Malko')
~~~

<p>So that's fixed Filip but now Daniel Naprous is being incorrectly parsed.</p>
 

<p>For Attempt #4 I decided to try excluding what I don't want instead:</p>



~~~python

regex = "([^0-9\(]*) as ([^0-9\(]*)"
~~~


~~~text

Peter Dinklage as Tyrion Lannister
('Peter Dinklage', 'Tyrion Lannister')

Daniel Naprous as Oznak zo Pahl(credited as Stunt Performer)
('Daniel Naprous', 'Oznak zo Pahl')

Filip Lozić as Young Nobleman
('Filip Lozi\xc4\x87', 'Young Nobleman')

Morgan C. Jones as a Braavosi captain
('Morgan C. Jones', 'a Braavosi captain')

Adewale Akinnuoye-Agbaje as Malko
('Adewale Akinnuoye-Agbaje', 'Malko')
~~~

<p>That does the job but has exposed my lack of regex skillz. If you know a better way let me know in the comments.</p>

