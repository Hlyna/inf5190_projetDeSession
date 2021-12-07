from flask import Flask
from flask import render_template
from flask import g
from flask import jsonify
from flask import request
from .database import Database




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


@app.route('/')
def form():
    pays = get_db().get_pays()
    return render_template('home.html', pays=pays)


@app.route('/provinces/<pays_id>')
def provinces(pays_id):
    provinces = get_db().get_provinces(pays_id)
    return render_template('provinces.html', provinces=provinces)


@app.route('/villes/<province_id>')
def villes(province_id):
    villes = get_db().get_villes(province_id)
    return render_template('villes.html', villes=villes)


@app.route('/api/pays/', methods=["GET", "POST"])
def liste_pays():
    if request.method == "GET":
        pays = get_db().get_pays()
        data = [{"nom": each[1], "_id": each[0]} for each in pays]
        return jsonify(data)
    else:
        data = request.get_json()
        get_db().add_pays(data["nom"])
        return "", 201


@app.route('/api/provinces/<pays_id>')
def liste_provinces(pays_id):
    provinces = get_db().get_provinces(pays_id)
    data = [{"nom": each[1], "_id": each[0]} for each in provinces]
    return jsonify(data)


@app.route('/api/villes/<province_id>')
def liste_villes(province_id):
    villes = get_db().get_villes(province_id)
    data = [{"nom": each[1], "_id": each[0]} for each in villes]
    return jsonify(data)
