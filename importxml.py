

#VERSION 2- My best
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import xml.etree.ElementTree as ET
from app import db


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen('http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml', context=ctx)
glissades = uh.read()
tree = ET.fromstring(glissades)
xml_file = open('glissades.xml','wb')
xml_file.write(glissades)
xml_file.close()

tree = ET.fromstring(glissades)
liste = tree.findall('glissade')
for item in liste:
    print ('Nom:', item.find('nom').text)
    liste_arrondissement = item.findall('arrondissement')
    for i in liste_arrondissement:
       print("hello")
       print ('Nom arrondissement:', i.find('nom_arr').text)
       print ('Cle:', i.find('cle').text)
       print ('Date maj:', i.find('date_maj').text)
    print ('Ouvert:', item.find('ouvert').text)
    print ('Deblaye:', item.find('deblaye').text)
    print ('Condition:', item.find('condition').text)
