+++
draft = false
date="2012-09-19 07:00:22"
title="Finding ways to use bash command line history shortcuts"
tag=['bash']
category=['Shell Scripting']
+++

A couple of months ago I wrote about a <a href="http://www.markhneedham.com/blog/2012/07/05/bash-shell-reusing-parts-of-previous-commands/">bunch of command line history shortcuts</a> that <a href="https://twitter.com/philandstuff">Phil</a> had taught me and after recently coming across <a href="http://www.catonmat.net/download/bash-history-cheat-sheet.pdf">Peteris Krumins' bash history cheat sheet</a> I thought it'd be interesting to find some real ways to use them.

A few weeks ago I wrote about <a href="http://www.markhneedham.com/blog/2012/09/03/a-rogue-357273277-utf-8-byte-order-mark/">a UTF-8 byte order mark (BOM) that I wanted to remove from a file</a> I was working on and I realised this evening that there were some other files with the same problem.

The initial command read like this:


~~~text

awk '{if(NR==1)sub(/^\xef\xbb\xbf/,"");print}' data/Taxonomy/Products.csv  > data/Taxonomy/Products.csv.bak
~~~

The version of the file without the BOM is <cite>data/Taxonomy/Products.csv.bak</cite> but I wanted it to be <cite>data/Taxonomy/Products.csv</cite> so I needed to <cite>mv</cite> it to that location.

By making use of history expansion we can write this as follows:


~~~text

mv !$ !!:2
~~~

<cite>!$</cite> represents the last argument which is <cite>data/Taxonomy/Products.csv.bak</cite> and <cite>!!:2</cite> gets the 2nd argument passed to the last command which in this case is <cite>data/Taxonomy/Products.csv</cite>.

As you're typing it will expand to the following:


~~~text

mv data/Taxonomy/Products.csv.bak data/Taxonomy/Products.csv 
~~~

One of the things that we do quite frequently is look at the nginx configurations and logs of our different applications which involved doing the following:


~~~text

$ tail -f /var/log/nginx/site-1-access.log
$ tail -f /var/log/nginx/site-2-access.log
~~~

or 


~~~text

$ vi /etc/nginx/sites-enabled/site-1-really-long-name-cause-we-can
$ vi /etc/nginx/sites-enabled/site-2-really-long-name-cause-we-can
~~~

Everything except for the file name is the same but typing the up arrow to get the previous command and then manually deleting the file name can end up taking longer than just writing out the whole command again if the site name is long.

Ctrl-w deletes the whole path so that doesn't help us either.

An alternative is the use the 'h' modifier which "Removes a trailing pathname component, leaving the head."

In this case we could do the following:


~~~text

$ vi /etc/nginx/sites-enabled/site-1-really-long-name-cause-we-can
$ vi !$:h/site-2-really-long-name-cause-we-can
~~~

We still have to type out the whole file name and we don't get any auto complete help which is a bit annoying. 

I realised that on my zsh if I type a space after a history expansion command it expands what I've typed to the full paths of everything, which is due to the following key binding:


~~~text

.oh-my-zsh $ grep -rn "magic-space" *
lib/key-bindings.zsh:20:bindkey ' ' magic-space    # also do history expansion on space
~~~

We can do the same thing in bash by running the following command:


~~~text

bind Space:magic-space
~~~

Then if I wanted to open that second nginx file I could do the following:


~~~text

$ vi !$:h # then type a space which will expand it to:
$ vi /etc/nginx/sites-enabled/ # I can then type backspace, then type 'site-2' and tab and open the file
~~~

It's not completely smooth because of the backspace but I think it's marginally quicker than the other options.

Another one which I mentioned in the first post is the <cite>^original^replacement</cite> which will run the previous command but replace the first instance of 'original' with 'replacement'. 

With this one it often seems faster to type the up arrow and change what you want manually or retype the command but when doing a grep of a specific folder I think this is faster. 

e.g.


~~~text

$ grep -rn "magic-space" ~/.oh-my-zsh/lib
/Users/mneedham/.oh-my-zsh/lib/key-bindings.zsh:20:bindkey ' ' magic-space    # also do history expansion on space
~~~

Let's say I was intrigued about <cite>bindkey</cite> and wanted to find all the instances of that. 

One way to do that would be to type up and then manually go back along the line using <cite>Meta-B</cite> until I get to 'bind-key' when I can delete that with a few <cite>Ctrl-W</cite>'s but in this case the search/replace approach is quicker:


~~~text

$ ^magic-space^bindkey
grep -rn "bindkey" ~/.oh-my-zsh/lib
/Users/mneedham/.oh-my-zsh/lib/completion.zsh:24:bindkey -M menuselect '^o' accept-and-infer-next-history
/Users/mneedham/.oh-my-zsh/lib/completion.zsh:71:  bindkey "^I" expand-or-complete-with-dots
~~~

I'm still looking for other ways to re-use bash history more effectively so let me know any other cool tricks in the comments.
