import sqlite3



class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            

    def get_installations(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from aquatiques")
        aquatiques = cursor.fetchall()
        return aquatiques



    def get_installation(self, nom_arr):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from aquatiques where arrondissement= ?",
                       (nom_arr,))
        installation = cursor.fetchall()
        return installation


    def get_recherche(self, recherche):
        cursor = self.get_connection().cursor()
        if recherche == '':
            return None
        else:
            cursor.execute("select titre, identifiant, date_publication from \
                        article where titre like ? or paragraphe like ?",
                       ('%' + recherche + '%', '%' + recherche + '%',))
            articles = cursor.fetchall()
            return articles

