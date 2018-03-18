+++
draft = false
date="2014-07-23 22:20:25"
title="Java: Determining the status of data import using kill signals"
tag=['java']
category=['Java']
+++

<p>A few weeks ago I was working on the initial import of ~ 60 million bits of data into Neo4j and we kept running into a problem where the import process just seemed to freeze and nothing else was imported.</p>


<p>It was very difficult to tell what was happening inside the process - taking a thread dump merely informed us that it was attempting to process one line of a CSV line and was somehow unable to do so.</p>


<p>One way to help debug this would have been to print out every single line of the CSV as we processed it and then watch where it got stuck but this seemed a bit over kill. Ideally we wanted to only print out the line we were processing on demand.</p>


<p>As luck would have it we can do exactly this by sending a kill signal to our import process and have it print out where it had got up to. We had to make sure we picked a signal which wasn't already being handled by the JVM and decided to go with 'SIGTRAP' i.e. kill -5 [pid]</p>


<p>We came across <a href="http://www.javawebdevelop.com/300909/">a neat blog post that explained how to wire everything up</a> and then created our own version:</p>



~~~java

class Kill3Handler implements SignalHandler
{
    private AtomicInteger linesProcessed;
    private AtomicReference<Map<String, Object>> lastRowProcessed;

    public Kill3Handler( AtomicInteger linesProcessed, AtomicReference<Map<String, Object>> lastRowProcessed )
    {
        this.linesProcessed = linesProcessed;
        this.lastRowProcessed = lastRowProcessed;
    }

    @Override
    public void handle( Signal signal )
    {
        System.out.println("Last Line Processed: " + linesProcessed.get() + " " + lastRowProcessed.get());
    }
}
~~~

<p>We then wired that up like so:</p>



~~~java

AtomicInteger linesProcessed = new AtomicInteger( 0 );
AtomicReference<Map<String, Object>> lastRowProcessed = new AtomicReference<>(  );
Kill3Handler kill3Handler = new Kill3Handler( linesProcessed, lastRowProcessed );
Signal.handle(new Signal("TRAP"), kill3Handler);

// as we iterate each line we update those variables

linesProcessed.incrementAndGet();
lastRowProcessed.getAndSet( properties ); // properties = a representation of the row we're processing
~~~

<p>This worked really well for us and we were able to work out that we had a slight problem with some of the data in our CSV file which was causing it to be processed incorrectly.</p>


<p>We hadn't been able to see this by visual inspection since the CSV files were a few GB in size. We'd therefore only skimmed a few lines as a sanity check.</p>


<p>I didn't even know you could do this but it's a neat trick to keep in mind - I'm sure it shall come in useful again.</p>

