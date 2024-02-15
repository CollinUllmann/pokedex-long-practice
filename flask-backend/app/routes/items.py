from flask import Blueprint, request
from ..models import db, Items
from ..forms.item_form import NewItemForm

item_routes = Blueprint('item_routes', __name__)

@item_routes.route('/')
def get_items():
  all_items = Items.query.all()
  return {'allItems': [item.to_dict() for item in all_items]}

@item_routes.route('/', methods=["POST"])
def new_item():
  form = NewItemForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    new_item = Items(
      id = form.data["id"],
      happiness = form.data["happiness"],
      imageUrl = form.data["image_url"],
      name = form.data["name"],
      price = form.data["price"],
      pokemonId = form.data["pokemonId"]
    )
    form.populate_obj(new_item)
    db.session.add(new_item)
    db.session.commit()
    return {"newItem": new_item.to_dict()}
  else:
    return 'Bad Data'
  
@item_routes.route('/delete/<int:id>')
def delete_item(id):
  item_to_delete = Items.query.get(id)
  db.session.delete(item_to_delete)
  db.session.commit()
  return {'message': 'Delete successful'}

@item_routes.route('/update/<int:id>')
def update_item(id):
  item_to_update = Items.query.get(id)
  db.session.delete(item_to_update)
  db.session.commit()
  form = NewItemForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    new_item = Items(
      id = form.data["id"],
      happiness = form.data["happiness"],
      imageUrl = form.data["image_url"],
      name = form.data["name"],
      price = form.data["price"],
      pokemonId = form.data["pokemonId"]
    )
    form.populate_obj(new_item)
    db.session.add(new_item)
    db.session.commit()
    return new_item
  return 'Bad Data'