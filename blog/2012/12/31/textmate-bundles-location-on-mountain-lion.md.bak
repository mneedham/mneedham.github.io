+++
draft = false
date="2012-12-31 23:59:42"
title="TextMate Bundles location on Mountain Lion"
tag=['software-development']
category=['Software Development']
+++

<p>Something that I've noticed when trying to install <a href="https://github.com/swannodette/textmate-clojure">various different</a> <a href="https://github.com/textmate/haskell.tmbundle">bundles</a> is that the installation instructions which worked flawlessly on Snow Leopard don't seem to do the job on Mountain Lion.</p>


<p>For example, the Clojure bundle assumes that the installation directory is '~/Library/Application\ Support/TextMate/Bundles' but for some reason the 'Bundles' folder doesn't exist.</p>


<p>We therefore have two choices:</p>


<ul>
<li>mkdir -p ~/Library/Application\ Support/TextMate/Bundles and then continue as normal</li>
<li>Install our bundle into '/Applications/TextMate.app/Contents/SharedSupport/Bundles' <a href="http://stackoverflow.com/questions/4547076/textmate-haskell-bundle">as suggested on this thread</a>.</p>
</li>
</ul>

<p>So for the Clojure bundle we'd do this instead:</p>



~~~text

$ cd /Applications/TextMate.app/Contents/SharedSupport/Bundles
$ git clone git://github.com/swannodette/textmate-clojure.git Clojure.tmbundle
$ osascript -e 'tell app "TextMate" to reload bundles'
~~~

<p>And similarly for the Haskell one:</p>



~~~text

$ cd /Applications/TextMate.app/Contents/SharedSupport/Bundles
$ git clone https://github.com/textmate/haskell.tmbundle.git haskell.tmbundle
$ osascript -e 'tell app "TextMate" to reload bundles'
~~~

<p>Thinking about it now I'm wondering whether I did actually create the 'Bundles' folder in '~/Library/Application\ Support/TextMate/' on my old machine and I just can't remember doing so!</p>

