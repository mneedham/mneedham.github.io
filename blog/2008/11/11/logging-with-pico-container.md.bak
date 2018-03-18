+++
draft = false
date="2008-11-11 00:08:16"
title="Logging with Pico Container"
tag=['picocontainer']
category=['Java']
+++

One thing that we've been working on recently is the logging for our current code base.

Nearly all the objects in our system are being created by <a href="http://picocontainer.org/">Pico Container</a> so we decided that writing an interceptor that hooked into Pico Container would be the easiest way to intercept and log any exceptions throw from our code.

Our initial Googling led us to the <a href="http://picocontainer.org/interception.html">AOP Style Interception</a> page on the Pico website which detailed how we could create a static proxy for a class that we put in the container.

The code to do this was as follows:


~~~java

        DefaultPicoContainer pico = new DefaultPicoContainer(new Intercepting());
        pico.addComponent(Interceptable.class, ConcreteInterceptable.class);
        Intercepted intercepted = pico.getComponentAdapter(Interceptable.class).findAdapterOfType(Intercepted.class);
        intercepted.addPreInvocation(Interceptable.class, new InterceptableReporter(intercepted.getController()));
        intercepted.addPostInvocation(Interceptable.class, new InterceptableReporter(intercepted.getController()));

        Interceptable a1 = pico.getComponent(Interceptable.class);
        a1.methodThatThrowsException();
~~~


~~~java

public interface Interceptable {
    void methodThatThrowsException();
}
~~~


~~~java

    private static class InterceptableReporter implements Interceptable {
        private Intercepted.Controller controller;

        public InterceptableReporter(Intercepted.Controller controller) {
            this.controller = controller;
        }


        public void methodThatThrowsException() {
            System.out.println("error happened");

        }
    }
~~~

While this approach works, the problem is that we need to define an individual proxy for every class that we want to intercept. It works as  a strategy if we just need to intercept a few classes but not on a larger scale.

Luckily it is possible to create a <a href="http://lizdouglass.wordpress.com/2008/08/31/small-things-amuse-small%E2%80%A6-hmph-well-anyway%E2%80%A6/">dynamic proxy</a> on the container so that we can intercept all the objects without having to create a static proxy for each one.

The code to do this was as follows:


~~~java

        DefaultPicoContainer pico = new DefaultPicoContainer(new LoggingAwareByDefault());
        pico.addComponent(Interceptable.class, ConcreteInterceptable.class);

        Interceptable interceptable = pico.getComponent(Interceptable.class);
        interceptable.methodThatThrowsException();
~~~


~~~java

import org.apache.commons.logging.LogFactory;
import org.picocontainer.Characteristics;
import org.picocontainer.ComponentAdapter;
import org.picocontainer.ComponentMonitor;
import org.picocontainer.LifecycleStrategy;
import org.picocontainer.Parameter;
import org.picocontainer.behaviors.AbstractBehaviorFactory;

import java.util.Properties;

public class LoggingAwareByDefault extends AbstractBehaviorFactory {
    private static final String DO_NOT_LOG_NAME = "support-team-opt-out";
    public static final Properties DO_NOT_LOG = Characteristics
            .immutable(DO_NOT_LOG_NAME, Characteristics.TRUE);


    public <T> ComponentAdapter<T> createComponentAdapter(ComponentMonitor componentMonitor,
                                                          LifecycleStrategy lifecycleStrategy,
                                                          Properties componentProperties,
                                                          Object componentKey, Class<T> componentImplementation,
                                                          Parameter... parameters) {
        if (removePropertiesIfPresent(componentProperties, DO_NOT_LOG)) {
            return super.createComponentAdapter(componentMonitor, lifecycleStrategy, componentProperties, componentKey,
                    componentImplementation, parameters);
        } else {
            return new LoggingAware<T>(super.createComponentAdapter(componentMonitor,
                    lifecycleStrategy, componentProperties, componentKey,
                    componentImplementation, parameters));
        }

    }
}
~~~


~~~java

import org.apache.commons.logging.Log;
import org.picocontainer.ComponentAdapter;
import org.picocontainer.ComponentMonitor;
import org.picocontainer.PicoContainer;
import org.picocontainer.behaviors.HiddenImplementation;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class LoggingAware<T> extends HiddenImplementation {
    public LoggingAware(ComponentAdapter delegate) {
        super(delegate);
    }

    protected Object invokeMethod(Object componentInstance, Method method, Object[] args, PicoContainer container)
            throws Throwable {
        ComponentMonitor componentMonitor = currentMonitor();
        try {
            componentMonitor.invoking(container, this, method, componentInstance);
            long startTime = System.currentTimeMillis();
            Object object = method.invoke(componentInstance, args);
            componentMonitor.invoked(container,
                                     this,
                                     method, componentInstance, System.currentTimeMillis() - startTime);
            return object;
        } catch (final InvocationTargetException ite) {
            componentMonitor.invocationFailed(method, componentInstance, ite);

            // log the error

            throw ite.getTargetException();
        }

    }
}
~~~

From what I recall from looking at the source code I think in order to create a proxy around an object it needs to implement an interface otherwise the proxy will not be created.
