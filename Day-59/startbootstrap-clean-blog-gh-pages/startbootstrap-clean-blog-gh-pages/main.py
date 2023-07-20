from flask import Flask, render_template
import requests

data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=data)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def get_post(index):
    final_post = None
    for i in range(len(data)):
        if index == data[i]["id"]:
            final_post = data[i]["id"]
    return render_template('post.html', article=final_post)

if __name__ == "__main__":
    app.run(debug=True)
