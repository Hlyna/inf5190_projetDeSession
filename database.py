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
            

    def get_installation(self,arrondissement,selection):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from aquatiques where arrondissement = ?",(arrondissement,))
        aquatiques = cursor.fetchall()
        print("I have ")
        print(aquatiques)
        cursor.execute("select * from arrondissements where nom_arr = ?",(arrondissement,))
        glissades = cursor.fetchall()
        cursor.execute("select * from patinoires where nom_arr = ?",(arrondissement,))
        patinoires = cursor.fetchall()
        if selection == "aquatiques":
            return aquatiques
        if selection == "glissades":
            return glissades
        if selection == "patinoires":
            return patinoires
        return "Aucune table choisie"








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

