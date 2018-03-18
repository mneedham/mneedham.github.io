+++
draft = false
date="2010-09-26 19:03:24"
title="RSpec: Fooled by stub!...with"
tag=['ruby', 'rspec']
category=['Ruby']
+++

We had an RSpec spec setup roughly like this the other day...


~~~ruby

describe "my stub test" do
  it "should be amazin" do
    Mark.stub!(:random).with("some_wrong_argument").and_return("something")

    Another.new.a_method
  end
end
~~~

...where 'Mark' and 'Another' were defined like so:


~~~ruby

class Mark
  def self.random(params)
    "do some amazing stuff"
  end
end
~~~


~~~ruby

class Another
  def a_method
    random = Mark.random("foo")
    # use random for something
  end
end
~~~

When we ran the spec we would get the following error message which was initially a little baffling:


~~~text

NoMethodError in 'my stub test should be amazin'
undefined method `random' for Mark:Class
./rspec_spec.rb:9:in `a_method'
./rspec_spec.rb:17:
~~~

We spent quite a while looking at how we'd set up the spec to make sure we were actually calling 'stub!' on the right class before eventually realising that we had unintentionally added 'with("some_wrong_argument")' to that stub.

A little investigation of the RSpec code shows that this is the expected behaviour for this scenario:


~~~ruby

module Spec
  module Mocks
    class Proxy
      ...
      def message_received(sym, *args, &block)
        expectation = find_matching_expectation(sym, *args)
        stub = find_matching_method_stub(sym, *args)

        if ok_to_invoke_stub?(stub, expectation)
          record_stub(stub, sym, args, &block)
        elsif expectation
          invoke_expectation(expectation, *args, &block)
        elsif expectation = find_almost_matching_expectation(sym, *args)
          record_almost_matching_expectation(expectation, sym, *args, &block)
        else
          @target.__send__ :method_missing, sym, *args, &block
        end
      end
    end
  end
end
~~~

In this case 'find_matching_method_stub' returns a nil value and since we didn't set up any expectation on 'Mark'  we fall through to the 'method_missing' exception.
