+++
draft = false
date="2011-11-20 20:20:08"
title="Java/Scala: Runtime.exec hanging/in 'pipe_w' state"
tag=['java']
category=['Java', 'Scala']
+++

On the system that I'm currently working on we have a data ingestion process which needs to take zip files, unzip them and then import their contents into the database.

As a result we delegate from Scala code to the system unzip command like so:


~~~scala

def extract {
  var command = "unzip %s -d %s" format("/file/to/unzip.zip", "/place/to/unzip/to")
  var process: Process = null

  try {
    process = Runtime.getRuntime.exec(command)
    val exitCode = process.waitFor
  } catch {
    case e : Exception => // do some stuff
  } finally {
    // close the stream here
  }
}
~~~

We ran into a problem where the unzipping process was hanging and executing 'ps' showed us that the 'unzip' process was stuck in the 'pipe_w' (pipe waiting) state which suggested that it was waiting for some sort of input.

After a bit of googling <a href="http://duncan-cragg.org/blog/">Duncan</a> found <a href="http://vyvaks.wordpress.com/2006/05/27/does-runtimeexec-hangs-in-java/">this blog</a> which explained that we needed to process the output stream from our process otherwise it might end up hanging
 
a.k.a. <a href="http://download.oracle.com/javase/1.4.2/docs/api/java/lang/Process.html">RTFM</a>:

<blockquote>
The Runtime.exec methods may not work well for special processes on certain native platforms, such as native windowing processes, daemon processes, Win16/DOS processes on Microsoft Windows, or shell scripts. 

The created subprocess does not have its own terminal or console. All its standard io (i.e. stdin, stdout, stderr) operations will be redirected to the parent process through three streams (Process.getOutputStream(), Process.getInputStream(), Process.getErrorStream()). 

The parent process uses these streams to feed input to and get output from the subprocess. 

Because some native platforms only provide limited buffer size for standard input and output streams, failure to promptly write the input stream or read the output stream of the subprocess may cause the subprocess to block, and even deadlock.
</blockquote>

For most of the zip files we presumably hadn't been reaching the limit of the buffer because the list of files being sent to STDOUT by 'unzip' wasn't that high.

In order to get around the problem we needed to gobble up the output stream from unzip like so:


~~~scala

import org.apache.commons.io.IOUtils
def extract {
  var command = "unzip %s -d %s" format("/file/to/unzip.zip", "/place/to/unzip/to")
  var process: Process = null

  try {
    process = Runtime.getRuntime.exec(command)
    val thisVariableIsNeededToSuckDataFromUnzipDoNotRemove = "Output: " + IOUtils.readLines(process.getInputStream)
    val exitCode = process.waitFor
  } catch {
    case e : Exception => // do some stuff
  } finally {
    // close the stream here
  }
}
~~~

We need to do the same thing with the error stream as well in case 'unzip' ends up overflowing that buffer as well.

On a couple of blog posts that we came across it was suggested that we should 'gobble up' the output and error streams on separate threads but we weren't sure why exactly that was considered necessary...

If anyone knows then please let me know in the comments.
