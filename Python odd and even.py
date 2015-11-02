def isOdd(value):
		if value % 2 != 0:
			print "Number is " + str(value) + ". This is an odd number"
		else:
			print "Number is " + str(value) + ". This is an even number"

for i in range(1,2001):
	isOdd(i)