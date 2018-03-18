+++
draft = false
date="2013-01-15 00:37:01"
title="Fabric/Boto: boto.exception.NoAuthHandlerFound: No handler was ready to authenticate. 1 handlers were checked. ['QuerySignatureV2AuthHandler'] Check your credentials"
tag=['devops-2', 'fabric', 'boto']
category=['DevOps']
+++

<p>In our Fabric code we make use of <a href="https://github.com/boto/boto">Boto</a> to connect to the EC2 API and pull back various bits of information and the first time anyone tries to use it they end up with the following stack trace:</p>



~~~text

  File "/Library/Python/2.7/site-packages/fabric/main.py", line 717, in main
    *args, **kwargs
  File "/Library/Python/2.7/site-packages/fabric/tasks.py", line 332, in execute
    results['<local-only>'] = task.run(*args, **new_kwargs)
  File "/Library/Python/2.7/site-packages/fabric/tasks.py", line 112, in run
    return self.wrapped(*args, **kwargs)
  File "/Users/mark/projects/forward-puppet/ec2.py", line 131, in running
    instances = instances_by_zones(running_instances(region, role_name))
  File "/Users/mark/projects/forward-puppet/ec2.py", line 19, in running_instances
    ec2conn = ec2.connect_to_region(region)
  File "/Library/Python/2.7/site-packages/boto/ec2/__init__.py", line 57, in connect_to_region
    for region in regions(**kw_params):
  File "/Library/Python/2.7/site-packages/boto/ec2/__init__.py", line 39, in regions
    c = EC2Connection(**kw_params)
  File "/Library/Python/2.7/site-packages/boto/ec2/connection.py", line 94, in __init__
    validate_certs=validate_certs)
  File "/Library/Python/2.7/site-packages/boto/connection.py", line 936, in __init__
    validate_certs=validate_certs)
  File "/Library/Python/2.7/site-packages/boto/connection.py", line 548, in __init__
    host, config, self.provider, self._required_auth_capability())
  File "/Library/Python/2.7/site-packages/boto/auth.py", line 633, in get_auth_handler
    'Check your credentials' % (len(names), str(names)))
boto.exception.NoAuthHandlerFound: No handler was ready to authenticate. 1 handlers were checked. ['QuerySignatureV2AuthHandler'] Check your credentials
~~~

<p>We <a href="http://stackoverflow.com/questions/5396932/why-are-no-amazon-s3-authentication-handlers-ready">haven't told Boto about our AWS credentials</a> and I've come across two ways of providing them:</p>


<h4>As environment variables</h4>

~~~text

export AWS_ACCESS_KEY_ID="aws_access_key_id"
export AWS_SECRET_ACCESS_KEY="aws_secret_access_key"
~~~

<h4>In the file <cite>~/.boto</cite></h4>


~~~text

[Credentials]
aws_access_key_id = aws_access_key_id
aws_secret_access_key = aws_secret_access_key
~~~

<p>And that should do the trick!</p>

