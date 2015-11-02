import random
def bubbleSort(list):
	# print "length = " + str(len(list))
	for x in range(0,len(list)-1):
		for y in range(x+1, len(list)):
			if list[x] > list[y]:
				temp = list[x]
				list[x] = list[y]
				list[y] = temp

#main execution
# x = [1,90, 24, 88, 98, 2, 7]
x=[random.randint(0,10000) for p in range(0,100)]
print "Original x = " + str(x)
bubbleSort(x)
print "New x = " + str(x)