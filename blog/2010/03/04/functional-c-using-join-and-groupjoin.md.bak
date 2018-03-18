+++
draft = false
date="2010-03-04 18:55:02"
title="Functional C#: Using Join and GroupJoin"
tag=['c', 'net']
category=['.NET']
+++

An interesting problem which I've come across a few times recently is where we have two collections which we want to use together in some way and get a result which could either be another collection or some other value.

In one which <a href="http://enginechris.wordpress.com">Chris</a> and I were playing around with we had a collection of years and a collection of cars with corresponding years and the requirement was to show all the years on the page with the first car we found for that year or an empty value if there was no car for that year.

We effectively needed to do a left join on the cars collection.

This is an imperative way of solving the problem:


~~~csharp

public class Car
{
     public int Year { get; set; }
     public string Description { get; set; }
}
~~~


~~~csharp

var years = new[] { 2000, 2001, 2002, 2003 };
var cars = new[] { new Car { Year = 2000, Description = "Honda" }, new Car { Year = 2003, Description = "Ford" } };

var newCars = new List<Car>();
foreach (var year in years)
{
    var car = cars.Where(x => x.Year == year).FirstOrDefault() ?? new Car  { Year = year, Description = ""};
    newCars.Add(car);
}
~~~

We can actually achieve the same result in a more declarative way by making use of '<a href="http://msdn.microsoft.com/en-us/library/bb534297.aspx">GroupJoin</a>':


~~~csharp

var newCars = years.GroupJoin(cars, 
                              year => year, 
                              car => car.Year,
                              (year, theCars) =>  theCars.FirstOrDefault() ??  new Car { Year = year, Description = ""  });
~~~

'GroupJoin' is useful if we want to keep all of the items in the first collection and get a collection of the items in the second collection which match for the specified keys.

In this case it allows us to identify where there are no matching cars for a specific year and then just set a blank description for those years.

One nice side effect is that if we later want to include multiple cars for a year then we shouldn't have to change the code too much to achieve that.

Another example which I came across is where we have one collection which contains filter criteria which it needs to apply against the other collection.

We have a collection of years and need to indicate whether there is a matching car for each of those years. 


~~~csharp

[Test]
public void JoinExample()
{
    var years = new[] { 2000, 2003 };
    var cars = new[] { new Car { Year = 2000, Description = "Honda" },
                       new Car { Year = 2003, Description = "Ford" },
                       new Car { Year = 2003, Description = "Mercedes"}};

    Assert.That(AreThereMatchingCars(years, cars), Is.True);
}
~~~


~~~csharp

public bool AreThereMatchingCars(IEnumerable<int> years, IEnumerable<Car> cars)
{
    foreach (var year in years)
    {
        if(cars.Where(c => c.Year == year).Count() == 0)
        {
            return false;
        }
    }
    return true;
}
~~~

We can rewrite this function like so:


~~~csharp

public bool AreThereMatchingCars(IEnumerable<int> years, IEnumerable<Car> cars)
{
    var distinctCars = cars.GroupBy(x => x.Year).Select(x => x.First());
    return years.Join(distinctCars, y => y, c => c.Year, (y, c) => c).Count() == years.Count();
}
~~~

This actually become more complicated than we expected because we were working out if there were matching cars for each of the specified years by checking the number of filter items and then comparing it to the number of items when we joined that collection with our collection of cars.

If we have more than one car for the same year that logic falls down so we needed to get just one car per year which is what the first line of the function does.

I can't decide whether or not the code is easier to read and understand by making use of these functions but it's an approach that I picked up when playing around with F# so it's interesting that it can still be applied in C# code as well.
