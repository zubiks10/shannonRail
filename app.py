from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask on macOS!"

if __name__ == "__main__":
    app.run(debug=True)
