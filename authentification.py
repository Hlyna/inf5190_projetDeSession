import hashlib
import sqlite3
import uuid


def authentification():
    print("Nom d'utilisateur : ")
    username = input()
    print("Mot de passe : ")
    password = input()

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute((
        "select salt, hash from users where utilisateur=?"), (username,))
    user = cursor.fetchone()
    connection.close()

    if user is None:
        print("Utilisateur inconnu")
    else:
        salt = user[0]
        hashed_password = hashlib.sha512(
            str(password + salt).encode("utf-8")).hexdigest()
        if hashed_password == user[1]:
            print("Accès autorisé")
        else:
            print("Accès refusé")
