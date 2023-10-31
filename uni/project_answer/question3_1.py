class HashTable:

	def __init__(self, hash_table, size):
		self.size = size
		self.hash_table = hash_table

	def retrieve_price(self, item):
		if item in self.hash_table:
			return (f'Price of {item} : R{self.hash_table[item]}')
		else:
			return 'Item not found'

	def delete(self, item):
		del self.hash_table[item]

	def set(self, item, price):
		self.hash_table[item] = price
		


dic = 	{	'Boxy T-Shirt' 								: 	140	,
			'U Neck Tank'								: 	220	,
			'Rib-Knit Sweater'							:	230	,
			'Gwyneth Cupro-Bllend Slip Dress'			:	230	,
			'Double-Breasted Jacket'					:	500	,
			'Padded Bomber Jacket'						:	500	,
			'Mason Pant'								:	1780,
			'Full Length Pants'							:	350	,
			'Wide-Leg Pants '							:	370	,
			'Knee-High Boots'							:	700	,
			'Daybreak Sneaker'							:	1200,
			'Ruched Midi Dress'							:	1150,
			'Ballet Flats in Leather'					:	50  ,
			'Laguna Waterproof boot'					:	1700,
			'Maesa Pleated Woven Wide-Leg Cargo Pants' 	: 	2100,
			'Oversized SingleBreasted Jacket'			:	755	,
			'Louisa Lady Jacket in Maritime Tweed'		:	3500
		}


Items = HashTable(dic, len(dic))
message = Items.retrieve_price('Padded Bomber Jacket')

print(message)
Items.delete('Padded Bomber Jacket')
value = dic.get('Padded Bomber Jacket', 'No value found')
print(value)

message = Items.retrieve_price('Boxy T-Shirt')
print(message)
Items.set('Boxy T-Shirt', 1000)
message = Items.retrieve_price('Boxy T-Shirt')
print(message)








