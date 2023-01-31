# -*- coding: utf-8 -*-

from flask import Flask,render_template

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html",message= "this is my message")

@app.route("/flask_cards")
def show_cards():
    card = db[0]
    return render_template("cards.html", card=card)