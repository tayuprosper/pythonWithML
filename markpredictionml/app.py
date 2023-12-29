from flask import Flask,render_template
from utils import predict_mark
app = Flask(__name__)

@app.route('/')
def home():
    predict_mark(300,10,30)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)