""" Let's test out elastic search and flask combination """
from flask import Flask
app = Flask(__name__) # pylint:disable=C0103

@app.route("/")
def run_me():
    """ Base run section """
    return "Hello World!"

if __name__ == "__main__":
    app.run()
