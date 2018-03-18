+++
draft = false
date="2012-10-14 09:28:28"
title="Play Framework 2.0: Rendering JSON data in the view"
tag=['software-development', 'play']
category=['Software Development']
+++

I've been playing around with the <a href="http://www.playframework.org/">Play Framework</a> which we're using to front a bunch of visualisations and one thing I wanted to do is send a data structure to a view and then convert that into JSON.

I've got a simple controller which looks like this:


~~~java

package controllers;

import play.mvc.Controller;
import play.mvc.Result;
import views.html.*;

public class SalesByCategory extends Controller {
    public static Result index() {
        ArrayList<Map<String, Object>> series = new ArrayList<Map<String, Object>>();
        Map<String, Object> oneSeries = new HashMap<String, Object>();
        oneSeries.put("name", "awesome");
        oneSeries.put("sales", calculateSales()); # would call a method elsewhere, implementation isn't important

        series.add(oneSeries);

        # I have a view named 'index.scala.html'
        return ok(index.render("Awesome visualisation", series));
    }
}
~~~

The top of the corresponding view looks like this:


~~~html

@(message: String)(series:List[Map[String, Object]])
~~~

I'm using the GSON library to convert objects into JSON so I need to import that into the view:


~~~html

@import com.google.gson.Gson
~~~

I was initially struggling to work out what the syntax would be to call the GSON code from within the page but with a bit of trial and error realised that the following would do the trick:


~~~html

<script lang="text/javascript">
  var series = @{new Gson().toJson(series)};
</script>
~~~

The problem with this version of the code was that the string was being escaped so I ended up with series having a value like this:


~~~text

[{&quot;name&quot;:&quot; #and so on!
~~~

I needed to tell Play not to escape this string which in Play v1 was done by calling 'raw()' on the string but <a href="http://stackoverflow.com/questions/10326050/getting-a-raw-string-back-for-use-in-javascript-in-play-framework-2-0">in Play v2 is done using the 'Html' method</a>:


~~~html

<script lang="text/javascript">
  var series = @{Html(new Gson().toJson(series))};
</script>
~~~

And now the JSON renders beautifully!
