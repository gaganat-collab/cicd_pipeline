from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi"


if __name__ == "__main__":
    # Use debug only in development
    app.run(host="0.0.0.0", port=5000, debug=False)