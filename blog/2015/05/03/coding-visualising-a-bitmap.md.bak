+++
draft = false
date="2015-05-03 00:19:51"
title="Coding: Visualising a bitmap"
tag=['coding']
category=['Coding', 'Java']
+++

<p>Over the last month or so I've spent some time each day reading a new part of the Neo4j code base to get more familiar with it, and one of my favourite classes is the <a href="https://github.com/neo4j/neo4j/blob/2.3/community/kernel/src/main/java/org/neo4j/kernel/impl/util/Bits.java">Bits</a> class which does all things low level on the wire and to disk.</p>


<p>In particular I like its toString method which returns a binary representation of the values that we're storing in bytes, ints and longs.
</p>


<p>I thought it'd be a fun exercise to try and write my own function which takes in a 32 bit map and returns a string containing a 1 or 0 depending if a bit is set or not.
</p>


<p>
The key insight is that we need to iterate down from the highest order bit and then create a bit mask of that value and do a bitwise and with the full bitmap. If the result of that calculation is 0 then the bit isn't set, otherwise it is.
</p>


<p>For example, to check if the highest order bit (index 31) was set our bit mask would have the 32nd bit set and all of the others 0'd out.</p>



~~~java

java> (1 << 31) & 0x80000000
java.lang.Integer res5 = -2147483648
~~~

<p>
If we wanted to check if lowest order bit was set then we'd run this computation instead:
</p>



~~~java

java> (1 << 0) & 0x00000001
java.lang.Integer res7 = 0

java> (1 << 0) & 0x00000001
java.lang.Integer res8 = 1
~~~

<p>Now let's put that into a function which checks all 32 bits of the bitmap rather than just the ones we define:</p>



~~~java

private String  asString( int bitmap )
{
    StringBuilder sb = new StringBuilder();
    sb.append( "[" );
    for ( int i = Integer.SIZE - 1; i >= 0; i-- )
    {
        int bitMask = 1 << i;
        boolean bitIsSet = (bitmap & bitMask) != 0;
        sb.append( bitIsSet ? "1" : "0" );

        if ( i > 0 &&  i % 8 == 0 )
        {
            sb.append( "," );
        }
    }
    sb.append( "]" );
    return sb.toString();
}
~~~

<p>
And a quick test to check it works:
</p>




~~~java

@Test
public void shouldInspectBits()
{
    System.out.println(asString( 0x00000001 ));
    // [00000000,00000000,00000000,00000001]

    System.out.println(asString( 0x80000000 ));
    // [10000000,00000000,00000000,00000000]

    System.out.println(asString( 0xA0 ));
    // [00000000,00000000,00000000,10100000]

    System.out.println(asString( 0xFFFFFFFF ));
    // [11111111,11111111,11111111,11111111]
}
~~~

<p>
Neat!
</p>

