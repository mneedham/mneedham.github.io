+++
draft = false
date="2006-09-02 01:31:40"
title="Inheritance and Delegation"
tag=['coding', 'thoughtworks', 'oop', 'twu']
category=['Coding']
+++

One of the major learning points this week at TWU has been understanding when it is appropriate to use <a href="http://en.wikipedia.org/wiki/Inheritance_%28computer_science%29" target="_blank">inheritance</a> and when <a href="http://en.wikipedia.org/wiki/Object_composition" target="_blank">delegation</a> is the better choice.

I had heard stories about how inheritance could be misused but I didn't think I would be stupid enough to fall straight into that trap! We were taught the concept using 'Measurement' as the problem domain. So to translate the previous sentence into English: The aim was to design classes which could handle old school measurement types such as Inches, Feet, Yards, and so on.

I went about the task by first creating a base Measurement class and then created Inch, Foot and Yard as sub classes of this. The code looked pretty slick to me and I was quite pleased with how it had turned out. I was feeling pretty confident that I had nailed the objective of the session. Alas, it was not meant to be!

Upon reviewing the code my partner and I had created, one of the trainers pointed out that the sub classes did not actually do very much at all. They were effectively useless classes and there was barely any difference between them! One of the other requirements for the code was that it should be possible to compare an instance of the Inch class with an instance of the Foot class, an instance of the Yard class with the Inch class and so on. No problem I thought and promptly created methods called 'ConvertToFoot' in my Inch class and 'ConvertToInch' in my Foot class.

One of the cardinal sins of object orientated programming had been committed! I now had 2 methods which did almost the exact same as the other for no additional benefit. What if there were 100 different measurements? That would mean 99 different conversion methods each to convert to all the other types of measurement. Clearly not an optimal solution - I had taken the bait and fallen into the trap of over use of inheritance.

Anyway, the lesson of the session was that in this particular case it was better to use delegation or composition. In this example it means that there is only the need for one Measurement class, each instance of which comprises of a Unit object. The concept of a 'slug' was introduced - no not one of those nasty little insects, but in this case meaning an instance of an object with a private constructor and one public static instance. In other words slugs are like a poor man's Singleton. The code looked something like this:
<table border="0" cellspacing="1" cellpadding="5" width="100%" bgcolor="#cccccc">
<tbody>
<tr>
<td bgcolor="#efefef"><span style="font-size: x-small; color: #0000ff;">class<span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #008080;">Unit
</span><span style="font-size: x-small;">{
</span><span style="font-size: x-small; color: #0000ff;"> public</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #0000ff;">static</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #0000ff;">readonly</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #008080;">Unit</span><span style="font-size: x-small;"> INCH = </span><span style="font-size: x-small; color: #0000ff;">new</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #008080;">Unit</span><span style="font-size: x-small;">(1);
</span><span style="font-size: x-small; color: #0000ff;"> public</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #0000ff;">static</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #0000ff;">readonly</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #008080;">Unit</span><span style="font-size: x-small;"> FOOT = </span><span style="font-size: x-small; color: #0000ff;">new</span><span style="font-size: x-small;"> </span><span style="font-size: x-small; color: #008080;">Unit</span><span style="font-size: x-small;">(12);
} </span></span></td>
</tr>
</tbody></table>
This made it far easier to add future measurement types, and meant that only two classes were needed instead of a potentially infinite amount.

I read an interesting article on this topic by Robert Martin, titled <a href="http://www.objectmentor.com/resources/articles/inheritanceVsDelegation" target="_blank">'Template Method & Strategy: Inheritance vs Delegation'</a> which explains the reasoning much better than I have here along with a code example.
