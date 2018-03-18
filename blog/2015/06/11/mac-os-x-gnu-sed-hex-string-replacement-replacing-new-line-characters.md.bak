+++
draft = false
date="2015-06-11 21:38:32"
title="Mac OS X: GNU sed -  Hex string replacement / replacing new line characters"
tag=['unix']
category=['Shell Scripting']
+++

<p>
Recently I was working with a CSV file which contained both Windows and Unix line endings which was making it difficult to work with.
</p>


<p>
The actual line endings were HEX '0A0D' i.e. Windows line breaks but there were also HEX 'OA' i.e. Unix line breaks within one of the columns.
</p>


<p>
I wanted to get rid of the Unix line breaks and discovered that you can do <a href="http://stackoverflow.com/questions/7760717/hex-string-replacement-using-sed">HEX sequence replacement using the GNU version of sed</a> - unfortunately the Mac ships with the BSD version which doesn't have this functionaltiy.
</p>


<p>
The first step was therefore to install the GNU version of sed.
</p>



~~~bash

brew install coreutils
brew install gnu-sed --with-default-names
~~~

<p>
I wanted to replace my system sed so that's why I went with the '--with-default-names' flag - without that flag I believe the sed installation would be accessible as 'gs-sed'.
</p>


<p>
The following is an example of what the lines in the file look like:
</p>



~~~bash

$ echo -e "Hello\x0AMark\x0A\x0D"
Hello
Mark
~~~

<p>
We want to get rid of the new line in between 'Hello' and 'Mark' but leave the other one be. I adapted one of the commands from <a href="http://backreference.org/2009/12/23/how-to-match-newlines-in-sed/">this tutorial</a> to look for lines which end in '0A' where that isn't followed by a '0D':
</p>



~~~bash

$ echo -e "Hello\x0AMark\x0A\x0D" | \
  sed 'N;/\x0A[^\x0D]/s/\n/ /'
Hello Mark

~~~

<p>
Let's go through the parts of the sed command:
</p>


<ul>
<li><cite>N</cite> - this creates a multiline pattern space by reading a new line of input and appending it to the contents of the pattern space. The two lines are separated by a new line.</li>
<li><cite>/\x0A[^\x0D]/</cite> - this matches any lines which contain 'OA' not followed by 'OD'</li>
<li><cite>/s/\n/ /</cite> - this substitutes the new line character with a space for those matching lines from the previous command.</li>
</ul>

<p>Now let's check it works if we have multiple lines that we want to squash:
</p>



~~~bash

$ echo -e "Hello\x0AMark\x0A\x0DHello\x0AMichael\x0A\x0D"
Hello
Mark
Hello
Michael

$ echo -e "Hello\x0AMark\x0A\x0DHello\x0AMichael\x0A\x0D" | \
  sed 'N;/\x0A[^\x0D]/s/\n/ /'
Hello Mark
Hello Michael

~~~

<p>Looks good! The actual file is a bit more nuanced so I've still got a bit more work to do but this is a good start.</p>

