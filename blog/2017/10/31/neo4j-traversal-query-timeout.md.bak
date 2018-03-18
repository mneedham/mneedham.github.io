+++
draft = false
date="2017-10-31 21:43:17"
title="Neo4j: Traversal query timeout"
tag=['neo4j', 'traversal-api']
category=['neo4j']
description="Learn how to set a timeout in a Neo4j user defined procedure that uses the traversal API."
+++

<p>
I've been spending some of my spare time over the last few weeks creating an application that generates running routes from <a href="https://www.ordnancesurvey.co.uk/business-and-government/products/os-open-roads.html">Open Roads</a> data - transformed and imported into Neo4j of course! 
</p>


<p>
I've created a user defined procedure which combines several shortest path queries, but I wanted to exit any of these shortest path searches if they were taking too long. My code without a timeout looks like this:
</p>



~~~java

StandardExpander orderedExpander = new OrderedByTypeExpander()
    .add( RelationshipType.withName( "CONNECTS" ), Direction.BOTH );

PathFinder<Path> shortestPathFinder = GraphAlgoFactory.shortestPath( expander, 250 );

...
~~~

<p>
There are several places where we could check the time elapsed, but the <cite>expand</cite> method in the <cite>Expander</cite> seemed like an obvious one to me. I wrote my own <cite>Expander</cite> class which looks like this:
</p>



~~~java

public class TimeConstrainedExpander implements PathExpander
{
    private final StandardExpander expander;
    private final long startTime;
    private final Clock clock;
    private int pathsExpanded = 0;
    private long timeLimitInMillis;

    public TimeConstrainedExpander( StandardExpander expander, Clock clock, long timeLimitInMillis )
    {
        this.expander = expander;
        this.clock = clock;
        this.startTime = clock.instant().toEpochMilli();
        this.timeLimitInMillis = timeLimitInMillis;
    }

    @Override
    public Iterable<Relationship> expand( Path path, BranchState state )
    {
        long timeSoFar = clock.instant().toEpochMilli() - startTime;
        if ( timeSoFar > timeLimitInMillis )
        {
            return Collections.emptyList();
        }

        return expander.expand( path, state );
    }

    @Override
    public PathExpander reverse()
    {
        return expander.reverse();
    }
}

~~~

<p>
The code snippet from earlier now needs to be updated to use our new class, which isn't too tricky:
</p>



~~~java

StandardExpander orderedExpander = new OrderedByTypeExpander()
    .add( RelationshipType.withName( "CONNECTS" ), Direction.BOTH );

TimeConstrainedExpander expander = new TimeConstrainedExpander(orderedExpander, 
    Clock.systemUTC(), 200);

PathFinder<Path> shortestPathFinder = GraphAlgoFactory.shortestPath( expander, 250 );
...
~~~

<p>
I'm not sure if this is the best way to achieve what I want but after failing with several other approaches at least this one actually works!
</p>

