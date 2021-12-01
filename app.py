from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

#Piscine dans la base de donnée
class Aquatiques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_uev = db.Column(db.String(120), nullable= False)
    type = db.Column(db.String(120), nullable= False)
    nom = db.Column(db.String(120), nullable= False)
    arrondissement = db.Column(db.String(120), nullable= False)
    adresse = db.Column(db.String(120), nullable= False)
    propriete = db.Column(db.String(120), nullable= False)
    gestion = db.Column(db.String(120), nullable= False)
    coord_x = db.Column(db.String(120), nullable= False)
    coord_y = db.Column(db.String(120), nullable= False)
    equipement = db.Column(db.String(120), nullable= False)
    long = db.Column(db.String(120), nullable= False)
    lat = db.Column(db.String(120), nullable= False)


class Arrondissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_arrondissement = db.Column(db.String(120), nullable= False)
    cle = db.Column(db.String(120), nullable= False)
    date_maj= db.Column(db.String(120), nullable= False)




class Glissade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = Arrondissement() 
    arrondissement = db.Column(db.String(120), nullable= False)
    ouvert = db.Column(db.Integer, nullable= False)
    deblaye = db.Column(db.Integer, nullable= False)
    condition = db.Column(db.String(120), nullable= False)


    


