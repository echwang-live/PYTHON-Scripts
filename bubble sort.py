import random
import datetime
def bubbleSort(list):
	sort = True

	while sort:
		sort = False
		for x in range(len(list)-1):
			if list[x] > list[x+1]:
				sort = True
				list[x], list[x+1] = list[x+1], list[x]
	

#main execution
x=[random.randint(0,10000) for p in range(0,10)]
print "Original x = " + str(x)
t1 = datetime.datetime.now()
bubbleSort(x)
t2 = datetime.datetime.now()
tdelta = t2 - t1
print "New x = " + str(x)

print "Bubble sort took " + str(tdelta)