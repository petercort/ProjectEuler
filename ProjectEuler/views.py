from ProjectEuler import app

from ProjectEuler.main import Problem, createObjects, getName, getDescription, getParams, getAnswer
from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
def index():
	allProblems = createObjects()
	problemList = []
	for problem in allProblems : 
		if(getParams(problem) != "") : 
			params = True
		else : 
			params = False 
		
		problemList.append([problem, getName(problem), getDescription(problem), params])

	return render_template('problems.html', allProblems=problemList)

@app.route("/Problems/<problem>", methods=('GET', 'POST'))
def problemPage(problem): 
	if request.args["paramsReq"] == 'True': 
		print("we are requiring params.")
		if request.method == 'POST': 
			params = request.form['params']
			print(f"there should be params here: {params}")
		## check to see if the params are there 
		else : 
			return redirect(url_for('input', problem=problem)) #(getParams(problem) 
	else : 
		params = ''

	answer = getAnswer(problem, params)
	return render_template('solutions.html', answer=answer)

@app.route("/input/<problem>", methods=('GET', 'POST'))
def input(problem): 
	params = getParams(problem)
	return render_template('form.html', parameters=params, problem=problem)