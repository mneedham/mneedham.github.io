+++
draft = false
date="2010-06-17 07:00:09"
title="Using real life metaphors"
tag=['metaphors']
category=['Software Development']
+++

My colleague <a href="http://twitter.com/dermotkilroy">Dermot Kilroy</a> attended the <a href="http://skillsmatter.com/event/design-architecture/ddd-exchange-2010">DDD 2010 Excange</a> in London last week and one of the ideas that he's been sharing with us from that is that of thinking how the user would solve a given problem without a technological solution i.e. how was something done before computers existed.

This encourages us to take a bigger picture view and can actually lead to a much simpler solution than we'd otherwise come up with.

An example that came up recently on the project I'm working on was related to how we should handle the situation where two agents tried to access the same users record at the same time. The agents are most likely in the same building.

The original technically focused solution was that we needed to lock the record so that if one agent had already opened the record then if another tried to access it they would be unable to.

Of course it's technically possible to do this but it's a bit tricky.

If there were no computers then there would probably be a physical folder which would contain all the information about the user.

It's not actually possible for two agents to both access that at the same time - if one wants to access it and it's already in use then they need not speak to their colleague and work out when they'll be finished with it.

If we consider it from this point of view then it becomes clear that putting in the effort to lock the record is unnecessary and that it would make more sense to just pop up a message on the screen informing the agent of the situation and allowing them to decide what to do.

This is the solution that we went with. It took way less time to implement and it's worked out fine so far.

--

I've retrospectively looked at this situation with my colleagues and realised that it seems to fit this pattern quite well but the way that it was reached originally was by <a href="http://www.markhneedham.com/blog/2010/03/26/finding-the-assumptions-in-stories/">looking at the requirement and finding the (initially hidden) reason for it</a>.

It would be interesting to see whether we can rely on this degree of user integrity on a public facing application, I suspect that we can to a much greater degree than we might think. 
 <br />
