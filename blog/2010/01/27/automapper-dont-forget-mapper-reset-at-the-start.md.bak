+++
draft = false
date="2010-01-27 07:57:22"
title="Automapper: Don't forget Mapper.Reset() at the start"
tag=['automapper']
category=['.NET']
+++

I wrote about <a href="http://www.markhneedham.com/blog/2010/01/22/automapper-first-thoughts/">my first thoughts using Automapper</a> last week and although I realised that it makes use of the static gateway pattern we ran into a problem where two consecutive calls to a method using AutoMapper always returned the same value for one of the mappings.

The code was roughly like this:


~~~csharp

public Bar CreateNewBar(Bar originalBar, string someNewValue)
{
	Mapper.CreateMap<Baz, Baz>()
      .ForMember(x => x.Id, opts => opts.Ignore())
      .ForMember(x => x.SomeProperty, opts => opts.MapFrom(source => someNewValue));
}
~~~

In our test everything worked fine because we were only calling the method once but when testing it out we were making multiple calls to the method and always receiving the same value for 'someNewValue'.

I hadn't quite pieced together that each mapping was probably only created once for each source/destination pair. I thought it would be recreated each time but browsing through the code we can see that's what's going on:

<a href="http://code.google.com/p/automapperhome/source/browse/trunk/src/AutoMapper/Configuration.cs">Configuration.cs</a>

~~~csharp

public IMappingExpression CreateMap(Type sourceType, Type destinationType)
{
   var typeMap = CreateTypeMap(sourceType, destinationType);

   return new MappingExpression(typeMap, _serviceCtor);
}
~~~


~~~csharp

public TypeMap CreateTypeMap(Type source, Type destination)
{
   TypeMap typeMap = FindExplicitlyDefinedTypeMap(source, destination);
				
   if (typeMap == null)
   {
   ...
   }
   return typeMap;
}
~~~


~~~csharp

private TypeMap FindExplicitlyDefinedTypeMap(Type sourceType, Type destinationType)
{
   return _typeMaps.FirstOrDefault(x => x.DestinationType == destinationType && x.SourceType == sourceType);
}
~~~

We put a test which called the method 'CreateNewBar' method twice to make sure that was actually the problem and then made use of the 'Reset' method on 'Mapper' to avoid the problem:


~~~csharp

public Bar CreateNewBar(Bar originalBar, string someNewValue)
{
    Mapper.Reset();
	Mapper.CreateMap<Baz, Baz>()
      .ForMember(x => x.Id, opts => opts.Ignore())
      .ForMember(x => x.SomeProperty, opts => opts.MapFrom(source => someNewValue));
}
~~~
