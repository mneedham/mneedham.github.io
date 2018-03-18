+++
draft = false
date="2012-11-30 16:56:16"
title="There's No such thing as a 'DevOps Team': Some thoughts"
tag=['devops-2']
category=['DevOps']
+++

<p>A few weeks ago <a href="http://jezhumble.net/">Jez Humble</a> wrote a blog post titled "<a href="http://continuousdelivery.com/2012/10/theres-no-such-thing-as-a-devops-team/">There's no such thing as a 'DevOps team'</a>" where he explains what DevOps is actually supposed to be about and describes a model of how developers and operations folk can work together.</p>

<p>Jez's suggestion is for developers to take responsibility for the systems they create but he notes that:</p>

<blockquote>[...] they need support from operations to understand how to build reliable software that can be continuous deployed to an unreliable platform that scales horizontally. They need to be able to self-service environments and deployments. They need to understand how to write testable, maintainable code. They need to know how to do packaging, deployment, and post-deployment support.</blockquote>
<p>His suggestions sound reasonably similar to the way <a href="https://dl.dropbox.com/u/1018963/Articles/SpotifyScaling.pdf">Spotify have their teams setup</a> whereby product teams own their product from idea to production but can get help from an operations team to make this happen.</p>

<blockquote>At Spotify there is a separate operations team, but their job is not to make releases for the squads - their job is to give the squads the support they need to release code themselves; support in the form of infrastructure, scripts, and routines. They are, in a sense, “building the road to production”.
<p>It’s an informal but effective collaboration, based on face-to-face communication rather than detailed process documentation.</p>

</blockquote>

<p>On a few of projects that I've worked on in the last 18 months or so we've tried to roughly replicate this model but there are a few challenges in doing so.</p>


<h4>Silo Mentality</h4>
<p>In a number of the organisations that I've worked at there is a mentality that people should only take responsibility for 'their bit' which in this case means developers code the application and operations deploy it.</p>


<p>This manifests itself when you hear comments such as "it must be an application problem" when something isn't working rather than working together to solve the problem.</p>
 

<p>There's also a more subtle version of this when we get into the belief that developers are only responsible for putting points on the board therefore they shouldn't spend time doing operations-y work.</p>


<h4>Release Pressure</h4>

<p>Even if we've got beyond the idea that people should only be responsible for their silo and have operations and developers working closely together it can still end up reverting back to type when people are under pressure.</p>


<p>When a big release is coming up there'll often be a push to ensure that the expected features have been completed and this leads us back towards the silo mentality, at least temporarily.</p>


<p>Presumably with a more frequent release schedule this becomes less of an issue but I haven't worked for long enough in that way to say for sure.</p>


<h4>Security Concerns</h4>

<p>In some environments there is often quite tight security around who is allowed to push into production and this would typically be folks in the operations team.</p>


<p>Obviously this means that the product team can't actually push their own changes unless they arrange to work together with one of the operations folks to do so.</p>


<p>We still don't have the 'throw it over the wall' mentality in this setup but it does create more of a bottle neck in the system than we'd have otherwise.</p>


<h4>In Summary</h4>

<p>These are just some of the obstacles that I've seen that can get in the way of our optimal setup.</p>


<p>I'm sure there are others that I haven't come across yet but the nice thing is that two of these are more a mindset thing than anything else so that can be fixed over time.</p>

