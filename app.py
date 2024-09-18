from dotenv import load_dotenv
from flask import Flask, render_template, request ,jsonify
from pro_intro import ice_breaker_with

load_dotenv()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
