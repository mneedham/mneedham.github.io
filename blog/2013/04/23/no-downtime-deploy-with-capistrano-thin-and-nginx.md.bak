+++
draft = false
date="2013-04-23 23:25:15"
title="No downtime deploy with capistrano, Thin and nginx"
tag=['capistrano', 'nginx', 'thin']
category=['Software Development']
+++

<p>As I mentioned a couple of weeks ago I've been working on a tutorial about <a href="http://www.markhneedham.com/blog/2013/04/13/capistrano-deploying-to-a-vagrant-vm/">thinking through problems in graphs</a> and since it's a Sinatra application I thought thin would be a decent choice for <a href="http://code.macournoyer.com/thin/">web server</a>.</p>


<p>In my initial setup I had the following nginx config file which was used to proxy requests on to thin:</p>


<em>/etc/nginx/sites-available/thinkingingraphs.conf</em>

~~~text

upstream thin {
  server 127.0.0.1:3000;
}

server {
  listen       80 default;
  server_name _;
  charset utf-8;
  
  rewrite  ^\/status(.*)$  $1 last;

  gzip  on;
  gzip_disable "MSIE [1-6]\.(?!.*SV1)";
  gzip_types       text/plain application/xml text/xml text/css application/x-javascript application/xml+rss text/javascript application/json;

  gzip_vary on;

  access_log  /var/www/thinkingingraphs/shared/log/nginx_access.log;
  error_log  /var/www/thinkingingraphs/shared/log/nginx_error.log;

  root   /var/www/thinkingingraphs/current/public;

  location / {
    proxy_pass http://thin;
  }

  error_page  404              /404.html;
  error_page   500 502 503 504  /500.html;
}
~~~

<p>I had an <a href="http://upstart.ubuntu.com/">upstart</a> script which started the thin server...</p>


<em>/etc/init/thinkingingraphs.conf</em>

~~~text

script
  export RACK_ENV=production
  export RUBY=ruby

  cd /var/www/thinkingingraphs/current
  exec su -s /bin/sh vagrant -c '$RUBY -S bundle exec thin -p 3000 start >> /var/www/thinkingingraphs/current/log/production.log 2>&1'
end script
~~~

<p>... and then I used the following <a href="https://github.com/capistrano/capistrano">capistrano</a> script to stop and start the server whenever I was deploying a new version of the application:</p>


<em>config/deploy.rb</em>

~~~ruby

namespace :deploy do
  task(:start) {}
  task(:stop) {}
 
  desc "Restart Application"
  task :restart do
    sudo "stop thinkingingraphs || echo 0"
    sudo "start thinkingingraphs"
  end
end
~~~

<p>The problem with this approach is that some requests receive a 502 response code while its restarting:</p>



~~~bash

$ bundle exec cap deploy
~~~


~~~bash

$ while true; do curl -w %{http_code}:%{time_total} http://localhost/ -o /dev/null -s; printf "\n"; sleep 0.5; done

200:0.076
200:0.074
200:0.095
502:0.003
200:0.696
~~~

<p>I wanted to try and make a no downtime deploy script and I came across <a href="http://jordanhollinger.com/2011/12/19/deploying-with-thin">a couple</a> <a href="http://www.treeder.com/2012/03/upstarting-thin-aka-using-upstart-to.html">of posts</a> which helped me work out how to do it.</p>


<p>The first step was to make sure that I had more than one thin instance running so that requests could be sent to one of the other ones while a restart was in progress.</p>


<p>I created the following config file:</p>


<em>/etc/thin/thinkingingraphs.yml</em>

~~~text

chdir: /var/www/thinkingingraphs/current
environment: production
address: 0.0.0.0
port: 3000
timeout: 30
log: log/thin.log
pid: tmp/pids/thin.pid
max_conns: 1024
max_persistent_conns: 100
require: []
wait: 30
servers: 3
daemonize: true
onebyone: true
~~~

<p>One of the other properties that we need to set is 'onebyone' which means that when you restart thin it will take down the thin instances one at a time. This means one of the other two can handle incoming requests.</p>


<p>We've set the number of servers to 3 which will spin up 3 instances on ports 3000, 3001 and 3002.</p>


<p>I changed my upstart script to look like this:</p>


<em>/etc/init/thinkingingraphs.conf</em>

~~~text

script
  export RACK_ENV=production
  export RUBY=ruby

  cd /var/www/thinkingingraphs/current
  exec su -s /bin/sh vagrant -c '$RUBY -S bundle exec thin -C /etc/thin/thinkingingraphs.yml start >> /var/www/thinkingingraphs/current/log/production.log 2>&1'
end script
~~~

<p>I also had to change the capistrano script to call 'thin restart' instead of stopping and starting the upstart script:</p>


<em>config/deploy.rb</em>

~~~ruby

namespace :deploy do
  task(:start) {}
  task(:stop) {}

  desc "Restart Application"
  task :restart do
    run "cd #{current_path} && bundle exec thin restart -C /etc/thin/thinkingingraphs.yml"
  end
end
~~~

<p>Finally I had to make some changes to the nginx config file to send on requests to other thin instances if the first attempt failed (due to it being restarted) using the <a href="http://wiki.nginx.org/HttpProxyModule#proxy_next_upstream">proxy_next_upstream</a> method:</p>


<em>/etc/nginx/sites-available/thinkingingraphs.conf</em>


~~~text

upstream thin {
  server 127.0.0.1:3000 max_fails=1 fail_timeout=15s;
  server 127.0.0.1:3001 max_fails=1 fail_timeout=15s;
  server 127.0.0.1:3002 max_fails=1 fail_timeout=15s;
}

server {
  listen       80 default;
  server_name _;
  charset utf-8;
  
  rewrite  ^\/status(.*)$  $1 last;

  gzip  on;
  gzip_disable "MSIE [1-6]\.(?!.*SV1)";
  gzip_types       text/plain application/xml text/xml text/css application/x-javascript application/xml+rss text/javascript application/json;

  gzip_vary on;

  access_log  /var/www/thinkingingraphs/shared/log/nginx_access.log;
  error_log  /var/www/thinkingingraphs/shared/log/nginx_error.log;

  root   /var/www/thinkingingraphs/current/public;

  location / {
    proxy_pass http://thin;
    proxy_next_upstream error timeout http_502 http_503;
  }

  error_page  404              /404.html;
  error_page   500 502 503 504  /500.html;
}
~~~

<p>We've also made a change to our upstream definition to proxy requests to one of the thin instances which will be running.</p>


<p>When I deploy the application now there is no downtime:</p>



~~~bash

$ bundle exec cap deploy
~~~


~~~bash

$ while true; do curl -w %{http_code}:%{time_total} http://localhost/ -o /dev/null -s; printf "\n"; sleep 0.5; done

200:0.094
200:0.095
200:0.082
200:0.102
200:0.080
200:0.081
~~~

<p>The only problem is that upstart now seems to have lost a handle on the thin processes and from what I can tell there isn't a master process which upstart could get a handle on so I'm not sure how to wire this up.</p>


<p>Any ideas welcome!</p>

