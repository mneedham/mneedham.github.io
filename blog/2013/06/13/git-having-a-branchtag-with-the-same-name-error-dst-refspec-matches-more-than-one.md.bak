+++
draft = false
date="2013-06-13 22:18:31"
title="git: Having a branch/tag with the same name (error: dst refspec matches more than one.)"
tag=['git']
category=['Version Control']
+++

<p><a href="https://twitter.com/andres_taylor">Andres</a> and I recently found ourselves wanting to delete a remote branch which had the same name as a tag and therefore the normal way of doing that wasn't worked out as well as we'd hoped.</p>


<p>I created a dummy repository to recreate the state we'd got ourselves into:</p>



~~~bash

$ echo "mark" > README
$ git commit -am "readme"
$ echo "for the branch" >> README 
$ git commit -am "for the branch"

$ git checkout -b same
Switched to a new branch 'same'

$ git push origin same
Counting objects: 5, done.
Writing objects: 100% (3/3), 263 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To ssh://git@bitbucket.org/markhneedham/branch-tag-test.git
 * [new branch]      same -> same

$ git checkout master
$ echo "for the tag" >> README
$ git commit -am "for the tag"
$ git tag same
$ git push origin refs/tags/same
Counting objects: 5, done.
Writing objects: 100% (3/3), 266 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To ssh://git@bitbucket.org/markhneedham/branch-tag-test.git
 * [new tag]         same -> same
~~~

<p>We wanted to delete the remote 'same' branch and the following command would work if we hadn't created a tag with the same name. Instead it throws an error:</p>



~~~bash

$ git push origin :same
error: dst refspec same matches more than one.
error: failed to push some refs to 'ssh://git@bitbucket.org/markhneedham/branch-tag-test.git'
~~~

<p>We learnt that what we needed to do was refer to the full path for the branch when trying to delete it remotely:</p>



~~~bash

$ git push origin :refs/heads/same
To ssh://git@bitbucket.org/markhneedham/branch-tag-test.git
 - [deleted]         same
~~~

<p>To delete the tag we could do the same thing:</p>



~~~bash

$ git push origin :refs/tags/same
remote: warning: Deleting a non-existent ref.
To ssh://git@bitbucket.org/markhneedham/branch-tag-test.git
 - [deleted]         same
~~~

<p>Of course the tag and branch still exist locally:</p>



~~~bash

$ ls -alh .git/refs/heads/
total 16
drwxr-xr-x  4 markhneedham  wheel   136B 13 Jun 23:09 .
drwxr-xr-x  5 markhneedham  wheel   170B 13 Jun 22:39 ..
-rw-r--r--  1 markhneedham  wheel    41B 13 Jun 23:08 master
-rw-r--r--  1 markhneedham  wheel    41B 13 Jun 23:08 same

$ ls -alh .git/refs/tags/
total 8
drwxr-xr-x  3 markhneedham  wheel   102B 13 Jun 23:08 .
drwxr-xr-x  5 markhneedham  wheel   170B 13 Jun 22:39 ..
-rw-r--r--  1 markhneedham  wheel    41B 13 Jun 23:08 same
~~~

<p>So we got rid of them as well:</p>



~~~bash

$ git checkout master
Switched to branch 'master'
$ git branch -d same
Deleted branch same (was 08ad88c).
$ git tag -d same
Deleted tag 'same' (was 1187891)
~~~

<p>And now they are gone:</p>



~~~bash

$ ls -alh .git/refs/heads/
total 8
drwxr-xr-x  3 markhneedham  wheel   102B 13 Jun 23:16 .
drwxr-xr-x  5 markhneedham  wheel   170B 13 Jun 22:39 ..
-rw-r--r--  1 markhneedham  wheel    41B 13 Jun 23:08 master
$ ls -alh .git/refs/tags/
total 0
drwxr-xr-x  2 markhneedham  wheel    68B 13 Jun 23:16 .
drwxr-xr-x  5 markhneedham  wheel   170B 13 Jun 22:39 ..
~~~

<p>Out of interest we'd ended up with this situation by mistake rather than by design but it was still fun to do a little bit of git digging to figure out how to solve the problem we'd created for ourselves.</p>

