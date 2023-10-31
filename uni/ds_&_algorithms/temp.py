marks = [100, 8, 50 ,10, 4]

x = len(marks)

for i in range(len(marks)):
	print(i,'i')
	for j in range(0,len(marks)-1):
		print(j,'j')
		
		if marks[j] > marks[j+1]:
			marks[j], marks[j+1] = marks[j+1], marks[j]
			print("bigger")
		
		
			

print(marks)