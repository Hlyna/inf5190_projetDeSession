from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, g, jsonify
from sqlalchemy.sql.schema import ForeignKey




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


class Arrondissements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_arrondissement = db.Column(db.String(120), nullable= False)
    cle = db.Column(db.String(120), nullable= False)
    date_maj= db.Column(db.String(120), nullable= False)




class Glissades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    arrondissement =  db.Column(db.Integer), ForeignKey("Arrondissement.id")
    ouvert = db.Column(db.Integer, nullable= False)
    deblaye = db.Column(db.Integer, nullable= False)
    condition = db.Column(db.String(120), nullable= False)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route ('/doc')
def index():
    return "Page de documentation raml"




