from flask import Flask
app = Flask(__name__)

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
