#find the sum of all the multiples of 3 or 5 below 1000

def problem1Name() : 
	return "Multiples of 3 and 5"

def problem1Description() :
	return "Find the sum of all the multiples of 3 or 5 below 1000"

def problem1Params() : 
	return ""

def problem1() : 
	counter = 0

	for x in range(0, 1000):
		if x % 3 == 0:
			counter+= x
		elif x % 5 == 0:
			counter+= x

	return counter
