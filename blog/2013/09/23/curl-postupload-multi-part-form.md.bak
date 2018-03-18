+++
draft = false
date="2013-09-23 22:16:29"
title="cURL: POST/Upload multi part form"
tag=['unix', 'curl']
category=['Shell Scripting']
+++

<p>I've been doing some work which involved uploading a couple of files from a HTML form and I wanted to check that the server side code was working by executing a cURL command rather than using the browser.</p>


<p>The form looks like this:</p>



~~~html

<form action="http://foobar.com" method="POST" enctype="multipart/form-data">
    <p>
        <label for="nodes">File 1:</label>
        <input type="file" name="file1" id="file1">
    </p>


    <p>
        <label for="relationships">File 2:</label>
        <input type="file" name="file2" id="file2">
    </p>


    <input type="submit" name="submit" value="Submit">
</form>
~~~

<p>If we convert the POST request from the browser into a cURL equivalent we end up with the following:</p>



~~~bash

curl 'http://foobar.com' -H 'Origin: null' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Host: foobar.com:7474' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36' -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryMxYFIg6GFEIPAe6V' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Cookie: splashShown1.6=1; undefined=0; _mkto_trk=id:773-GON-065&token:_mch-localhost-1373821432078-37666; JSESSIONID=123cbkxby1rtcj3dwipqzs7yu' -H 'Connection: keep-alive' --data-binary $'------WebKitFormBoundaryMxYFIg6GFEIPAe6V\r\nContent-Disposition: form-data; name="file1"; filename="file1.csv"\r\nContent-Type: text/csv\r\n\r\n\r\n------WebKitFormBoundaryMxYFIg6GFEIPAe6V\r\nContent-Disposition: form-data; name="file2"; filename="file2.csv"\r\nContent-Type: text/csv\r\n\r\n\r\n------WebKitFormBoundaryMxYFIg6GFEIPAe6V\r\nContent-Disposition: form-data; name="submit"\r\n\r\nSubmit\r\n------WebKitFormBoundaryMxYFIg6GFEIPAe6V--\r\n' --compressed
~~~

<p>I tried executing this command but I couldn't quite get it to work, and in any case it seemed extremely complicated. Thankfully, I came across a <a href="http://curl.haxx.se/docs/httpscripting.html">cURL tutorial</a> which described a much simpler alternative which does work:</p>



~~~bash

curl --form file1=@file1.csv --form file2=@file2.csv --form press=submit http://foobar.com
~~~

<p>I knew it couldn't be that complicated!</p>

