from flask import Flask
from flask import request
from flask import render_template
import joblib

app = Flask(__name__)

# @ is a function decorator
# must run the app.route first before running any function below


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get('rates')
        print(rates)
        model = joblib.load("DBS_predict_linear")
        pred = model.predict([[rates]])
        print(pred)
        share_price = "The predicted DBS Share Price is $" + str(pred[0][0])
        return (render_template("index.html", result=share_price))
    else:
        return (render_template("index.html", result='2'))
