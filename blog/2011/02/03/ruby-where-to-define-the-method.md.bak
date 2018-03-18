+++
draft = false
date="2011-02-03 19:37:17"
title="Ruby: Where to define the method?"
tag=['ruby']
category=['Ruby']
+++

In our application we deal with items which can be put into a shopping cart.

An item is defined like so:


~~~ruby

class Item < ActiveRecord::Base

end
~~~

One problem that we had to solve recently was working out how to display a message to the user if the item they wanted to buy was out of stock.

We can find out if items are out of stock by making a call to an external service:


~~~ruby

def out_of_stock_items
  items_from_external_service_call.map do |i|
    item = look_up_item_by(i[:id])
    item.number_available = i[:number_available]
    ...
  end
end
~~~

Line 5 is the interesting one because we needed to work out where to define the 'number_available' method.

The easiest way to do it is this:


~~~ruby

class Item < ActiveRecord::Base
  attr_accessor :number_available
end
~~~

But it seems a bit misleading because the concept of availability doesn't exist in every context that we use the 'Item' object.

Another approach could be to add an instance method to each of the cart items in that context which is a bit more complicated:


~~~ruby

def out_of_stock_items
  items_from_external_service_call.map do |i|
    item = look_up_item_by(i[:id])

    def item.number_available=(value)
      @number_available = value
    end

    def item.number_available
      @number_available
    end

    item.number_available = i[:number_available]
    ...
  end
end
~~~

Right now we've gone for the easier option and put the method onto the 'Item' class but I'd be curious how others would solve this problem...
