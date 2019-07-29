from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/bmi_calc', methods = ["GET", "POST"])
def bmi_calc():
    userData = dict(request.form)
    weight = float(userData["weight"])
    height = float(userData["height"])
    bmiNum = model.bmi(weight, height)
    if bmiNum < 18.5:
        weight_range = 'underweight'
    elif (bmiNum >= 18.5) and (bmiNum < 24.9):
        weight_range = 'normal weight'
    elif (bmiNum >=25) and (bmiNum < 29.9):
        weight_range = 'overweight'
    elif bmiNum >= 30:
        weight_range = 'obese'
    return render_template("bmi_calc.html", bmiNum = bmiNum, weight_range = weight_range)
