+++
draft = false
date="2011-06-20 22:36:48"
title="MarkLogic: Customising a result set"
tag=['marklogic']
category=['Mark Logic']
+++

One of the stories we worked on last week had us needing to be able to customise the output of a MarkLogic search query to include some elements which aren't included in the default view.

We started off with this:

search.xqy

~~~text

xquery version "1.0-ml";
import module namespace search = "http://marklogic.com/appservices/search" at "/MarkLogic/appservices/search/search.xqy";

declare variable $term as xs:string := xdmp:get-request-field("query", "");

search:search($term)
~~~

Which gives us back a list of results showing where in the documents the search term appeared.

We wanted to be able to get the title of the document and some other meta data about it though so we needed to make use of the <cite><a href="http://developer.marklogic.com/pubs/4.1/apidocs/SearchAPI.html">transform-results</a></cite> option to do this.

The original query changes to look like this:

search.xqy

~~~text

xquery version "1.0-ml";
import module namespace search = "http://marklogic.com/appservices/search" at "/MarkLogic/appservices/search/search.xqy";

declare variable $term as xs:string := xdmp:get-request-field("query", "");

search:search($term,
   <options xmlns="http://marklogic.com/appservices/search">
     <transform-results apply="transformed-result" ns="http://www.markhneedham.com/search" at="transform.xqy" />
   </options>)
~~~

And then we have another xquery file which we use to do the transformation: 

transfom.xqy

~~~text

xquery version "1.0-ml";
module namespace custom-search = "http://markhneedham.com/search";
import module namespace search = "http://marklogic.com/appservices/search" at "/MarkLogic/appservices/search/search.xqy";

declare function custom-search:transformed-result(
         $result as node(),
         $ctsquery as schema-element(cts:query),
         $options as element(search:transform-results)?
) as element(search:snippet)
{
<search:snippet>
{
(
         search:snippet($result, $ctsquery, $options)/*,
         <extra>{$result//*:Id}{$result//*:Title}</extra>
)
}
</search:snippet>
};
~~~

We put the extra elements that we wanted to include in our search result in the <cite><extra></cite> tag but we can name that anything we want.

The code snippets assume that both <cite>search.xqy</cite> and <cite>transform.xqy</cite> are both at the top level of the documents database.
