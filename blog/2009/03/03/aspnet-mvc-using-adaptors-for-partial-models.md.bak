+++
draft = false
date="2009-03-03 23:55:36"
title="ASP.NET MVC: Reducing duplication for partial models"
tag=['aspnet', 'aspnet-mvc']
category=['.NET']
+++

One of the problems we can encounter when using <a href="http://www.markhneedham.com/blog/2009/02/21/aspnet-mvc-driving-partials-by-convention/">partials</a> throughout our views is how we should create the model needed for those partials.

The approach that we have been following is to have the partial/child model on the parent model and then just call the appropriate method where we create the partial.

e.g.


~~~csharp

public class ParentModel 
{
	public string Property1 {get;set;}
	public ChildModel ChildModel { get;set; }
}

public class ChildModel
{
	public string Property1 {get;set;}
}
~~~

We have sometimes run into the problem where the data in the ChildModel is being populated from the ParentModel (due to it also being needed there) leading to data duplication.


~~~csharp

ParentModel parentModel = new ParentModel();
parentModel.Property1 = "value1"
parentModel.ChildModel = new ChildModel 
						{	
							Property1 = parentModel.Property1;
					  	}
~~~

Now the other problem with this is that we are relying on line 2 being executed before line 3 - we have created an order dependency in our code for no gain!

We are following a convention of having minimal logic in our views which means that we want to avoid creating the ChildModel in our view, meaning that we now have a problem to solve.

A cool approach which <a href="http://twitter.com/davcamer">Dave</a> introduced me to makes use of the <a href="http://www.dotnetheaven.com/Uploadfile/rajeshvs/AdapterPatternInCS02012006034414AM/AdapterPatternInCS.aspx">Adaptor pattern</a> to solve the problem.

We would adjust the ParentModel like so:


~~~csharp

public class ParentModel
{
	public IChildModel { get { return new ChildModelAdaptor(this); }}
}
~~~

We then just delegate the calls to the ParentModel and drive the ChildModel to become an interface since it no longer needs to be a class.
	

~~~csharp

public interface ChildModel
{
	string Property1 {get;set;}
}
~~~


~~~csharp

public class ChildModelAdaptor : IChildModel 
{
	private ParentModel parentModel;

	public ChildModelAdaptor(ParentModel parentModel)
	{
		this.parentModel = parentModel;
	}

	public string Property1
	{		
		get { return parentModel.Property1; }
	}
}
~~~

If the data on the ChildModel is completely independent of the ParentModel then I would probably just create the model like before.

If the data on the ChildModel is a combination of data from the ParentModel and other classes then I would pass in those other classes in the constructor of the adaptor.
