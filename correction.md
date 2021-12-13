# Points developpés dans le fichier 

## A1 -15xp-
L'ensemble des informations est tiré à partir des URL fournies et dépose les informations directement dans la base donnée à l'aide de SqlAlchemy. Les schémas des différentes tables se trouvent dans le fichier app.py. Le téléchargement des données se fait dans la fonction import_files du fichier manage.py. Autrement dit. Lancer la commande 
```
python manage.py
```
va télécharger toutes les données nécessaires dans les tables. Si un élément existe déjà dans la table, celui-ci ne se répètera pas et le téléchargent passe à l'élément suivant.

## A2 -5xp-
Les mises à jour se font automatichement à minuit à l'aide d'un bg scheduler à minuit automatiquement. L'heure choisie est automatiquement 'hour = 0' donc minuit. Il est possible de le changer dans le script ```bgscheduler.py```

## A3 -5xp-
La documentation de chaque service implémenté se trouve sur le chemin /doc, elle se trouve dans le fichier documentation.html qui est généré à partir du fichier documentation.raml à l'aide de la commande raml2html. Cette commande est appelé dans le Makefil et est donc exécuté direment au lancement de l'application. 

## A4 -10xp-
Dans la route "api/installations/<nom_arrondissement>" où nom représente le nom de l'arrondissement recherché. Il est possible de visualiser les noms de toutes les installations "glissades/patinoires/piscines" au choix qui se trouvent dans l'arrondissement choisie. Il est possible de choisir grâce à un menu déroulant, quel type d'installation nous voulons trouver.

## B1 -10xp-
Une boite email a été créée dans le but de réaliser cette tâche "projetdesession5190@gmail.com". Lors du lancement de la commande ```manage.py``` si jamais de nouvelles installations ont été ajoutés dans les URL. Il est possible de changer l'adresse mail à laquelle on souhaite recevoir les informations dans le script ```courrier.py```. L'adresse courriel est stockée dans le fichier de configuration ```courrier.yml```

## B2 -10xp-
La même informations est publié dans un compte twitter. Le compte twitter a également été créé pour ce projet. L'identifiant est @prj_session5190 et il a été créé avec l'adrese mail utilisé dans la mission B1. À chaque nouvelle installation ajoutée. Un tweet contenant le nom de cette installation est publié dans ce compte là. 

## C1 -10xp-
Pour chaque installation, on indique toute l'information connue trié en ordre croissant selon le nom de l'installation à la route ```api/installations```


## C2 -10xp-
Les informations des installations se retrouvent toutes dans le fichier ```installations.xml```. L'opération est effectuée dans le fichier ```stock_fichiers.py```


## C3 -5xp-
Les informations des installations se retrouvent toutes dans le fichier ```installations.csv```. En lançant la commande ``` python stock_fichiers``` 3 fichiers csv sont créés contenant les informations des installations te sont déposés dans le répertoire csv.

## E1 -10xp-
L'application prend les informations se trouvant le fichier ```users.json```, qui est validé par json-schema au travers de la fonction validate dans le script ``` jsonValidate.py ``` . Si le lancement de ```python jsonValidate.json``` ne lance aucune exception, alors le fichier est dans un format valide. 

Le script python recupère les informations python, et met les informations de l'usager dans la table Utilisateur. Ce service est lancé par le script ```authentification.py``` avec la commande ```python authentification.py```. Il est possivle

## E2 -5xp-
La route /inscription qui rend la page ```inscription.html``` permet à un utilisateur de se créer un profil. Ces informations sont ajoutées directement dans la base de données. 