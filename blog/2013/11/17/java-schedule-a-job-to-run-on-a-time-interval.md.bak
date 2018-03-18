+++
draft = false
date="2013-11-17 22:58:35"
title="Java: Schedule a job to run on a time interval"
tag=['java']
category=['Java']
+++

<p>Recently I've spent some time building a set of tests around rolling upgrades between <a href="http://www.neo4j.org/">Neo4j</a> versions and as part of that I wanted to log the state of the cluster as the upgrade was happening.</p>


<p>The main thread of the test blocks waiting until the upgrade is done so I wanted to log on another thread every few seconds. Alistair pointed me at the <cite><a href="http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html">ScheduledExecutorService</a></cite> which worked quite nicely.</p>


<p>I ended up with a test which looked roughly like this:</p>



~~~java

public class MyUpgradeTest {
    @Test
    public void shouldUpgradeFromOneVersionToAnother() throws InterruptedException
    {
        ScheduledExecutorService scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
        scheduledExecutorService.scheduleAtFixedRate( new LogAllTheThings(), 0, 1, TimeUnit.SECONDS );

        Thread.sleep(10000);
        // do upgrade of cluster
        scheduledExecutorService.shutdown();
    }

    static class LogAllTheThings implements Runnable
    {
        @Override
        public void run()
        {
            Date time = new Date( System.currentTimeMillis() );

            try
            {
                Map<String, Object> masterProperties = selectedProperties( client(), URI.create( "http://localhost:7474/" ) );
                System.out.println( String.format( "%s: %s", time, masterProperties ) );
            }
            catch ( Exception ignored )
            {
                ignored.printStackTrace();
            }
        }

        private static Client client()
        {
            DefaultClientConfig defaultClientConfig = new DefaultClientConfig();
            defaultClientConfig.getClasses().add( JacksonJsonProvider.class );
            return Client.create( defaultClientConfig );
        }

        public static Map<String, Object> selectedProperties( Client client, URI uri )
        {
            Map<String, Object> jmxProperties = new HashMap<String, Object>();

            ArrayNode transactionsProperties = jmxBean( client, uri, "org.neo4j/instance%3Dkernel%230%2Cname%3DTransactions" );
            addProperty( jmxProperties, transactionsProperties, "LastCommittedTxId" );

            ArrayNode kernelProperties = jmxBean( client, uri, "org.neo4j/instance%3Dkernel%230%2Cname%3DKernel" );
            addProperty( jmxProperties, kernelProperties, "KernelVersion" );

            ArrayNode haProperties = jmxBean( client, uri, "org.neo4j/instance%3Dkernel%230%2Cname%3DHigh+Availability" );
            addProperty( jmxProperties, haProperties, "Role" );
            addProperty( jmxProperties, haProperties, "InstanceId" );

            return jmxProperties;
        }

        private static void addProperty( Map<String, Object> jmxProperties, ArrayNode properties, String propertyName )
        {
            jmxProperties.put( propertyName, getProperty( properties, propertyName ) );
        }

        private static String getProperty( ArrayNode properties, String propertyName )
        {
            for ( JsonNode property : properties )
            {
                if ( property.get( "name" ).asText().equals( propertyName ) )
                {
                    return property.get( "value" ).asText();
                }
            }

            throw new RuntimeException( "Could not find requested property: " + propertyName );
        }

        private static ArrayNode jmxBean( Client client, URI uri, String beanExtension )
        {
            ClientResponse clientResponse = client
                    .resource( uri + "db/manage/server/jmx/domain/" + beanExtension )
                    .accept( MediaType.APPLICATION_JSON )
                    .get( ClientResponse.class );

            JsonNode transactionsBean = clientResponse.getEntity( JsonNode.class );
            return (ArrayNode) transactionsBean.get( 0 ).get( "attributes" );
        }
    }
}
~~~

<p><cite>LogAllTheThings</cite> gets called once every second and it logs the KernelVersion, InstanceId, LastCommittedTxId and Role which Neo4j server exposes as JMX properties.</p>


<p>If we run that against a local Neo4j cluster we'd see something like the following:</p>



~~~text

Sun Nov 17 22:31:55 GMT 2013: {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
Sun Nov 17 22:31:56 GMT 2013: {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
Sun Nov 17 22:31:57 GMT 2013: {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
Sun Nov 17 22:31:58 GMT 2013: {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
Sun Nov 17 22:31:59 GMT 2013: {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
...
removed for brevity
~~~

<p>The next step was to get the properties of all the members of the cluster at the same time and to do that we can introduce another <cite>ExecutorService</cite> which has a thread pool of 3 so that it will evaluate each machine (at least close to) simultaneously:</p>



~~~java

    static class LogAllTheThings implements Runnable
    {
        private ExecutorService executorService = Executors.newFixedThreadPool( 3 );

        @Override
        public void run()
        {
            List<URI> machines = new ArrayList<>(  );
            machines.add(URI.create( "http://localhost:7474/" ));
            machines.add(URI.create( "http://localhost:7484/" ));
            machines.add(URI.create( "http://localhost:7494/" ));

            Map<URI, Future<Map<String, Object>>> futureJmxProperties = new HashMap<>(  );
            for ( final URI machine : machines )
            {
                Future<Map<String, Object>> futureProperties = executorService.submit( new Callable<Map<String, Object>>()
                {
                    @Override
                    public Map<String, Object> call() throws Exception
                    {
                        try
                        {
                            return selectedProperties( client(), machine );
                        }
                        catch ( Exception ignored )
                        {
                            ignored.printStackTrace();
                            return new HashMap<>();
                        }
                    }
                } );

                futureJmxProperties.put( machine, futureProperties );
            }

            Date time = new Date( System.currentTimeMillis() );
            System.out.println( time );
            for ( Map.Entry<URI, Future<Map<String, Object>>> uriFutureEntry : futureJmxProperties.entrySet() )
            {
                try
                {
                    System.out.println( "==> " + uriFutureEntry.getValue().get() );
                }
                catch ( Exception ignored )
                {

                }
            }
        }

        // other methods the same as above
    }
~~~

<p>We submit each job to the <cite>ExecutorService</cite> and receive back a <cite>Future</cite> which we store in a map before retrieving its result later on. If we run that we'll see the following output:</p>



~~~text

Sun Nov 17 22:49:58 GMT 2013
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=2, LastCommittedTxId=18, Role=slave}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=3, LastCommittedTxId=18, Role=slave}
Sun Nov 17 22:49:59 GMT 2013
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=2, LastCommittedTxId=18, Role=slave}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=3, LastCommittedTxId=18, Role=slave}
Sun Nov 17 22:50:00 GMT 2013
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=1, LastCommittedTxId=18, Role=master}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=2, LastCommittedTxId=18, Role=slave}
==> {KernelVersion=Neo4j - Graph Database Kernel 2.0.0-M06, InstanceId=3, LastCommittedTxId=18, Role=slave}

...
removed for brevity
~~~

<p>Overall the approach works quite well although I'm always open to learning of a better way if there is one!</p>

