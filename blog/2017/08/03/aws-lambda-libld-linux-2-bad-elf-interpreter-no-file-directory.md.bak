+++
draft = false
date="2017-08-03 17:24:16"
title="AWS Lambda: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory'"
tag=['aws', 'aws-lambda']
category=['Software Development']
+++

<p>
I've been working on an AWS lambda job to convert a HTML page to PDF using a Python wrapper around the wkhtmltopdf library but ended up with the following error when I tried to execute it:
</p>



~~~text

b'/bin/sh: ./binary/wkhtmltopdf: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory\n': Exception
Traceback (most recent call last):
File "/var/task/handler.py", line 33, in generate_certificate
wkhtmltopdf(local_html_file_name, local_pdf_file_name)
File "/var/task/lib/wkhtmltopdf.py", line 64, in wkhtmltopdf
wkhp.render()
File "/var/task/lib/wkhtmltopdf.py", line 56, in render
raise Exception(stderr)
Exception: b'/bin/sh: ./binary/wkhtmltopdf: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory\n'
~~~
		
<p>
It turns out this is the error you get if <a href="https://stackoverflow.com/questions/8328250/centos-64-bit-bad-elf-interpreter">you run a 32 bit binary on a 64 bit operating system</a> which is <a href="http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html">what AWS uses</a>.
</p>
				

<blockquote>
If you are using any native binaries in your code, make sure they are compiled in this environment. Note that only 64-bit binaries are supported on AWS Lambda.
</blockquote>

<p>
I changed to the 64 bit binary and am now happily converting HTML pages to PDF.
</p>

