import os, requests, json

from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/result", methods=['GET','POST'])
def result():
    if request.method=='POST':
        schoolname=request.form.get("name")
        rad=request.form.get("rad")
        return render_template("result.html", schoolname=schoolname, rad=rad)

@app.route("/routing",methods=["GET","POST"])
def routing():
    if request.method=='POST':
        schoolname=request.form.get("name")
        return render_template("routing.html", schoolname=schoolname)
