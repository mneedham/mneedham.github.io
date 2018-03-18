+++
draft = false
date="2011-03-24 21:58:31"
title="Java: Faking System.in"
tag=['java']
category=['Java']
+++

We ran a <a href="http://www.markhneedham.com/blog/2011/03/22/thoughtworks-university-a-refactoring-dojo/">refactoring dojo</a> a couple of days ago at ThoughtWorks University and in preparation I wrote some system level tests around <a href="https://github.com/mneedham/biblioteca/blob/master/src/main/Program.java">the coding problem</a> that we were going to use during the session.

It's a command line application which is called through the main method of 'Program' and since there's no dependency injection we need to be able to set System.in and System.out in order to do any testing.

My initial thinking was that it should be possible to fake System.in with the following code:


~~~java

String input = "1\n9\n";
System.setIn(new ByteArrayInputStream(input.getBytes()));
~~~

This works fine when I just want to simulate one value being passed to System.in but it doesn't work so well if I want to simulate passing more than one value because we had a BufferedReader being created each time we loop.


~~~java

...
while(true) {
	...
	InputStreamReader inputStream = new InputStreamReader(System.in);
	BufferedReader reader = new BufferedReader(inputStream);
	...
}
~~~

This means that the second time System.in gets read it is empty.

<a href="http://jimbarritt.com/non-random/">Jim</a> and I paired on the problem for a bit and came to the conclusion that we'd need to 'stub' the 'read' method of 'InputStream' if we wanted to be able to control exactly what was being returned by System.in.

We eventually ended up with the following <a href="https://github.com/mneedham/biblioteca/blob/master/src/test/StubbedInputStream.java">StubbedInputStream</a>:


~~~java

class StubbedInputStream extends InputStream {
    private Queue<String> input;

    public StubbedInputStream(Queue<String> input) {
        this.input = input;
    }

    @Override
    public int read(byte[] bytes, int i, int i1) throws IOException {
        if(input.isEmpty()) {
            return -1;
        }

        int byteLocation = 0;
        for(byte b : input.remove().getBytes()) {
            bytes[byteLocation] = b;
            byteLocation++;
        }
        bytes[byteLocation] = "\n".getBytes()[0];
        return byteLocation + 1;
    }

	public static InputStreamBuilder stubInputStream() {
        return new InputStreamBuilder();
    }
	...
}
~~~

Which can be constructed using the <a href="https://github.com/mneedham/biblioteca/blob/master/src/test/InputStreamBuilder.java">following DSL</a>:


~~~java

System.setIn(stubInputStream().toReturn("1").then("9").atSomePoint());
~~~

The code we wrote is on <a href="https://github.com/mneedham/biblioteca/tree/master/src">github</a> - I'm not sure that it covers every possible scenario that you might come up with but it does pass the tests that I've managed to come up with!
