from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

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

class NewPokemon(FlaskForm):
  number = IntegerField("Number", validators=[DataRequired()])
  image_url = StringField("Image URL", validators=[DataRequired()])
  name = StringField("Name", validators=[DataRequired(), Length(min = 3, max = 255)])
  attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(0, 100)])
  defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(0, 100)])
  type = SelectField("Type", choices=[types.enumerate()], validators=[DataRequired()])
  move_1 = StringField("Move 1", validators=[DataRequired()])
  move_2 = StringField("Move 2", validators=[DataRequired()])
  move_3 = StringField("Move 3", validators=[DataRequired()])
  move_4 = StringField("Move 4", validators=[DataRequired()])
  captured = BooleanField("Captured", validators=[DataRequired()])
  submit = SubmitField("Submit")