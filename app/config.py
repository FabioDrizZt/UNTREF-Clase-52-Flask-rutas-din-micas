from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

mongo = PyMongo()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # Conexión a MongoDB
    app.config["MONGO_URI"] = (
        "mongodb+srv://python:python@cluster0.j6h3on9.mongodb.net/Frutas?retryWrites=true&w=majority&appName=Cluster0"
    )
    mongo.init_app(app)

    # Conexión a MySQL
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://root:123456@127.0.0.1:3306/frutas"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    return app
