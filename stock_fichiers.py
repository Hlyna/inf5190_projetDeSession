import pandas as pd
import sqlite3

con = sqlite3.connect("db/database.db")

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