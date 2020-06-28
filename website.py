from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/mypage')
def mypage():
    print("We received GET")
    return render_template("parent.html")

@app.route('/mypage/me')
def mypage_me():
    print("We received GET")
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def mypage_contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/contact")