from app.config import mongo

def get_all_collection():
  return mongo.db.Frutas

def get_all_frutas():
  return list(get_all_collection().find({}, {"_id": 0}))

def get_all_frutas_by_id(id):
  return list(get_all_collection().find({"id": id}, {"_id": 0}))

def get_all_frutas_by_name(name):
  return list(get_all_collection().find({"nombre": name}, {"_id": 0}))

def get_all_frutas_by_price(importe):
  return list(get_all_collection().find({"importe": {"$gte": importe}}, {"_id": 0}))