+++
draft = false
date="2009-08-24 22:11:26"
title="Rock Scissors Paper: TDD as if you meant it"
tag=['tdd']
category=['Testing']
+++

I decided to spend a bit of time on Saturday having another go at writing Rock Scissors Paper while following <a href="http://www.parlezuml.com/softwarecraftsmanship/sessions/tdd_as_if_you_meant_it.htm">Keith Braithwaite's TDD as if you meant it exercise</a>. 

We <a href="http://www.markhneedham.com/blog/2009/05/15/coding-dojo-14-rock-scissors-paper-tdd-as-if-you-meant-it/">previously did this exercise at a coding dojo</a> but I wanted to see what happens when you code for a longer period of time with this exercise since we typically only code for maybe a couple of hours at a dojo.

I decided to also checkin the code I was writing into Git after every single change I made - an idea I originally learnt from <a href="http://dannorth.net/">Dan North</a>, and the <a href="http://github.com/mneedham/rock-scissors-paper/tree/e3901aa9b93e09699e490b3c637bc56a203bce57/RockScissorsPaper">code is all on github</a>.

<h4>What did I learn?</h4>
<ul>
<li>I was coding for maybe 4 or 5 hours and <strong>checked in about 120 times</strong> which is far more frequently than I would do normally although perhaps it shouldn't be. <br />

I thought it would be quite distracting to have to check in that often but the checkin messages ended up becoming a stream of consciousness of what I was thinking which proved quite useful on a few occasions when I got side tracked a bit and retraced my steps in the history to find out what I was supposed to be doing - Git was pretty much acting as my sounding board since I didn't have a pair to work with on this exercise.

I'd definitely try this out again and as I've mentioned a few times I want to try it out in a coding dojo some time.</li>
<li>While trying to remove <a href="http://github.com/mneedham/rock-scissors-paper/blob/163193b8d5b483d6f001fc344cdf73e56324195d/RockScissorsPaper/Scissors.cs">some</a> <a href="http://github.com/mneedham/rock-scissors-paper/blob/860f1ebf76eaf640cd2a580a26c9bf34c5a64c2f/RockScissorsPaper/Rock.cs">duplication</a> that had worked its way into the code I realised that the template method would be the easiest way to remove that duplication and <a href="http://www.markhneedham.com/blog/2009/04/25/oo-with-a-bit-of-functional-mixed-in/">as I mentioned in an earlier post</a>, having functions/actions in C# makes the implementation of this pattern <a href="http://github.com/mneedham/rock-scissors-paper/blob/e3901aa9b93e09699e490b3c637bc56a203bce57/RockScissorsPaper/ThrowBase.cs">a bit simpler</a>:


~~~csharp

    public abstract class ThrowBase : IThrow
    {
        private readonly Func<IThrow, bool> beatenBy;
 
        protected ThrowBase(Func<IThrow, bool> beatenBy)
        {
            this.beatenBy = beatenBy;
        }
 
	 ....		

        public bool Beats(IThrow aThrow)
        {
            return IsDifferentThrowTo(aThrow) && !beatenBy(aThrow);
        }

    }
}
~~~


~~~csharp

    public class Scissors : ThrowBase
    {
        public Scissors() : base(weapon => weapon.BeatsScissors()) { }
 
	...
    }
~~~

If we didn't have functions then we'd need a method on 'ThrowBase' which we would need to implement in each of its sub classes.

As it is we can just pass a function into the constructor which does the same job.</li>
<li>Another thing I found quite interesting about this exercise was that  I was seeing more easily where methods didn't seem to belong on an existing object and I ended up creating a new object which described the interaction - chatting about the code with <a href="http://lizdouglass.wordpress.com/">Liz</a> she pointed out that I was probably creating <strong>domain events</strong> which we had <a href="http://www.markhneedham.com/blog/2009/08/24/book-club-what-ive-learned-about-ddd-since-the-book-eric-evans/">discussed a few days earlier in book club</a>. 

Once I started thinking about this interactions as 'domain events' the naming of them seemed to be much more obvious - for example after this conversation with Liz I realised that the interaction between two 'Throws' would be a 'ThrowDown' and that there would probably be a 'ThrowDownAdjudicator' to decide the outcome of a 'ThrowDown'. </li>
<li>I found it quite difficult to follow the rules of the exercise when I realised that I wanted to return a 'ThrowDownResult' which would indicate whether there was a winner for a 'ThrowDown' and if so who it was. I couldn't see a way to write all of this code in the test since I had already created the class previously so I ended up writing this code straight onto the class.

I think I probably <strong>extracted to a class too early</strong> on some occasions instead of waiting for a more complete version of a method to be written before moving it. 

Next time I think I'd wait until I'd completed all the examples /tests I want to write around a particular method before moving it onto a class.</li>
</ul>
