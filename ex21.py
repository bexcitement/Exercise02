#Exercise 02, Exercise 21

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING: %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING: %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING: %d / %d" % (a, b)
	return a / b

print "Let's do some math with functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
IQ = divide(100, 2)

print "Age: %d, Height: %d, Weight:  %d, IQ: %d" % (age, height, weight, IQ)

print "Here is a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(IQ, 2))))

print "That becomes:", what, "Can't you do it by hand?"