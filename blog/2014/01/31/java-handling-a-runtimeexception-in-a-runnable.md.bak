+++
draft = false
date="2014-01-31 23:59:58"
title="Java: Handling a RuntimeException in a Runnable"
tag=['java']
category=['Java']
+++

<p>At the end of last year I was playing around with <a href="http://www.markhneedham.com/blog/2013/11/17/java-schedule-a-job-to-run-on-a-time-interval/">running scheduled tasks to monitor a Neo4j cluster</a> and one of the problems I ran into was that the monitoring would sometimes exit.</p>


<p>I eventually realised that this was because a RuntimeException was being thrown inside the Runnable method and I wasn't handling it. The following code demonstrates the problem:</p>



~~~java

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class RunnableBlog {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();

        executor.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                    System.out.println(Thread.currentThread().getName() + " -> " + System.currentTimeMillis());
                    throw new RuntimeException("game over");
            }
        }, 0, 1000, TimeUnit.MILLISECONDS).get();


        System.out.println("exit");
        executor.shutdown();
    }
}
~~~

<p>If we run that code we'll see the RuntimeException but the executor won't exit because the thread died without informing it:</p>



~~~text

Exception in thread "main" pool-1-thread-1 -> 1391212558074
java.util.concurrent.ExecutionException: java.lang.RuntimeException: game over
	at java.util.concurrent.FutureTask$Sync.innerGet(FutureTask.java:252)
	at java.util.concurrent.FutureTask.get(FutureTask.java:111)
	at RunnableBlog.main(RunnableBlog.java:11)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)
Caused by: java.lang.RuntimeException: game over
	at RunnableBlog$1.run(RunnableBlog.java:16)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
	at java.util.concurrent.FutureTask$Sync.innerRunAndReset(FutureTask.java:351)
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603)
	at java.lang.Thread.run(Thread.java:722)
~~~

<p>At the time I ended up adding a try catch block and printing the exception like so:</p>



~~~java

public class RunnableBlog {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();

        executor.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                try {
                    System.out.println(Thread.currentThread().getName() + " -> " + System.currentTimeMillis());
                    throw new RuntimeException("game over");
                } catch (RuntimeException e) {
                    e.printStackTrace();
                }
            }
        }, 0, 1000, TimeUnit.MILLISECONDS).get();

        System.out.println("exit");
        executor.shutdown();
    }
}
~~~

<p>This allows the exception to be recognised and as far as I can tell means that the thread executing the Runnable doesn't die.</p>



~~~text

java.lang.RuntimeException: game over
pool-1-thread-1 -> 1391212651955
	at RunnableBlog$1.run(RunnableBlog.java:16)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
	at java.util.concurrent.FutureTask$Sync.innerRunAndReset(FutureTask.java:351)
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603)
	at java.lang.Thread.run(Thread.java:722)
pool-1-thread-1 -> 1391212652956
java.lang.RuntimeException: game over
	at RunnableBlog$1.run(RunnableBlog.java:16)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
	at java.util.concurrent.FutureTask$Sync.innerRunAndReset(FutureTask.java:351)
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603)
	at java.lang.Thread.run(Thread.java:722)
pool-1-thread-1 -> 1391212653955
java.lang.RuntimeException: game over
	at RunnableBlog$1.run(RunnableBlog.java:16)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
	at java.util.concurrent.FutureTask$Sync.innerRunAndReset(FutureTask.java:351)
	at java.util.concurrent.FutureTask.runAndReset(FutureTask.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:178)
	at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603)
	at java.lang.Thread.run(Thread.java:722)
~~~

<p>This worked well and allowed me to keep monitoring the cluster.<p> 

<p>However, I recently started reading '<a href="http://www.amazon.co.uk/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601">Java Concurrency in Practice</a>' (only 6 years after I bought it!) and realised that this might not be the proper way of handling the RuntimeException.</p>
 

<p.The authors suggest the proper way of handling an exception is to let the thread die but inform the framework that it's died so another thread can be spun up in its place. We end up with the following code instead:</p>



~~~java

public class RunnableBlog {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();

        executor.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                try {
                    System.out.println(Thread.currentThread().getName() + " -> " + System.currentTimeMillis());
                    throw new RuntimeException("game over");
                } catch (RuntimeException e) {
                    Thread t = Thread.currentThread();
                    t.getUncaughtExceptionHandler().uncaughtException(t, e);
                }
            }
        }, 0, 1000, TimeUnit.MILLISECONDS).get();

        System.out.println("exit");
        executor.shutdown();
    }
}
~~~

<p>I don't see much difference between the two approaches so it'd be great if someone could explain to me why this approach is better than my previous one of catching the exception and printing the stack trace.</p>

