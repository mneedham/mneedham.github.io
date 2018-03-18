+++
draft = false
date="2014-01-31 06:51:06"
title="Java: Work out the serialVersionUID of a class"
tag=['java']
category=['Java']
+++

<p>Earlier in the week I wanted to work out the <cite>serialVersionUID</cite> of a serializable class so that I could override its <cite>toString</cite> method without breaking everything.</p>


<p>I came across <a href="http://betweengo.com/2005/07/30/serialver/">Frank Kim's blog post</a> which suggested using the <cite>serialver</cite> tool which comes with the JDK.</p>


<p>I created a little Maven project to test this tool out on a very simple class:</p>



~~~java

import java.io.Serializable;

public class SerialiseMe implements Serializable
{

}
~~~

<p>If we compile that class into a JAR and then run the <cite>serialver</cite> tool we see the following output:</p>



~~~bash

$ serialver -classpath target/serialiser-0.0.1-SNAPSHOT.jar SerialiseMe
SerialiseMe:    static final long serialVersionUID = -6060222249255158490L;
~~~

<p>I wanted to quickly confirm that I could serialise and deserialise this class using this value so I wrote the following bit of code to serialise the class (when it didn't have a serial version UID):</p>



~~~java

public class Serialiser
{
    public static void main( String[] args ) throws IOException, ClassNotFoundException
    {
        ByteArrayOutputStream bout = new ByteArrayOutputStream(  );
        ObjectOutputStream oout = new ObjectOutputStream( bout );

        Object value = new SerialiseMe();

        oout.writeObject( value );
        oout.close();
        byte[] bytes = bout.toByteArray();

        FileOutputStream fileOuputStream = new FileOutputStream("/tmp/foo.txt");
        fileOuputStream.write(bytes);
        fileOuputStream.close();
    }
}
~~~

<p>After I'd done that, I wrote the following bit of code to deserialise the file:</p>



~~~java

public class Deserialiser
{
    public static void main( String[] args ) throws IOException, ClassNotFoundException
    {
        FileInputStream fileInputStream = new FileInputStream( new File( "/tmp/foo.txt" ) );
        byte[] bytes = IOUtils.toByteArray( fileInputStream );

        ByteArrayInputStream in = new ByteArrayInputStream( bytes, 0, bytes.length );
        ObjectInputStream oin = new ObjectInputStream( in );
        Object object = oin.readObject();
    }
}
~~~

<p>I plugged the serial version UID into the class and was able to deserialise it correctly. I tried changing one of the digits just to check it would blow up and indeed it did:</p>



~~~java

import java.io.Serializable;

public class SerialiseMe implements Serializable
{
    static final long serialVersionUID = -6060222249255158491L;
}
~~~


~~~text

Exception in thread "main" java.io.InvalidClassException: SerialiseMe; local class incompatible: stream classdesc serialVersionUID = -6060222249255158490, local class serialVersionUID = -6060222249255158491
	at java.io.ObjectStreamClass.initNonProxy(ObjectStreamClass.java:604)
	at java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:1620)
	at java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1515)
	at java.io.ObjectInputStream.readOrdinaryObject(ObjectInputStream.java:1769)
	at java.io.ObjectInputStream.readObject0(ObjectInputStream.java:1348)
	at java.io.ObjectInputStream.readObject(ObjectInputStream.java:370)
	at Deserialiser.main(Deserialiser.java:18)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
~~~

<p><cite>serialver</cite> #ftw!</p>

