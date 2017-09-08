from flask import Flask, render_template, request, redirect, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/', methods=['GET', 'POST'])
def register():
    app.num=random.randrange(0,101)
    if request.method == 'POST':
        number = request.form['number']
        if request.form["number"] == app.num:
            return redirect('/success')
        elif request.form["number"] != app.num:
            return redirect("/fail")
    return render_template('index.html')
@app.route("/fail", methods=["GET","POST"])
def fail():
    print app.num
    if request.method == 'POST':
        return redirect("/")
    return render_template("fail.html",num=app.num)
@app.route("/success", methods=["GET","POST"])
def success():
    print app.num
    if request.method == "POST":
        return redirect("/")
    return render_template("success.html",num=app.num)
app.run(debug=True) 
# session['name'] = request.form['name']app.num= random.randrange(0,101)