from flask import Flask

app = Flask(__name__)


def make_bold(func_to_bold):
    def bold_wrapper():
        return "<b>" + func_to_bold() + "</b>"
    return bold_wrapper


def make_emphasis(func_to_emphasis):
    def emphasis_wrapper():
        return "<em>" + func_to_emphasis() + "</em>"
    return emphasis_wrapper


def make_underlined(func_to_underline):
    def underlined_wrapper():
        return "<u>" + func_to_underline() + "</u>"
    return underlined_wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "<p>Oieeeeeeeeee!</p>"


if __name__ == "__main__":
    app.run(debug=True)
