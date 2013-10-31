#find the sum of all the multiples of 3 or 5 below 1000

counter = 0

for x in range(0, 1000):
	if x % 3 == 0:
		counter+= x
	elif x % 5 == 0:
		counter+= x

print(counter)
exit()
