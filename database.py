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

    def get_installation(self, arrondissement, selection):
        cursor = self.get_connection().cursor()
        cursor = self.get_connection().cursor()
        if arrondissement == '':
            return None
        else:
            cursor.execute(
                "select * from aquatiques where arrondissement = \
                    ? order by nom ASC ",
                (arrondissement,))
            aquatiques = cursor.fetchall()
            print("I have ")
            print(aquatiques)
            cursor.execute(
                "select * from glissades WHERE arrondissement = ? \
                    order by nom ASC ",
                (arrondissement,))
            glissades = cursor.fetchall()
            cursor.execute(
                "select * from patinoires WHERE nom_arr = ? order \
                    by nom_pat ASC",
                (arrondissement,))
            patinoires = cursor.fetchall()
            if selection == "aquatiques":
                return aquatiques
            if selection == "glissades":
                return glissades
            if selection == "patinoires":
                return patinoires

    def get_installations(self, selection):
        cursor = self.get_connection().cursor()
        cursor = self.get_connection().cursor()
        cursor.execute("select * from aquatiques order by nom ASC")
        aquatiques = cursor.fetchall()
        print("I have ")
        print(aquatiques)
        cursor.execute("select * from glissades order by nom ASC")
        glissades = cursor.fetchall()
        cursor.execute("select * from patinoires order by nom_pat ASC")
        patinoires = cursor.fetchall()
        if selection == "aquatiques":
            return aquatiques
        if selection == "glissades":
            return glissades
        if selection == "patinoires":
            return patinoires

    def create_user(
            self, username, email, salt, hashed_password, arrondissement):
        connection = self.get_connection()
        connection.execute((
            "insert into users(utilisateur, email, salt, hash, \
                arrondissement)" "values(?, ?, ?, ?, ?)"),
                (username, email, salt, hashed_password, arrondissement))
        connection.commit()

    def get_user_login_info(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute((
            "select salt, hash from users where utilisateur=?"),
            (username,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return user[0], user[1]

    def save_session(self, id_session, username):
        connection = self.get_connection()
        connection.execute(("insert into sessions(id_session, utilisateur) "
                            "values(?, ?)"), (id_session, username))
        connection.commit()

    def delete_session(self, id_session):
        connection = self.get_connection()
        connection.execute((
            "delete from sessions where id_session=?"),
            (id_session,))
        connection.commit()

    def get_session(self, id_session):
        cursor = self.get_connection().cursor()
        cursor.execute((
            "select utilisateur from sessions where id_session=?"),
            (id_session,))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return data[0]
