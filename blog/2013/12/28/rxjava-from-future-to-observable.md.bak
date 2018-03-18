+++
draft = false
date="2013-12-28 21:46:42"
title="RxJava: From Future to Observable"
tag=['java']
category=['Java']
+++

<p>I first came across <a href="https://rx.codeplex.com/">Reactive Extensions</a> about 4 years ago on <a href="http://weblogs.asp.net/podwysocki/">Matthew Podwysocki's blog</a> but then haven't heard much about it until I saw Matthew give a talk at <a href="http://codemesh.io/">Code Mesh</a> a few weeks ago.</p>


<p>It seems to have grown in popularity recently and I noticed that's there's now a Java version called <a href="https://github.com/Netflix/RxJava">RxJava</a> <a href="http://techblog.netflix.com/2013/02/rxjava-netflix-api.html">written by Netflix</a>.</p>


<p>I thought I'd give it a try by changing <a href="http://www.markhneedham.com/blog/2013/12/23/neo4j-cypher-using-merge-with-schema-indexesconstraints/">some code I wrote while exploring cypher's MERGE function</a> to expose an Observable instead of Futures.</p>


<p>To recap, we have 50 threads and we do 100 iterations where we create random (user, event) pairs. We create a maximum of 10 users and 50 events and the goal is to concurrently send requests for the same pairs.</p>


<p>In the example of my other post I was throwing away the result of each query whereas here I returned the result back so I had something to subscribe to.</p>


<p>The outline of the code looks like this:</p>



~~~java

public class MergeTimeRx
{
    public static void main( final String[] args ) throws InterruptedException, IOException
    {
        String pathToDb = "/tmp/foo";
        FileUtils.deleteRecursively( new File( pathToDb ) );

        GraphDatabaseService db = new GraphDatabaseFactory().newEmbeddedDatabase( pathToDb );
        final ExecutionEngine engine = new ExecutionEngine( db );

        int numberOfThreads = 50;
        int numberOfUsers = 10;
        int numberOfEvents = 50;
        int iterations = 100;

        Observable<ExecutionResult> events = processEvents( engine, numberOfUsers, numberOfEvents, numberOfThreads, iterations );

        events.subscribe( new Action1<ExecutionResult>()
        {
            @Override
            public void call( ExecutionResult result )
            {
                for ( Map<String, Object> row : result )
                {
                }
            }
        } );

        ....
    }

}
~~~

<p>The nice thing about using RxJava is that there's no mention of how we got our collection of <cite>ExecutionResult</cite>s, it's not important. We just have a stream of them and by calling the <cite>subscribe</cite> function on the <cite>Observable</cite> we'll be informed whenever another one is made available.</p>


<p>Most of the examples I found show how to generate events from a single thread but I wanted to use a thread pool so that I could fire off lots of requests at the same time. The <cite>processEvents</cite> method ended up looking like this:</p>



~~~java

    private static Observable<ExecutionResult> processEvents( final ExecutionEngine engine, final int numberOfUsers, final int numberOfEvents, final int numberOfThreads, final int iterations )
    {
        final Random random = new Random();
        final List<Integer> userIds = generateIds( numberOfUsers );
        final List<Integer> eventIds = generateIds( numberOfEvents );

        return Observable.create( new Observable.OnSubscribeFunc<ExecutionResult>()
        {
            @Override
            public Subscription onSubscribe( final Observer<? super ExecutionResult> observer )
            {
                final ExecutorService executor = Executors.newFixedThreadPool( numberOfThreads );

                List<Future<ExecutionResult>> jobs = new ArrayList<>();
                for ( int i = 0; i < iterations; i++ )
                {
                    Future<ExecutionResult> job = executor.submit( new Callable<ExecutionResult>()
                    {
                        @Override
                        public ExecutionResult call()
                        {
                            Integer userId = userIds.get( random.nextInt( numberOfUsers ) );
                            Integer eventId = eventIds.get( random.nextInt( numberOfEvents ) );

                            return engine.execute(
                                    "MERGE (u:User {id: {userId}})\n" +
                                    "MERGE (e:Event {id: {eventId}})\n" +
                                    "MERGE (u)-[:HAS_EVENT]->(e)\n" +
                                    "RETURN u, e",
                                    MapUtil.map( "userId", userId, "eventId", eventId ) );
                        }
                    } );
                    jobs.add( job );
                }

                for ( Future<ExecutionResult> future : jobs )
                {
                    try
                    {
                        observer.onNext( future.get() );
                    }
                    catch ( InterruptedException | ExecutionException ignored )
                    {
                    }
                }

                observer.onCompleted();
                executor.shutdown();

                return Subscriptions.empty();
            }
        } );
    }

~~~

<p>I'm not sure if that's the correct way of using <cite>Observable</cite>s so please let me know in the comments if I've got it wrong.<p>

<p>I wasn't sure what the proper way of handling errors was. I initially had a call to <cite>observer#onError</cite> in the catch block but that means that no further events are produced which wasn't what I wanted.</p>


<p>The code is <a href="https://gist.github.com/mneedham/8164614">available as a gist</a> if you want to play around with it. I added the following dependency to get the RxJava library:</p>



~~~xml

    <dependency>
      <groupId>com.netflix.rxjava</groupId>
      <artifactId>rxjava-core</artifactId>
      <version>0.15.1</version>
    </dependency>

~~~
