+++
draft = false
date="2012-09-29 09:56:16"
title="Upstart: Job getting stuck in the start/killed state"
tag=['upstart']
category=['Shell Scripting']
+++

We're using <a href="http://upstart.ubuntu.com/">upstart</a> to handle the processes running on our machines and since the <a href="http://haproxy.1wt.eu/">haproxy</a> package only came package with an init.d script we wanted to make it upstartified.

When defining an upstart script you need to specify an <cite>expect</cite> stanza in which you specify whether or not the process which you're launching is going to fork.

<blockquote>
If you do not specify the expect stanza, Upstart will track the life cycle of the first PID that it executes in the exec or script stanzas. 

However, most Unix services will "daemonize", meaning that they will create a new process (using fork(2)) which is a child of the initial process. 

Often services will "double fork" to ensure they have no association whatsoever with the initial process.
</blockquote>

There is a table on the upstart cookbook under the '<a href="http://upstart.ubuntu.com/cookbook/#id155">Implications of Misspecifying expect</a>' section which explains what will happen if we specify this incorrectly:

<table border="1" class="docutils">
<caption>Expect Stanza Behaviour</caption>
<colgroup>
<col width="10%">
<col width="31%">
<col width="31%">
<col width="28%">
</colgroup>
<thead valign="bottom">
<tr><th class="head">&nbsp;</th>
<th class="head" colspan="3">Specification of Expect Stanza</th>
</tr>
<tr><th class="head">Forks</th>
<th class="head">no <tt class="docutils literal">expect</tt></th>
<th class="head"><tt class="docutils literal">expect fork</tt></th>
<th class="head"><tt class="docutils literal">expect daemon</tt></th>
</tr>
</thead>
<tbody valign="top">
<tr><td>0</td>
<td>Correct</td>
<td><a class="reference internal" href="#start">start</a> hangs</td>
<td><a class="reference internal" href="#start">start</a> hangs</td>
</tr>
<tr><td>1</td>
<td>Wrong pid tracked †</td>
<td>Correct</td>
<td><a class="reference internal" href="#start">start</a> hangs</td>
</tr>
<tr><td>2</td>
<td>Wrong pid tracked</td>
<td>Wrong pid tracked</td>
<td>Correct</td>
</tr>
</tbody>
</table>

When we were defining our script we went for <cite>expect daemon</cite> instead of <cite>expect fork</cite> and had also mistyped the arguments to the haproxy script which meant it failed to start and ended up in the <cite>start/killed</cite> state.

From what we could tell upstart had a handle on a PID which didn't actually exist and when we tried a <cite>stop haproxy</cite> the command seemed to succeed but didn't actually do anything.

<a href="https://twitter.com/philandstuff">Phil</a> pointed us to <a href="https://bugs.launchpad.net/upstart/+bug/406397/comments/24">a neat script written by Clint Byrum</a> which spins up and then kills loads of processes in order to exhaust the PID space until a process with the PID upstart is tracking exists and can be re-attached and killed.

It's <a href="http://heh.fi/tmp/workaround-upstart-snafu">available on his website</a> but that wasn't responding for a period of time yesterday so I'll repeat it here just in case:


~~~ruby

#!/usr/bin/env ruby1.8

class Workaround
  def initialize target_pid
    @target_pid = target_pid

    first_child
  end

  def first_child
    pid = fork do
      Process.setsid

      rio, wio = IO.pipe

      # Keep rio open
      until second_child rio, wio
        print "\e[A"
      end
    end

    Process.wait pid
  end

  def second_child parent_rio, parent_wio
    rio, wio = IO.pipe

    pid = fork do
      rio.close
      parent_wio.close

      puts "%20.20s" % Process.pid

      if Process.pid == @target_pid
        wio << 'a'
        wio.close

        parent_rio.read
      end
    end
    wio.close

    begin
      if rio.read == 'a'
        true
      else
        Process.wait pid
        false
      end
    ensure
      rio.close
    end
  end
end

if $0 == __FILE__
  pid = ARGV.shift
  raise "USAGE: #{$0} pid" if pid.nil?
  Workaround.new Integer pid
end
~~~

We can <a href="https://gist.github.com/3803604">put that into a shell script</a>, run it and the world of upstart will get back into a good place again!
