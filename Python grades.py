def grade(value):
	if value >= 60 and value <= 69:
		print "Score " + str(value) + "; Your grade is D"
	elif value >= 70 and value <= 79:
		print "Score " + str(value) + "; Your grade is C"
	elif value >= 80 and value <= 89:
		print "Score " + str(value) + "; Your grade is B"
	elif value >= 90 and value <= 100:
		print "Score " + str(value) + "; Your grade is A"
	else:
		print "Score not in range"

	#function should consider validate if the input is really integer
	
print "Scores and Grades"

for numInput in range(0, 10):
	grade(input())
