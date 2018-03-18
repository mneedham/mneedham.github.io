+++
draft = false
date="2010-11-12 15:43:37"
title="Experiments in not using the mouse"
tag=['software-development']
category=['Software Development']
+++

<a href="http://twitter.com/#!/priyaaank">Priyank</a> and I have been pairing a bit lately and we thought it'd be interesting to try and not use the mouse for anything that we had to do while pairing.

<h3>Editor</h3>

Priyank uses <a href="http://gvim.en.softonic.com/">GVim</a> (<a href="http://yehudakatz.com/2010/07/29/everyone-who-tried-to-convince-me-to-use-vim-was-wrong/">Yehuda Katz</a> recommends <a href="http://macvim.org/">MacVim</a> if you're using Mac OS) so we already don't need to use the mouse at all when we're inside the editor.

One annoying thing we found is that sometimes we wanted to copy stuff from the terminal into GVim and couldn't think of a good way to do that without selecting the text on the terminal with a mouse and then 'Ctrl-C'ing.

A bit of Googling led us to the <a href="http://www.vergenet.net/~conrad/software/xsel/">xsel</a> command which takes standard input and makes it available on the clipboard.

For example we've been using <a href="http://www.grymoire.com/Unix/Sed.html">sed</a> and wanted to copy the code we'd been spiking into a shell script:


~~~text

# code to replace backslashes with pipes in a file
echo "sed -i 's/\\/|\g' some_file.text'" | xsel -bi
~~~

In OS X we have '<a href="http://prefetch.net/blog/index.php/2009/02/13/pbcopy-pbpaste-in-os-x/">pbcopy</a>' which allows us to do the same type of thing.

Once we've got that onto the clipboard we need to use 'Ctrl R' followed by '+' in order to paste into GVim.

The next step is to get away from having to use the arrow keys which are annoyingly far away from all the others on a full sized keyboard but we're not there yet!

<h3>Browser</h3>

We're using Chrome so Priyank has installed the <a href="http://vimium.github.com/">Vimium</a> extension which allows us to use Vim shortcuts inside Chrome.

So far I've only been using the 'f' command which gives you key combinations to click on any of the links on the page but it's still much more fun than having to scroll around with the mouse!

If anyone has any other tips or tools for us to experiment with that'd be cool to hear about - it was much more fun constraining ourselves slightly and seeing how we got on!
