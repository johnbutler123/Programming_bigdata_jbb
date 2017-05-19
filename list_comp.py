#http://www.python-course.eu/list_comprehension.php

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print "Farenheit temperature is ", Fahrenheit

n = 30
print "list of pythagorean triples"
print [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x**2 + y**2 == z**2]

print "alternative coding for pythagorean triples"
pyt_triples = []
for x in range(1, 30):
	for y in range(x,30):
		for z in range(y,30):
			if x**2 + y**2 == z**2:
				pyt_triples.append((x,y,z))

print pyt_triples					

#the above code is basically doing the following operation:
#my_list = []
#for x in Celsius:
#	my_list.append(((float(9)/5)*x + 32) )
	

print "Cartesian join of 'colours' and 'things'"
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things	