+++
draft = false
date="2012-01-01 03:22:34"
title="Learning Android: 'Unable to start service Intent not found'"
tag=['android']
category=['Android']
+++

In the Android application that I've been playing around with I wrote a service which consumes the Twitter streaming API which I trigger from the app's main activity like so:


~~~java

public class MyActivity extends Activity {
    ...
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Intent intent = new Intent(this, TweetService.class);
        startService(intent);
        ...
    }
}
~~~

Where <cite>TweetService</cite> is defined roughly like this:


~~~java

public class TweetService extends IntentService {
    @Override
    protected void onHandleIntent(Intent intent) {
      // Twitter streaming API stuff goes here
    }
}
~~~

Unfortunately when I tried to deploy the app the service wasn't starting and I got this message in the log:


~~~text

01-01 03:10:31.758: WARN/ActivityManager(106): Unable to start service Intent { cmp=com.example/.TweetService }: not found
~~~

What I hadn't realised is that the service needs to be specified in the <cite>AndroidManifest.xml</cite> file but <a href="http://stackoverflow.com/questions/6313793/unable-to-start-service-intent-cmp-com-marie-mainactivity-backgroundservice">not inside the activity definition</a>:


~~~xml

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example" android:versionCode="1" android:versionName="1.0">
    <application android:label="@string/app_name">
        <activity android:name="MyActivity" android:label="@string/app_name" android:launchMode="singleInstance">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <service android:name="TweetService"></service>
    </application>
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest> 

~~~

After adding the service definition it works fine.
