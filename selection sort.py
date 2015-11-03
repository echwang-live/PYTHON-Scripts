import random
import datetime

def selectionSort(list):
	# min = 0;
	for x in range(len(list)-1):
		print "DEBUGGING: x = " + str(x)
		for y in range(x+1, len(list)):
			print "DEBUGGING: y = " + str(y)		
			if list[y] < list[x]:
				list[x],list[y] = list[y],list[x]

#main execution
x=[random.randint(0,100) for p in range(5)]
print "Original x = " + str(x)
t1 = datetime.datetime.now()
selectionSort(x)
t2 = datetime.datetime.now()
tdelta = t2 - t1
print "New x = " + str(x)
print "Selection sort took " + str(tdelta)