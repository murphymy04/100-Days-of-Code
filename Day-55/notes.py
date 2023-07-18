from flask import Flask
app = Flask(__name__)

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emph(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Howdy World!</h1>' \
            '<p style="text-align: center">This is a paragraph.</p>' \
            '<img src=https://media.giphy.com/media/vD0AuAqhDmKli/giphy.gif>' \
            ''

@app.route("/bye")
@make_bold
@make_emph
@make_underline
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)
