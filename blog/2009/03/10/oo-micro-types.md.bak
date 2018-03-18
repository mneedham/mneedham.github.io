+++
draft = false
date="2009-03-10 22:40:57"
title="OO: Micro Types"
tag=['oop', 'micro-types']
category=['OOP']
+++

Micro or Tiny types present an approach to coding which seems to divide opinion in my experience, from those who think it's a brilliant idea to those who believe it's static typing gone mad. 

I fall into the former group.

So what is it?

The idea is fairly simple - <strong>all primitives and strings in our code are wrapped by a class, meaning that we never pass primitives around.</strong> 

In essence Rule #3 of Jeff Bay's <a href="http://jimbarritt.com/non-random/2009/03/04/object-calisthenics-jeff-bay/">Object Calisthenics</a>.

As I mentioned on a previous post about <a href="http://www.markhneedham.com/blog/2009/02/25/c-wrapping-datetime/">wrapping dates</a>, I was first introduced to the idea by <a href="http://darrenhobbs.com/">Darren Hobbs</a> as a way of making APIs easier for others to use.

In the world of Java method signatures of 3rd party libraries with minimal Javadoc documentation tend to read like so when you look at their method signatures in your chosen editor.


~~~java

doSomething(string, string, string, string)
~~~

The parameter name is sometimes not available meaning that it is now almost impossible to work out what each of those strings is supposed to represent - guesswork becomes the way forward!

I noticed an even more subtle example when working on a project last year where there was a method to transfer money between accounts. It looked like a bit like this:


~~~java

public void transferMoney(Account debitAccount, Account creditAccount) {
	// code
}
~~~

See how easy it would be to get those accounts the wrong way around and suddenly the money is going in the wrong direction!

I always had to look twice to make sure we were doing the right thing - it was quite confusing.

Using micro types we could solve this problem by wrapping account with a more specific class. The signature could potentially read like so:


~~~java

public void transferMoney(DebitAccount debitAccount, CreditAccount creditAccount) {
	// code
}
~~~

And the confusion has been removed.

The cost of doing this is obviously that we need to write more code - for the above example maybe something like this:


~~~java

public class DebitAccount {
	private Account debitAccount;

	public DebitAccount(Account debitAccount) {
		this.debitAccount = debitAccount;
	}
}
~~~

We'd then delegate the necessary method calls through to the underlying Account although we probably don't need to expose as many methods as the normal account object would since we only care about it in this specific context.

I had the opportunity to work on a project led by <a href="http://pilchardfriendly.wordpress.com/">Nick</a> for a couple of months last year where we were micro typing everything and I quite enjoyed it although opinion was again split.

I felt it helped to keep behaviour and the data together and was constantly forcing you to open your mind to new abstractions.

The other argument against the approach is that you are creating objects which have no behaviour.

I find here that it depends what you classify as behaviour - for me if there is some logic around the way that a string is formatted when it is going to be displayed then that is behaviour and we should look to put that logic as close to the data as possible i.e. within the micro type.

On that project each object rendered itself into a ViewData container which we accessed from our views.


~~~java

public class Micro {
	private string micro;

	public Micro(string micro) {
		this.micro = micro;
	}

	public void renderTo(ViewData viewData) {
		viewData.add(micro);
	}
}
~~~

If an object contained more than one piece of data it could then decide which bits needed to be rendered.

It's certainly not for everyone but it's an approach that I felt made coding much more enjoyable and code much easier to navigate.
