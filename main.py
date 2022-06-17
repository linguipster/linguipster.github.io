import os
from flask import Flask, render_template

extra_dirs = ['./static', './templates']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

app = Flask(__name__)
application = app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/lacovis")
def lacovis():
    return render_template("lacoviz.html")


@app.route("/lacoviz")
def lacoviz():
    return render_template("lacoviz.html")


@app.route("/qualifikationsarbeiten")
def quali():
    return render_template("quali.html")


@app.route("/timeline")
def timeline():
    return render_template("timeline.html")


if __name__ == "__main__":
    application.run(debug=True, extra_files=extra_files, static_folder='/static')
