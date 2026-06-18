from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World! This is my first GitHub website!</h1><p>I am learning Git.</p>"

if __name__ == '__main__':
    app.run(debug=True)