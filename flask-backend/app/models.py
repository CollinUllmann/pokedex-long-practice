from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pokemon(db.Model):
  __tablename__ = 'pokemon'

  number = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  image_url = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False, unique=True)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  type = db.Column(db.String(255), nullable=False)
  moves = db.Column(db.String(255), nullable=False)
  captured = db.Column(db.Boolean, nullable=False)
  encounter_rate = db.Column(db.Integer, nullable=True)
  catch_rate = db.Column(db.Integer, nullable=True)

  item = db.relationship('Items', back_populates='pokemon')

  def to_dict(self):
    return {
      'number': self.number,
      'imageUrl': self.image_url,
      'name': self.name,
      'attack': self.attack,
      'defense': self.defense,
      'type': self.type,
      'moves': self.moves.split(','),
      'captured': self.captured,
      'encounterRate': self.encounter_rate / 100,
      'catchRate': self.catch_rate / 100
    }


class PokemonType(db.Model):
  __tablename__ = 'pokemon_types'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)

  def to_dict(self):
    return {
      'type': self.name
    }


class Items(db.Model):
  __tablename__ = 'items'

  id = db.Column(db.Integer, primary_key=True)
  happiness = db.Column(db.Integer)
  image_url = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemonId = db.Column(db.Integer, db.ForeignKey('pokemon.number'), nullable=False)

  pokemon = db.relationship('pokemon', back_populates='items')

  def to_dict(self):
    return {
      'id': self.id,
      'happiness': self.happiness,
      'imageUrl': self.image_url,
      'name': self.name,
      'price': self.price,
      'pokemonId': self.pokemonId
    }