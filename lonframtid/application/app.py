from flask import Flask
app = Flask(name)




@app.route("/")


def startsida():


    return "<p>Hello, World!</p>"




@app.post("/prognos")


def prognos_arbete():


    return "<p>Hello, World!</p>"





@app.post("/lön")


def lön_arbete():


    return "<p>Hello, World!</p>"


