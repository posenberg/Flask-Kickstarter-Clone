# just a convention in python to include __init__ 

#after creating template with index.html, import render_template
from flask import Flask, render_template
from flask.ext.script import Manager #from pip install flask-script library

app = Flask(__name__)
manager = Manager(app)

#Look for any request that hi the route directory and  
#Hello world response.
@app.route("/")
def hello():
    return render_template("index.html")

