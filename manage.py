import os
import requests, csv
from app import db, aquatiques

def import_file():
    req = requests.get("https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e4b4a-805d-9af73af03b14/download/piscines.csv")
    url_content = req.content
    csv_file = open('piscines.csv','wb')
    csv.file.write(url_content)
    csv_file.close()

    def import_data():
        import_file()
        with open('piscines.csv', newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter=",",quoting= csv.QUOTE_NONE) #Mettre ici le cas ou on voudrait faire un autre type fichier

            for row in reader :
                    id_uev =  row[0]
                    type = row[1]
                    nom = row[2]
                    arrondissement = row[3]
                    adresse = row[4]
                    propriete = row[5]
                    gestion = row[6]
                    coord_x = row[7]
                    coord_y = row[8]
                    equipement = row[9]
                    long = row[10]
                    lat = row[11]

                    check_db = db.session.query(aquatiques).filter_by(id_uev=id_uev,adresse=adresse,coord_x = coord_x, coord_y=coord_y).all()


                    if len(check_db) == 0 :
                        aquatiques = aquatiques(id_uev = id_uev, type =  type, nom = nom, arrondissement=arrondissement, adresse=adresse, propriete = propriete, gestion = gestion, coord_x = coord_x, coord_y = coord_y, equipement = equipement, long = long, lat = lat)
                        db.session.add(aquatiques)
                        db.session.commit()


                    else:
                        print('existe')
                        pass

            csvfile.close()