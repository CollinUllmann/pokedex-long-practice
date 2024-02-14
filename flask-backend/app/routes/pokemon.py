from flask import Blueprint
from ..models import Pokemon

pokemon_routes = Blueprint('pokemon_routes', __name__)

@pokemon_routes.route('/')
def index():
  all_pokemon = Pokemon.query.all()
  print(all_pokemon)
  return {"allPokemon": [pokemon.to_dict() for pokemon in all_pokemon]}

@pokemon_routes.route('/', methods=["POST"])
def new_pokemon():
  form = NewPokemonForm()
  if form.validate_on_submit():
    params = {

    }