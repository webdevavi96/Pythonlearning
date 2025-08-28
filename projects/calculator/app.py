from flask import Flask, render_template,request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculat():
    inputData = request.form.get("input")
    
    try:
        result = eval(inputData)
    except Exception:
        result = "error"
    
    return render_template("index.html", result = result)
    
if __name__ == "__main__":
    app.run(debug=True)