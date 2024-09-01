from flask import Flask, render_template, request
import google.generativeai as palm
import os



api = os.getenv("MAKERSUITE_API_TOKEN") #Add an environment variable called MAKERSUITE_API_TOKEN and set its value to your Google API
palm.configure(api_key=api)
model = {"model": "models/text-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods=["GET", "POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.generate_text(prompt=q, **model)
    return(render_template("makersuite.html", r=r.result))

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke-set", methods=["GET", "POST"])
def joke_set():
    return(render_template("joke-set.html"))

@app.route("/news", methods=["GET", "POST"])
def news():
    return(render_template("news.html"))

@app.route("/joke-AI", methods=["GET", "POST"])
def joke_AI():
    r = palm.generate_text(prompt="Tell me one joke rooted in Singaporean culture that can only be as long as two sentences.", **model)
    return(render_template("joke-AI.html", r=r.result))

if __name__ == "__main__":
    app.run()
