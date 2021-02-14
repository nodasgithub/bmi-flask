#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    weight = ''
    height = ''
    bmi = ''

    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))

        bmi = weight / ((height / 100.0) * (height / 100.0))

    return render_template("index.html",
                            bmi=bmi)

app.run()