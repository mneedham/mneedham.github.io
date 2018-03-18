+++
draft = false
date="2013-04-07 01:00:08"
title="Sublime: Getting Textmate's Reveal/Select in Side Bar (Cmd + Ctrl + R)"
tag=['software-development', 'sublime']
category=['Software Development']
+++

<p>After coming across this post about <a href="http://delvarworld.github.io/blog/2013/03/16/just-use-sublime-text/">why you should use Sublime Text</a> I decided to try using it a bit more and one of the things that I missed from Textmate was the way you can select the current file on the sidebar.</p>


<p>In Textmate the shortcut to do that is 'Cmd + Ctrl + R' so I wanted to be able to do something similar or  configure Sublime so it responded to the same shortcut.</p>


<p>The option to reveal a file in the side bar is accessible from the context menu by right clicking on the contents of a file after it's opening and selecting 'Reveal in Side Bar' which is a good start.</p>


<p>To map that to a key binding we need to go 'Preferences > Key Bindings (User)' and <a href="http://sublimetext.userecho.com/topic/41241-reveal-file-in-project-tree/">put the following into that file</a>:</p>



~~~text

[
	{ "keys": ["ctrl+super+r"], "command": "reveal_in_side_bar" }
]
~~~

<p>Of course if we already have other custom key bindings then we can just add it after those instead.</p>


<p>We can work out what the name of commands are by turning on command logging in the Sublime console.</p>


<p>We need to first open the console with 'Ctrl + `" and then <a href="http://www.sublimetext.com/forum/viewtopic.php?f=2&t=11217">paste the following</a>:</p>



~~~text

sublime.log_commands(True)
~~~

<p>Any commands that we run will now have their name printed in the console window. e.g.</p>



~~~text

>>> sublime.log_commands(True)
command: context_menu {"event": {"button": 1, "x": 390.21484375, "y": 329.66796875}}
command: reveal_in_side_bar
command: rename_path {"paths": ["/Users/markhneedham/code/thinkingingraphs/public/js/bootstrap.js"]}
no command for selector: noop:
command: show_panel {"panel": "console", "toggle": true}
~~~

<p>We can then setup appropriate key bindings for whichever commands we like.</p>

