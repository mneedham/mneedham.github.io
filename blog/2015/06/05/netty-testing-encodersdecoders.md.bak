+++
draft = false
date="2015-06-05 21:25:25"
title="Netty: Testing encoders/decoders"
tag=['java', 'netty']
category=['Java']
+++

<p>I've been working with Netty a bit recently and having built a pipeline of encoders/decoders as described in this <a href="http://seeallhearall.blogspot.co.uk/2012/05/netty-tutorial-part-1-introduction-to.html">excellent tutorial</a> wanted to test that the encoders and decoders were working without having to send real messages around.</p>


<p>Luckily there is a <a href="https://netty.io/4.0/api/io/netty/channel/embedded/EmbeddedChannel.html">EmbeddedChannel</a> which makes our life very easy indeed.</p>


<p>Let's say we've got a message 'Foo' that we want to send across the wire. It only contains a single integer value so we'll just send that and reconstruct 'Foo' on the other side.</p>


<p>We might write the following encoder to do this:</p>



~~~java

// Examples uses Netty 4.0.28.Final
public static class MessageEncoder extends MessageToMessageEncoder<Foo>
{
    @Override
    protected void encode( ChannelHandlerContext ctx, Foo msg, List<Object> out ) throws Exception
    {
        ByteBuf buf = ctx.alloc().buffer();
        buf.writeInt( msg.value() );
        out.add( buf );
    }
}

public static class Foo
{
    private Integer value;

    public Foo(Integer value)
    {
        this.value = value;
    }

    public int value()
    {
        return value;
    }
}
~~~

<p>
So all we're doing is taking the 'value' field out of 'Foo' and putting it into the list which gets passed downstream.
</p>


<p>Let's write a test which simulates sending a 'Foo' message and has an empty decoder attempt to process the message:
</p>



~~~java

@Test
public void shouldEncodeAndDecodeVoteRequest()
{
    // given
    EmbeddedChannel channel = new EmbeddedChannel( new MessageEncoder(), new MessageDecoder() );

    // when
    Foo foo = new Foo( 42 );
    channel.writeOutbound( foo );
    channel.writeInbound( channel.readOutbound() );

    // then
    Foo returnedFoo = (Foo) channel.readInbound();
    assertNotNull(returnedFoo);
    assertEquals( foo.value(), returnedFoo.value() );
}

public static class MessageDecoder extends MessageToMessageDecoder<ByteBuf>
{
    @Override
    protected void decode( ChannelHandlerContext ctx, ByteBuf msg, List<Object> out ) throws Exception { }
}
~~~

<p>So in the test we write 'Foo' to the outbound channel and then read it back into the inbound channel and then check what we've got. If we run that test now this is what we'll see:</p>



~~~java

junit.framework.AssertionFailedError
	at NettyTest.shouldEncodeAndDecodeVoteRequest(NettyTest.java:28)
~~~

<p>
The message we get back is null which makes sense given that we didn't bother writing the decoder. Let's implement the decoder then:
</p>



~~~java

public static class MessageDecoder extends MessageToMessageDecoder<ByteBuf>
{
    @Override
    protected void decode( ChannelHandlerContext ctx, ByteBuf msg, List<Object> out ) throws Exception
    {
        int value = msg.readInt();
        out.add( new Foo(value) );
    }
}
~~~

<p>Now if we run our test again it's all green and happy. We can now go and encode/decode some more complex structures and update our test accordingly.
</p>

