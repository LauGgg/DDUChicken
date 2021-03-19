from flask import Flask, render_template, request, make_response, jsonify, redirect, session, flash

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")