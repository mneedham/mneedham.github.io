+++
draft = false
date="2012-01-06 23:40:53"
title="Learning Android: Freezing the UI with a BroadcastReceiver"
tag=['android']
category=['Android']
+++

As I <a href="http://www.markhneedham.com/blog/2012/01/05/learning-android-getting-a-service-to-communicate-with-an-activity/">mentioned in a previous post</a> I recently wrote some code in my Android app to inform a <a href="http://developer.android.com/reference/android/content/BroadcastReceiver.html">BroadcastReceiver</a> whenever a service processed a tweet with a link in it but in implementing this I managed to freeze the UI every time that happened.

I made the stupid (in hindsight) mistake of not realising that I shouldn't be doing a lot of logic in <cite>BroadcastReceiver.onReceive</cite> since that bit of code gets executed on the UI thread.

The service code which raises the broadcast message is the same as in the previous post:


~~~java

public class TweetService extends IntentService {
    ...
    @Override
    protected void onHandleIntent(Intent intent) {
        StatusListener listener = new UserStreamListener() {
           // override a whole load of methods - removed for brevity

            public void onStatus(Status status) {
                String theTweet = status.getText();
                if (status.getText().contains("http://")) {
                    Intent tweetMessage = new Intent(TweetTask.NEW_TWEET);
                    tweetMessage.putExtra(android.content.Intent.EXTRA_TEXT, status.getText());
                    sendBroadcast(tweetMessage);
                }

            }
        };

        // code to connect to the twitter streaming API
    }
}
~~~

That is then handled like this by the BroadcastReceiver:


~~~java

public class MyActivity extends Activity {
    protected void onPause() {
        super.onPause();
        if (dataUpdateReceiver != null) unregisterReceiver(dataUpdateReceiver);
    }

    protected void onResume() {
        super.onResume();
        if (dataUpdateReceiver == null) dataUpdateReceiver = new DataUpdateReceiver();
        IntentFilter intentFilter = new IntentFilter(TweetTask.NEW_TWEET);
        registerReceiver(dataUpdateReceiver, intentFilter);
    }

    private class DataUpdateReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            if (intent.getAction().equals(TweetTask.NEW_TWEET)) {
                Pattern p = Pattern.compile("(http://[^\\s]+)");
                String theTweet = intent.getStringExtra(TweetTask.NEW_TWEET);
                Matcher matcher = p.matcher(theTweet);

                int startIndex = -1;
                int endIndex = -1;
                while (matcher.find()) {
                    startIndex = matcher.start();
                    endIndex = matcher.end();
                }

                if (startIndex != -1 && endIndex != -1) {
                    String resolvedUrl = resolveUrl(theTweet.substring(startIndex, endIndex));
                    saveToDatabase(resolvedUrl);
                    updateUI(resolvedUrl);
                }
            }
        }
    }
}
~~~

In particular the 'resolveUrl' line was probably the one one causing the problem since it makes a network call to<a href="http://www.markhneedham.com/blog/2011/12/31/clojure-casting-to-a-java-class-or-not/"> resolve URLs from link shorteners</a>.

To stop the screen freezing up I just needed to move most of the code from BroadcastReceiver into the TweetService:


~~~java

public class TweetService extends IntentService {
    ...
    @Override
    protected void onHandleIntent(Intent intent) {
        StatusListener listener = new UserStreamListener() {
           // override a whole load of methods - removed for brevity

            public void onStatus(Status status) {
                String theTweet = status.getText();
                if (status.getText().contains("http://")) {
                    Pattern p = Pattern.compile("(http://[^\\s]+)");
                    Matcher matcher = p.matcher(theTweet);

                    int startIndex = -1;
                    int endIndex = -1;
                    while (matcher.find()) {
                        startIndex = matcher.start();
                        endIndex = matcher.end();
                    }

                    if (startIndex != -1 && endIndex != -1) {
                        String resolvedUrl = resolveUrl(theTweet.substring(startIndex, endIndex));
                        saveToDatabase(resolvedUrl);

                        Intent tweetMessage = new Intent(TweetTask.NEW_TWEET);
                        tweetMessage.putExtra(android.content.Intent.EXTRA_TEXT, resolvedUrl);
                        sendBroadcast(tweetMessage);
                    }
                }
            }
        };

        // code to connect to the twitter streaming API
    }
}
~~~

And then the code for BroadcastReceiver becomes much simpler which means we're doing less work on the UI thread:


~~~java

    private class DataUpdateReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            if (intent.getAction().equals(TweetTask.NEW_TWEET)) {
                String url = intent.getStringExtra(TweetTask.NEW_TWEET);
                updateUI(url);
            }
        }
    }
~~~

And the freezing up of the UI is gone!
