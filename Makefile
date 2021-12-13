export FLASK_APP=app.py

run:
	raml2html doc.raml > templates/documentation.html
	flask run
	
