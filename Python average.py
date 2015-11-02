a = [1, 2, 5, 10, 255, 3]
temp = 0
for val in a :
	temp += val
	temp = temp / len(a)
print temp