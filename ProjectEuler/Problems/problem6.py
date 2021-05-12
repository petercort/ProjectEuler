#The sum of the squares of the first ten natural numbers is,

#The square of the sum of the first ten natural numbers is,

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def problem6Name() : 
	return "Problem 6"

def problem6Description() :
	return "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."

def problem6Params() : 
	return "Enter the number to calculate difference between. "

def sumOfSquares(start, stop) : 
	x = 0
	for i in range(start, stop + 1, 1) : 
		x += i ** 2 
	return(x)

def squareOfSums(start, stop) :
	x = 0
	for i in range(start, stop + 1, 1) : 
		x+=i 
	y = x ** 2 
	return(y)

def problem6(start, stop) : 
	sumSquare = sumOfSquares(start, stop)
	squareSum = squareOfSums(start, stop)

	diff = squareSum - sumSquare
	return diff