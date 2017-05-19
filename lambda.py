add = lambda x,y: x+y

print "answer to lambda add = ", add(1,1)

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39,10)

F = map(fahrenheit, temp)
print "Temperature Farenheit is ",  F
C = map(celsius, F)
print "Temperature Celcius is ", C

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
print "'a' list  + 'b' list = ", map(lambda x,y:x+y, a,b)
print "'a' list + 'b' list + 'c' list = ", map(lambda x,y,z:x+y+z, a,b,c)
print "a' list + 'b' list - 'c' list = ", map(lambda x,y,z:x+y-z, a,b,c)

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print "list as filtered to show odd numbers only", result




result = filter(lambda x: x % 2 == 0, fib)
print "list as filtered to show even numbers only", result

print "sum items in list ", reduce(lambda x, y: x+y, [47, 11, 42, 13])

max = lambda a,b: a if (a>b) else b
print " max of numbers in list = ", reduce(max, [47, 11, 42, 13]) 

def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
print "Maximum of numbers in list = ", max([47, 11, 42, 13])	

def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)
	
print "Minimum of numbers in list = ", min([47, 11, 42, 13])	

def add(values):
	return reduce(lambda a,b: a+b, values)
	
print "sum of numbers in list = ", add([47, 11, 42, 13])	

def sub(values):
	return reduce(lambda a,b: a-b, values)
	
print "cumulative total of subtract consequetive numbers in list ", sub([47, 11, 42, 13])	

def mul(values):
	return reduce(lambda a,b: a*b, values)
	
print "Product of items in list = ", mul([3, 5, 2, 4])	

def div(values):
	return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)
	
print "Result of dividing by consequetive numbers in list ",  div([100, 2, 2, 5])

def is_even(values):
	return filter(lambda x: x % 2 == 0, values)
	
print "Show even numbers in list ", is_even([47, 12, 42, 13])	

def to_fahrenheit(values):
	return map(fahrenheit, values)
	
print "Conversion to Farenheit for items in list is ", to_fahrenheit([0, 37, 40, 100])	
	
def to_celsius(values):
	return map(celsius, values)	
	
print "Conversion to Celcius for items in list is ", to_celsius([0, 32, 100, 212])

def sum(to):
	return reduce(lambda x, y: x+y, range(1, to+1))
	
print "Cumulative total of numbers in range = ", sum(100)


