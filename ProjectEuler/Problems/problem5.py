## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problem5Name() : 
	return "Problem 5"

def problem5Description() :
	return "Calculate the smallest number evenly divisible by all numbers in a range. "

def problem5Example() : 
	return "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder."

def problem5Params() : 
	return "rangestart, rangeend"

def rangeCheck(rangeStart, rangeEnd) :
	rangeList = []
	for i in range(rangeStart, rangeEnd + 1) :
		rangeList.append(i)
		## if a number is divisible evenly into another number we can throw it out 
		x = 1
		while x <= rangeEnd :
			if x != i and x % i == 0 : ## number's divisible, throw it out 
				del rangeList[len(rangeList) - 1]
				break
			x+=1
	return rangeList

def isDivisible(rangeList) :
	## determining the number to check, we have some known 'shortcuts'
	## must be an even number 
	## test the highest number in the range first 
	## can test in intervals of the largest number in the range
	found = False
	x = rangeList[len(rangeList) - 1]
	#print(f"last val is {x}")
	while found != True :
	#while x <= 2550 :
		for i in rangeList :
			#print(f"is {x} divisible by {i}?")
			if x % i == 0 :
				if i == rangeList[len(rangeList) - 1] : ## not divisible, move on 
					found = True 
					answer = x
			else : 
				break
				## made it through the list! 
			#found = True 
		x+=rangeList[len(rangeList) - 1]

	return answer 
	
def problem5(rangeStart, rangeEnd) : 
	## define the range of numbers to check divisibility. 
	## we can establish that if a number is divisible by 8 it will also be divisible by 4, so we don't need to check 4.
	condensedRange = rangeCheck(rangeStart, rangeEnd) 
	answer = isDivisible(condensedRange)
	return answer 