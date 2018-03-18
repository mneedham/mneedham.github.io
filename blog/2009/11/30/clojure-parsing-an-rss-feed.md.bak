+++
draft = false
date="2009-11-30 18:33:55"
title="Clojure: Parsing an RSS feed"
tag=['clojure']
category=['Clojure']
+++

I've been playing around with a little script in Clojure to parse the <a href="http://blogs.thoughtworks.com/rss20.xml">ThoughtWorks Blogs RSS feed</a> and then create a tweet for each of them which contains a link to the blog post and the person's Twitter ID if they have one.

It's not finished yet but I'm finding the way that we parse documents like this in Clojure quite intriguing.

The xml to parse looks roughly like this:


~~~text

<rss version="2.0"> 
	<channel> 
 		...
		<item> 
			<title>Simon Brunning: Links for 2009-11-27 [del.icio.us]</title> 
			<link>http://feedproxy.google.com/~r/SmallValuesOfCool/~3/WDqeLyMA-RE/brunns</link> 
		</item>
		<item> 
			<title>Alex Hung: Extending iPhone battery life</title> 
			<link>http://alexhung.vox.com/library/post/extending-iphone-battery-life.html?_c=feed-atom-full</link> 
		</item>
		...
	</channel> 
</rss>
~~~

I've only included the parts of the document that I'm interested in getting.

Following the examples from <a href="http://www.amazon.com/Programming-Clojure-Pragmatic-Programmers-Halloway/dp/1934356336/ref=sr_1_1?ie=UTF8&s=books&qid=1259561307&sr=8-1">Stuart Halloway's book</a> one approach to do this is to make use of the '<a href="http://clojure.org/api#toc674">clojure.xml.parse</a>' and '<a href="http://clojure.org/api#toc618">clojure.core.xml-seq</a>' functions to create a sequence representing the tree structure of the feed.

I'm used to parsing XML with XPath but that doesn't make as much sense when we have a sequence of hash maps. Instead I'm using '<a href="http://clojure.org/api#toc248">filter</a>' and '<a href="http://clojure.org/api#toc356">map</a>' to try and achieve the same outcome.

I found that while I was trying to work out how to use these functions together I was often trying to solve the whole problem in one go instead of breaking it down into smaller more manageable pieces.

I also noticed that I was using 'filter' more often than I needed to instead of filtering the data to the point that everything I wanted to extract was in the remaining data set.

When I was playing with F# I got into the habit of trying to minimise the number of intermediate values I created but this seemed to be making life more difficult so I've allowed myself some intermediate values for the moment!

The goal is to poll the ThoughtWorks RSS feed and then update the <a href="http://twitter.com/planettw">planettw</a> account with the latest blog posts. The current setup does that but doesn't include people's Twitter names in the tweet so I'm trying to sort that out.

This is the code I have so far:


~~~lisp

(use '[clojure.xml :only (parse)])
(def feed (xml-seq (parse (java.io.File. "clojure-play/tw-blogs-rss.txt"))))

(def rss-entries (filter #(= :item (:tag %)) feed))

(defn- get-href [link]
  ((comp :href :attrs) link))

(defn- get-value [node]
  (first (:content node)))

(defn rss-link [entry]
  (get-value (first (filter #(= :link (:tag %))
                            (:content entry)))))

(defn rss-title [entry]
  (get-value (first (filter #(= :title (:tag %))
                            (:content entry)))))

(def rss-titles (map #(rss-title %) rss-entries))
(def rss-links (map #(rss-link %) rss-entries))

(defn- get-author [title]
  (second (first (re-seq #"([\w ]+):" title))))

(defn- get-title [title]
  (second (first (re-seq #"[a-zA-Z0-9 ]+:\s(.*)" title))))

(def authors (map #(get-author %) rss-titles))
(def titles (map #(get-title %) rss-titles))

(defn- get-display-name [twitter-names real-name]
  (let [twitter-name (twitter-names real-name)]
    (if twitter-name (str "@" twitter-name) real-name)))

(def twitter-names {"Mark Needham" "markhneedham"
                    "Alex Hung" "alexhung"
                    "Simon Brunning" "brunns"
                    "Ola Bini" "olabini"
                    "Patrick Kua" "patkua"
                    "Marc McNeill" "dancingmango"
                    "Dahlia Bock" "dlbock"
                    "Sumeet Moghe" "sumeet_moghe"
                    "Brian Guthrie" "bguthrie"
                    "Ian Robinson" "iansrobinson"
                    "Ian Cartwright" "cartwrightian"
                    "Duncan Cragg" "duncancragg"
                    "David Cameron" "davcamer"
                    "Steven List" "athought"
                    "Philip Calcado" "pcalcado"
                    "Perryn Fowler" "perrynfowler"
                    "Jason Yip" "jchyip"
                    "Christopher Read" "cread"
                    "Jim Webber" "jimwebber"
                    "John Hume" "duelin_markers"
                    })

(defn- create-blog-post [title link author]
  {:tweet (str title " by " (get-display-name twitter-names author) " " link)})

(defn create-blog-posts [titles links authors]
  (map #(create-blog-post %1 %2 %3) titles links authors))
~~~

To use that you'd need to do this:


~~~lisp

(create-blog-posts titles rss-links authors)
~~~

Which returns a sequence of hash maps with key 'tweet' and a value of the tweet to display on Twitter:


~~~text

({:tweet "Links for 2009-11-27 [del.icio.us] by @brunns http://feedproxy.google.com/~r/SmallValuesOfCool/~3/WDqeLyMA-RE/brunns"} 
{:tweet "Extending iPhone battery life by @alexhung http://alexhung.vox.com/library/post/extending-iphone-battery-life.html?_c=feed-atom-full"} 
{:tweet "Threshold Anxiety by Adrian Wible http://thoughtadrian.blogspot.com/2009/11/threshold-anxiety.html"})
~~~

The next step is to get this hooked up to the Twitter API.

There are still some things I'm unsure of when it comes to writing applications in Clojure:

<ul>
<li>I'm not sure what to do with 'twitter-names'. It's pretty much a global data store so I can't decide whether to just refer to it directly inside other functions or if it should be passed in as a parameter.</li>
<li>I used 'first' quite a few times in the code to get the first value in a sequence but it doesn't feel like the code expresses the structure of the document very well.</li>
<li>What's the best way to lay out code for 'defn' expressions? I've been putting the signature on it's own line and then the implementation on other lines which seems to be the way that it's done in the <a href="http://code.google.com/p/clojure/source/browse/">Clojure source code</a> but it sometimes seems like I could just write it all on one line.</li> 
</ul>
