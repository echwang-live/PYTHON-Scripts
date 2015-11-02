def multiply(list, factor):
	#iterate each item in the list and multiply by factor
	b = [];
	for value in list:
		b.append(value * factor)
	#return a new list
	return b

a = [2, 4, 10, 16]
b = multiply(a, 2)
c = multiply(a, 5)
print "(a,2) = " + str(b)
print "(a,5) = " + str(c)