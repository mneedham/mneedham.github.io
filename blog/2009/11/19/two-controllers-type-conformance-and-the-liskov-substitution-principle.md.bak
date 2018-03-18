+++
draft = false
date="2009-11-19 00:08:39"
title="Two controllers, type conformance and the Liskov Substitution Principle "
tag=['coding']
category=['Coding']
+++

An interesting object orientation related problem that <a href="http://twitter.com/raphscallion">Raph</a> and I were looking at recently revolved around the design of two controllers in the application we've been working on.

The two controllers in question look roughly like this:


~~~java

public class GenericController extends Controller {
	private final SomeFactory someFactory;

	public GenericController(SomeFactory someFactory);
        this.someFactory = someFactory;
	}

    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
        // do some stuff but never use 'request' or 'response'
    }
}
~~~


~~~java

public class MoreSpecificController extends GenericController {
	private final SomeFactory someFactory;

	public MoreSpecificController(SomeFactory someFactory);
        super(someFactory);
	}

    public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
    		...    
		// do some stuff which does use 'request'
		String someValue = request.getParameter("someParameter");
    }
}
~~~

We noticed from the way that we wrote tests for these two classes that we seem to be breaking the principle of type conformance as defined in Meilir Page Jones' '<a href="http://www.amazon.com/gp/product/020169946X?ie=UTF8&tag=marneesblo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=020169946X">Fundamentals of Object Oriented Design in UML</a>' and more commonly referred to as the <a href="http://www.objectmentor.com/resources/articles/lsp.pdf">Liskov Substitution Principle</a>.

The principle states:
<blockquote>If S is a true subtype of T, then S must conform to T. In other words, an object of type S can be provided in any context where an object of T is expected and correctness is still preserved when any accessor operation of the object is executed</blockquote>

This means that wherever we make use of 'GenericController' in our code it should be possible to pass in an instance of 'MoreSpecificController' and it would adhere to the same contract.

Our tests for each of the controllers looked a bit like this:


~~~java

@Test
public void someTest() {
	GenericController genericController = new GenericController();

	genericController.handleRequest(null, null);

	// and so on
}
~~~


~~~java

@Test
public void someTest() {
	MoreSpecificController moreSpecificController = new MoreSpecificController();

	moreSpecificController.handleRequest(mock(HttpServletRequest.class), mock(HttpServletResponse.class));

	// and so on
}
~~~

In 'MoreSpecificController' we need to get a value from the request which means that we can't have it as null in the test. In 'GenericController' the request is actually irrelevant so we can pass in a null value.

This means that the pre condition for 'MoreSpecificController' is stronger than the pre condition for 'GenericController' which violates the principle of contravariance which states the following:

<blockquote>Every operation's precondition is no stronger than the corresponding operation in the superclass. The strength of operation preconditions in the subclass goes in the opposite direction to the strength of the class invariant. That is, the operations preconditions get, if anything, weaker</blockquote>

The reason this might cause a problem is because if a client had a reference to a 'GenericController' they should expect that they can treat an instance of 'MoreSpecificController' as if it was a 'GenericController' which should mean that we can pass null values for request and response.

We weren't ever referring to a 'GenericController' when we instantiated a 'MoreSpecificController' in our code base so it didn't prove to be a problem but in theory it seems like something we'd want to avoid.
