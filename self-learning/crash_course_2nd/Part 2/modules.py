import pizza

pizza.make_pizza(15, 'Pepporoni')

from pizza import print_order_info, make_pizza

pizza.print_order_info('John', "Pizza")


# aliasing also works with imported functions
from pizza import make_pizza as mp 

mp(17, 'Cheese')

# Aliasing also works for the module name
import pizza as p 
p.make_pizza(13, 'Ham')

# Asterisk imports all the functions from the module
from pizza import *
