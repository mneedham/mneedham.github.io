+++
draft = false
date="2012-02-11 10:29:15"
title="Java: Fooled by java.util.Arrays.asList"
tag=['java']
category=['Java']
+++

I've been playing around with the <a href="http://code.google.com/p/boilerpipe/">boilerpipe</a> code base by writing some tests around it to check my understanding but ran into an interesting problem using <cite>java.util.Arrays.asList</cite> to pass a list into one of the functions.

I was testing the <cite><a href="https://github.com/mneedham/boilerpipe/blob/master/src/main/de/l3s/boilerpipe/filters/heuristics/BlockProximityFusion.java">BlockProximityFusion</a></cite> class which is used to merge together adjacent text blocks.

I started off calling that class like this:


~~~java

import static java.util.Arrays.asList;

@Test
public void willCallBlockProximityFustion() throws Exception {    
    TextDocument document = new TextDocument(asList(contentBlock("some words"), contentBlock("followed by more words")));
    BlockProximityFusion.MAX_DISTANCE_1.process(document);
}

private TextBlock contentBlock(String words) {
    TextBlock textBlock = new TextBlock(words, new BitSet(), wordCount(words), 0, 0, 0, 0);
    textBlock.setIsContent(true);
    return textBlock;
}
~~~

Which blows up like this:


~~~java

java.lang.UnsupportedOperationException
	at java.util.AbstractList.remove(AbstractList.java:144)
	at java.util.AbstractList$Itr.remove(AbstractList.java:360)
	at de.l3s.boilerpipe.filters.heuristics.BlockProximityFusion.process(BlockProximityFusion.java:115)
	at de.l3s.boilerpipe.filters.heuristics.BlockProximityFusionTest.willCallBlockProximityFustion(BlockProximityFusionTest.java:63)
~~~

The code around that area is trying to remove an element from an iterator...


~~~java

                if (ok) {
                    prevBlock.mergeNext(block);
                    it.remove();
                    changes = true;
                } else {
~~~

...which was created from the list that we passed into the constructor of <cite>TextDocument</cite>:


~~~java

        for (Iterator<TextBlock> it = textBlocks.listIterator(offset); it
~~~

The <cite>remove</cite> method is not implemented on the list created by 'Arrays.asList' which is weird since I thought it created an <cite>ArrayList</cite> which does implement <cite>remove</cite>!

I've now learnt that the <cite>ArrayList</cite> created by 'Arrays.asList' is actually a private inner class of <cite>Arrays</cite> and doesn't implement the <cite>remove</cite> method!

Who knew...
