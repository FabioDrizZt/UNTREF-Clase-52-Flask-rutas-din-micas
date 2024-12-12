from app.config import db
from sqlalchemy import Column, Integer, String, DECIMAL


class Frutas(db.Model):
    __tablename__ = "frutas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    imagen = Column(String(10))
    nombre = Column(String(50), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "imagen": self.imagen,
            "nombre": self.nombre,
            "precio": float(self.precio),
        }


def get_all_frutas():
    frutas = Frutas.query.all()
    return [fruta.to_dict() for fruta in frutas]


def get_all_frutas_by_id(id):
    frutas = Frutas.query.filter_by(id=id).all()
    return [fruta.to_dict() for fruta in frutas]


def get_all_frutas_by_name(name):
    frutas = Frutas.query.filter_by(nombre=name).all()
    return [fruta.to_dict() for fruta in frutas]


def get_all_frutas_by_price(importe):
    frutas = Frutas.query.filter(Frutas.precio >= importe).all()
    return [fruta.to_dict() for fruta in frutas]


def create_fruta(data):
    try:
        nueva_fruta = Frutas(
            imagen=data.get("imagen"),
            nombre=data.get("nombre"),
            precio=data.get("precio"),
        )
        db.session.add(nueva_fruta)
        db.session.commit()
        return nueva_fruta.to_dict()
    except Exception as e:
        db.session.rollback()
        raise e


def update_fruta(id, data):
    fruta = Frutas.query.get(id)
    if fruta:
        fruta.imagen = data.get("imagen", fruta.imagen)
        fruta.nombre = data.get("nombre", fruta.nombre)
        fruta.precio = data.get("precio", fruta.precio)
        db.session.commit()
        return fruta.to_dict()
    return None


def delete_fruta(id):
    fruta = Frutas.query.get(id)
    if fruta:
        db.session.delete(fruta)
        db.session.commit()
        return fruta.to_dict()
    return None
