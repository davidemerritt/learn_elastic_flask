from flask import Flask
app = Flask(__name__)

@app.route("/")
def run_me():
    return "Hello World!"

if __name__ == "__main__":
    app.run()