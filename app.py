from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    some = "Hello WORLD!"
    return render_template("home.html", something=some)


@app.route("/hello", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        greet = request.form["greet"]
        greeting = f"Hello {name}, {greet}"
        return render_template("index.html", greeting=greeting)
    else:
        greeting = request.args.get("name", "Nobody")
        return render_template("index.html", greeting=greeting)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
