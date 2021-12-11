from logging import debug
from xml.etree.ElementTree import TreeBuilder
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, render_template, request, redirect, g, jsonify
from sqlalchemy.sql.schema import ForeignKey
from database import Database
import json

app = Flask(__name__, static_url_path="", static_folder="static")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'projetdesession5190@gmail.com'
app.config['MAIL_PASSWORD'] = 'supersecret'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
db = SQLAlchemy(app)

# Piscine dans la base de donnée


class Aquatiques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_uev = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    nom = db.Column(db.String(120), nullable=False)
    arrondissement = db.Column(db.String(120), nullable=False)
    adresse = db.Column(db.String(120), nullable=False)
    propriete = db.Column(db.String(120), nullable=False)
    gestion = db.Column(db.String(120), nullable=False)
    coord_x = db.Column(db.String(120), nullable=False)
    coord_y = db.Column(db.String(120), nullable=False)
    equipement = db.Column(db.String(120), nullable=False)
    long = db.Column(db.String(120), nullable=False)
    lat = db.Column(db.String(120), nullable=False)


class Arrondissements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_arr = db.Column(db.String(120), nullable=False)
    cle = db.Column(db.String(120), nullable=False)
    date_maj = db.Column(db.String(120), nullable=False)


class Glissades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    arrondissement = db.Column(
        db.String(50),
        ForeignKey(Arrondissements.nom_arr)
        )
    ouvert = db.Column(db.Integer)
    deblaye = db.Column(db.String(20), nullable=True)
    condition = db.Column(db.String(120))


class Conditions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_patinoire = db.Column(db.Integer)
    date_heure = db.Column(db.String)
    ouvert = db.Column(db.Integer)
    deblaye = db.Column(db.Integer)
    arrose = db.Column(db.Integer)
    resurface = db.Column(db.Integer)


class Patinoires(db.Model):
    nom_arr = db.Column(db.String(50))
    nom_pat = db.Column(db.String(50))
    condition = db.Column(
        db.Integer,
        db.ForeignKey(Conditions.id_patinoire),
        autoincrement=True,
        primary_key=True
        )

class Users(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    utlisateur = db.Column(db.String(25))
    salt = db.Column(db.String(32))
    hash = db.Column(db.String(128))


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


@app.route('/doc')
def doc():
    return render_template("documentation.html")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/installations/<nom_arrondissement>')
def installation(nom_arrondissement):
    installations_aquatiques = get_db().get_installation(
        nom_arrondissement,
        "aquatiques"
        )
    installations_aquatiques = json.dumps(installations_aquatiques)
    installations_glissades = get_db().get_installation(
        nom_arrondissement,
        "glissades"
        )
    installations_glissades = json.dumps(installations_glissades)
    installations_patinoires = get_db().get_installation(
        nom_arrondissement,
        "patinoires"
        )
    installations_patinoires = json.dumps(installations_patinoires)
    return render_template(
        'installations.html',
        installations_aquatiques=installations_aquatiques,
        installations_glissades=installations_glissades,
        installations_patinoires=installations_patinoires,
        nom_arrondissement=nom_arrondissement
        )
