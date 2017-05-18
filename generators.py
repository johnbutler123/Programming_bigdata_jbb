def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
	
x = city_generator()	
print x.next()
print x.next()
print x.next()
print x.next()
#print x.next() 				#there isnt a 5th element so you get a stopiteration error

print "\n"

cities = city_generator()
for city in cities:
	print city

print "\n"	
	
def get_triplets(n):
	for x in range(1, n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)
					
triplets = get_triplets(100)
for triplet in triplets:
	print triplet,			# the , here instructs python to print one after the other and not on a new line each
	

print "\n"		
	
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(5) 		#prints the first 5 fibonacci numbers i.e. each number is the sum of the previous 2 numbers
for x in f:
    print x,
print	