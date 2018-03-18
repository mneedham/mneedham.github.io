+++
draft = false
date="2010-03-19 07:48:51"
title="Functional C#: Continuation Passing Style"
tag=['c', 'functional-programming']
category=['.NET']
+++

Partly inspired by <a href="http://alexscordellis.blogspot.com/2010/03/lambda-passing-style-for-access-to.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+alexscordellis+(Alex+Scordellis)">my colleague Alex Scordellis' recent post about lambda passing style</a> I spent some time trying out a <a href="http://www.markhneedham.com/blog/2009/06/22/f-continuation-passing-style/">continuation passing style</a> style on some of the code in one of our controllers to see how different the code would look compared to its current top to bottom imperative style.

We had code similar to the following:


~~~csharp

public ActionResult Submit(string id, FormCollection form)
{
	var shoppingBasket = CreateShoppingBasketFrom(id, form);

	if (!validator.IsValid(shoppingBasket, ModelState))
	{
	    return RedirectToAction("index", "ShoppingBasket", new { shoppingBasket.Id });
	}
	try
	{
	    shoppingBasket.User = userService.CreateAccountOrLogIn(shoppingBasket);
	}
	catch (NoAccountException)
	{
	    ModelState.AddModelError("Password", "User name/email address was incorrect - please re-enter");
	    return RedirectToAction("index", ""ShoppingBasket", new { Id = new Guid(id) });
	}

	UpdateShoppingBasket(shoppingBasket);
	return RedirectToAction("index", "Purchase", new { Id = shoppingBasket.Id });
}
~~~

The user selects some products that they want to buy and then just before they click to go through to the payment page we have the option for them to login if they are an existing user.

This code handles the server side validation of the shopping basket and tries to login the user. If it fails then we return to the original page with an error message. If not then we forward them to the payment page.

With a continuation passing style we move away from the imperative style of programming whereby we call a function, get a result and then do something with that result to a style where we call a function and pass it a continuation/block of code which represents the rest of the program. After it has calculated the result it should call the continuation.

If we apply that style to the above code we end up with the following:


~~~csharp

public ActionResult Submit(string id, FormCollection form)
{
	var shoppingBasket = CreateShoppingBasketFrom(id, form);
	return IsValid(shoppingBasket, ModelState,
					() => RedirectToAction("index", "ShoppingBasket", new { shoppingBasket.Id} ),
					() => LoginUser(shoppingBasket, 
							() =>
								{
									ModelState.AddModelError("Password", "User name/email address was incorrect - please re-enter");
									return RedirectToAction("index", ""ShoppingBasket", new { Id = new Guid(id) });
								},
							user => 
								{
									shoppingBasket.User = user;
									UpdateShoppingBasket(shoppingBasket);
									return RedirectToAction("index", "Purchase", new { Id = shoppingBasket.Id });
								}));
}


private RedirectToRouteResult IsValid(ShoppingBasket shoppingBasket, ModelStateDictionary modelState, Func<RedirectToRouteResult> failureFn, Func<RedirectToRouteResult> successFn)
{

	return validator.IsValid(shoppingBasket, modelState) ? successFn() : failureFn();
}

private RedirectToRouteResult LoginUser(ShoppingBasket shoppingBasket, Func<RedirectToRouteResult> failureFn, Func<User,RedirectToRouteResult> successFn)
{
	User user = null;
	try
	{
	    user = userService.CreateAccountOrLogIn(shoppingBasket);
	}

	catch (NoAccountException)
	{
		return failureFn();
	}

	return successFn(user);
}
~~~

The common theme in this code seemed to be that there we both success and failure paths for the code to follow depending on the result of a function so I passed in both success and failure continuations.

I quite like the fact that the try/catch block is no longer in the main method and the different things that are happening in this code now seem grouped together more than they were before.

In general though the way that I read the code doesn't seem that different.

Instead of following the flow of logic in the code from top to bottom we just need to follow it from left to right instead and since that's not as natural the code is more complicated than it was before.

I do understand how the code works more than I did before I started playing before this but I'm not yet convinced this is a better approach to designing code in C#.
