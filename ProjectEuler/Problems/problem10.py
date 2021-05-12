#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from ProjectEuler.Problems.problem3 import isPrime 

def problem10Name() : 
	return "Problem 10"

def problem10Description() :
	return "Find the sum of all the primes below a given number"

def problem10Params() : 
	return "Provide the value to find the sum of primes below."

def problem10(primeLimit) : 
	primeSum = 0
	for i in range (2, primeLimit) :
		if (isPrime(i) == True) : 
			primeSum += i

	return primeSum


## for testing
#answer = problem10(10) 
#print(answer)