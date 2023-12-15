from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db= SQLAlchemy()

class Usuario(db.Model):
    __tablename__= 'user'
    
    id_user= db.Column(db.Integer, primary_key=True)
    nombre_y_apellido= db.Column(db.String(30))
    city= db.Column(db.String(20))
    email=db.Column(db.String(20))
    contrasenha=db.Column(db.String(10))
    
    tickets= relationship("Ticket", backref='user')
    
class Profesional(db.Model):
    __tablename__= 'profesional'
    
    id_prof= db.Column(db.Integer, primary_key=True)
    nombre_y_apellido= db.Column(db.String(30))
    city=db.Column(db.String(20))
    email=db.Column(db.String(20))
    numero_phone= db.Column(db.Integer)
    contrasenha=db.Column(db.String(10))
    profesion= db.Column(db.String(20))
    descripcion= db.Column(db.String(50))
    descripcion_det = db.Column(db.String(250))
    tickets= relationship("Ticket", backref='profesional')
    
class Ticket(db.Model):
    __tablename__= 'tickets'
    
    id_ticket= db.Column(db.Integer, primary_key=True)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id_user'))
    tipo_trabajo= db.Column(db.String(20))
    descripcion= db.Column(db.String(250))
    ciudad= db.Column(db.String(20))
    id_prof= db.Column(db.Integer, db.ForeignKey('profesional.id_prof'))
    
    