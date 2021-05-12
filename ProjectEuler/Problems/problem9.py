## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

from math import sqrt

def problem9Name() : 
	return "Problem 9"

def problem9Description() :
	return "There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."

def problem9Params() : 
	return "Please provide the sum to calculate sum of triplets for.\n"

def getTriplets(tripletSum) : 
	## step 1, find potential values of C 
	## a + b = 1000 - c 
	## C must also be 
	answer = ''
	for c in range(tripletSum, 1, -1) : 
		## get values for a and b, square them add them and determine if sqrt(c) is integer
		## square c which is the values of a^2 + b^2. 
		## c^2 = 25.  therefore a^2 = 25 - b^2. 
		cSquare = c ** 2
		for b in range(1, tripletSum, 1) :
			bSquare = b ** 2 
			#print(f"b: {bSquare} c: {cSquare}")
			if bSquare < cSquare :
				aSquare = cSquare - bSquare 
				#print(f"Testing A Squared value of {aSquare}")
				
				a = sqrt(aSquare)
				#print(a)
				
				if a.is_integer() : 
					#print(a + b + c)
					## A is a square root, so we'll see if the whole thing comes together. 
					if (a + b + c == tripletSum) :
						## found it
						answer = [int(a), int(b), int(c)]
						break

		#if isinstance(i, int)
		
	return answer 

def problem9(tripletSum) : 
	## Valid pythagorean theorem values
	triplets = getTriplets(tripletSum)
	product = triplets[0] * triplets[1] * triplets[2]
	answer = "Triplets that form the sum of {tripletSum} are {triplets[0]}, {triplets[1]}, {triplets[2]}. Product of these 3 is {product}".format(**locals())
	return answer


## for testing
#answer = problem9(1000) 
#print(answer)