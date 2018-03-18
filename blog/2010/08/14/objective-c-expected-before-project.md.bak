+++
draft = false
date="2010-08-14 10:33:24"
title="Objective C: Expected '(' before 'Project'"
tag=['objective-c-2']
category=['Objective C']
+++

A mistake I've made more than a few times while declaring headers in Objective C is forgetting to explicitly import the classes used in the interface definition.

I've been refactoring <a href="http://www.markhneedham.com/blog/2010/08/09/ipad-redrawing-the-screen/">some of the code I wrote earlier in the week</a> and wanted to create a 'LabelFactory'. I had the following code:

LabelFactory.h

~~~objc

#import <UIKit/UIKit.h>

@interface LabelFactory : NSObject {
}

+ (UILabel*)createLabelFrom:(Project *)project withXCoordinate:(NSInteger)x withYCoordinate:(NSInteger)y;

@end
~~~

Which gives this error on compilation:


~~~text

/Users/mneedham/SandBox/iPad/CIMon/LabelFactory.h:9:0 /Users/mneedham/SandBox/iPad/CIMon/LabelFactory.h:9: error: expected ')' before 'Project'
~~~

I've been wondering what that error message actually means for a while and more by accident than design I re-read the section of Apple's documentation on '<a href="http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocDefiningClasses.html">referring to other classes</a>'

<blockquote>
An interface file declares a class and, by importing its superclass, implicitly contains declarations for all inherited classes, from NSObject on down through its superclass. If the interface mentions classes not in this hierarchy, it must import them explicitly or declare them with the @class directive:
</blockquote>

Declaring 'Project' with the '@class' directive just above '@interface' helps fix that problem:


~~~objc

...
@class Project;

@interface LabelFactory : NSObject {

}
...
~~~

The original error message I was getting is still slightly mystifying to me...
