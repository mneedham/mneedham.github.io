+++
draft = false
date="2013-07-21 11:07:11"
title="Jersey: Listing all resources, paths, verbs to build an entry point/index for an API"
tag=['jersey']
category=['Java']
+++

<p>I've been playing around with <a href="https://jersey.java.net/">Jersey</a> over the past couple of days and one thing I wanted to do was create an entry point or index which listed all my resources, the available paths and the verbs they accepted.</p>


<p><a href="http://stackoverflow.com/users/1657364/guido-simone">Guido Simone</a> explained <a href="http://stackoverflow.com/questions/13484350/find-a-list-of-all-jersey-resource-methods-in-my-app">a neat way of finding the paths and verbs for a specific resource</a> using Jersey's <cite><a href="http://grepcode.com/file/repo1.maven.org/maven2/com.sun.jersey/jersey-server/1.0.3/com/sun/jersey/server/impl/modelapi/annotation/IntrospectionModeller.java">IntrospectionModeller</a></cite>:</p>



~~~java

AbstractResource resource = IntrospectionModeller.createResource(JacksonResource.class);
System.out.println("Path is " + resource.getPath().getValue());

String uriPrefix = resource.getPath().getValue();
for (AbstractSubResourceMethod srm :resource.getSubResourceMethods())
{
    String uri = uriPrefix + "/" + srm.getPath().getValue();
    System.out.println(srm.getHttpMethod() + " at the path " + uri + " return " + srm.getReturnType().getName());
}
~~~

<p>If we run that against <a href="https://github.com/mneedham/j4-minimal">j4-minimal</a>'s <cite><a href="https://github.com/mneedham/j4-minimal/blob/master/src/main/java/com/g414/j4/minimal/JacksonResource.java">JacksonResource</a></cite> class we get the following output:</p>



~~~text

Path is /jackson
GET at the path /jackson/{who} return com.g414.j4.minimal.JacksonResource$Greeting
GET at the path /jackson/awesome/{who} return javax.ws.rs.core.Response
~~~

<p>That's pretty neat but I didn't want to have to manually list all my resources since I've already done that using Guice .</p>


<p>I needed a way to programatically get hold of them and I partially found the way to do this from <a href="http://stackoverflow.com/questions/3132944/javaee6rest-how-do-i-get-all-rest-resources-at-runtime">this post</a> which suggests using <cite>Application.getSingletons()</cite>.</p>


<p>I actually ended up using <cite>Application.getClasses()</cite> and I ended up with <cite><a href="https://github.com/mneedham/j4-minimal/blob/249078d2c8e982b81ae810310eb2340fa4fd909f/src/main/java/com/g414/j4/minimal/ResourceListingResource.java">ResourceListingResource</a></cite>:</p>



~~~java

@Path("/")
public class ResourceListingResource
{
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response showAll( @Context Application application,
                             @Context HttpServletRequest request)
    {
        String basePath = request.getRequestURL().toString();

        ObjectNode root = JsonNodeFactory.instance.objectNode();
        ArrayNode resources = JsonNodeFactory.instance.arrayNode();

        root.put( "resources", resources );

        for ( Class<?> aClass : application.getClasses() )
        {
            if ( isAnnotatedResourceClass( aClass ) )
            {
                AbstractResource resource = IntrospectionModeller.createResource( aClass );
                ObjectNode resourceNode = JsonNodeFactory.instance.objectNode();
                String uriPrefix = resource.getPath().getValue();

                for ( AbstractSubResourceMethod srm : resource.getSubResourceMethods() )
                {
                    String uri = uriPrefix + "/" + srm.getPath().getValue();
                    addTo( resourceNode, uri, srm, joinUri(basePath, uri) );
                }

                for ( AbstractResourceMethod srm : resource.getResourceMethods() )
                {
                    addTo( resourceNode, uriPrefix, srm, joinUri( basePath, uriPrefix ) );
                }

                resources.add( resourceNode );
            }

        }


        return Response.ok().entity( root ).build();
    }

    private void addTo( ObjectNode resourceNode, String uriPrefix, AbstractResourceMethod srm, String path )
    {
        if ( resourceNode.get( uriPrefix ) == null )
        {
            ObjectNode inner = JsonNodeFactory.instance.objectNode();
            inner.put("path", path);
            inner.put("verbs", JsonNodeFactory.instance.arrayNode());
            resourceNode.put( uriPrefix, inner );
        }

        ((ArrayNode) resourceNode.get( uriPrefix ).get("verbs")).add( srm.getHttpMethod() );
    }


    private boolean isAnnotatedResourceClass( Class rc )
    {
        if ( rc.isAnnotationPresent( Path.class ) )
        {
            return true;
        }

        for ( Class i : rc.getInterfaces() )
        {
            if ( i.isAnnotationPresent( Path.class ) )
            {
                return true;
            }
        }

        return false;
    }

}
~~~

<p>The only change I've made from Guido Simone's solution is that I also call <cite>resource.getResourceMethods()</cite> because <cite>resource.getSubResourceMethods()</cite> only returns methods which have a <cite>@Path</cite> annotation.</p>


<p>Since we'll sometimes define our path at the class level and then define different verbs that operate on that resource it misses some methods out.</p>


<p>If we run a cURL command (<a href="http://stackoverflow.com/questions/352098/how-to-pretty-print-json-from-the-command-line">piped through python to make it look nice</a>) against the root we get the following output:</p>



~~~bash

$ curl http://localhost:8080/ -w "\n" 2>/dev/null | python -mjson.tool

{
    "resources": [
        {
            "/bench": {
                "path": "http://localhost:8080/bench",
                "verbs": [
                    "GET",
                    "POST",
                    "PUT",
                    "DELETE"
                ]
            }
        },
        {
            "/sample/{who}": {
                "path": "http://localhost:8080/sample/{who}",
                "verbs": [
                    "GET"
                ]
            }
        },
        {
            "/jackson/awesome/{who}": {
                "path": "http://localhost:8080/jackson/awesome/{who}",
                "verbs": [
                    "GET"
                ]
            },
            "/jackson/{who}": {
                "path": "http://localhost:8080/jackson/{who}",
                "verbs": [
                    "GET"
                ]
            }
        },
        {
            "/": {
                "path": "http://localhost:8080/",
                "verbs": [
                    "GET"
                ]
            }
        }
    ]
}
~~~
