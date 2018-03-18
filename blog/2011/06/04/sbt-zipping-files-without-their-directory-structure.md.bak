+++
draft = false
date="2011-06-04 17:24:16"
title="Sbt: Zipping files without their directory structure"
tag=['scala', 'sbt']
category=['Build', 'Scala']
+++

We're using <a href="http://code.google.com/p/simple-build-tool/">SBT</a> on our project and <a href="http://twitter.com/#!/patforna">Pat</a> and I have been trying to work out how to zip together some artifacts so that they're all available from the top level of the zip file i.e. we don't want to copy the directory structure where the files come from.

I've been playing around with this in the Scala REPL which we can launch with our project's dependencies loaded with the following command:


~~~text

./sbt console-project
~~~

Our original attempt to zip together the artifacts looked like this:


~~~scala

FileUtilities.zip(List(("ops" / "deploy")), "dist.zip", true, log)  
~~~

But unfortunately that keeps the directory structure which isn't what we want!


~~~text

mneedham@markneedham.home ~/Projects/core$ unzip -l dist.zip 
Archive:  dist.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
        0  06-04-11 17:52   ops/
        0  06-04-11 17:52   ops/deploy/
     2534  06-03-11 17:47   ops/deploy/start-server.sh
 --------                   -------
     2534                   3 files
~~~

Pat figured out that what we needed to do was <a href="http://code.google.com/p/simple-build-tool/wiki/Paths">make use of the ## function after our path</a> so our code would read like this:


~~~scala

FileUtilities.zip(List(("ops" / "deploy") ##), "dist.zip", true, log)
~~~

Et voila:


~~~text

mneedham@markneedham.home ~/Projects/core$ unzip -l dist.zip 
Archive:  dist.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     2534  06-03-11 17:47   start-server.sh
 --------                   -------
     2534                   1 file

~~~

The <a href="https://github.com/rossabaker/xsbt/blob/master/sbt/src/main/scala/sbt/Path.scala">## function is defined like so</a> and converts a path object into a BaseDirectory:



~~~scala

override def ## : Path = new BaseDirectory(this)
~~~

The <a href="https://github.com/rossabaker/xsbt/blob/master/sbt/src/main/scala/sbt/FileUtilities.scala">code in FileUtilities</a> that generates an entry for each file in the zip file looks like this:




~~~scala

               def makeFileEntry(path: Path) =
                {   
                        val relativePath = path.relativePathString("/")
                        log.debug("\tAdding " + path + " as " + relativePath + " ...")

                        val e = createEntry(relativePath)
                        e setTime path.lastModified
                        e   
                } 

                def addFileEntry(path: Path)
                {   
                        val file = path.asFile
                        if(file.exists)
                        {   
                                output putNextEntry makeFileEntry(path)
                                transferAndClose(new FileInputStream(file), output, log)
                                output.closeEntry()
                        }   
                        else
                                log.warn("\tFile " + file + " does not exist.")
                } 
~~~

Line 179 is where the meta data is defined for the archive and it makes use of "relativePathString" which has been overriden by BaseDirectory to return "":


~~~scala

private final class BaseDirectory(private[sbt] val path: Path) extends Path
{
        override def ## : Path = this
        override def toString = path.toString
        def asFile = path.asFile
        def relativePathString(separator: String) = ""
        def projectRelativePathString(separator: String) = path.projectRelativePathString(separator)
        private[sbt] def prependTo(s: String) = "." + sep + s 
}
~~~

Line 176 returns the file in its original location so it can still be copied into the archive.

The problem with using an identifier like ## is that it's very difficult to Google so you end up trawling the source code for its uses or hoping that you can find the explanation for its use in the documentation!
