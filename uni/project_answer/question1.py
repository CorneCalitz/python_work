# Corne Calitz 24/10/2022
# String permuation function which does not repeat used characters

"""
Question 1
Using the non-repetitive characters that form your name, write a python function that uses
recursion. The function should be called string_permuation, it should generate strings formed
using the characters of your name. The generated string must use each character only once.
For example the name Eunice, the characters to use will be E,u,n,i and c. 
"""

def string_permuation(string):
	if len(string) == 1:
		return string

	permuated_strings = string_permuation(string[1:])
	char = string[0]
	list_results = []

	for permuated_string in permuated_strings:
		for i in range(len(permuated_string) + 1):
			list_results.append(permuated_string[:i] + char + permuated_string[i:])

	return list_results

	

name = list(input('Please input your name.\n>>>'))
unique_name = ''
for letter in name:
	if letter.upper() not in unique_name:
		unique_name += letter

print(string_permuation(unique_name))







