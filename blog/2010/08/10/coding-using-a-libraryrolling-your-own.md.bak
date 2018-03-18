+++
draft = false
date="2010-08-10 17:25:39"
title="Coding: Using a library/rolling your own"
tag=['coding']
category=['Coding']
+++

One of the things that I've noticed as we've started writing more client side code is that I'm much more likely to look for a library which solves a problem than I would be with server side code.

A requirement that we've had on at least the last 3 or 4 projects I've worked on is to do client side validation on the values entered into a form by the user.

The <a href="http://docs.jquery.com/Plugins/Validation">jQuery.validate</a> plugin is quite a good fit for this problem and as long as the validation is just on a field by field basis then it works fine.

On the last project I worked on, however, we had validation rules which had field interdependencies and suddenly we ended up writing a lot of custom code to handle that on top of what jQuery.validate already did.

Eventually we got to the stage where the code had become a complete mess and we decided to rewrite the validation code server side and only fire the validation when the user submitted the form.

In this situation that was an acceptable trade off to make but in another we may have needed to write our own Javascript code to handle the various validation rules. 

In that case we'd probably want to write our own code to handle the inter field dependencies but still use jQuery.validate to handle individual field validation.

While thinking about this I was reminded of <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=8826">a post written by Michael Feathers back in 2003 where he discusses 'stunting a framework'</a>:

<blockquote>
[...]let's think about great frameworks... erm.. there aren't many are there? In fact, even the good ones are a pain in the ass, aren't they? There was that time when we downloaded framework X and it took quite a bit of time to learn how to use it, and that other time when we thought it would be useful if only it did that, but we spent the next week trying to force it and..."

Framework use is hard, yet we keep trying. Why do we do it? Mainly because we want to [...] leverage the work of others. If we use someone's else framework, we may save some time. Moreover, we've benefited from someone's "crystalized thought," thought in the form of working code. The code shows a proven way of doing things and if it's well-designed it can accommodate our thoughts and we can roll them back to the community.
</blockquote>

Although the majority of the article is talking about frameworks from the angle of avoiding the temptation to create frameworks, I think it's interesting to consider whether we always need to use a framework.

One other area where I've noticed we instinctively turn to a framework is when we have to interact with a database. The instinct is to straight away use Hibernate/NHibernate/ActiveRecord when frequently the initial use case doesn't really require their use.

However, if we don't make that decision up front then <strong>we need to be quite vigilant about observing the point at which we're actually just reinventing the wheel</strong> rather than making a pragmatic decision not to use an ORM tool.

There are certainly other considerations to make when deciding whether to use a library or not such as our familiarity with it and its reputation/reliability in the community but it is still a decision point and one that I've frequently not recognised as being one and just gone straight for the library option.
