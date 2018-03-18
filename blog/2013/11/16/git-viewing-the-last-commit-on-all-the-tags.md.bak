+++
draft = false
date="2013-11-16 21:58:08"
title="Git: Viewing the last commit on all the tags"
tag=['git', 'neo4j']
category=['Version Control']
+++

<p>A couple of days ago I was curious when different versions of <a href="http://www.neo4j.org/">Neo4j</a> had been released and although the <a href="http://www.neo4j.org/release-notes">release notes page</a> was helpful I thought I'd find more detailed information if I looked up the git tags.</p>


<p>Assuming that we've already got a clone of the repository on our machine:</p>



~~~bash

$ git clone git@github.com:neo4j/neo4j.git
~~~

<p>We can pull down the latest tags by calling <cite>git fetch --tags</cite> or <cite>git fetch -t</cite></p>



~~~bash

$ git fetch -t
remote: Counting objects: 542, done.
remote: Compressing objects: 100% (231/231), done.
remote: Total 287 (delta 247), reused 84 (delta 50)
Receiving objects: 100% (287/287), 42.85 KiB, done.
Resolving deltas: 100% (247/247), completed with 191 local objects.
From github.com:neo4j/neo4j
 * [new tag]         1.9.2      -> 1.9.2
 * [new tag]         1.9.5      -> 1.9.5
 * [new tag]         2.0.0-M06  -> 2.0.0-M06
~~~

<p>We can get a list of all the tags in the repository with the following command:</p>



~~~bash

$ git tag | head -n5
1.3
1.4
1.4.1
1.4.2
1.4.M01
~~~

<p>Now let's have a look which commit that tag points at:</p>



~~~bash

$ git show 1.3

tag 1.3
Tagger: Neo4j Build Server <buildserver@neotechnology.com>
Date:   Tue Nov 20 17:03:38 2012 +0000

Tagging for release 1.3

commit ff16757dd53399eccb8f3db40eb48bab065459b0
Author: Neo Technology buildbox <buildserver@neotechnology.com>
Date:   Tue Apr 12 22:03:33 2011 +0000
~~~

<p>That command gets us the appropriate information but ideally we want to get the commit hash and the date on a single line which we can do by passing the '<a href="https://www.kernel.org/pub/software/scm/git/docs/git-log.html#_pretty_formats">--format</a>' flag to <cite>git log</cite>:</p>



~~~bash

$ git log --format="%h %ad%n" 1.3
ff16757 Tue Apr 12 22:03:33 2011 +0000

9651aa8 Tue Apr 12 21:58:58 2011 +0000

21c637d Tue Apr 12 12:39:49 2011 +0200

4ed65eb Tue Apr 12 12:39:28 2011 +0200
~~~

<p>We can pipe that to <cite>head</cite> to get the most recent commit:</p>



~~~bash

$ git log --format="%h %ad%n" 1.3 | head -n1
ff16757 Tue Apr 12 22:03:33 2011 +0000
~~~

<p>I tried to pipe the output of <cite>git tag</cite> to <cite>git log</cite> using <cite>xargs</cite> but I couldn't get it to work so I resorted to a for loop instead:</p>



~~~bash

$ for tag in `git tag`; do printf "%-20s %-100s \n" $tag "`git log --format="%h %ad%n" $tag | head -n1`"; done | head -n5
1.3                  ff16757 Tue Apr 12 22:03:33 2011 +0000                                                               
1.4                  5c19dc3 Fri Jul 8 16:22:37 2011 +0200                                                                
1.4.1                55f4ab2 Tue Aug 2 15:14:11 2011 +0300                                                                
1.4.2                cb85742 Tue Sep 27 18:59:13 2011 +0100                                                               
1.4.M01              f5aacf4 Fri Apr 29 10:12:52 2011 +0200  
~~~

<p>We could then pipe that output through grep to only show non point releases:</p>



~~~bash

$ for tag in `git tag`; do printf "%-20s %-100s \n" $tag "`git log --format="%h %ad%n" $tag | head -n1`"; done | grep -E "^\d\.\d "
1.3                  ff16757 Tue Apr 12 22:03:33 2011 +0000                                                               
1.4                  5c19dc3 Fri Jul 8 16:22:37 2011 +0200                                                                
1.5                  0225cb7 Thu Oct 20 03:51:06 2011 +0200                                                               
1.6                  f6f3cc1 Sun Jan 22 15:02:04 2012 +0100                                                               
1.7                  cc4ad98 Wed Apr 18 18:32:20 2012 +0200                                                               
1.8                  084acc9 Tue Sep 25 09:47:04 2012 +0100                                                               
1.9                  2efc04c Mon May 20 12:08:24 2013 +0100
~~~

<p>I first played around with Neo4j in September 2011 and I now know that I was using version 1.4 at the time.</p>
 

<p>We're now at 1.9.5 and the latest beta release is 2.0.0-M06 so there have been quite a few releases in between!</p>

