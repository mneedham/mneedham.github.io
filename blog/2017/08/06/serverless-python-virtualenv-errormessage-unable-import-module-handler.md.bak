+++
draft = false
date="2017-08-06 19:03:30"
title="Serverless: Python - virtualenv - { \"errorMessage\": \"Unable to import module 'handler'\" }"
tag=['python', 'serverless']
category=['Software Development']
+++

<p>
I've been using the <a href="https://serverless.com/">Serverless</a> library to deploy and run some Python functions on AWS lambda recently and was initially confused about how to handle my dependencies.
</p>


<p>
I tend to create a new <a href="https://virtualenv.pypa.io/en/stable/">virtualenv</a> for each of my project so let's get that setup first:
</p>


<h3>Prerequisites</h3>


~~~bash

$ npm install serverless
~~~


~~~bash

$ virtualenv -p python3 a
$ . a/bin/activate
~~~

<p>
Now let's create our Serverless project. I'm going to install the <a href="http://docs.python-requests.org/en/master/">requests</a> library so that I can use it in my function.
</p>


<h3>My Serverless project</h3>

<p>
<em>serverless.yaml</em>
</p>



~~~yaml

service: python-starter-template

frameworkVersion: ">=1.2.0 <2.0.0"

provider:
  name: aws
  runtime: python3.6
  timeout: 180

functions:
  starter-function:
      name: Starter
      handler: handler.starter
~~~

<p>
<em>handler.py</em>
</p>



~~~python

import requests

def starter(event, context):
    print("event:", event, "context:", context)
    r = requests.get("http://www.google.com")
    print(r.status_code)
~~~


~~~bash

$ pip install requests
~~~

<p>
Ok, we're now ready to try out the function. A nice feature of Serverless is that it lets us try out functions locally before we deploy them onto one of the Cloud providers:
</p>



~~~bash

$ ./node_modules/serverless/bin/serverless invoke local --function starter-function
event: {} context: <__main__.FakeLambdaContext object at 0x10bea9a20>
200
null
~~~

<p>
So far so good. Next we'll deploy our function to AWS. I'm assuming you've already got your credentials setup but if not you can follow the <a href="https://serverless.com/framework/docs/providers/aws/guide/credentials/">tutorial on the Serverless page</a>.
</p>



~~~bash

$ ./node_modules/serverless/bin/serverless deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (26.48 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.........
Serverless: Stack update finished...
Service Information
service: python-starter-template
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  None
functions:
  starter-function: python-starter-template-dev-starter-function
~~~

<p>
Now let's invoke our function:
</p>



~~~bash

$ ./node_modules/serverless/bin/serverless invoke --function starter-function
{
    "errorMessage": "Unable to import module 'handler'"
}
 
  Error --------------------------------------------------
 
  Invoked function failed
 
     For debugging logs, run again after setting the "SLS_DEBUG=*" environment variable.
 
  Get Support --------------------------------------------
     Docs:          docs.serverless.com
     Bugs:          github.com/serverless/serverless/issues
     Forums:        forum.serverless.com
     Chat:          gitter.im/serverless/serverless
 
  Your Environment Information -----------------------------
     OS:                     darwin
     Node Version:           6.7.0
     Serverless Version:     1.19.0

~~~

<p>
Hmmm, that's odd - I wonder why it can't import our handler module? We can call the logs function to check. The logs are usually a few seconds behind so we'll have to be a bit patient if we don't see them immediately.
</p>



~~~bash

$ ./node_modules/serverless/bin/serverless logs  --function starter-function
START RequestId: 735efa84-7ad0-11e7-a4ef-d5baf0b46552 Version: $LATEST
Unable to import module 'handler': No module named 'requests'

END RequestId: 735efa84-7ad0-11e7-a4ef-d5baf0b46552
REPORT RequestId: 735efa84-7ad0-11e7-a4ef-d5baf0b46552	Duration: 0.42 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 22 MB
~~~

<p>
That explains it - the requests module wasn't imported.
</p>


<p>
If we look in <cite>.serverless/python-starter-template.zip</p>
 we can see that the requests module is hidden inside the <cite>a</cite> directory and the instance of Python that runs on Lambda doesn't know where to find it. 
</p>


<p>
I'm sure there are other ways of solving this but the easiest one I found is a Serverless plugin called <a href="https://www.npmjs.com/package/serverless-python-requirements">serverless-python-requirements</a>. 
</p>


<p>So how does this plugin work?</p>


<blockquote>
A Serverless v1.x plugin to automatically bundle dependencies from requirements.txt and make them available in your PYTHONPATH.
</blockquote>

<p>
Doesn't sound too tricky - we can use <cite>pip freeze</cite> to get our list of requirements and write them into a file. Let's rework <cite>serverless.yaml</cite> to make use of the plugin:
</p>


<h3>My Serverless project using serverless-python-requirements</h3>


~~~bash

$ npm install --save serverless-python-requirements
~~~


~~~bash

$ pip freeze > requirements.txt
$ cat requirements.txt 
certifi==2017.7.27.1
chardet==3.0.4
idna==2.5
requests==2.18.3
urllib3==1.22
~~~

<p>
<em>serverless.yaml</em>
</p>



~~~yaml

service: python-starter-template

frameworkVersion: ">=1.2.0 <2.0.0"

provider:
  name: aws
  runtime: python3.6
  timeout: 180

plugins:
  - serverless-python-requirements

functions:
  starter-function:
      name: Starter
      handler: handler.starter

package:
  exclude:
    - a/** # virtualenv
~~~

<p>
We have two changes from before: 
</p>


<ul>

<li>
We added the <cite>serverless-python-requirements</cite> plugin
</li>

<li>
We excluded the <cite>a</cite> directory since we don't need it
</li>

</ul>

<p>
Let's deploy again and run the function:
</p>



~~~bash

$ ./node_modules/serverless/bin/serverless deploy
Serverless: Parsing Python requirements.txt
Serverless: Installing required Python packages for runtime python3.6...
Serverless: Linking required Python packages...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Unlinking required Python packages...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (14.39 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.........
Serverless: Stack update finished...
Service Information
service: python-starter-template
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  None
functions:
  starter-function: python-starter-template-dev-starter-function
~~~


~~~bash

$ ./node_modules/serverless/bin/serverless invoke --function starter-function
null
~~~

<p>Looks good. Let's check the logs:</p>



~~~bash

$ ./node_modules/serverless/bin/serverless logs --function starter-function
START RequestId: 61e8eda7-7ad4-11e7-8914-03b8a7793a24 Version: $LATEST
event: {} context: <__main__.LambdaContext object at 0x7f568b105f28>
200
END RequestId: 61e8eda7-7ad4-11e7-8914-03b8a7793a24
REPORT RequestId: 61e8eda7-7ad4-11e7-8914-03b8a7793a24	Duration: 55.55 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 29 M
~~~

<p>
All good here as well so we're done!
</p>

