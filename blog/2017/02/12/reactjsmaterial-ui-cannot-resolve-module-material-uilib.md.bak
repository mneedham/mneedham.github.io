+++
draft = false
date="2017-02-12 22:43:53"
title="ReactJS/Material-UI: Cannot resolve module 'material-ui/lib/'"
tag=['reactjs']
category=['Javascript']
+++

<p>
I've been playing around with ReactJS and the Material-UI library over the weekend and ran into this error while trying to follow <a href="http://www.material-ui.com/v0.15.0-alpha.1/#/components/subheader">one of the example from the demo application</a>:
</p>



~~~text

ERROR in ./src/app/modules/Foo.js
Module not found: Error: Cannot resolve module 'material-ui/lib/Subheader' in /Users/markneedham/neo/reactjs-test/src/app/modules
 @ ./src/app/modules/Foo.js 13:17-53
webpack: Failed to compile.
~~~

<p>This was the component code:</p>



~~~javascript

import React from 'react'
import Subheader from 'material-ui/lib/Subheader'

export default React.createClass({
  render() {
    return <div>
    <Subheader>Some Text</Subheader>
    </div>
  }
})
~~~

<p>
which is then rendered like this:
</p>



~~~javascript

import Foo from './modules/Foo'
render(Foo, document.getElementById("app"))
~~~

<p>
I came across <a href="https://github.com/callemall/material-ui/issues/4845">this post on Stack Overflow</a> which seemed to describe a similar issue and led me to realise that I was actually on the wrong version of the documentation. I'm using version 0.16.7 but the demo I copied from is for version 0.15.0-alpha.1!
</p>


<p>This is the component code that we actually want:</p>



~~~javascript

import React from 'react'
import Subheader from 'material-ui/Subheader'

export default React.createClass({
  render() {
    return <div>
    <Subheader>Some Text</Subheader>
    </div>
  }
})
~~~

<p>And that's all I had to change. There are several other components that you'll see the same error for and it looks like the change was made between the 0.14.x and 0.15.x series of the library.</p>

