pip install flask

from flask import Flask, request, render_template

app = Flask(__name__)

#decorator
@app.route("/", methods=["GET", "POST"])

#flask framework
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html", result=(rate*-50.6)+90.2))
    else:
        return(render_template("index.html", result="waiting for rate ..."))

#double confirming if you want to launch
if __name__ == "__main__":
    app.run()
