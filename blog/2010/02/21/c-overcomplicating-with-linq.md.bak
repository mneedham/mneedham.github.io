+++
draft = false
date="2010-02-21 12:01:22"
title="C#: Overcomplicating with LINQ"
tag=['c', 'net']
category=['.NET']
+++

I recently came across an interesting bit of code which was going through a collection of strings and then only taking the first 'x' number of characters and discarding the rest.

The code looked roughly like this:


~~~csharp

var words = new[] {"hello", "to", "the", "world"};
var newWords = new List<string>();
foreach (string word in words)  
{
    if (word.Length > 3)
    {
        newWords.Add(word.Substring(0, 3));
        continue;
    }
    newWords.Add(word);
}
~~~

For this initial collection of words we would expect 'newWords' to contain ["hel", "to", "the", "wor"]

In a way it's quite annoying that the API for 'Substring' throws an exception if you try and get just the first 3 characters of a string which contains less than 3 characters. If it didn't do that then we would have an easy 'Select' call on the collection.

Instead we have an annoying if statement which stops us from treating the collection as a whole - we do two different things depending on whether or not the string contains more than 3 characters.

In the spirit of the <a href="http://www.markhneedham.com/blog/2010/01/20/functional-collectional-parameters-some-thoughts/#comment-30627">transformational mindset</a> I tried to write some code using functional collection parameters which didn't make use of an if statement.

Following this idea we pretty much have to split the collection into two resulting in this initial attempt:


~~~csharp

var newWords = words
    .Where(w => w.Length > 3)
    .Select(w => w.Substring(0, 3))
    .Union(words.Where(w => w.Length <= 3).Select(w => w));
~~~

This resulted in a collection containing ["hel", "wor", "to", "the"] which is now in a different order to the original!

To keep the original order I figured that we needed to keep track of the original index position of the words, resulting in this massively overcomplicated version:


~~~csharp

var wordsWithIndex = words.Select((w, index) => new { w, index });

var newWords = wordsWithIndex
               .Where(a => a.w.Length >= 3)
               .Select((a, index) => new {w = a.w.Substring(0, 3), a.index})
               .Union(wordsWithIndex.Where(a => a.w.Length < 3).Select(a => new { a.w, a.index }))
               .OrderBy(a => a.index);
~~~

We end up with a collection of anonymous types from which we can get the transformed words but it's a far worse solution than any of the others because it takes way longer to understand what's going on.

I couldn't see a good way to make use of functional collection parameters to solve this problem but luckily at this stage <a href="http://enginechris.wordpress.com/">Chris Owen</a> came over and pointed out that we could just do this:


~~~csharp

var newWords = words.Select(w => w.Length > 3 ? w.Substring(0, 3) : w);
~~~

I'd been trying to avoid doing what is effectively an if statement inside a 'Select' but I think in this case it makes a lot of sense and results in a simple and easy to read solution.
