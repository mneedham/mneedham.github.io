+++
draft = false
date="2012-09-30 15:48:10"
title="Testing XML generation with vimdiff"
tag=['coding', 'testing']
category=['Testing']
+++

A couple of weeks ago I spent a bit of time writing a Ruby DSL to automate the setup of load balancers, firewall and NAT rules through the <a href="http://communities.vmware.com/community/vmtn/developer/forums/vcloudapi?rct=j&q=&esrc=s&source=web&cd=1&ved=0CC4QFjAA&url=http://www.vmware.com/go/vcloudapi&ei=QWNoUOz4JqOG0AX74oHwBA&usg=AFQjCNHrnaSOCy4H4jMXwEvIB9WEhp2eXg&sig2=cBNs29bb-q8VoCGf_wN38w">VCloud API</a>.

The VCloud API deals primarily in XML so the DSL is just a thin layer which creates the appropriate mark up.

When we started out we configured everything manually through the web console and then exported the XML so the first thing that the DSL needed to do was create XML that matched what we already had. 

My previous experience using testing frameworks to do this is that they'll tell you whether the XML you've generated is equivalent to your expected XML but if they differ <strong>it isn't easy to work out what was different</strong>.

I therefore decided to use a poor man's approach where I first copied one rule into an XML file, attempted to replicate that in the DSL, and then used <a href="http://vimdoc.sourceforge.net/htmldoc/diff.html">vimdiff</a> to compare the files.

Although I had to manually verify whether or not the code was working I found this approach useful as any differences between the two pieces of XML were very easy to see.

90% of the rules were almost identical so I focused on the 10% that were different and once I'd got those working it was reasonably plain sailing.

My vimdiff command read like this:


~~~text

ruby generate_networking_xml.rb > bar && vimdiff -c 'set diffopt+=iwhite' bar initialFirewall.xml
~~~

After I was reasonably confident that I understood the way that the XML should be generated I created an Rspec test which checked that we could correctly create all of the existing configurations using the DSL.

While discussing this approach with <a href="https://twitter.com/jennifersmithco">Jen</a> she suggested that an alternative would be to start with a Rspec test with most of the rules hard coded in XML and then replace them one by one with the DSL.

I think that probably does make more sense but I still quite like my hacky approach as well!
