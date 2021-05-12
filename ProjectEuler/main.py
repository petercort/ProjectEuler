## Main page python
from os.path import dirname, basename, isfile, join
import glob
from ProjectEuler.Problems import *
#import timer


## Instantiate a class of type Problem. Each problem has the following data
## Problem Name
## Problem Description
## Problem Parameters 
## Problem Answer (Set on return from the program? Maybe this doesn't need to be here. Unclear.)

class Problem(object) : 
	def __init__(self, name, description, parameters) : 
		self.name = name
		self.description = description
		self.parameters = parameters

	def getName(self) : 
		return self.name

	def getDescription(self) : 
		return self.Description

	def getParamaters(self) : 
		return self.parameters


def createObjects() : 
	allFiles = glob.glob(join(dirname(__file__)+"/Problems/", "*.py"))
	allProblems = [ basename(f)[:-3] for f in allFiles if isfile(f) and f.startswith(dirname(__file__)+"/Problems/problem")]
	sortedProblems = sorted(allProblems, key=lambda a: int(a[7:]))

	for problem in sortedProblems :
		problemName = getName(problem)
		problemDescription = getDescription(problem)
		problemParameters = getParams(problem) 
		problem = Problem(problemName, problemDescription, problemParameters)

	return sortedProblems

def getProblem() : 
	problem = input("Please enter a problem to solve, or enter 'all' to view all problems: ")
	if problem.lower() == "all" :
		allProblems = getAll() 

		for problem in allProblems :
		  print(problem)
		  problemName = getName(problem) 
		  problemDescription = getDescription(problem) 
		  print(problemName)
		  print(problemDescription)

		getProblem() 
	elif problem.lower().startswith('problem') : 
		return problem.lower()
	elif problem == 'exit' : 
		exit("Thanks for using my program and have a great day!")

def getName(problem) : 
	problemName = eval("{}.{}Name".format(str(problem), str(problem)) + "()")
	return problemName 

def getDescription(problem) : 
	problemDescription = eval("{}.{}Description".format(str(problem), str(problem)) + "()")
	return problemDescription

def getParams(problem) :
	problemParameters = eval("{}.{}Params".format(str(problem), str(problem)) + "()")
	return problemParameters
	#if problemParameters != "" :
	#	parameters = input("Please provide the following parameters: {}".format(problemParameters))
	#else : 
	#	parameters = ""
	

def getAnswer(problem, params) : 
	answer = eval("{}.{}".format(problem, problem) + "(" + params + ")")
	return answer

def gatherer():
	problem = getProblem()
	problemName = getName(problem)
	description = getDescription(problem)
	params = getParams(problem)
	startTime = timer.startTimer() 
	answer = getAnswer(problem, params)
	totalTime = timer.endTimer(startTime) 
	#print(f"The answer to {problemName}, {description}, is: \n{answer} ")
	#print(f"Time taken to solve was {totalTime:0.4f} seconds")

	gatherer()

