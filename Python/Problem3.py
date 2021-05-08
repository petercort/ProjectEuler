#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

## Prime calculation function 
import time

def isPrime(num):
  if num % 2 == 0: 
  	return False 
  else : 
	  x = 3
	  while(x < num-1): 
	  	if num % x == 0:
	  		## factor is not a prime, toss it out 
	  	  return False
	  	  break
	  	#else : 
	  		#print(num)
	  		#(x)
	  	x+=2
	  return True



topVal = 600851475143
#topVal = 13195
#topVal = 60
tic = time.perf_counter()
## Start low and grab the larger factor and see if it's a prime 
for x in range(1, topVal // 2) :
	if topVal % x == 0:
		#print("testing value ")
		response = isPrime (topVal // x)
		if response == True :
			toc = time.perf_counter()
			largestPrime = topVal // x
			print(f"Found largest prime {largestPrime} in {toc - tic:0.4f} seconds")
			exit()

print("Didn't find one?!")
exit()