## timer.py 

import time


def startTimer() : 
	tic = time.perf_counter()
	return tic

def endTimer(tic) : 
	toc = time.perf_counter()
	timeTaken = toc - tic
	return timeTaken