+++
draft = false
date="2009-10-26 06:32:24"
title="Scala: Converting an input stream to a string"
tag=['scala']
category=['Scala']
+++

I was playing around with Scala over the weekend and one thing that I wanted to do was get the data from a HTTP response as a string so that I could parse the xml returned. 

The data source is fairly small so loading the stream into memory wasn't a problem.

<a href="http://www.lixo.org/">Carlos</a> pointed me to <a href="http://www.kodejava.org/examples/266.html">a bit of Java code that did this</a> and I converted it as literally as possible into Scala.  


~~~scala

 def convertStreamToString(is: InputStream): String = {
    val reader = new BufferedReader(new InputStreamReader(is));
    val sb = new StringBuilder();

    var line : String = null;
    try {
      while ((line = reader.readLine()) != null) {
        sb.append(line + "\n");
      }
    } catch {
      case e: IOException => e.printStackTrace();
    } finally {
      try {
        is.close();
      } catch {
        case e: IOException => e.printStackTrace();
      }
    }

    sb.toString();
  }
~~~

The problem with this bit of code becomes clear when we try to run it through the REPL:


~~~text

7:warning: comparing values of types Unit and Null using `!=' will always yield true
             while ((line = reader.readLine()) != null) {
~~~

In Java the expression '(line = reader.readLine())' would return the value of 'reader.readLine()'  as far as I understand. We can then compare that to null. 

In Scala the evaluation of that expression is 'Unit' so if we ever run this function we end up in an infinite loop and eventually run out of memory.

I rewrote this function making use of recursion to get around the problem:


~~~scala

  def convertStreamToString(is : InputStream) : String = {
    def inner(reader : BufferedReader, sb : StringBuilder) : String = {
      val line = reader.readLine()
      if(line != null) {
        try {
          inner(reader, sb.append(line + "\n"))
        } catch {
          case e : IOException => e.printStackTrace()
        } finally {
          try {
            is.close()
          } catch {
            case e : IOException => e.printStackTrace()
          }
        }

      }
      sb.toString()
    }

    inner(new BufferedReader(new InputStreamReader(is)), new StringBuilder())
  }
~~~

The code is still peppered with error handling statements but it now allows us to convert the stream into a string.

Is there a better/cleaner/more Scala-esque way to do this?
