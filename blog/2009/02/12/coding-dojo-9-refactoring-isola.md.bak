+++
draft = false
date="2009-02-12 21:46:23"
title="Coding Dojo #9: Refactoring Isola"
tag=['coding-dojo']
category=['Coding Dojo']
+++

Our latest coding dojo involved refactoring the code we wrote a couple of weeks ago for the board game <a href="http://en.wikipedia.org/wiki/Isola_(board_game)">Isola</a>.

We started a <a href="http://bitbucket.org/codingdojosydney/isola">repository on Bit Bucket</a> to store our code from these sessions.

<h3>The Format</h3>

We used the <a href="http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata">Randori</a> approach again with four people participating for the whole session.

<h3>What We Learnt</h3>

<ul>
<li>Last time we had spent most of our time purely making the code functional so all the objects were completely mutable. We decided to start by <strong>removing that mutability to allow us to add additional functionality</strong> more easily. We came up with a rough idea of where we were aiming for and then started refactoring towards that.</li>
<li>The <strong>tests were really useful for this as they provided feedback after every small refactoring</strong> with respect to whether or not it had broken the original functionality. In some cases we had to redesign the tests a bit to cater for the fact that we were no longer mutating the original Isola class so some our assertions were incorrect.</li>
<li>It was quite surprising to me how much time it took to refactor the code. On the first session we didn't spend any time refactoring the code so it made it difficult to change bits of the code without other bits being affected, several times leading into a bit of a <a href="http://sethgodin.typepad.com/seths_blog/2005/03/dont_shave_that.html">yak shaving</a> exercise. Luckily we backed out of these refactorings without spending too much time on them. It pretty much drilled into us how we shouldn't forget the Refactor part of <strong>'Red, Green, Refactor'</strong> or we will suffer!</li>
<li>While trying to implement what I have previously heard referred to as a <a href="http://www.markhneedham.com/blog/2006/09/02/inheritance-and-delegation/">slug</a> but which may in fact be a variance of the <a href="http://en.wikipedia.org/wiki/Flyweight_pattern">flyweight pattern</a> we realised that our IsolaPlayer object was mutable meaning that our tests were now dependent on each other! This was the code that led us into trouble:


~~~java

public class IsolaPlayer {
	public IsolaPlayer playerOne = new IsolaPlayer("-1");
	public IsolaPlayer playerTwo = new IsolaPlayer("-2");

    private final String playerRepresentation;private final String HOME_POSITION = "[]";
    private String stomach;

    public IsolaPlayer(String playerRepresentation) {
        this.playerRepresentation = playerRepresentation;
        this.stomach = HOME_POSITION;
    }

    public String toBoardRepresentation() {
        return playerRepresentation;
    }

    public String poop() {
        return stomach;
    }

    public void eat(String boardPosition) {
        stomach = boardPosition;
    }
}
~~~

As you can see the class is mutable but being referenced by a static instance. We quickly backed that change out and refactored to that pattern later on when IsolaPlayer was immutable.</li>
<li>We used a combination of the techniques from <a href="http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/ref=sr_1_1?ie=UTF8&s=books&qid=1234438503&sr=8-1">Working Effectively With Legacy Code</a> to allow us to extract an IsolaBoard from the original Isola class. IsolaBoard was kept completely inside Isola while we refactored the code so that it could exist on its own. This approach allowed us to continually validate that we hadn't broken any tests while we gradually put more and more of the board logic into the appropriate class.</li>
<li><strong>When we write mutable code the order of operations makes a big difference</strong> and the application doesn't work correctly if we change the order. We learnt this with an early refactoring to inline some variables - an innocuous enough change, but one which led to 50% of our tests breaking.</li>
<li>We had an interesting discussion around how we can have code which is <strong>mutable but in a non dangerous way</strong>. On our way to creating value objects at one stage we had the code in a state where we were returning a new Isola object evey time but we were passing the same instance of our coveredSquares queue around. The queue was mutable meaning that we had references between difference instances of Isola to the same queue. In this case we were throwing away old Isolas but this might have been a problem if we had multiple games running at the same time. The next step was to refactor Isola to be completely immutable.</li>
</ul>

<h3>For next time</h3>

<ul>
<li>Since we spent the whole of this weeks session refactoring the code the plan for next week is to add some more functionality to the application. There is still quite a bit of logic left before we have a  working game.</li>
</ul>
