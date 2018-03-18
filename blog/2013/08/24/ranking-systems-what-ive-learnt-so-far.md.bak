+++
draft = false
date="2013-08-24 11:05:58"
title="Ranking Systems: What I've learnt so far"
tag=['ranking-systems']
category=['Software Development', 'Ranking Systems']
+++

<p>I often go off on massive tangents reading all about a new topic but don't record what I've read so if I go back to the topic again in the future I have to start from scratch which is quite frustrating.</p>


<p>In this instance after playing around with <a href="http://www.markhneedham.com/blog/2013/08/11/neo4j-extracting-a-subgraph-as-an-adjacency-matrix-and-calculating-eigenvector-centrality-with-jblas/">calculating the</a> <a href="http://www.markhneedham.com/blog/2013/08/05/javajblas-calculating-eigenvector-centrality-of-an-adjacency-matrix/">eigenvector centrality</a> of a sub graph I learnt that this algorithm can also be used in ranking systems.</p>


<p>I started off by reading a paper written by James Keener about the <a href="https://umdrive.memphis.edu/ccrousse/public/MATH%207375/PERRON.pdf">Perron-Frobenius Theorem and the ranking of American football teams</a>.</p>


<p>The <a href="http://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem">Perron-Frobenius Theorem</a> asserts the following:</p>


<blockquote>
a real square matrix with positive entries has a unique largest real eigenvalue and that the corresponding eigenvector has strictly positive components
</blockquote>

<p>This is applicable for <strong>network based ranking systems</strong> as we can build up a matrix of teams, store a value representing their performance against each other, and then calculate an ordered ranking based on eigenvector centrality.</p>


<p>I also came across the following articles describing different network-based approaches to ranking teams/players in tennis and basketball respectively:</p>


<ul>
<li>
<a href="http://www.nature.com/srep/2012/121205/srep00904/full/srep00904.html">A network-based dynamical ranking system for competitive sports</a>
</li>
<li>
<a href="http://blog.biophysengr.net/2012/03/eigenbracket-2012-using-graph-theory-to.html">Using Graph Theory to Predict NCAA March Madness Basketball</a>
</li>
</ul>

<p>Unfortunately I haven't come across any corresponding code showing how to implement those algorithms so I need to do a bit more reading and figure out how to do it.</p>


<p>In the world of non network based ranking systems I came across 3 algorithms:</p>


<ul>
<li><a href="http://en.wikipedia.org/wiki/ELO_rating_system">Elo</a> - this is a method originally developed to calculate the relative skill of chess players. 

Players start out with an average rating which then increases/decreases based on games they take part in. If they beat someone much more highly ranked then they'd gain a lot of points whereas losing to someone similarly ranked wouldn't affect their ranking too much.

I came across a version used to rank <a href="http://www.eloratings.net/system.html">country football teams</a>. and the algorithm is quite well described in Christopher Allen's article on  <a href="http://www.lifewithalacrity.com/2006/01/ranking_systems.html">competitive ranking systems</a>.</li>
<li><a href="http://math.bu.edu/people/mg/research/gdescrip.pdf">Glicko</a> - this method was developed as the author, Mark Glickman, detected some flaws in the Elo rating system around the reliability of players' ratings. 

This algorithm therefore introduces the concept of a ratings deviation (RD) to measure uncertainty in a rating. If a player player plays regularly they'd have a low RD and if they don't it'd be higher. This is then taken into account when assigning points based on games between different players.

Rob Kohr has an implementation of this one using <a href="https://github.com/RobKohr/glicko">Javascript on his github</a>.</li>
<li><a href="http://research.microsoft.com/en-us/projects/trueskill/">TrueSkill</a> - this one was developed by Microsoft Research to rank players using XBox Live. This seems similar to Glicko in that it has a rating and uncertainty for each player. <a href="http://research.microsoft.com/en-us/projects/trueskill/faq.aspx">TrueSkill's FAQs</a> suggest the following difference between the two:

<blockquote>
Glicko was developed as an extension of ELO and was thus naturally limited to two player matches which end in either win or loss. Glicko cannot update skill levels of players if they compete in multi-player events or even in teams. The logistic model would make it computationally expensive to deal with team and multi-player games. Moreover, chess is usually played in pre-set tournaments and thus matching the right opponents was not considered a relevant problem in Glicko. In contrast, the TrueSkill ranking system offers a way to measure the quality of a match between any set of players.
</blockquote>
</li>
</ul>

<p>Scott Hamilton has <a href="https://github.com/McLeopold/PythonSkills">an implementation of all these algorithms in Python</a> which I need to play around with. He based his algorithms on a blog post written by <a href="http://www.moserware.com/2010/03/computing-your-skill.html">Jeff Moser</a> in which he explains probabilities, the Gaussian distribution, Bayesian probability and factor graphs in deciphering the TrueSkill algorithm. Moser's created <a href="https://github.com/moserware/Skills">a project implementing TrueSkill in C#</a> on github.</p>


<p>I follow tennis and football reasonably closely so I thought I'd do a bit of reading about the main two rankings I know about there as well:

<ul>
<li><a href="http://www.uefa.com/memberassociations/uefarankings/club/index.html">UEFA club coefficients</a> - used to rank football clubs that have taken part in a European competition over the last 5 seasons. It takes into account the importance of the match but not the strength of the opposition</li>
<li><a href="http://www.atpworldtour.com/rankings/rankings-faq.aspx">ATP Tennis Rankings</a> - used to rank tennis players on a rolling basis over the last 12 months. They take into account the importance of a tournament and the round a player reached to assign ranking points.</li>
</ul>

<p>Now that I've recorded all that it's time to go and play with some of them!</p>

