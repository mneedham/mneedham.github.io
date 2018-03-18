+++
draft = false
date="2012-06-24 00:58:43"
title="Brightbox Repository: GPG error: The following signatures couldn't be verified because the public key is not available"
tag=['software-development']
category=['Software Development']
+++

We're using the <a href="https://launchpad.net/~brightbox/+archive/ruby-ng">Brightbox Ruby repository</a> to get the versions of Ruby which we install on our machines and although we eventually put the configuration for this repository into Puppet we initially tested it out on a local VM.

To start with you need to add the repository to <cite>/etc/apt/sources.list</cite>:

~~~text

deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu lucid main
~~~

To get that picked up we run the following:


~~~text

apt-get update
~~~

Which initially threw this error because it's a gpg signed repository and we hadn't added the key:

<blockquote>
W: GPG error: http://ppa.launchpad.net lucid Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F5DA5F09C3173AA6
</blockquote>

I recently realised that the instructions explaining how to sign the repository are hidden away in an overlay on the page but the <a href="http://docs.opsview.com/doku.php?id=opsview-community:repository-key">opsview wiki</a> also explains what to do.

To add the key we need to run the following:


~~~text

sudo apt-key add -

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.0.10

mI0ETKTCMQEEAMX3ttL4YFO5AQ7Z6L5gaGw57CJBQl6jCv6lka0p8DaGNkeX0Rs9DhINa8qR
hxJCPK6ijeoNss69G/ni+sMSRViJBFWXzitEE1ew5YM2sw7wLE3guToDu60kaDwIn5mR3GTx
cgqDrQeCuGZJgz3e2lgmGYw2rAhMe78rRgkR5GFvABEBAAG0G0xhdW5jaHBhZCBQUEEgZm9y
IEJyaWdodGJveIi4BBMBAgAiBQJMpMIxAhsDBgsJCAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAK
CRD12l8Jwxc6pl2BA/4p5DFEpGVvkgLj7/YLYCtYmZDw8i/drGbkWfIQiOgPWIf8QgpJXVME
1tkH8N1ssjbJlUKl/HubNBKZ6HDyQsQASFug+eI6KhSFMScDBf/oMX3zVCTTvUkgJtOWYc5d
77zJacEUGoSEx63QUJVvp/LAnqkZbt17JJL6HOou/CNicw==
=G8vE
-----END PGP PUBLIC KEY BLOCK-----
~~~

Then press Ctrl-D to exit the command.

The public key comes from <a href="http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xF5DA5F09C3173AA6">here</a> and is referenced under the <a href="https://launchpad.net/~brightbox/+archive/ruby-ng">'Signing key' section</a>.
