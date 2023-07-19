from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):
    age = requests.get(url=f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(url=f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("index.html", nam=name.capitalize(), sex=gender, number=age)

@app.route('/blog')
def get_blog():
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url=blog_url).json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)