from flask import Blueprint, request
from ..models import Pokemon, PokemonType, db
from ..forms.pokemon_form import NewPokemonForm

pokemon_routes = Blueprint('pokemon_routes', __name__)

@pokemon_routes.route('/')
def index():
  all_pokemon = Pokemon.query.all()
  print(all_pokemon)
  return {"allPokemon": [pokemon.to_dict() for pokemon in all_pokemon]}

@pokemon_routes.route('/', methods=["POST"])
def new_pokemon():
  form = NewPokemonForm()
  form.type.choices = [(type.id, type.name) for type in PokemonType.query.all()]
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    new_pokemon = Pokemon(
      number = form.data["number"],
      imageUrl = form.data["image_url"],
      name = form.data["name"],
      attack = form.data["attack"],
      defense = form.data["defense"],
      type = form.data["type"],
      moves = [form.data["move_1"], form.data["move_2"]],
      captured = form.data["captured"]
    )
    form.populate_obj(new_pokemon)
    db.session.add(new_pokemon)
    db.session.commit()
    return {"newPokemon": new_pokemon.to_dict()}
  else:
    return 'Bad Data'


@pokemon_routes.route('/delete/<int:number>')
def delete_pokemon(number):
  pokemon_to_delete = Pokemon.query.get(number)
  db.session.delete(pokemon_to_delete)
  db.session.commit()
  return {'message': 'Delete successful'}

@pokemon_routes.route('/types')
def get_types():
  pokemon_types = PokemonType.query.all()
  return {"allPokemonTypes": [type.to_dict() for type in pokemon_types]}
