# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("CANNOT DIVIDE BY ZERO")
	else:
		print (c)

# Driver program to test above function
AbyB(0, 0)
AbyB(3.0, 4.0)
