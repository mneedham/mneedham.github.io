+++
draft = false
date="2017-09-30 07:51:29"
title="Serverless: Building a mini producer/consumer data pipeline with AWS SNS"
tag=['aws', 'serverless', 'sns', 'ec2', 'data-pipeline']
category=['Software Development']
+++

<p>
I wanted to create a little data pipeline with <a href="https://serverless.com/">Serverless</a> whose main use would be to run once a day, call an API, and load that data into a database.
</p>


<p>
It's mostly used to pull in recent data from that API, but I also wanted to be able to invoke it manually and specify a date range.
</p>


<p>
I created the following pair of lambdas that <a href="https://forum.serverless.com/t/solved-publishing-to-created-sns-topic/1426">communicate with each other via an SNS topic</a>.
</p>



<h2>The code</h2>

<p>
<cite>serverless.yml</cite>
</p>



~~~yaml

service: marks-blog

frameworkVersion: ">=1.2.0 <2.0.0"

provider:
  name: aws
  runtime: python3.6
  timeout: 180
  iamRoleStatements:
    - Effect: 'Allow'
      Action:
        - "sns:Publish"
      Resource:
        - ${self:custom.BlogTopic}

custom:
  BlogTopic:
    Fn::Join:
      - ":"
      - - arn
        - aws
        - sns
        - Ref: AWS::Region
        - Ref: AWS::AccountId
        - marks-blog-topic

functions:
  message-consumer:
    name: MessageConsumer
    handler: handler.consumer
    events:
      - sns:
          topicName: marks-blog-topic
          displayName: Topic to process events
  message-producer:
    name: MessageProducer
    handler: handler.producer
    events:
      - schedule: rate(1 day)
~~~

<p>
<cite>handler.py</cite>
</p>




~~~python

import boto3
import json
import datetime
from datetime import timezone

def producer(event, context):
    sns = boto3.client('sns')

    context_parts = context.invoked_function_arn.split(':')
    topic_name = "marks-blog-topic"
    topic_arn = "arn:aws:sns:{region}:{account_id}:{topic}".format(
        region=context_parts[3], account_id=context_parts[4], topic=topic_name)

    now = datetime.datetime.now(timezone.utc)
    start_date = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    end_date = now.strftime("%Y-%m-%d")

    params = {"startDate": start_date, "endDate": end_date, "tags": ["neo4j"]}

    sns.publish(TopicArn= topic_arn, Message= json.dumps(params))


def consumer(event, context):
    for record in event["Records"]:
        message = json.loads(record["Sns"]["Message"])

        start_date = message["startDate"]
        end_date = message["endDate"]
        tags = message["tags"]

        print("start_date: " + start_date)
        print("end_date: " + end_date)
        print("tags: " + str(tags))
~~~

<h2>Trying it out</h2>

<p>
We can simulate a message being received locally by executing the following command:
</p>



~~~bash

$ serverless invoke local \
    --function message-consumer \
    --data '{"Records":[{"Sns": {"Message":"{\"tags\": [\"neo4j\"], \"startDate\": \"2017-09-25\", \"endDate\": \"2017-09-29\"  }"}}]}'

start_date: 2017-09-25
end_date: 2017-09-29
tags: ['neo4j']
null
~~~

<p>
That seems to work fine. What about if we invoke the message-producer on AWS?
</P>


~~~bash

$ serverless invoke --function message-producer

null
~~~

<p>
Did the consumer received the message?</p>



~~~bash

$ serverless logs --function message-consumer

START RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f Version: $LATEST
start_date: 2017-09-29
end_date: 2017-09-30
tags: ['neo4j']
END RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f
REPORT RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f	Duration: 0.46 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 32 MB
~~~

<p>
Looks like it! We can also invoke the consumer directly on AWS:
</p>



~~~bash

$ serverless invoke \
    --function message-consumer \
    --data '{"Records":[{"Sns": {"Message":"{\"tags\": [\"neo4j\"], \"startDate\": \"2017-09-25\", \"endDate\": \"2017-09-26\"  }"}}]}'

null
~~~

<p>
And now if we check the consumer's logs we'll see both messages:
</p>



~~~bash

$ serverless logs --function message-consumer

START RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f Version: $LATEST
start_date: 2017-09-29
end_date: 2017-09-30
tags: ['neo4j']
END RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f
REPORT RequestId: 0ef5be87-a5b1-11e7-a905-f1387e68c65f	Duration: 0.46 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 32 MB	

START RequestId: 4cb42bc9-a5b1-11e7-affb-99fa6b4dc3ed Version: $LATEST
start_date: 2017-09-25
end_date: 2017-09-26
tags: ['neo4j']
END RequestId: 4cb42bc9-a5b1-11e7-affb-99fa6b4dc3ed
REPORT RequestId: 4cb42bc9-a5b1-11e7-affb-99fa6b4dc3ed	Duration: 16.46 ms	Billed Duration: 100 ms 	Memory Size: 1024 MB	Max Memory Used: 32 MB
~~~

<p>
Success!
</p>

