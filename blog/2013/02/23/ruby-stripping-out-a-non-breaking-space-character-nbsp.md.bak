+++
draft = false
date="2013-02-23 15:04:58"
title="Ruby: Stripping out a non breaking space character (&amp;nbsp;)"
tag=['ruby', 'character-encoding']
category=['Ruby']
+++

<p>A couple of days ago I was playing with some code to scrape data from a web page and I wanted to skip a row in a table if the row didn't contain any text.</p>


<p>I initially had the following code to do that:</p>



~~~ruby

rows.each do |row|
  next if row.strip.empty?
  # other scraping code
end
~~~

<p>Unfortunately that approach broke down fairly quickly because empty rows contained a <a href="http://www.yellowpipe.com/yis/tools/ASCII-HTML-Characters/index.php">non breaking space</a> i.e. '&nbsp;'.</p>


<p>If we try called <cite>strip</cite> on a string containing that character we can see that it doesn't get stripped:</p>



~~~ruby

# it's hex representation is A0
> "\u00A0".strip
=> " "
> "\u00A0".strip.empty?
=> false
~~~

<p>I wanted to see whether I could use <cite>gsub</cite> to solve the problem so I tried the following code which didn't help either:</p>



~~~ruby

> "\u00A0".gsub(/\s*/, "")
=> " "
> "\u00A0".gsub(/\s*/, "").empty?
=> false
~~~

<p>A bit of googling led me to this <a href="http://stackoverflow.com/questions/3913900/ruby-1-9-strip-not-removing-whitespace">Stack Overflow post</a> which suggests using the <a href="http://en.wikipedia.org/wiki/Regular_expression#POSIX_character_classes">POSIX space character class</a> to match the non breaking space rather than '\s' because that will match more of the different space characters.</p>


<p>e.g.</p>



~~~ruby

> "\u00A0".gsub(/[[:space:]]+/, "")
=> ""
> "\u00A0".gsub(/[[:space:]]+/, "").empty?
=> true
~~~

<p>So that we don't end up indiscriminately removing all spaces to avoid problems like this where we mash the two names together...</p>



~~~ruby

> "Mark Needham".gsub(/[[:space:]]+/, "")
=> "MarkNeedham"
~~~

<p>...the poster suggested the following regex which does the job:</p>



~~~ruby

> "\u00A0".gsub(/\A[[:space:]]+|[[:space:]]+\z/, '')
=> ""
> ("Mark" + "\u00A0" + "Needham").gsub(/\A[[:space:]]+|[[:space:]]+\z/, '')
=> "Mark Needham"
~~~

<ul>
<li>\A matches the beginning of the string</li>
<li>\z matches the end of the string</li>
</ul>

<p>So what this bit of code does is match all the spaces that appear at the beginning or end of the string and then replaces them with ''.</p>

