export FLASK_APP=app.py

run:
	raml2html templates/doc.raml > templates/documentation.html
	flask run
	
