# Tuples cannot change
# This makes them immutable
# immutable list is called a tuple
dimensions = (200,5)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

# Tuples are defined by the presence of a comma; the parentheses make them look neater
# and more readable.
my_tuple = (3,)
print(my_tuple)
# You cannot alter the values found within a tuple, however you can write over the tuple.
my_tuple = (4,)
print(my_tuple)

