from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, URL

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class NewPokemonForm(FlaskForm):
  number = IntegerField("Number", validators=[DataRequired()])
  image_url = StringField("Image URL", validators=[DataRequired(), URL()])
  name = StringField("Name", validators=[DataRequired(), Length(min = 3, max = 255)])
  attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(0, 100)])
  defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(0, 100)])
  type = SelectField("Type", validators=[DataRequired()])
  move_1 = StringField("Move 1", validators=[DataRequired()])
  move_2 = StringField("Move 2", validators=[DataRequired()])
  captured = BooleanField("Captured", validators=[DataRequired()])
  submit = SubmitField("Submit")