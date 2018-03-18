+++
draft = false
date="2012-09-16 13:35:56"
title="zsh: Don't verify substituted history expansion a.k.a.  disabling histverify"
tag=['zsh']
category=['Shell Scripting']
+++

I use <a href="http://www.zsh.org/">zsh</a> on my Mac terminal and in general I prefer it to bash but it has an annoying default setting whereby when you try to repeat a command via substituted history expansion it asks you to verify that.

For example let's say by mistake I try to vi into a directory rather than cd'ing into it:


~~~text

vi ~/.oh-my-zsh
~~~

If I try to cd into the directory by using '!$' to grab the last argument from the previous command it will make me confirm that I want to do this:


~~~text

$ cd !$
$ cd ~/.oh-my-zsh
~~~

While reading another one of Peter Krumins' blog posts, this time about <a href="http://www.catonmat.net/blog/the-definitive-guide-to-bash-command-line-history/">bash command line history</a>, I came to learn that this is because a setting called <cite><a href="http://wiki.bash-hackers.org/internals/shell_options#histverify">histverify</a></cite> has been enabled.

<blockquote>
histverify

Allow to review a history substitution result by loading the resulting line into the editing buffer, rather than directly executing it.
</blockquote>

I found <a href="http://stackoverflow.com/questions/11917567/how-to-view-default-zsh-settings-histsize-savehist">a thread on StackOverflow which explains all the zsh settings in more detail</a> but for my purposes I needed to run the following command to disable <cite>histverify</cite>:


~~~text

unsetopt histverify
~~~

I also put that into my <cite>~/.zshrc</cite> file so it will carry across to any new terminal sessions that I open.
