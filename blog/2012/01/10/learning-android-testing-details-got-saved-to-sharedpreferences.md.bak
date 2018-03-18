+++
draft = false
date="2012-01-10 09:53:48"
title="Learning Android: Robolectric - Testing details got saved to SharedPreferences"
tag=['android']
category=['Android']
+++

I've been writing some tests around an app I've been working on using the <a href="http://pivotal.github.com/robolectric/">Robolectric</a> testing framework and one thing I wanted to do was check that an OAuth token/secret were being saved to the <a href="http://stackoverflow.com/questions/2614719/how-do-i-get-the-sharedpreferences-from-a-preferenceactivity-in-android">user's preferences</a>.

The code that saved the preferences looked like this:


~~~java

public class AuthoriseWithTwitterActivity extends RoboActivity {
    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(intent);
        ...
        save("fakeToken", "fakeSecret");
        ...
    }

    private void save(String userKey, String userSecret) {
        SharedPreferences settings = PreferenceManager.getDefaultSharedPreferences(getBaseContext());
        SharedPreferences.Editor editor = settings.edit();
        editor.putString("user_key", userKey);
        editor.putString("user_secret", userSecret);
        editor.commit();
    }
}
~~~

This is an outline of what I wanted to do in the test:


~~~java

@RunWith(InjectedTestRunner.class)
public class AwesomeTest {
    @Test public void shouldSaveOAuthDetails() {
        activity.onCreate(null);

        ShadowIntent shadowIntent = shadowOf(activity).getNextStartedActivity();

        // Get SharedPreferences and check 'fakeToken' and 'fakeSecret' are stored. 
    }
}
~~~

In Robolectric it's possible to replace classes with shadow versions of themselves which get used in the test so I first created a shadow version of  <cite>PreferenceManager</cite>:


~~~java

@Implements(PreferenceManager.class)
public class ShadowPreferenceManager {
    private static SharedPreferences  preferences = new TestSharedPreferences(new HashMap<String, Map<String, Object>>(), "__default__", Context.MODE_PRIVATE);

    @Implementation
    public static SharedPreferences getDefaultSharedPreferences(Context context) {
        return preferences;
    }

    public static void reset() {
        preferences = new TestSharedPreferences(new HashMap<String, Map<String, Object>>(), "__default__", Context.MODE_PRIVATE);
    }
}
~~~

I had to make <cite>preferences</cite> a static variable here so that it'll retain state. It's a bit hacky but it'll do for now.

Then to hook it up I had to change my test to read like this:


~~~java

@RunWith(InjectedTestRunner.class)
public class AwesomeTest {
    @Test public void shouldSaveOAuthDetails() {
        Robolectric.bindShadowClass(ShadowPreferenceManager.class);
        activity.onCreate(null);

        ShadowIntent shadowIntent = shadowOf(activity).getNextStartedActivity();

        SharedPreferences defaultSharedPreferences = PreferenceManager.getDefaultSharedPreferences(activity);
        assertThat(defaultSharedPreferences.getString("user_key", ""), equalTo("fakeToken"));
        assertThat(defaultSharedPreferences.getString("user_secret", ""), equalTo("fakeSecret"));

        ShadowPreferenceManager.reset();
    }
}
~~~

The <cite>InjectedTestRunner</cite> class used here is pretty much like <a href="https://github.com/pivotal/RobolectricSample/blob/master/src/test/java/com/pivotallabs/injected/InjectedTestRunner.java">the one in the Robolectric code base</a>.

There is actually a <cite>ShadowPreferenceManager</cite> in the Robolectric library but it doesn't seem to store preferences anywhere as far as I can tell so it wasn't quite what I wanted.
