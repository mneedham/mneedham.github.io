+++
draft = false
date="2012-01-02 02:39:52"
title="Learning Android: Authenticating with Twitter using OAuth"
tag=['android']
category=['Android']
+++

I want to be able to get the tweets from my timeline into my app which means I need to authorise the app with Twitter using OAuth.

The last time I tried to authenticate using OAuth a couple of years ago was a bit of a failure but luckily this time <a href="http://honza.ca/2010/09/how-to-use-twitter-oauth-on-android">Honza Pokorny has written a blog post explaining what to do</a>.

I had to adjust the code a little bit from what's written on his post so I thought I'd document what I've done.

We're using the <a href="https://github.com/kaeppler/signpost">signpost</a> library for which we need to download the following two jars and put them into the app's 'libs' directory.


~~~text

wget http://oauth-signpost.googlecode.com/files/signpost-commonshttp4-1.2.1.1.jar
wget http://oauth-signpost.googlecode.com/files/signpost-core-1.2.1.1.jar
~~~

I created a button that had to be clicked to fire the first step of OAuth authentication with twitter. The code looks like this:


~~~java

public class MyActivity extends Activity {
  private String CALLBACKURL = "app://twitter";
  private String consumerKey = "TwitterConsumerKey";
  private String consumerSecret = "TwitterConsumerSecret";

  private OAuthProvider httpOauthprovider = new DefaultOAuthProvider("https://api.twitter.com/oauth/request_token", "https://api.twitter.com/oauth/access_token", "https://api.twitter.com/oauth/authorize");
  private CommonsHttpOAuthConsumer httpOauthConsumer = new CommonsHttpOAuthConsumer(consumerKey, consumerSecret);

  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    ImageButton oauth = (ImageButton) findViewById(R.id.oauth_button);
    oauth.setOnClickListener(new View.OnClickListener() {
      public void onClick(View v) {
        try {
          String authUrl = httpOauthprovider.retrieveRequestToken(httpOauthConsumer, CALLBACKURL);
          Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(authUrl));
          v.getContext().startActivity(intent);
        } catch (Exception e) {
          Log.w("oauth fail", e);
          Toast.makeText(v.getContext(), e.getMessage(), Toast.LENGTH_LONG).show();
        }
      }
    });
  }
}
~~~

The <cite>CALLBACK</cite> URL is called by Twitter when the user authorises the application (and therefore the request token). Usually it would be a HTTP URL but in this case we need to define a special URL which gets handled by our application.

The <cite>consumerKey</cite> and <cite>consumerSecret</cite> are values <a href="https://dev.twitter.com/apps">assigned by Twitter for the application</a>.

The definition of the callback URL in the manifest file looks like this:


~~~xml

<activity android:name="MyActivity" android:label="@string/app_name" android:launchMode="singleInstance">
  ...
  <intent-filter>
    <action android:name="android.intent.action.VIEW"/>
    <category android:name="android.intent.category.DEFAULT"/>
    <category android:name="android.intent.category.BROWSABLE"/>
    <data android:scheme="app" android:host="twitter" />
  </intent-filter>
</activity>
~~~

We can change <cite>app://twitter</cite> to be anything we want but it <a href="http://stackoverflow.com/questions/4644239/how-i-can-call-back-in-android-using-oauth-for-twitter">needs to match what's defined</a> in the <cite>data</cite> element in our manifest file.

I found that I needed to define <cite>Callback URL</cite> in my application's settings on Twitter otherwise I ended up getting this error:


~~~text

oauth.signpost.exception.OAuthCommunicationException: Communication with the service provider failed: https://api.twitter.com/oauth/request_token
        at oauth.signpost.AbstractOAuthProvider.retrieveToken(AbstractOAuthProvider.java:214)
        at oauth.signpost.AbstractOAuthProvider.retrieveRequestToken(AbstractOAuthProvider.java:69)
...
 Caused by: java.io.FileNotFoundException: https://api.twitter.com/oauth/request_token
        at org.apache.harmony.luni.internal.net.www.protocol.http.HttpURLConnectionImpl.getInputStream(HttpURLConnectionImpl.java:521)
        at org.apache.harmony.luni.internal.net.www.protocol.https.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:258)
        at oauth.signpost.basic.HttpURLConnectionResponseAdapter.getContent(HttpURLConnectionResponseAdapter.java:18)
        at oauth.signpost.AbstractOAuthProvider.handleUnexpectedResponse(AbstractOAuthProvider.java:228)
        at oauth.signpost.AbstractOAuthProvider.retrieveToken(AbstractOAuthProvider.java:189)
~~~

I ended up just setting my callback URL on Twitter to the URL of this blog. It doesn't seem to matter what you put the URL as since it's going to be overridden by our callback URL anyway but it does need to be set.

The callback then gets handled by the following code in <cite>MyActivity</cite>...


~~~java

public class MyActivity extends Activity {
  ...

  @Override
  protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);

    Log.w("redirect-to-app", "going to save the key and secret");

    Uri uri = intent.getData();
    if (uri != null && uri.toString().startsWith(CALLBACKURL)) {

        String verifier = uri.getQueryParameter(oauth.signpost.OAuth.OAUTH_VERIFIER);

        try {
            // this will populate token and token_secret in consumer

            httpOauthprovider.retrieveAccessToken(httpOauthConsumer, verifier);
            String userKey = httpOauthConsumer.getToken();
            String userSecret = httpOauthConsumer.getTokenSecret();

            // Save user_key and user_secret in user preferences and return
            SharedPreferences settings = getBaseContext().getSharedPreferences("your_app_prefs", 0);
            SharedPreferences.Editor editor = settings.edit();
            editor.putString("user_key", userKey);
            editor.putString("user_secret", userSecret);
            editor.commit();

        } catch (Exception e) {

        }
    } else {
        // Do something if the callback comes from elsewhere
    }
  }
}
~~~

...which makes another call to Twitter to get the user's key and secret (the access token) which it then stored in shared preferences so we can use it in future without having to re-authenticate with Twitter.

We can then query Twitter like so:


~~~java

HttpGet get = new HttpGet("http://api.twitter.com/1/statuses/home_timeline.json");
HttpParams params = new BasicHttpParams();
HttpProtocolParams.setUseExpectContinue(params, false);
get.setParams(params);

try {
  SharedPreferences settings = getContext().getSharedPreferences("your_app_prefs", 0);
  String userKey = settings.getString("user_key", "");
  String userSecret = settings.getString("user_secret", "");

  httpOauthConsumer.setTokenWithSecret(userKey, userSecret);
  httpOauthConsumer.sign(get);

  DefaultHttpClient client = new DefaultHttpClient();
  String response = client.execute(get, new BasicResponseHandler());
  JSONArray array = new JSONArray(response);
} catch (Exception e) { 
  // handle this somehow
} 
~~~

Here we retrieve the user's key and secret which we saved on the previous step and then set them on our OAuth consumer which we use to sign our request to Twitter. 

There is a nice explanation of how OAuth works about <a href="http://stackoverflow.com/questions/1390881/how-does-twitters-oauth-system-work">half way down this StackOverFlow post</a>, Eran Hammer-Lahav has a pretty good <a href="http://hueniverse.com/2007/10/beginners-guide-to-oauth-part-i-overview/">"beginner's guide to OAuth"</a> on his blog and <a href="http://tools.ietf.org/html/rfc5849">the OAuth spec</a> is surprisingly readable as well.
