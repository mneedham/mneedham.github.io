+++
draft = false
date="2011-12-31 17:47:47"
title="Clojure: Casting to a Java class...or not!"
tag=['clojure']
category=['Clojure']
+++

I have a bit of Java code for <a href="http://stackoverflow.com/questions/2659000/java-how-to-find-the-redirected-url-of-a-url">working out the final destination of a URL</a> assuming that there might be one redirect which looks like this:


~~~java

private String resolveUrl(String url) {
  try {
    HttpURLConnection con = (HttpURLConnection) (new URL(url).openConnection());
    con.setInstanceFollowRedirects(false);
    con.connect();
    int responseCode = con.getResponseCode();

    if (String.valueOf(responseCode).startsWith("3")) {
      return con.getHeaderField("Location");
    }
  } catch (IOException e) {
    return url;
  }

  return url;
}
~~~

I need to cast to <cite>HttpURLConnection</cite> on the first line so that I can make the call to <cite>setInstanceFollowRedirects</cite> which isn't available on <cite>URLConnection</cite>.

I wanted to write some similar code in Clojure and my first thought was that I needed to work out how to do the cast, which I didn't know how to do.

I then remembered that Clojure is actually dynamically typed so there isn't any need - as long as the object has the method that we want to call on it everything will be fine.

In this case we end up with the following code:


~~~clojure

(defn resolve-url [url]
  (let [con (.. (new URL url) openConnection)]
    (doall
     (.setInstanceFollowRedirects con false)
     (.connect con))
    (if (.startsWith (str (.getResponseCode con)) "3")
      (.getHeaderField con "Location")
      url)))
~~~

Which can be simplified to this:


~~~clojure

(defn resolve-url [url]
  (let [con (doto (.. (new URL url) openConnection)
                  (.setInstanceFollowRedirects false)
                  (.connect))]
  (if (.startsWith (str (.getResponseCode con)) "3")
    (.getHeaderField con "Location")
    url)))
~~~
