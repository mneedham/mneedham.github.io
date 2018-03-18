+++
draft = false
date="2010-08-16 07:18:05"
title="iPad: Getting PragProg books onto the Kindle App"
tag=['ipad']
category=['iPad']
+++

As <a href="http://www.markhneedham.com/blog/2010/07/12/linchpin-book-review/">I've mentioned previously</a> I think the <a href="http://itunes.apple.com/us/app/kindle/id302584613?mt=8">Kindle application on the iPad</a> is the best one for reading books and as a result of that I wanted to be able to read some books which I'd bought from the <a href="http://www.pragprog.com/">PragProg</a> store onto it.

The first step is to download the '.mobi' version of the book and use <a href="http://www.macroplant.com/iphoneexplorer/">iPhoneExplorer</a> to drag the file into the 'Kindle/Documents/eBook' folder on the iPad.

This works fine but if you add more than one book in this way they all have the same cover image when viewed on the iPad which is quite annoying when trying to work out which book is which.

I went on a yak shaving mission to try and figure out how to solve that problem and came across <a href="http://www.mobileread.com/forums/showthread.php?t=89040">a post by GRiker where he described how to set a custom cover image</a>.

His instructions were as follows:
<blockquote>
For example, let's say you want to sideload WarOfTheWorlds.MOBI with its cover WarOfTheWorlds.JPG into the Kindle for iPad app:
<ul>
<li>Modify WarOfTheWorlds.MOBI (using Mobi2Mobi, for example), adding or modifying the ASIN field (in the EXTH block) with the name of the cover jpg, WarOfTheWorlds.JPG. (Since your sideloaded book didn't come from Amazon, you don't need a real ASIN.)</li>
<li>Copy the modified WarOfTheWorlds.MOBI to Kindle/Documents/eBooks (using iPhone Explorer)</li>
<li>Copy WarOfTheWorlds.JPG to Kindle/Documents/LibraryCovers (using iPhone Explorer)</li>
</ul>
</blockquote>

I first loaded the mobi files into <a href="http://calibre-ebook.com/">Calibre</a> so that I could get the cover image by doing the following:

<ul>
<li>Click on the icon in the top left hand corner which looks like a book with a + sign on it</li>
<li>Add books from a single directory</li>
<li>Find the .mobi file you want to import</li>
<li>Right click on the book</li>
<li>Open containing folder</li>
</ul>

After I'd done that I needed to install 'mobi2mobi' in order to update the 'ASIN' number of the book. The Kindle application looks for a file with the same name as the ASIN number in the 'LibraryCovers' folder and uses that as the cover image for the book.

There are a <a href="http://wiki.mobileread.com/wiki/Install_Mobi2Mobi_Mac">crazy number of instructions to follow on the mobileread wiki in order to install this</a>.

I followed these but was getting the following error when I tried to run the command:


~~~text

Can't locate GD.pm in @INC (@INC contains: /Users/mneedham/eBooks/tools /Library/Perl/Updates/5.10.0/darwin-thread-multi-2level /Library/Perl/Updates/5.10.0 /System/Library/Perl/5.10.0/darwin-thread-multi-2level /System/Library/Perl/5.10.0 /Library/Perl/5.10.0/darwin-thread-multi-2level /Library/Perl/5.10.0 /Network/Library/Perl/5.10.0/darwin-thread-multi-2level /Network/Library/Perl/5.10.0 /Network/Library/Perl /System/Library/Perl/Extras/5.10.0/darwin-thread-multi-2level /System/Library/Perl/Extras/5.10.0 .) at /Users/mneedham/eBooks/tools/MobiPerl/Util.pm line 23.
BEGIN failed--compilation aborted at /Users/mneedham/eBooks/tools/MobiPerl/Util.pm line 23.
~~~

I came across <a href="http://www.mobileread.mobi/forums/showthread.php?t=61639">the following thread where pilotbob described a way to fix this</a>:

<blockquote>
I got it working on Snow Leopard. Here is what I did.

1. Install MacPorts... this will make it a whole lot easier. http://www.macports.org

2. Once you get ports installed use macports to install the gd lib stuff:
sudo port install gd2

This will also install perl 5.8.9... perl 5.10 comes with Snow Leopard. Not sure it any mac stuff requires that... but you can always go back, macports puts stuff in a separate location.

I also installed the following macports:

p5-gd
p5-palm
p5-timedate
p5-getopt-mixed
p5-image-size
p5-xml-parser-lite-tree
p5-encode

Then, I use CPAN to install the following... there didn't seem to be any macports for them:

HTML::TreeBuilder
Image::BMP

After that mobi2mobi ran... well it gave me the command line options. I didn't actually try it. But, it doesn't seem to run unless all the dependencies are there.
</blockquote>

I tried to install all of those dependencies as he suggests although not all of them worked for me.

After I'd done that I went back to the mobileread wiki and re-ran the following commands:


~~~text

sudo perl -MCPAN -e shell

install Palm::PDB
install XML::Parser::Lite::Tree
install GD
install Image::BMP
install Image::Size

install HTML::TreeBuilder
install Getopt::Mixed
install Date::Parse
install Date::Format
~~~

And after all that I was finally able to run 'mobi2mobi' to change the 'ASIN' of the file which can be done by executing the following command:


~~~text

mobi2mobi my.mobi --outfile my.mobi --exthtype asin --exthdata "mycoverimage.jpg"
~~~

To get the Kindle application to pick up the new image I needed to be connected to the internet for some reason but all my books are showing with the correct covers now.
