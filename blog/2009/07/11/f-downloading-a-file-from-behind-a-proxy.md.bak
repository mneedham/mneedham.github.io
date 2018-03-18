+++
draft = false
date="2009-07-11 03:20:25"
title="F#: Downloading a file from behind a proxy"
tag=['f', 'proxy']
category=['F#']
+++

I've been continuing working on a little script to <a href="http://www.markhneedham.com/blog/2009/07/08/f-parsing-cruise-build-data/">parse Cruise build data</a> and the latest task was to work out how to download my Google Graph API created image onto the local disk.

I'm using the <a href="http://msdn.microsoft.com/en-us/library/system.net.webclient(VS.80).aspx">WebClient</a> class to do this and the  code looks like this:


~~~ocaml

let DownloadGraph (fileLocation:string) (uri:System.Uri) = async {
    let webClient = new WebClient()
    webClient.DownloadFileAsync(uri, fileLocation)}
~~~

Sadly this doesn't work when I run it from the client site where I have access to the build metrics as there is a corporate proxy sitting in the way.

I tried Googling how to do this but all the ways that I tried kept resulting in the following error:


~~~text

407 proxy authentication required
~~~

Even though I was entering a user name and password!

I didn't succeed until my colleague showed me a way of getting past the proxy in C# which I could quite easily use in my code:


~~~ocaml

let DownloadGraph (fileLocation:string) (uri:System.Uri) = async {
    let webClient = new WebClient()
    webClient.Proxy <- new WebProxy("proxyName:port", true, null, new NetworkCredential("userName", "password", "corporateDomain"))
    webClient.DownloadFileAsync(uri, fileLocation)}
~~~

One thing I was doing wrong was putting a 'http' at the start of the proxyName which I think in my case was wrong as I later learn that the proxy isn't a HTTP one.

I'm also making use of <a href="http://www.infoq.com/articles/pickering-fsharp-async">asynchronous workflows</a> in this example so that the actual downloading of the files will be done away from the main thread - this also gives me the option to download multiple files asynchronously if I want to.
