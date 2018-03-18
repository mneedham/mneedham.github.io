+++
draft = false
date="2012-07-08 21:55:53"
title="ganglia: Importing gmond Python modules"
tag=['software-development']
category=['Software Development']
+++

My colleague <a href="http://www.linkedin.com/pub/shodhan-sheth/2/277/287">Shohdan</a> and I spent a couple of days last week wiring up various monitoring metrics into ganglia and while most of them come built in, we also <a href="http://www.mail-archive.com/ganglia-general@lists.sourceforge.net/msg06458.html">found some </a> <a href="https://github.com/ganglia/gmond_python_modules">python based modules that we wanted to use</a>.

Unfortunately we couldn't find any instructions on github explaining how to set them up but after a bit of trial and error we figured it out.

One of the modules that we wanted to use was <a href="https://github.com/ganglia/gmond_python_modules/tree/master/diskstat">diskstat</a> which provides I/O wait time metrics which we couldn't find in the built in modules.

The first thing we needed to do was enable the Python module which comes built in with ganglia:

/etc/ganglia/gmond.conf

~~~text

modules {
  module {
    name = "core_metrics"
  }
  ...
  module {
    name = "python_module"
    path = "/usr/lib/ganglia/modpython.so"
    params = "/usr/lib/ganglia/python_modules/"
  }
}
~~~

As part of this we had to point the module at the folder location where we'd be putting the python modules - the 'params' argument.

In this case we put <a href="https://github.com/ganglia/gmond_python_modules/blob/master/diskstat/python_modules/diskstat.py">diskstat.py</a> into that folder.


~~~text

$ ls -alh /usr/lib/ganglia/python_modules/
total 52K
drwxr-xr-x 2 root     root     4.0K 2012-07-06 01:49 .
drwxr-xr-x 3 root     root     4.0K 2012-07-03 08:27 ..
-rw-r--r-- 1 mneedham mneedham  15K 2012-07-03 08:28 diskstat.py
-rw-r--r-- 1 root     root      12K 2012-07-03 09:00 diskstat.pyc
~~~

We also needed to add the <a href="https://github.com/ganglia/gmond_python_modules/blob/master/diskstat/conf.d/diskstat.pyconf">diskstat.pyconf</a> configuration file so that ganglia knows which metrics to measure. We were having problems with the 'name_match' wildcard property and ended up listing the metrics individually:

/etc/ganglia/conf.d/diskstat.pyconf

~~~text

modules {
  module {
    name = 'diskstat'
    language = 'python'

    param devices {
      value = 'sda1'
    }
  }
}

collection_group {
  collect_every = 30
  time_threshold = 30

  metric {
    name = "diskstat_sda1_io_time"
  }
  ...
}
~~~

The last step was to edit gmond.conf again to pick up the python configuration files:

/etc/ganglia/gmond.conf

~~~text

include ('/etc/ganglia/conf.d/*.conf') 
# add this line
include ('/etc/ganglia/conf.d/*.pyconf') 
~~~

There are a bunch of other modules for different tools in the repository and we've followed the above approach for installation of them as well.
