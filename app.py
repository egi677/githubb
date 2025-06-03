from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/reals")
def reals():
    return render_template("reals.html")


if __name__ == "__main__":
    app.run(debug=True)