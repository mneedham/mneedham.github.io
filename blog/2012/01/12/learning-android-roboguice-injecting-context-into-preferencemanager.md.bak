+++
draft = false
date="2012-01-12 17:24:30"
title="Learning Android: Roboguice - Injecting context into PreferenceManager"
tag=['android']
category=['Android']
+++

In my last post I showed how I'd been able to <a href="http://www.markhneedham.com/blog/2012/01/10/learning-android-testing-details-got-saved-to-sharedpreferences/">write a test around saved preferences in my app by making use of a ShadowPreferenceManager</a> but it seemed a bit hacky.

I didn't want to have to do that for every test where I dealt with preferences - I thought it'd be better if I could wrap the preferences in an object of my own and then inject it where necessary.

Another benefit of taking this approach is that the interface of exactly what I'm storing as user preferences.

I wanted the class to be roughly like this:


~~~java

public class UserPreferences {
    public String userKey() {
        return getDefaultSharedPreferences().getString("user_key", "");
    }

    public String userSecret() {
        return getDefaultSharedPreferences().getString("user_secret", "");
    }

    private SharedPreferences getDefaultSharedPreferences() {
        return PreferenceManager.getDefaultSharedPreferences(getContextHereSomehow());
    }
}
~~~

Initially it wasn't entirely obvious how I could get a <cite>Context</cite> to pass to <cite>getDefaultSharedPreferences</cite> but I came across <a href="http://www.irasenthil.com/2011/09/how-to-inject-context-in-android-with.html">a blog post explaining how to do it</a>.

What we need to do is inject a <cite>Context</cite> object via the constructor of the class and decorate the constructor with the <cite>@Inject</cite> attribute so that Roboguice will resolve the dependency:


~~~java

public class UserPreferences {
    private Context context;

    @Inject
    public UserPreferences(Context context) {
        this.context = context;
    }

    public SharedPreferences getDefaultSharedPreferences() {
        return PreferenceManager.getDefaultSharedPreferences(context.getApplicationContext());
    }

    public String userKey() {
        return getDefaultSharedPreferences().getString("user_key", "");
    }

    public String userSecret() {
        return getDefaultSharedPreferences().getString("user_secret", "");
    }
}
~~~

We never have to explicitly setup a binding for <cite>Context</cite> in our Roboguice because it's already been done for us in <a href="https://github.com/abombss/roboguice/blob/master/roboguice/src/main/java/roboguice/config/RoboModule.java">RoboModule</a> which is instantiated by <a href="https://github.com/abombss/roboguice/blob/master/roboguice/src/main/java/roboguice/application/RoboApplication.java">RoboApplication</a> which we extend like so:


~~~java

public class TweetBoardApplication extends RoboApplication {
    private Module module = new RobolectricSampleModule();

    @Override protected void addApplicationModules(List<Module> modules) {
        modules.add(module);
    }

    public void setModule(Module module) {
        this.module = module;
    }
}
~~~

We then hook <cite>TweetBoardApplication</cite> up in the AndroidManifest.xml file like this:


~~~xml

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.pivotallabs"
          android:versionCode="1"
          android:versionName="1.0">
    <application
            android:label="@string/app_name"
            android:theme="@android:style/Theme.Light.NoTitleBar"
            android:icon="@drawable/app_icon"
            android:name="TweetBoardApplication">
   </application>
</manifest>
~~~ 

And that's it!
