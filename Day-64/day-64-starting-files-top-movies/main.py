from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

load_dotenv()
KEY = os.getenv("key")
PARAMS = {
    "key": KEY,
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-games.db"
db.init_app(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable = True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateGame(FlaskForm):
    rating = StringField("Your Rating Out of 10 ex. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddGame(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Game).order_by(Game.ranking))
    all_games = result.scalars()
    return render_template("index.html", games = all_games)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateGame()
    game_id = request.args.get('id')
    game = db.get_or_404(Game, game_id)
    if form.validate_on_submit():
        game.rating = float(form.rating.data)
        game.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", game=game, form=form)

@app.route("/delete")
def delete():
    game_id = request.args.get('id')
    game = db.get_or_404(Game, game_id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add")
def add():
    form = AddGame()
    return render_template("select.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)
