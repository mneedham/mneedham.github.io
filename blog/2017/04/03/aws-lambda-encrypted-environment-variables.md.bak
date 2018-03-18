+++
draft = false
date="2017-04-03 05:49:53"
title="AWS Lambda: Encrypted environment variables"
tag=['lambda', 'aws-lambda']
category=['Software Development']
description="In this post we look at how to pass encrypted environment variables to an AWS lambda function and then decrypt them inside the function."
+++

<p>Continuing on from my post showing how to create a <a href="http://www.markhneedham.com/blog/2017/04/02/aws-lambda-programatically-create-a-python-hello-world-function/">'Hello World' AWS lambda function</a> I wanted to pass encrypted environment variables to my function.</p>


<p>The following function takes in both an encrypted and unencrypted variable and prints them out.</p>


<p>
<strong>Don't print out encrypted variables in a real function, this is just so we can see the example working!</strong>
</p>



~~~python

import boto3
import os

from base64 import b64decode

def lambda_handler(event, context):
    encrypted = os.environ['ENCRYPTED_VALUE']
    decrypted = boto3.client('kms').decrypt(CiphertextBlob=b64decode(encrypted))['Plaintext']

    # Don't print out your decrypted value in a real function! This is just to show how it works.
    print("Decrypted value:", decrypted)

    plain_text = os.environ["PLAIN_TEXT_VALUE"]
    print("Plain text:", plain_text)
~~~

<p>Now we'll zip up our function into HelloWorldEncrypted.zip, ready to send to AWS.</p>



~~~bash

zip HelloWorldEncrypted.zip HelloWorldEncrypted.py
~~~

<p>Now it&#8217;s time to upload our function to AWS and create the associated environment variables.</p>


<p>If you&#8217;re using a Python editor then you&#8217;ll need to install boto3 locally to keep the editor happy but you don&#8217;t need to include boto3 in the code you send to AWS Lambda - it comes pre-installed.</p>


<p>Now we write the following code to automate the creation of our Lambda function:</p>


~~~python

import boto3
from base64 import b64encode

fn_name = "HelloWorldEncrypted"
kms_key = "arn:aws:kms:[aws-zone]:[your-aws-id]:key/[your-kms-key-id]"
fn_role = 'arn:aws:iam::[your-aws-id]:role/lambda_basic_execution'

lambda_client = boto3.client('lambda')
kms_client = boto3.client('kms')

encrypt_me = "abcdefg"
encrypted = b64encode(kms_client.encrypt(Plaintext=encrypt_me, KeyId=kms_key)["CiphertextBlob"])

plain_text = 'hijklmno'

lambda_client.create_function(
        FunctionName=fn_name,
        Runtime='python2.7',
        Role=fn_role,
        Handler="{0}.lambda_handler".format(fn_name),
        Code={ 'ZipFile': open("{0}.zip".format(fn_name), 'rb').read(),},
        Environment={
            'Variables': {
                'ENCRYPTED_VALUE': encrypted,
                'PLAIN_TEXT_VALUE': plain_text,
            }
        },
        KMSKeyArn=kms_key
)
~~~

<p>
The tricky bit for me here was figuring out that I needed to pass the value that I wanted to base 64 encode the output of the value encrypted by the KMS client. The KMS client relies on a KMS key that <a href="http://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html">we need to setup</a>. We can see a list of all our KMS keys by running the following command:
</p>



~~~bash

$ aws kms list-keys
~~~

<p>
The format of these keys is <cite>arn:aws:kms:[zone]:[account-id]:key/[key-id]</cite>.
</p>


<p>Now let&#8217;s try executing our Lambda function from the AWS console:</p>



~~~bash

$ python CreateHelloWorldEncrypted.py
~~~

<p>Let's check it got created:</p>



~~~bash

$ aws lambda list-functions --query "Functions[*].FunctionName"
[
    "HelloWorldEncrypted", 
]
~~~

<p>
And now let's execute the function:
</p>



~~~bash

$ aws lambda invoke --function-name HelloWorldEncrypted --invocation-type RequestResponse --log-type Tail /tmp/out | jq ".LogResult"
"U1RBUlQgUmVxdWVzdElkOiA5YmNlM2E1MC0xODMwLTExZTctYjFlNi1hZjQxZDYzMzYxZDkgVmVyc2lvbjogJExBVEVTVAooJ0RlY3J5cHRlZCB2YWx1ZTonLCAnYWJjZGVmZycpCignUGxhaW4gdGV4dDonLCAnaGlqa2xtbm8nKQpFTkQgUmVxdWVzdElkOiA5YmNlM2E1MC0xODMwLTExZTctYjFlNi1hZjQxZDYzMzYxZDkKUkVQT1JUIFJlcXVlc3RJZDogOWJjZTNhNTAtMTgzMC0xMWU3LWIxZTYtYWY0MWQ2MzM2MWQ5CUR1cmF0aW9uOiAzNjAuMDQgbXMJQmlsbGVkIER1cmF0aW9uOiA0MDAgbXMgCU1lbW9yeSBTaXplOiAxMjggTUIJTWF4IE1lbW9yeSBVc2VkOiAyNCBNQgkK"
~~~

<p>
That's a bit hard to read, some decoding is needed:
</p>



~~~bash

$ echo "U1RBUlQgUmVxdWVzdElkOiA5YmNlM2E1MC0xODMwLTExZTctYjFlNi1hZjQxZDYzMzYxZDkgVmVyc2lvbjogJExBVEVTVAooJ0RlY3J5cHRlZCB2YWx1ZTonLCAnYWJjZGVmZycpCignUGxhaW4gdGV4dDonLCAnaGlqa2xtbm8nKQpFTkQgUmVxdWVzdElkOiA5YmNlM2E1MC0xODMwLTExZTctYjFlNi1hZjQxZDYzMzYxZDkKUkVQT1JUIFJlcXVlc3RJZDogOWJjZTNhNTAtMTgzMC0xMWU3LWIxZTYtYWY0MWQ2MzM2MWQ5CUR1cmF0aW9uOiAzNjAuMDQgbXMJQmlsbGVkIER1cmF0aW9uOiA0MDAgbXMgCU1lbW9yeSBTaXplOiAxMjggTUIJTWF4IE1lbW9yeSBVc2VkOiAyNCBNQgkK" | base64 --decode
START RequestId: 9bce3a50-1830-11e7-b1e6-af41d63361d9 Version: $LATEST
('Decrypted value:', 'abcdefg')
('Plain text:', 'hijklmno')
END RequestId: 9bce3a50-1830-11e7-b1e6-af41d63361d9
REPORT RequestId: 9bce3a50-1830-11e7-b1e6-af41d63361d9	Duration: 360.04 ms	Billed Duration: 400 ms 	Memory Size: 128 MB	Max Memory Used: 24 MB	
~~~

<p>
And it worked, hoorah!
</p>

