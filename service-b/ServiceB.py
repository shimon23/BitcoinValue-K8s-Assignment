from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Service B"


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)