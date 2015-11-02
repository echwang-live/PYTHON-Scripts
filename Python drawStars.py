def draw_stars(list):
	for num in list:
		print "*" * num

def draw_stars2(list):
	for val in list:
		if isinstance(val, int):
			print "*" * val
		else:
			print val[0].lower() * len(val)

#main execution
print "Draw Stars Example------------------------"
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

print "Draw Stars Improved-----------------------"
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(y)