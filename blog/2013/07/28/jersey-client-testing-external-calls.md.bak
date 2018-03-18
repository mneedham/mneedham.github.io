+++
draft = false
date="2013-07-28 20:43:24"
title="Jersey Client: Testing external calls"
tag=['java', 'jersey']
category=['Java']
+++

<p><a href="https://twitter.com/jimwebber">Jim</a> and I have been doing a bit of work over the last week which involved calling neo4j's <a href="http://docs.neo4j.org/chunked/stable/ha-rest-info.html">HA status URI to check whether or not an instance was a master/slave</a> and we've been using <a href="https://jersey.java.net/documentation/latest/user-guide.html#client">jersey-client</a>.</p>


<p>The code looked roughly like this:</p>



~~~java

class Neo4jInstance {
    private Client httpClient;
    private URI hostname;

    public Neo4jInstance(Client httpClient, URI hostname) {
        this.httpClient = httpClient;
        this.hostname = hostname;
    }

    public Boolean isSlave() {
        String slaveURI = hostname.toString() + ":7474/db/manage/server/ha/slave";
        ClientResponse response = httpClient.resource(slaveURI).accept(TEXT_PLAIN).get(ClientResponse.class);
        return Boolean.parseBoolean(response.getEntity(String.class));
    }
}
~~~

<p>While writing some tests against this code we wanted to stub out the actual calls to the HA slave URI so we could simulate both conditions and a brief search suggested that <a href="http://stackoverflow.com/questions/11005279/how-do-i-unit-test-code-which-calls-the-jersey-client-api">mockito was the way to go</a>.</p>


<p>We ended up with a test that looked like this:</p>



~~~java

@Test
public void shouldIndicateInstanceIsSlave() {
    Client client = mock( Client.class );
    WebResource webResource = mock( WebResource.class );
    WebResource.Builder builder = mock( WebResource.Builder.class );

    ClientResponse clientResponse = mock( ClientResponse.class );
    when( builder.get( ClientResponse.class ) ).thenReturn( clientResponse );
    when( clientResponse.getEntity( String.class ) ).thenReturn( "true" );
    when( webResource.accept( anyString() ) ).thenReturn( builder );
    when( client.resource( anyString() ) ).thenReturn( webResource );

    Boolean isSlave = new Neo4jInstance(client, URI.create("http://localhost")).isSlave();

    assertTrue(isSlave);
}
~~~

<p>which is pretty gnarly but does the job.</p>


<p>I thought there must be a better way so I continued searching and eventually came across <a href="http://jersey.576304.n2.nabble.com/How-to-test-a-REST-client-Jersey-td5184618.html">this post on the mailing list</a> which suggested creating a custom ClientHandler and stubbing out requests/responses there.</p>


<p>I had a go at doing that and wrapped it with a little DSL that only covers our very specific use case:</p>



~~~java

private static ClientBuilder client() {
    return new ClientBuilder();
}

static class ClientBuilder {
    private String uri;
    private int statusCode;
    private String content;

    public ClientBuilder requestFor(String uri) {
        this.uri = uri;
        return this;
    }

    public ClientBuilder returns(int statusCode) {
        this.statusCode = statusCode;
        return this;
    }

    public Client create() {
        return new Client() {
            public ClientResponse handle(ClientRequest request) throws ClientHandlerException {
                if (request.getURI().toString().equals(uri)) {
                    InBoundHeaders headers = new InBoundHeaders();
                    headers.put("Content-Type", asList("text/plain"));
                    return createDummyResponse(headers);
                }
                throw new RuntimeException("No stub defined for " + request.getURI());
            }
        };
    }

    private ClientResponse createDummyResponse(InBoundHeaders headers) {
        return new ClientResponse(statusCode, headers, new ByteArrayInputStream(content.getBytes()), messageBodyWorkers());
    }

    private MessageBodyWorkers messageBodyWorkers() {
        return new MessageBodyWorkers() {
            public Map<MediaType, List<MessageBodyReader>> getReaders(MediaType mediaType) {
                return null;
            }

            public Map<MediaType, List<MessageBodyWriter>> getWriters(MediaType mediaType) {
                return null;
            }

            public String readersToString(Map<MediaType, List<MessageBodyReader>> mediaTypeListMap) {
                return null;
            }

            public String writersToString(Map<MediaType, List<MessageBodyWriter>> mediaTypeListMap) {
                return null;
            }

            public <T> MessageBodyReader<T> getMessageBodyReader(Class<T> tClass, Type type, Annotation[] annotations, MediaType mediaType) {
                return (MessageBodyReader<T>) new StringProvider();
            }

            public <T> MessageBodyWriter<T> getMessageBodyWriter(Class<T> tClass, Type type, Annotation[] annotations, MediaType mediaType) {
                return null;
            }

            public <T> List<MediaType> getMessageBodyWriterMediaTypes(Class<T> tClass, Type type, Annotation[] annotations) {
                return null;
            }

            public <T> MediaType getMessageBodyWriterMediaType(Class<T> tClass, Type type, Annotation[] annotations, List<MediaType> mediaTypes) {
                return null;
            }
        };
    }

    public ClientBuilder content(String content) {
        this.content = content;
        return this;
    }
}
~~~

<p>If we change our test to use this code it now looks like this:</p>



~~~java

@Test
public void shouldIndicateInstanceIsSlave() {
    Client client = client().requestFor("http://localhost:7474/db/manage/server/ha/slave").
                             returns(200).
                             content("true").
                             create();
    Boolean isSlave = new Neo4jInstance(client, URI.create("http://localhost")).isSlave();
    assertTrue(isSlave);
}
~~~

<p>Is there a better way?</p>


<p>In Ruby I've used <a href="https://github.com/bblimke/webmock">WebMock</a> to achieve this and <a href="https://twitter.com/a5hok">Ashok</a> pointed me towards <a href="https://github.com/tusharm/WebStub">WebStub</a> which looks nice except I'd need to pass in the hostname + port rather than constructing that in the code.<p>
