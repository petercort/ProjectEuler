#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

## Prime calculation function 

from math import sqrt

def problem3Name() : 
	return "Problem 3"

def problem3Description() :
	return "The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?"

def problem3Params() : 
	return ""

def isPrime(num):
  if num > 1: 
  	for i in range(2, int(sqrt(num))+1) :
  		if (num % i) == 0:
	  		## factor is not a prime, toss it out 
	  	  return False
  		  break
  	else : 
  		## is prime 
  		return True 
  else : 
  	return False

def problem3() :
	topVal = 600851475143
	#topVal = 13195
	#topVal = 60

	## Start low and grab the larger factor and see if it's a prime 
	for x in range(1, topVal // 2) :
		if topVal % x == 0:
			#print("testing value ")
			response = isPrime (topVal // x)
			if response == True :
				largestPrime = topVal // x
				#print(f"Found largest prime {largestPrime} in {toc - tic:0.4f} seconds")
				return largestPrime

