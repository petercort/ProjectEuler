##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

##What is the 10 001st prime number?

from ProjectEuler.Problems.problem3 import isPrime 
def problem7Name() : 
	return "Problem 7"

def problem7Description() :
	return "What is the 10,001st prime number?"

def problem7Params() : 
	return "Enter the prime to find"

def problem7(num) : 
	count = 0
	x=0
	while count != num : 
		x += 1
		primeResult = isPrime(x)
		if primeResult == True : 
			count += 1
			#print(f"Found {count} prime: {x}")
	return x 


## for testing
#answer = problem7(10001) 
#print(answer)