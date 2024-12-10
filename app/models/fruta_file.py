from app.data.frutas import frutas

def get_all_frutas():
  return frutas

def get_all_frutas_by_id(id):
  return next((fruta for fruta in frutas if fruta['id'] == id), None)