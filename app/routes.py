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
    return render_template("bmi_calc.html", bmiNum = bmiNum)
