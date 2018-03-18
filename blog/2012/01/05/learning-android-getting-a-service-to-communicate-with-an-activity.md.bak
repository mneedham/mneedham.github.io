+++
draft = false
date="2012-01-05 01:41:32"
title="Learning Android: Getting a service to communicate with an activity"
tag=['android']
category=['Android']
+++

In the app I'm working on I created a service which runs in the background away from the main UI thread consuming the Twitter streaming API using <a href="http://twitter4j.org/en/index.html">twitter4j</a>. 

It looks like this:


~~~java

public class TweetService extends IntentService {
    String consumerKey = "TwitterConsumerKey";
    String consumerSecret = "TwitterConsumerSecret";

    public TweetService() {
        super("Tweet Service");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        AccessToken accessToken = createAccessToken();

        StatusListener listener = new UserStreamListener() {
           // override a whole load of methods - removed for brevity

            public void onStatus(Status status) {
                String theTweet = status.getText();
                if (status.getText().contains("http://")) {
                    // do something with the tweet
                }

            }
        };
        ConfigurationBuilder configurationBuilder = new ConfigurationBuilder();
        configurationBuilder.setOAuthConsumerKey(consumerKey);
        configurationBuilder.setOAuthConsumerSecret(consumerSecret);

        TwitterStream twitterStream = new TwitterStreamFactory(configurationBuilder.build()).getInstance(accessToken);
        twitterStream.addListener(listener);
        twitterStream.user();
    }
}
~~~

That gets called from <cite>MyActivity</cite> like so:


~~~java

public class MyActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        ...
        super.onCreate(savedInstanceState);
        Intent intent = new Intent(this, TweetService.class);
        startService(intent);
    }
}
~~~

I wanted to be able to inform the UI each time there was a tweet which contained a link in it so that the link could be displayed on the UI.

I found <a href="http://stackoverflow.com/questions/2463175/how-to-have-android-service-communicate-with-activity">a post on StackOverflow which suggested that one way to do this would be to raise a broadcast message which could then be listened to by a BroadcastReceiver in the activity</a>.

It is possible for any other apps to listen to the broadcast message as well if they wanted to but in this case the information isn't very important so I think it's fine to take this approach.

I first had to change the service to look like this:


~~~java

public class TweetTask {
    public static final String NEW_TWEET = "tweet_task.new_tweet";
}

public class TweetService extends IntentService {
    String consumerKey = "TwitterConsumerKey";
    String consumerSecret = "TwitterConsumerSecret";

    public TweetService() {
        super("Tweet Service");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        AccessToken accessToken = createAccessToken();

        StatusListener listener = new UserStreamListener() {
           // override a whole load of methods - removed for brevity

            public void onStatus(Status status) {
                String theTweet = status.getText();
                if (status.getText().contains("http://")) {
                    Intent tweetMessage = new Intent(TweetTask.NEW_TWEET);
                    tweetMessage.putExtra(android.content.Intent.EXTRA_TEXT, document);
                    sendBroadcast(tweetMessage);
                }

            }
        };
        ConfigurationBuilder configurationBuilder = new ConfigurationBuilder();
        configurationBuilder.setOAuthConsumerKey(consumerKey);
        configurationBuilder.setOAuthConsumerSecret(consumerSecret);

        TwitterStream twitterStream = new TwitterStreamFactory(configurationBuilder.build()).getInstance(accessToken);
        twitterStream.addListener(listener);
        twitterStream.user();
    }
}
~~~

I then had to define the following code in <cite>MyActivity</cite>:


~~~java

public class MyActivity extends Activity {
    protected void onResume() {
        super.onResume();
        if (dataUpdateReceiver == null) dataUpdateReceiver = new DataUpdateReceiver(textExtractionService);
        IntentFilter intentFilter = new IntentFilter(TweetTask.NEW_TWEET);
        registerReceiver(dataUpdateReceiver, intentFilter);
    }

    protected void onPause() {
        super.onPause();
        if (dataUpdateReceiver != null) unregisterReceiver(dataUpdateReceiver);
    }

    private class DataUpdateReceiver extends BroadcastReceiver {
        private CachedTextExtractionService textExtractionService;

        public DataUpdateReceiver(CachedTextExtractionService textExtractionService) {
            this.textExtractionService = textExtractionService;
        }

        @Override
        public void onReceive(Context context, Intent intent) {
            if (intent.getAction().equals(TweetTask.NEW_TWEET)) {
                // do something with the tweet
            }

        }
    }
}
~~~

Now whenever there's a tweet with a link in it my BroadcastReceiver gets notified and I can do whatever I want with the tweet.

This seems like a reasonably simple solution to the problem so I'd be interested to know if there are any other drawbacks other than the one I identified above.
