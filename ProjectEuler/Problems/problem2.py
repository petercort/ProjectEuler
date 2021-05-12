#Find the sum of even valued terms of the Fibonacci Sequence
#for values less than 4 million

#brute force technique
def problem2Name() : 
	return "Problem 2"

def problem2Description() :
	return "Find the sum of even valued terms of the Fibonacci Sequence for values less than 4 million"

def problem2Params() : 
	return ""

def problem2() :
	term1 = 0
	term2 = 1
	term3 = 0
	counter = 0

	while term3 < 4000000:
		term3 = term2 + term1
		term1 = term2
		term2 = term3
		if term3 % 2 == 0:
			counter+= term3
	return counter