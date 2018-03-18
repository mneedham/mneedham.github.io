+++
draft = false
date="2009-05-28 05:44:52"
title="The 5 dysfunctions of teams in code"
tag=['coding', 'five-dysfunctions']
category=['Coding']
+++

I recently came across an <a href="http://www.thekua.com/atwork/2009/05/evidence-in-favour-of-conways-law/">interesting post by my colleague Pat Kua</a> where he talks about how some patterns he's noticed in code can be linked to <a href="http://en.wikipedia.org/wiki/Conway%27s_Law">Conway's law</a> which suggests that the structure of systems designed in organisations will mirror the communication structure of that organisation.

I recently read a book called '<a href="http://www.markhneedham.com/blog/2009/04/22/the-five-dysfunctions-of-a-team-book-review/">The Five Dysfunctions of Teams</a>' which describe some behaviours in teams which aren't working in an effective way.

Playing the devil's advocate I became intrigued as to if there is some sort of link between these dysfunctions and whether they manifest themselves in our code as anti patterns.

The five dysfunctions are:

<ol>
<li>Absence of Trust - team members are unwilling to be vulnerable within the group</li>
<li>Fear of Conflict - team cannot engage in unfiltered and passionate debate of ideas</li>
<li>Lack of Commitment - team members rarely have buy in or commit to decisions</li>
<li>Avoidance of Accountability - team members don't call their peers on actions/behaviours which hurt the team</li>
<li>Inattention to Results - team members put their individual needs before those of the team</li></ol>

<h3>Absence of Trust</h3>

I think having <strong>null checks all over the code</strong> is the most obvious indicator that people don't trust the code that they are working with.

If the person writing the code had faith in their colleagues who had written the code they now need to interact with then I think it would be more likely that they would trust the code to do the right thing and they wouldn't feel driven to such a <a href="http://www.thekua.com/atwork/2008/08/defensive-programming-depends-on-context/">defensive approach</a>. 

<h3>Fear of Conflict</h3>

Fear of conflict in a team seems to manifest itself most obviously in code when we have <strong>a lot of duplication happening</strong> - there are several reasons why duplication can happen but I think one of them is when people aren't engaging in discussions when they disagree with something that a colleague has written and therefore end up writing their own version of something that's already been done.

This probably manifests itself even more obviously when you end up with multiple different frameworks all in the same code base and all doing the same thing just because people don't want to engage in a conversation to choose which one the team is going to use.

<h3>Lack of Commitment</h3>
This is one which seems to overlap a lot with the previous two although perhaps one specific way that this would manifest itself in the code might be if we see <strong>sloppy mistakes or lack of care being shown with the code</strong> - an example of this could be changing the name of a class but then not ensuring that all the places where the old name was used in variables have been changed accordingly.

This leaves the code in a half baked state which becomes quite difficult for other people to work with and they have to do some clean up work before being able to effectively make changes to the code.

<h3>Avoidance of Accountability</h3>

The coding anti pattern that stands out for me here is <strong>when we allow people to write code without tests</strong> and then check those into source control.

From my experience so far this never seems to work out well and I think it shows a lack of respect for the rest of the team since we don't have an easy way of verifying whether this code actually works and other people can't make use of it elsewhere in the code base with any degree of confidence.

<h3>Inattention to Results</h3>

Team members putting their individual needs before the team manifests itself in code when we end up with <strong>code that has been written in such a  way that only the person who wrote it is really able to understand it</strong>.

I think this manifests itself in '<strong>clever code</strong>' which is fine in your own projects but in a team context is very detrimental as you become a bit of a bottleneck when people want to make changes in this area of the code and can't do it because they can't understand what's going on.

Something else that falls under this dysfunctions is <strong>when there is a convention for how to do certain things in the code but we decide to go off and do it our own way</strong>. Now granted sometimes it's fine to do this if you're working the code towards a better state and the rest of the team are aware you're trying to work towards this goal but otherwise it's not a very effective approach.

<h3>In Summary</h3>
I found it quite intriguing that in my mind at least some of the problems we see in code do seem to have some correlation to the problems that we see in teams.

One thing I remember from reading Gerald Weinberg's '<a href="http://www.amazon.com/Secrets-Consulting-Giving-Getting-Successfully/dp/0932633013/ref=sr_1_1?ie=UTF8&s=books&qid=1243452602&sr=1-1">The Secrets of Consulting</a>' is his claim that '<a href="http://www.codinghorror.com/blog/archives/001033.html">no matter what the problem is it's always a people problem</a>' - if indeed this is true then in theory problems that we see in code should be indicative of a people problem which I think probably to an extent is true. 

I think certainly not all problems in code are linked to the dysfunctions of teams - certainly some anti patterns creep into our code due to a lack of experience of team members of how they to do things better but then again maybe that's indicative of the team not having senior members working closely enough with their colleagues!

Maybe we can therefore work out how we can therefore identify ways that we can improve our team by starting with a look at the code.

