+++
draft = false
date="2008-09-29 23:27:37"
title="Connecting to LDAP server using OpenDS in Java"
tag=['java', 'ldap', 'opends']
category=['Java']
+++

A colleague and I have spent the past couple of days spiking solutions for connecting to LDAP servers from Ruby.

We decided that the easiest way to do this is by using <a href="https://opends.dev.java.net/">OpenDS</a>, an open source directory service based on LDAP.

One option we came up with for doing this was to make use of the Java libraries for connecting to the LDAP server and then calling through to these from our Ruby code using the <a href="http://rjb.rubyforge.org/">Ruby Java Bridge</a>.

This post is not about Ruby, but about how we did it in Java to check that the idea was actually feasible.

The interfaces and classes we need to use to do this are not very <a href="http://domaindrivendesign.org/discussion/messageboardarchive/IntentionRevealingInterfaces.html">obvious</a> so it was a little bit fiddly getting it to work. The following code seems to do the trick though:


~~~java

import org.opends.server.admin.client.ldap.JNDIDirContextAdaptor;

import javax.naming.directory.DirContext;
import javax.naming.NamingException;
import javax.naming.Context;
import javax.naming.ldap.LdapName;
import javax.naming.ldap.InitialLdapContext;

import com.sun.jndi.ldap.LdapCtx;

import java.util.Hashtable;

public class OpenDs {

    public static void main(String[] args) throws NamingException {
        DirContext dirContext = createLdapContext();
        JNDIDirContextAdaptor adaptor =  JNDIDirContextAdaptor.adapt(dirContext);

        // do other stuff with the adaptor
    }

    private static DirContext createLdapContext() throws NamingException {
        Hashtable env = new Hashtable();
        env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put(Context.PROVIDER_URL, "ldap://localhost:389");
        env.put(Context.SECURITY_AUTHENTICATION, "simple");
        env.put(Context.SECURITY_PRINCIPAL, "cn=Directory Manager");
        env.put(Context.SECURITY_CREDENTIALS, "password");

        return new InitialLdapContext(env, null);
    }
}
~~~

Some points about the code:
<ul>
<li>
Port 389 is the default port for the LDAP server so unless it's in use this is probably the port you need to connect to.</li>
<li>'Directory Manager' is the default 'Root User DN' that was setup when we installed OpenDS although there is more information on what this value may need to be on the <a href="http://java.sun.com/products/jndi/tutorial/ldap/security/ldap.html">official documentation</a>.</li>
<li>We originally tried to connect using <a href="http://www.opends.org/promoted-builds/1.0.0/javadoc/org/opends/server/admin/client/ldap/JNDIDirContextAdaptor.html">JNDIDirContextAdaptor.simpleBind(...)</a> but it didn't seem to work for us so we went with the JNDIDirContextAdaptor.adapt(...) approach.</li>
</ul>

