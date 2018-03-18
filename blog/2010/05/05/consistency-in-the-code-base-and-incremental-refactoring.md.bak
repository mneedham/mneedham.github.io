+++
draft = false
date="2010-05-05 22:34:56"
title="Consistency in the code base and incremental refactoring"
tag=['coding']
category=['Coding', 'Incremental Refactoring']
+++

I wrote a post a while ago about <a href="http://www.markhneedham.com/blog/2009/11/04/consistency-in-the-code-base/">keeping consistency in the code base</a> where I covered some of the reasons that you might want to rewrite parts of a code base and the potential impact of those changes but an interesting side to this discussion which I didn't cover that much but which seems to play a big role is the role of <strong>incremental refactoring</strong>. 

In our code base we recently realised that the naming of the fields in some parts of a form don't really make sense and I wanted to start naming new fields with the new naming style and then go back and change the existing ones incrementally when it was a good time to do so.

<a href="http://uk.linkedin.com/pub/richard-filippi/1/39/b7">Richard</a> and <a href="https://twitter.com/christianralph">Christian</a> suggested that this wouldn't be such a good approach because it would make the naming issue even more confusing until all the fields had been renamed.

In order to avoid this problem we had to either go and change every single field to follow the new naming approach immediately or settle on the old names even though they might not be as descriptive.

Since doing the former would involve changing the names of around 15-20 fields across several different objects, in Hibernate mapping code, probably in the database, on HTML forms and in Watin tests we decided not to do that - the project is only for a short amount of time so the investment probably wouldn't be worthwhile.

Although in this case it makes sense not to make the improvement it doesn't strike me as being entirely satisfactory that we would need to make this type of change in a big bang fashion.

From my experience there are often insights into the code or improvements in the ubiquitous language as time goes on and while consistency is of course an important thing in any code base it's not the only thing.

When do we decide that actually gradually moving to a better approach is worth the temporary pain that having this inconsistency will cause?
