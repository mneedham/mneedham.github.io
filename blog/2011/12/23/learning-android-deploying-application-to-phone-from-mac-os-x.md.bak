+++
draft = false
date="2011-12-23 22:55:17"
title="Learning Android: Deploying application to phone from Mac OS X"
tag=['android']
category=['Android']
+++

I've been playing around a little bit today with writing an Android application and while for the majority of the time I've been deploying to an emulator I wanted to see what it'd look like on my phone.

<a href="http://developer.android.com/guide/developing/device.html">The developer guide contains all the instructions</a> on how to do this but unfortunately I'm blessed with the ability to skim over instructions which meant that my phone wasn't getting picked up by the <a href="http://developer.android.com/guide/developing/tools/adb.html">Android Debug Bridge</a>.

We can check which devices have been detected by running the following command from wherever the SDK is installed:


~~~text

/Users/mneedham/github/android/android-sdk-macosx/platform-tools/adb devices
~~~

This was initially returning no devices and <a href="http://esausilva.com/2010/10/02/how-to-set-up-adb-android-debug-bridge-in-mac-osx/">reading Esau Silva's blog</a> made me realise that I'd failed to follow this instruction:

<blockquote>
On the device, go to Settings > Applications > Development and enable USB debugging (on an Android 4.0 device, the setting is located in Settings > Developer options).
</blockquote>

I'd assumed it was only necessary if I wanted to debug the application on my phone but it seems like you need to set it to be able to deploy in the first place. 

And now my phone gets picked up and can be deployed to, yay!


~~~text

/Users/mneedham/github/android/android-sdk-macosx/platform-tools/adb devices

List of devices attached 
3933C40945FA00EC	device
~~~

If it still doesn't work then <a href="http://esausilva.com/2010/10/02/how-to-set-up-adb-android-debug-bridge-in-mac-osx/">Esau Silva has some other ideas</a> which I haven't yet needed to try.
