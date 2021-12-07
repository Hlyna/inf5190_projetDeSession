from logging import debug
from xml.etree.ElementTree import TreeBuilder
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, render_template, request, redirect, g, jsonify
from sqlalchemy.sql.schema import ForeignKey
import connexion
from database import Database
import json,xmltodict


app = Flask(__name__, static_url_path="", static_folder="static")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

#Piscine dans la base de donnée
class Aquatiques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_uev = db.Column(db.String(120), nullable= False)
    type = db.Column(db.String(120), nullable= False)
    nom = db.Column(db.String(120), nullable= False)
    arrondissement = db.Column(db.Integer, nullable= False)
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
    nom_arr = db.Column(db.String(120), nullable= False)
    cle = db.Column(db.String(120), nullable= False)
    date_maj= db.Column(db.String(120), nullable= False)


class Glissades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50),nullable = False)
    arrondissement = db.Column(db.String(50),ForeignKey(Arrondissements.nom_arr))
    ouvert = db.Column(db.Integer, nullable = True)
    deblaye = db.Column(db.Integer,nullable = False)
    condition = db.Column(db.String(120))



class Conditions(db.Model):
    id = db.Column( db.Integer, primary_key = True )
    id_patinoire = db.Column(db.Integer)
    date_heure=db.Column(db.String)
    ouvert= db.Column(db.Integer)
    deblaye=db.Column(db.Integer)
    arrose=db.Column(db.Integer)
    resurface=db.Column(db.Integer)


class Patinoires(db.Model):
    nom_arr = db.Column(db.String(50))
    nom_pat = db.Column(db.String(50), primary_key=True)
    condition = db.Column(db.Integer) ,ForeignKey(Conditions.id_patinoire)


















def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route ('/doc')
def index():
    return "Page de documentation raml"


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/installations')
def installations():
    with open('glissades.xml','r') as myfile:
        obj = xmltodict.parse(myfile.read())
        glissade = json.dumps(obj)
        
        
     
    #print(aquatiques.json())
    return render_template('aquatiques.html', glissades = glissade )















@app.route('/api/installations/<nom_arrondissement>')
def installation(nom_arrondissement):
    installation = get_db().get_installation(nom_arrondissement)
    return render_template('aquatique.html', installation=installation)



@app.route("/resultat-recherche", methods=["GET", "POST"])
def recherche():
    if request.method == "GET":
        return render_template("aquatique.html")
    else:
        recherche = request.form["champ-recherche"]

    if recherche == "":
        error1 = "Le champ recherche est vide"
        return render_template("home.html", error1=error1)
    else:
        articles = get_db().get_recherche(recherche)
    if articles is None :
        error = "Aucun article ne correspond à votre recherche :("
        return render_template("aquatique.html", error=error)
    print(articles)
    return render_template("aquatique.html", articles=articles)

