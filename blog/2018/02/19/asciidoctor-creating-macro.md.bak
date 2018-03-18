+++
draft = false
date="2018-02-19 20:51:31"
title="Asciidoctor: Creating a macro"
tag=['asciidoc', 'asciidoctor']
category=['Software Development']
+++

<p>
I've been writing the <a href="https://neo4j.com/tag/twin4j/">TWIN4j blog</a> for almost a year now and during that time I've written a few different <a href="http://asciidoc.org/chunked/ch21.html">asciidoc macros</a> to avoid repetition.
</p>


<p>
The most recent one I wrote does the formatting around the Featured Community Member of the Week. I call it like this from the asciidoc, passing in the name of the person and a link to an image:
</p>



~~~text

featured::https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/20180202004247/this-week-in-neo4j-3-february-2018.jpg[name="Suellen Stringer-Hye"]
~~~

<p>
The code for the macro has two parts. The first is some wiring code that registers the macro with Asciidoctor:
</p>


<p>
<cite>lib/featured-macro.rb</cite>
</p>



~~~ruby

RUBY_ENGINE == 'opal' ? (require 'featured-macro/extension') : (require_relative 'featured-macro/extension')

Asciidoctor::Extensions.register do
  if (@document.basebackend? 'html') && (@document.safe < SafeMode::SECURE)
    block_macro FeaturedBlockMacro
  end
end
~~~

<p>
And this is the code for the macro itself:
</p>


<p>
<cite>lib/featured-macro/extension.rb</cite>
</p>



~~~ruby

require 'asciidoctor/extensions' unless RUBY_ENGINE == 'opal'

include ::Asciidoctor

class FeaturedBlockMacro < Extensions::BlockMacroProcessor
  use_dsl

  named :featured

  def process parent, target, attrs
    name = attrs["name"]

    html = %(<div class="imageblock image-heading">
                <div class="content">
                    <img src="#{target}" alt="#{name} - This Week’s Featured Community Member" width="800" height="400">
                </div>
            </div>
            <p style="font-size: .8em; line-height: 1.5em;" align="center">
              <strong>#{name} - This Week's Featured Community Member</strong>
            </p>
)

    create_pass_block parent, html, attrs, subs: nil
  end
end
~~~

<p>
When we convert the asciidoc into HTML we need to tell asciidoctor about the macro, which we can do like this:
</p>




~~~bash

asciidoctor template.adoc \
  -r ./lib/featured-macro.rb \
  -o -
~~~

<p>
And that's it!
</p>

