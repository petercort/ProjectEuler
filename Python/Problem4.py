#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import functools
import time

def palindromeCheck(num):
	#reversenum 
	arrayNum = list(map(int,str(num)))
	x = len(arrayNum) - 1
	newStr=[]
	while x >= 0 : 
		#print(arrayNum[x])
		newStr.append(arrayNum[x]) 
		x-=1 

	if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,arrayNum,newStr), True): 
	  return True 
	else: 
	  return False 

tic = time.perf_counter()

z = 999
highestFound = 0
while (z > 0) : 
	print(f"Z value is {z}")
	for x in range(z,z-100,-1) :
		for y in range(z,z-100, -1) : 
			num = x*y
			response = palindromeCheck(num)
			if response == True : 
				print(f"Found a palindrome {num} with factors {x} and {y}")
				if num > highestFound :
					highestFound = num 

	z-=100
	if highestFound != 0 :
		toc = time.perf_counter()
		print(f"Biggest palindrome is {highestFound}, found in {toc - tic:0.4f} seconds")
		exit() 