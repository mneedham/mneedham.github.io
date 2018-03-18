+++
draft = false
date="2014-04-30 01:24:33"
title="Jersey/Jax RS: Streaming JSON"
tag=['java', 'jersey']
category=['Java']
+++

<p>About a year ago I wrote a blog post showing how to <a href="http://www.markhneedham.com/blog/2013/07/08/jax-rs-streaming-a-response-using-streamingoutput/">stream a HTTP response using Jersey/Jax RS</a> and I recently wanted to do the same thing but this time using JSON.</p>


<p>A common pattern is to take our Java object and get a JSON string representation of that but that isn't the most efficient use of memory because we now have the Java object and a string representation.</p>
 

<p>This is particularly problematic if we need to return a lot of the data in a response.</p>


<p>By writing a little bit more code we can get our response to stream to the client as soon as some of it is ready rather than building the whole result and sending it all in one go:</p>



~~~java

@Path("/resource")
public class MadeUpResource
{
    private final ObjectMapper objectMapper;

    public MadeUpResource() {
        objectMapper = new ObjectMapper();
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadHierarchy(@PathParam( "pkPerson" ) String pkPerson) {
        final Map<Integer, String> people  = new HashMap<>();
        people.put(1, "Michael");
        people.put(2, "Mark");

        StreamingOutput stream = new StreamingOutput() {
            @Override
            public void write(OutputStream os) throws IOException, WebApplicationException
            {
                JsonGenerator jg = objectMapper.getJsonFactory().createJsonGenerator( os, JsonEncoding.UTF8 );
                jg.writeStartArray();

                for ( Map.Entry<Integer, String> person : people.entrySet()  )
                {
                    jg.writeStartObject();
                    jg.writeFieldName( "id" );
                    jg.writeString( person.getKey().toString() );
                    jg.writeFieldName( "name" );
                    jg.writeString( person.getValue() );
                    jg.writeEndObject();
                }
                jg.writeEndArray();

                jg.flush();
                jg.close();
            }
        };


        return Response.ok().entity( stream ).type( MediaType.APPLICATION_JSON ).build()    ;
    }
}
~~~

<p>If we run that this is the output we'd see:</p>



~~~text

[{"id":"1","name":"Michael"},{"id":"2","name":"Mark"}]
~~~

<p>It's a simple example but hopefully it's easy to see how we could translate that if we wanted to stream more complex data.</p>

