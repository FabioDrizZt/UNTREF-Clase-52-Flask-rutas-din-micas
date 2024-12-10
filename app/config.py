from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
  app = Flask(__name__)
  #Conexión a MongoDB
  app.config["MONGO_URI"] = "mongodb+srv://python:python@cluster0.j6h3on9.mongodb.net/Frutas?retryWrites=true&w=majority&appName=Cluster0"

  mongo.init_app(app)

  return app