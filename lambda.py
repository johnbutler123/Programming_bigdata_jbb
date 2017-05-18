add = lambda x,y: x+y

print add(1,1)

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F
C = map(celsius, F)
print C

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
print map(lambda x,y:x+y, a,b)
print map(lambda x,y,z:x+y+z, a,b,c)
print map(lambda x,y,z:x+y-z, a,b,c)

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

print reduce(lambda x, y: x+y, [47, 11, 42, 13])

max = lambda a,b: a if (a>b) else b
print reduce(max, [47, 11, 42, 13]) 

def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
print max([47, 11, 42, 13])	

def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)
	
print min([47, 11, 42, 13])	

def add(values):
	return reduce(lambda a,b: a+b, values)
	
print add([47, 11, 42, 13])	

def sub(values):
	return reduce(lambda a,b: a-b, values)
	
print sub([47, 11, 42, 13])	

def mul(values):
	return reduce(lambda a,b: a*b, values)
	
print mul([47, 11, 42, 13])	

def div(values):
	return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)
	
print div([47, 'Nan', 0, 11])

def is_even(values):
	return filter(lambda x: x % 2 == 0, values)
	
print is_even([47, 11, 42, 13])	

def to_fahrenheit(values):
	return map(fahrenheit, values)
	
print to_fahrenheit([0, 37, 40, 100])	
	
def to_celsius(values):
	return map(celsius, values)	
	
print to_celsius([0, 32, 100, 212])

def sum(to):
	return reduce(lambda x, y: x+y, range(1, to+1))
	
print sum(100)