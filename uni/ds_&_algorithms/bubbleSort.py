marks = [100, 8, 50 ,10, 4]


for i in range(len(marks)):
	for j in range(0,len(marks)-i-1):
		if marks[j] > marks[j+1]:
			marks[j], marks[j+1] = marks[j+1], marks[j]
			
		
		
	

print(marks)