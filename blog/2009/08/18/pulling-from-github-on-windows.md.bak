+++
draft = false
date="2009-08-18 00:33:11"
title="Pulling from github on Windows"
tag=['git', 'github']
category=['Version Control']
+++

My colleague <a href="http://intwoplacesatonce.com/">Dave Cameron</a> has been telling me about his adventures playing around with <a href="http://github.com/henon/GitSharp/tree/master">Git Sharp</a> (a C# port of the Java Git implementation <a href="http://www.jgit.org/">jGit</a>) so I thought I'd get a copy of the code and have a look as well.

I tend to check out all code bases from my host machine instead of virtual machine so I got the code all checked out on the Mac and accessed it via a shared folder on my VM.

The problem with doing this is I was unable to run the tests due to <a href="http://msdn.microsoft.com/en-us/library/ms345097.aspx">the following error</a> which I received repeatedly:


~~~text

System.Security.SecurityException: That assembly does not allow partially trusted callers.
at GitSharp.Tests.ObjectCheckerTests.testInvalidCommitNoTree2() 
~~~

I'm not sure exactly why I got this error but it's probably due to the fact that I didn't open the project in normal mode since I am accessing it on a shared drive.

I decided it would probably just be quicker to checkout the code directly from the VM instead. 

I installed <a href="http://code.google.com/p/msysgit/downloads/list">msysgit</a> which all worked fine and then I went to clone my repository:


~~~text

C:\Playbox>git clone git@github.com:mneedham/GitSharp.git
~~~

Which resulted in the following error:


~~~text

Initialized empty Git repository in C:/Playbox/GitSharp/.git/
Permission denied (publickey).
fatal: The remote end hung up unexpectedly
~~~

I had the public key setup on my github account from when I was using Git from my Mac but I hadn't setup the private key that it requires inside my VM!

Browsing through <a href="http://github.com/guides/providing-your-ssh-key#windowsxp">the instructions on the github website</a> I realised that I needed to copy my private key into the '.ssh' folder (which as I understand is the default folder for ssh settings to be stored).

This folder needs to be at the root of your <strong>user folder</strong> rather than at the root of the drive as I originally thought.

Therefore it should be at 'C:/Documents and Settings/Administrator/.ssh' for example rather than 'C:/.ssh' as I mistakenly had it.

I couldn't find a way to create a folder which started with a '.' from Windows explorer so I just created a folder called 'ssh' and then renamed it using 'mv ssh .ssh' from the command line.

I then copied my private key (which I got from the Mac by running 'less ~/.ssh/id_rsa') into a file called 'id_rsa' inside the '.ssh' folder and all was good:


~~~text

C:\Playbox>git clone git@github.com:mneedham/GitSharp.git
Initialized empty Git repository in C:/Playbox/GitSharp/.git/
Enter passphrase for key '/c/Documents and Settings/Administrator/.ssh/id_rsa':
remote: Counting objects: 3138, done.
remote: Compressing objects: 100% (880/880), done.
remote: Total 3138 (delta 2319), reused 3039 (delta 2220)
Receiving objects: 100% (3138/3138), 3.72 MiB | 191 KiB/s, done.
Resolving deltas: 100% (2319/2319), done.
Checking out files: 100% (505/505), done.
~~~

In the process of working out what I'd done wrong I came across <a href="http://devlicio.us/blogs/sergio_pereira/archive/2009/05/06/git-ssh-putty-github-unfuddle-the-kitchen-sink.aspx">a nice post by Sergio Pereira which describes the whole process of getting up and running with Git</a> in more detail.
