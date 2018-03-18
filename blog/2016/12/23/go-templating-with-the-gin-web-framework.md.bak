+++
draft = false
date="2016-12-23 14:30:09"
title="Go: Templating with the Gin Web Framework"
tag=['go', 'golang']
category=['Go']
+++

<p>
I spent a bit of time over the last week building a little internal web application using Go and the <a href="https://github.com/gin-gonic/gin">Gin Web Framework</a> and it took me a while to get the hang of the templating language so I thought I'd write up some examples.
</p>


<p>
Before we get started, I've got my GOPATH set to the following path:
</p>



~~~bash

$ echo $GOPATH
/Users/markneedham/projects/gocode
~~~

<p>And the project containing the examples sits inside the src directory:
</p>



~~~bash

$ pwd
/Users/markneedham/projects/gocode/src/github.com/mneedham/golang-gin-templating-demo
~~~

<p>Let's first install Gin:</p>



~~~bash

$ go get gopkg.in/gin-gonic/gin.v1
~~~

<p>
It gets installed here:
</p>



~~~bash

$ ls -lh $GOPATH/src/gopkg.in
total 0
drwxr-xr-x   3 markneedham  staff   102B 23 Dec 10:55 gin-gonic
~~~

<p>
Now let's create a main function to launch our web application:
</p>



<p><cite>demo.go</cite></p>


~~~go

package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	router := gin.Default()
	router.LoadHTMLGlob("templates/*")

	// our handlers will go here

	router.Run("0.0.0.0:9090")
}
~~~

<p>
We're launching our application on port 9090 and the templates live in the <cite>templates</cite> directory which is located relative to the file containing the main function:
</p>



~~~bash

$ ls -lh
total 8
-rw-r--r--  1 markneedham  staff   570B 23 Dec 13:34 demo.go
drwxr-xr-x  4 markneedham  staff   136B 23 Dec 13:34 templates
~~~

<h4>Arrays</h4>

<p>
Let's create a route which will display the values of an array in an unordered list:
</p>



~~~go

	router.GET("/array", func(c *gin.Context) {
		var values []int
		for i := 0; i < 5; i++ {
			values = append(values, i)
		}

		c.HTML(http.StatusOK, "array.tmpl", gin.H{"values": values})
	})
~~~


~~~html

<ul>
  {{ range .values }}
  <li>{{ . }}</li>
  {{ end }}
</ul>
~~~

<p>
And now we'll cURL our application to see what we get back:
</p>



~~~bash

$ curl http://localhost:9090/array
<ul>
  <li>0</li>
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
</ul>
~~~

<p>
What about if we have an array of structs instead of just strings?
</p>



~~~go

import "strconv"

type Foo struct {
	value1 int
	value2 string
}

	router.GET("/arrayStruct", func(c *gin.Context) {
		var values []Foo
		for i := 0; i < 5; i++ {
			values = append(values, Foo{Value1: i, Value2: "value " + strconv.Itoa(i)})
		}

		c.HTML(http.StatusOK, "arrayStruct.tmpl", gin.H{"values": values})
	})

~~~


~~~html

<ul>
  {{ range .values }}
  <li>{{ .Value1 }} -> {{ .Value2 }}</li>
  {{ end }}
</ul>
~~~

<p>cURL time:</p>



~~~bash

$ curl http://localhost:9090/arrayStruct
<ul>
  <li>0 -> value 0</li>
  <li>1 -> value 1</li>
  <li>2 -> value 2</li>
  <li>3 -> value 3</li>
  <li>4 -> value 4</li>  
</ul>
~~~

<h4>Maps</h4>

<p>
Now let's do the same for maps.
</p>



~~~go

	router.GET("/map", func(c *gin.Context) {
		values := make(map[string]string)
		values["language"] = "Go"
		values["version"] = "1.7.4"

		c.HTML(http.StatusOK, "map.tmpl", gin.H{"myMap": values})
	})
~~~


~~~html

<ul>
  {{ range .myMap }}
  <li>{{ . }}</li>
  {{ end }}
</ul>

~~~

<p>And cURL it:</p>



~~~bash

$ curl http://localhost:9090/map
<ul>
  <li>Go</li>
  <li>1.7.4</li>
</ul>
~~~

<p>What if we want to see the keys as well?</p>



~~~go

	router.GET("/mapKeys", func(c *gin.Context) {
		values := make(map[string]string)
		values["language"] = "Go"
		values["version"] = "1.7.4"

		c.HTML(http.StatusOK, "mapKeys.tmpl", gin.H{"myMap": values})
	})
~~~


~~~html

<ul>
  {{ range $key, $value := .myMap }}
  <li>{{ $key }} -> {{ $value }}</li>
  {{ end }}
</ul>
~~~


~~~bash

$ curl http://localhost:9090/mapKeys
<ul>  
  <li>language -> Go</li>  
  <li>version -> 1.7.4</li>  
</ul>
~~~

<p>And finally, what if we want to select specific values from the map?</p>



~~~go

	router.GET("/mapSelectKeys", func(c *gin.Context) {
		values := make(map[string]string)
		values["language"] = "Go"
		values["version"] = "1.7.4"

		c.HTML(http.StatusOK, "mapSelectKeys.tmpl", gin.H{"myMap": values})
	})
~~~


~~~html

<ul>
  <li>Language: {{ .myMap.language }}</li>
  <li>Version: {{ .myMap.version }}</li>
</ul>
~~~


~~~bash

$ curl http://localhost:9090/mapSelectKeys
<ul>
  <li>Language: Go</li>
  <li>Version: 1.7.4</li>
</ul>
~~~

<p>
I've found the <a href="https://gohugo.io/templates/go-templates/">Hugo Go Template Primer</a> helpful for figuring this out so that's a good reference if you get stuck. You can find a <a href="https://github.com/mneedham/golang-gin-templating-demo/blob/master/demo.go">go file containing all the examples on github</a> if you want to use that as a starting point.</p>

