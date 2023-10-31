
a = [1,2,3]
b = a 			# b is an alias for a
b += [4,5]		# b extends with 2 items but this also extends to the original list
b = b + [6] 	# b extends another item but this in turn extends b to new list as well making the extend not part of the original list
print(a)
print(b)