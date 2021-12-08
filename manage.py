from datetime import date
import os
import xml.etree.ElementTree as ET 
from app import db, Aquatiques,Arrondissements,Glissades,Conditions,Patinoires
import urllib.request, urllib.parse, urllib.error,requests, csv,json
import xml.etree.ElementTree as ET
import bgscheduler




def import_files():
    db.create_all()
    db.session.commit
    
    #importer fichier csv 
    req = requests.get("https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv")
    url_content = req.content
    csv_file = open('piscines.csv','wb')
    csv_file.write(url_content)
    csv_file.close()

    with open('piscines.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",",quoting= csv.QUOTE_NONE) #Mettre ici le cas ou on voudrait faire un autre type fichier
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
            
            #Je verifie que les data ne se répetent pas pour ne rien dupliquer
            check_db = db.session.query(Aquatiques).filter_by(id_uev=id_uev,adresse=adresse,coord_x = coord_x, coord_y=coord_y).all()
            #Je récupère les informations
            if len(check_db) == 0 :
                print("je vais ajouter")
                aquatique = Aquatiques(id_uev = id_uev, type =  type, nom = nom, arrondissement=arrondissement, adresse=adresse, propriete = propriete, gestion = gestion, coord_x = coord_x, coord_y = coord_y, equipement = equipement, long = long, lat = lat)
                db.session.add(aquatique)
                db.session.commit()
                print('Ajout nouvel aqua-thing !')
            else:
                print('aqua - existe déjà')
                pass
    csvfile.close()














    #importer xml de glissades 
    my_url = 'http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml'
    root = ET.parse(urllib.request.urlopen(my_url)).getroot()
    for glissade in root : 
        nom = glissade[0].text 
        nom_arr = glissade[1][0].text 
        cle = glissade[1][1].text 
        date_maj = glissade[1][2].text 
        ouvert = glissade[2].text 
        deblaye = glissade[3].text 
        condition = glissade[4].text 

        check_db = db.session.query(Arrondissements).filter_by(nom_arr = nom_arr, cle =cle, date_maj=date_maj).all()
        #Je filtre pour ne pas avoir de doublons.
        if len(check_db) == 0 :
            print("je vais ajouter")
            arrondissement = Arrondissements(nom_arr = nom_arr, cle =cle, date_maj=date_maj)   
            db.session.add(arrondissement)
            db.session.commit()

        check_db = db.session.query(Glissades).filter_by(nom = nom, arrondissement = nom_arr).all()
        if len(check_db) == 0 :
            print("je vais ajouter")
            glissade = Glissades(nom = nom , arrondissement = nom_arr, ouvert = ouvert, deblaye = deblaye, condition = condition)
            db.session.add(glissade)    #Ajouter ici la maj à minuitss
            db.session.commit()
            print('Ajout nouvelle glissade!')
        else:
            print('Glissade : existe déjà')


    #importer xml de glissades 
    my_url = 'https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml'
    root = ET.parse(urllib.request.urlopen(my_url)).getroot()

    i = 1
    j = -1
    for pati in root : 
        j= j+1
        nom_arr = pati[0].text
        nom_pat = pati[1][0].text

        check_db = db.session.query(Patinoires).filter_by(nom_arr=nom_arr,nom_pat = nom_pat).all()
        if len(check_db) == 0 :
            print("je vais ajouter")
            patinoires = Patinoires(nom_arr=nom_arr,nom_pat = nom_pat)
            db.session.add(patinoires)
            db.session.commit()
            print('Ajout nouvelle patinoire')
        else:
            print('Patinoire : existe déjà')
            pass

        date_heure = pati[1][1][0].text
        print(date_heure)
           
        for condition in pati[1][1]:
            date_heure =pati[1][i][0].text
            ouvert = pati[1][i][1].text
            deblaye = pati[1][i][2].text
            arrose = pati[1][i][3].text
            resurface = pati[1][i][4].text
            id_patinoire = j
            check_db1 = db.session.query(Conditions).filter_by(id_patinoire= id_patinoire, date_heure= date_heure,ouvert = ouvert,deblaye =deblaye,arrose=arrose, resurface = resurface).all()
            if len(check_db1) == 0 :
                condition = Conditions ( id_patinoire = id_patinoire, date_heure= date_heure,ouvert = ouvert,deblaye =deblaye,arrose=arrose, resurface = resurface)
                db.session.add(condition)
                db.session.commit()
                print('Ajout nouvelle condition !')

            else :
                print("condition : existe déjà")
               
            i = i+1 
                

            

    
       


    



















if __name__ == '__main__':
    import_files()