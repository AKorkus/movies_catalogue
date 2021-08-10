from flask import Flask, render_template, url_for

app = Flask(__name__)

movies = range(16)

@app.route('/')
def homepage():
    return render_template("homepage.html", movies = movies)

if __name__ ==("__main__"):
    app.run(debug=True)