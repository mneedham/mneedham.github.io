+++
draft = false
date="2009-11-11 20:30:08"
title="Coding: Pushing the logic back"
tag=['coding']
category=['Coding']
+++

I was reading <a href="http://www.ur-ban.com/blog/2009/10/25/law-of-demeter-and-the-delegate-method/">a post on the law of demeter by Richard Hart</a> recently and it reminded me that a lot of the refactorings that we typically do on code bases are about pushing the logic back into objects instead of exposing data and performing calculations elsewhere.

An example that I spotted where we did this recently was while building a 'BusinessSummary' object whose state was based on the state of a collection of other objects.

The code was keeping a count of the various states of the business objects:


~~~java

public BusinessSummary buildSummaryObject() {
	BusinessSummary businessSummary = new BusinessSummary();

	for(BusinessObject businessObject : businessObjects) {
		State state = businessObject.getState();
		if(State.STATE_1.equals(state)) {
			businessSummary.incrementState1();	
		} else if(State.STATE_2.equals(state)) {
			businessSummary.incrementState2();
		} else {
			// and so on
		}					
	}	
	return businessSummary;
}
~~~
In this example 'State' is an enum representing the state the 'BusinessObject' is currently in.

Our first change to the code was to push the logic around state back into the 'BusinessObject' which results in the following code:


~~~java

public BusinessSummary buildSummaryObject() {
	BusinessSummary businessSummary = new BusinessSummary();

	for(BusinessObject businessObject : businessObjects) {
		if(businessObject.hasState1()) {
			businessSummary.incrementState1();	
		} else if(businessObject.hasState2()) {
			businessSummary.incrementState2();
		} else {
			// and so on
		}					
	}	
	return businessSummary;
}
~~~


~~~java

public class BusinessObject {
	...
	public boolean hasState1() {
		return State.STATE_1.equals(state);
	}
	...
}
~~~

I think this is an improvement but it still isn't following the <a href="http://www.pragprog.com/articles/tell-dont-ask">tell don't ask</a> principle, we're just asking to be told about the data instead of asking for the data itself.

We didn't have the time to do the next change where we would have got rid of the 'hasState' methods and just got the 'BusinessObject' to update the 'BusinessSummary' itself:


~~~java

public BusinessSummary buildSummaryObject() {
	BusinessSummary businessSummary = new BusinessSummary();

	for(BusinessObject businessObject : businessObjects) {
		businessObject.writeTo(businessSummary);					
	}	
	return businessSummary;
}
~~~


~~~java

public class BusinessObject {
	private final State state;
	...
	public void writeTo(BusinessSummary businessSummary) {
		if(State.STATE_1.equals(state)) {
			businessSummary.incrementState1();	
		} else if(State.STATE_2.equals(state)) {
			businessSummary.incrementState2();
		} else {
			// and so on
		}
	}
	...
}
~~~

Looking back on this code having written this post I wonder whether we need to do the loop or whether it would be better to pass the collection of 'businessObjects' to the 'BusinessSummary' and let it take care of that logic instead.

If we did that then we would need to expose 'hasState1' and 'hasState2' methods on 'BusinessObject' like on the first refactoring so that we could work out how to populate 'BusinessSummary'.

I prefer the solution where 'BusinessObject' writes to the 'BusinessSummary' although it seems like 'BusinessObject' now has more than one reason to change - if it changes or if 'BusinessSummary' changes. This would violate the <a href="http://blogs.agilefaqs.com/2009/10/19/single-responsibility-principle-demystified/">single responsibility principle</a>

I discussed this with <a href="http://intwoplacesatonce.com/">Dave</a> and he pointed out that as long as the contract that 'BusinessSummary' and 'BusinessObject' have - i.e. the 'incrementState1' and 'incrementState2' methods - stays the same then it wouldn't really be a problem.
