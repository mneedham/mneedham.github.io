+++
draft = false
date="2009-05-03 19:08:27"
title="Pair Programming: When your pair steps away"
tag=['pair-programming']
category=['Pair Programming']
+++

I've been having a bit of a discussion recently with some of my colleagues about what we should do when pair programming and one of the people in the pair has to step away to go and help someone else or to take part in an estimation session or whatever it happens to be.

If we're pairing in an effective way then it should be possible for the person still at the computer to keep on going on the story/task that the pair were working on alone. Obviously sometimes that isn't the case especially if <a href="http://www.markhneedham.com/blog/2008/11/05/pair-programming-the-over-eager-driver/">one person has been driving for the majority of the time</a> but for this post we'll assume that both people are capable of continuing alone.

Continuing alone doesn't necessarily mean that you become the <a href="http://www.markhneedham.com/blog/2009/04/10/pair-programming-the-code-fairy/">code fairy</a>, which is where one of the people in a pair goes and implements the functionality of something they had been pairing on in their own favoured style. 

My initial thought is that if the absence is only short term then you shouldn't plow on too much otherwise you need to spend time bringing them back on the same page when they return. 

To give an example, a couple of weeks ago I was pairing with a colleague and we were retrieving a value from a Dictionary if it existed and creating a value in the Dictionary if it did not exist.

<a href="http://www.twitter.com/davcamer">Dave</a> had recently shown me quite a clean way of doing this which I wanted to discuss with my colleague in case they hadn't seen it before - the approach we had been taking to solve this problem wasn't along these lines before my pair was called away.


~~~csharp

public class DictionaryExample
{
    private readonly Dictionary<string, string> values = new Dictionary<string, string>();

    public string FindValue(string key)
    {
        if(!values.ContainsKey(key))
        {
            values[key] = "somethingNew";
        }
        return values[key];
    }
}
~~~

When he came back I suggested this approach and he was happy to go with it.

I sometimes write down stuff I'm unsure of when pairing and I find that if my pair goes off for a short amount of time then this can be a useful time to look that up.

If we decide to keep on going during their absence then I think it's important that we keep going down the same path  that we were when we were pairing to reduce the amount of catching up our pair needs to do when they return.

If they have gone away for a longer period of time then we should treat it as them having left the pair and we can look for someone else to pair with or just code as if we were working alone.

That's my current thinking on this - some colleagues have suggested they think it's better if we just keep on coding regardless but I think this approach finds a happy medium.
