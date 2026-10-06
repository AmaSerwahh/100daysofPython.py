from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def make_bold(function):
    def wrapper(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return "<i>" + function(*args, **kwargs) + "</i>"
    return wrapper


def make_underlined(function):
    def wrapper(*args, **kwargs):
        return "<u>" + function(*args, **kwargs) + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)


