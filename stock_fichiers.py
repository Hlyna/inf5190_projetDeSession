import pandas as pd
import sqlite3
import psycopg

con = sqlite3.connect("db/database.db")

#Téléchargement en xml

outfile = open('piscines.csv', 'wb')
connection = psycopg.connect(con)
cursor = connection.cursor()
cursor.execute("SELECT * from aquatiques")
rows = cursor.fetchall()
outfile.write('<?xml version="1.0" ?>\n')
outfile.write('<mydata>\n')
for row in rows:
    outfile.write('  <row>\n')
    outfile.write('    <type>%s</type>\n' % row[0])
    outfile.write('    <nom>%s</nom>\n' % row[1])
    outfile.write('    <arrondissement>%s</arrondissement>\n' % row[2])
    outfile.write('    <adresse>%s</adresse>\n' % row[3])
    outfile.write('    <propriete>%s</propriete>\n' % row[4])
    outfile.write('    <gestion>%s</gestion>\n' % row[5])
    outfile.write('    <coord_x>%s</coord_x>\n' % row[6])
    outfile.write('    <coord_y>%s</coord_y>\n' % row[7])
    outfile.write('    <equipement>%s</equipement>\n' % row[8])
    outfile.write('    <long>%s</long>\n' % row[9])
    outfile.write('    <lat>%s</lat>\n' % row[10])
    outfile.write('  </row>\n')
outfile.write('</mydata>\n')
outfile.close()




# Téléchargement en csv.

sql= "SELECT * from aquatiques"
df = pd.read_sql_query(sql,con)
df_agg = df.groupby(['nom','arrondissement']).count()
list(df['nom'].unique())
df_agg.to_csv('csv/aquatiques.csv')


sql= "SELECT * from glissades"
df = pd.read_sql_query(sql,con)
df_agg = df.groupby(['nom','arrondissement']).count()
list(df['nom'].unique())
df_agg.to_csv('csv/glissades.csv')

sql= "SELECT * from patinoires"
df = pd.read_sql_query(sql,con)
df_agg = df.groupby(['nom_arr','nom_pat']).count()
list(df['nom_pat'].unique())
df_agg.to_csv('csv/patinoires.csv')



con.close()