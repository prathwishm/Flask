from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def welcome():
    height=0
    weight=0
    bmi=0
    if request.method =="POST" and 'userweight' and 'userheight' in request.form:
        height = request.form.get('userheight')
        weight = request.form.get('userweight')
        bmi = int(weight)/((int(height)/100)**2)
    return render_template("index.html", height=height, weight=weight, bmi=bmi)



app.run()
