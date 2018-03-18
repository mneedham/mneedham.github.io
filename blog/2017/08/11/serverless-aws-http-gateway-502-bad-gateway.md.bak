+++
draft = false
date="2017-08-11 16:01:50"
title="Serverless: AWS HTTP Gateway - 502 Bad Gateway"
tag=['aws-lambda', 'serverless', 'http-gateway']
category=['Software Development']
description="Learn how to get up and running with a simple Python Serverless function that works with an AWS HTTP gateway."
+++

<p>
In my continued work with Serverless and AWS Lambda I ran into a problem when trying to call a <a href="https://serverless.com/framework/docs/providers/aws/events/apigateway/">HTTP gateway</a>.
</p>


<p>
My project looked like this:
</p>


<p>
<em>serverless.yaml</em>
</p>




~~~text

service: http-gateway

frameworkVersion: ">=1.2.0 <2.0.0"

provider:
  name: aws
  runtime: python3.6
  timeout: 180

functions:
  no-op:
      name: NoOp
      handler: handler.noop
      events:
        - http: POST noOp
~~~

<p>
<em>handler.py</em>
</p>




~~~python

def noop(event, context):
    return "hello"
~~~

<p>
Let's deploy to AWS:
</p>



~~~bash

$ serverless  deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (179 B)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: http-gateway
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://29nb5rmmd0.execute-api.us-east-1.amazonaws.com/dev/noOp
functions:
  no-op: http-gateway-dev-no-op
~~~

<p>
And now we'll try and call it using cURL:
</p>




~~~bash

$ curl -X POST https://29nb5rmmd0.execute-api.us-east-1.amazonaws.com/dev/noOp
{"message": "Internal server error"}
~~~

<p>
That didn't work so well, what do the logs have to say?
</p>



~~~bash

$ serverless  logs --function no-op	
START RequestId: 64ab69b0-7d8f-11e7-9db5-13b228cd4cb6 Version: $LATEST
END RequestId: 64ab69b0-7d8f-11e7-9db5-13b228cd4cb6
REPORT RequestId: 64ab69b0-7d8f-11e7-9db5-13b228cd4cb6	Duration: 0.27 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 21 MB
~~~

<p>
So the function is completely fine. It turns out I'm not very good at reading the manual and should have been returning <a href="https://medium.com/@jconning/tutorial-aws-lambda-with-api-gateway-36a8513ec8e3">a map instead of a string</a>:
</p>


<blockquote>
API Gateway expects to see a json map with keys “body”, “headers”, and “statusCode”.
</blockquote>

<p>Let's update our handler function and re-deploy.</p>



~~~python

def noop(event, context):
    return {
        "body": "hello",
        "headers": {},
        "statusCode": 200
        }
~~~

<p>
Now we're ready to try the endpoint again:
</p>



~~~bash

$ curl -X POST https://29nb5rmmd0.execute-api.us-east-1.amazonaws.com/dev/noOp
hello
~~~

<p>
Much better!
</p>

