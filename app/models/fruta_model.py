from app.config import mongo

def get_all_collection():
  return mongo.db.Frutas

def get_all_frutas():
  return list(get_all_collection().find({}, {"_id": 0}))
