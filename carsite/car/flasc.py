from flask import Flask, render_template

app = Flask(__name__)
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Про flasc')

@app.route("/about")
def about():
    return render_template('about.html', title='Про flasc')

if __name__ == "__main__":
    app.run(debug=True)