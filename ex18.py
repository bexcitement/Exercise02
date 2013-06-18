#Exercise 01, Exercise 18


# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#okay, that's *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes on argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no args
def print_none():
	print "I've got nothing."


print_two("zed", "shaw") 
print_two_again("meagan", "becca")
print_one("first!")
print_none()

