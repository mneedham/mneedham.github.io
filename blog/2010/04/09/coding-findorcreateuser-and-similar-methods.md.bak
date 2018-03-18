+++
draft = false
date="2010-04-09 07:09:28"
title="Coding: FindOrCreateUser and similar methods"
tag=['coding']
category=['Coding']
+++

One of the general guidelines that I like to follow when writing methods is trying to ensure that it's only doing one thing but on several recent projects I've noticed us breaking this guideline and it feels like the right thing to do.

The method in question typically takes in some user details, looks up that user in some data store and then returning it if there is an existing user and creating a new user if not.

It would probably look something like this:


~~~csharp

public class UserService
{
	public User FindOrCreateUser(string username)
	{
		var user = userRepository.FindUserBy(username);
		if(user == null)
		{
			user = CreateUserFrom(username);
		}	
		return user;
	}
}
~~~

My initial thought when we wrote it was that it seemed wrong but the method name does clearly describe our requirement so I'm not so sure it's a bad thing.

NHibernate has a 'SaveOrUpdate' method which to me seems to cover similar ground although Save/Update are much closer in functionality then Find/Create so maybe that's more justifiable. 

I'd be interested to know whether you think this type of method is perfectly fine or whether we're very very bad people for writing it!
