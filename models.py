import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False, unique=True)
    apellido = db.Column(db.String(100), nullable = False, unique=True)
    email = db.Column(db.String(100), nullable = False, unique=True)
    direccion = db.Column(db.String(100), nullable = False, unique=True)
    nombre = db.Column(db.String(100), nullable = False, unique=True)
    telefono = db.Column(db.String(100), nullable = False)
    clave = db.Column(db.String(100), nullable = True)
    usuario = db.relationship('Tienda', backref= 'tienda', lazy = True)
    usuarioFactura = db.relationship('Factura',  backref= 'factura', lazy = True)



class Tienda(db.Model):
    __tablename__ = 'Tienda'
    id = Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False, unique=True)
    rut = db.Column(db.String(100), nullable = False, unique=True)
    email = db.Column(db.String(100), nullable = False, unique=True)
    direccion = db.Column(db.String(100), nullable = False, unique=True)
    clave = db.Column(db.String(100), nullable = False, unique=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    tienda = db.relationship('Productos', backref= 'productos', lazy = True)
    tiendaCategory = db.relationship('CategoriaTienda',  backref= 'categoria', lazy = True)

class Productos(db.Model):
    __tablename__ = 'Productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False, unique=True)
    foto = db.Column(db.String(100), nullable = False, unique=True)
    stock = db.Column(db.String(100), nullable = False, unique=True)
    precio = db.Column(db.String(100), nullable = False, unique=True)
    clave = db.Column(db.String(100), nullable = False, unique=True)
    tienda_id = db.Column(db.Integer, db.ForeignKey('Tienda.id'))
    producto = db.relationship('CategoriaProductos', backref= 'CategoryProduc', lazy = True) 



class CategoriaProductos(db.Model):
    __tablename__ = 'CategoriaProductos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable = False, unique=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('Productos.id'))
    


class CategoriaTienda(db.Model):
    __tablename__ = 'CategoriaTienda'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable = False, unique=True)
    tienda_id = db.Column(db.Integer, db.ForeignKey('Tienda.id'))
    




class Factura(db.Model):
    __tablename__ = 'Factura'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    factura = db.relationship('Detallefactura',  backref= 'detalle', lazy = True)
    


class Detallefactura(db.Model):
    __tablename__ = 'DetalleFactura'
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('Factura.id'))
    
    

'''  def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email

        }'''
