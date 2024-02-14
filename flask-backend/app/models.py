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

  type = db.Column(db.String(255), primary_key=True, nullable=False)


class Items(db.Model):
  __tablename__ = 'items'

  happiness = db.Column(db.Integer)
  imageUrl = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemonId = db.Column(db.Integer, nullable=False)