from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, URL, Length


class NewItemForm(FlaskForm):

  happiness = IntegerField("Happiness", validators=[DataRequired()])
  image_url = StringField("Image URL", validators=[DataRequired(), URL(), Length(min=0, max=255)])
  name = StringField("Name", validators=[DataRequired()])
  price = IntegerField("Price", validators=[DataRequired()])
  pokemonId = IntegerField("Pokemon Id", validators=[DataRequired()])
  submit = SubmitField("Submit")