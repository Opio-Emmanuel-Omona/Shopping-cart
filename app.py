from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def home():
    return "Hello world"


if __name__ == '__main__':
	APP.run(debug=True)