## insert project euler description here 

def problem11Name() : 
	return "Problem 11"

def problem11Description() :
	return "Given the grid of numbers visible here https://projecteuler.net/problem=11, find the largest product of a given amount of numbers."

def problem11Params() : 
	return "How many integers in your line?"

## Directional bits 
## NORTH: ( y - step - 1 ) >= 0  				||   y-i
## EAST: ( (x + step - 1) < len(mapping[y]))  	||   x+i
## SOUTH: ( (y + step - 1) <= len(mapping))  	||   y+i 
## WEST: ( x - step - 1 ) >= 0    				||   x-i 



def north(x, y, step) : 
	## grab 3 values above on y axis
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( y - (step - 1) ) >= 0 :
		for i in range(1, step ) :
			 product *= int(mapping[y-i][x])
			 groupRange.append(mapping[y-i][x])
	else : 
		product = 0

	return product, groupRange

def northeast(x, y, step) :
	## up to the right
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( y - step - 1 ) >= 0 and ( (x + step - 1) < len(mapping[y])):
		for i in range(1, step ) :
			 product *= int(mapping[y-i][x+i])
			 groupRange.append(mapping[y-i][x+i])
	else : 
		product = 0
	return product, groupRange

def east(x, y, step) : 
	## time to go up x
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if( (x + step - 1) < len(mapping[y])) :
		for i in range(1, step ) :
			 product *= int(mapping[y][x+i])
			 groupRange.append(mapping[y][x+i])
	else : 
		product = 0
	return product, groupRange

def southeast(x, y, step) : 
	## this time we're headed y+1 x+1
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( (y + step) <= len(mapping)) and ( (x + step - 1) < len(mapping[y])):
		for i in range(1, step ) :
			 product *= int(mapping[y+i][x+i])
			 groupRange.append(mapping[y+i][x+i])
	else : 
		product = 0
	return product, groupRange

def south(x, y, step) : 
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( (y + step) <= len(mapping)) :
		for i in range(1, step ) :
			 product *= int(mapping[y+i][x])
			 groupRange.append(mapping[y+i][x])
	else : 
		product = 0
	return product, groupRange

def southwest(x, y, step) : 
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( (y + step) <= len(mapping)) and ( x - step - 1 ) >= 0 :
		for i in range(1, step ) :
			 product *= int(mapping[y+i][x-i])
			 groupRange.append(mapping[y+i][x-i])
	else : 
		product = 0
	return product, groupRange

def west(x, y, step) : 
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( x - step - 1 ) >= 0 :
		for i in range(1, step ) :
			 product *= int(mapping[y][x-i])
			 groupRange.append(mapping[y][x-i])
	else : 
		product = 0
	return product, groupRange

def northwest(x, y, step) : 
	product = mapping[y][x]
	groupRange = [mapping[y][x]]
	if ( y - step - 1 ) >= 0 and ( x - step - 1 ) >= 0 :
		for i in range(1, step ) :
			 product *= int(mapping[y-i][x-i])
			 groupRange.append(mapping[y-i][x-i])
	else : 
		product = 0
	return product, groupRange

def problem11(step) : 
	listOfProducts = []
	keyValueDic = {}
	for y in range(len(mapping)) : 
		for x in range(len(mapping[y])) : 
			## do 8 tests here, n ne e se s sw w nw
			nVal, nRange = north(x, y, step)
			listOfProducts.append(nVal)
			keyValueDic[nVal] = nRange

			neVal, neRange = northeast(x, y, step)
			listOfProducts.append(neVal)
			keyValueDic[neVal] = neRange

			eVal, eRange = east(x, y, step)
			listOfProducts.append(eVal)
			keyValueDic[eVal] = eRange

			seVal, seRange = southeast(x, y, step)
			listOfProducts.append(seVal)
			keyValueDic[seVal] = seRange

			sVal, sRange = south(x, y, step)
			listOfProducts.append(sVal)
			keyValueDic[sVal] = sRange

			swVal, swRange = southwest(x, y, step)
			listOfProducts.append(swVal)
			keyValueDic[swVal] = swRange

			wVal, wRange = west(x, y, step)
			listOfProducts.append(wVal)
			keyValueDic[wVal] = wRange

			nwVal, nwRange = northwest(x, y, step)
			listOfProducts.append(nwVal)
			keyValueDic[nwVal] = nwRange
			#print(compare)
			#sortedCompare = sorted(compare, reverse=True)
			#if int(sortedCompare[0]) > highest :
				#print(f"found new highest {highest}")
				#highest = sortedCompare[0]
	listOfProducts.sort(reverse=True)

	return listOfProducts[0], keyValueDic[listOfProducts[0]]
			## testing north, we subtract 3 from x 

			## testing northeast we subtract 1 from x and 1 from y each time 

	#return answer

## for testing
r1 =[ '08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08']
r1 = [int(i) for i in r1]
r2 =[ '49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00']
r2 = [int(i) for i in r2]
r3 =[ '81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65']
r3 = [int(i) for i in r3]
r4 =[ '52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91']
r4 = [int(i) for i in r4]
r5 =[ '22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80']
r5 = [int(i) for i in r5]
r6 =[ '24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50']
r6 = [int(i) for i in r6]
r7 =[ '32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70']
r7 = [int(i) for i in r7]
r8 =[ '67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21']
r8 = [int(i) for i in r8]
r9 =[ '24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72']
r9 = [int(i) for i in r9]
r10 =[ '21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95']
r10 = [int(i) for i in r10]
r11 =[ '78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92']
r11 = [int(i) for i in r11]
r12 =[ '16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57']
r12 = [int(i) for i in r12]
r13 =[ '86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58']
r13 = [int(i) for i in r13]
r14 =[ '19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40']
r14 = [int(i) for i in r14]
r15 =[ '04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66']
r15 = [int(i) for i in r15]
r16 =[ '88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69']
r16 = [int(i) for i in r16]
r17 =[ '04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36']
r17 = [int(i) for i in r17]
r18 =[ '20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16']
r18 = [int(i) for i in r18]
r19 =[ '20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54']
r19 = [int(i) for i in r19]
r20 =[ '01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']
r20 = [int(i) for i in r20]

mapping = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

#answer, values = problem11() 
#print(f"Values are: {str(values)}, and the product is {int(answer)}")