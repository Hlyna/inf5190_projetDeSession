export FLASK_APP=app.py

run:
	flask run
	raml2html example.raml > example.html
	raml2html --theme raml2html-markdown-theme example.raml > example.html
	raml2html --template my-custom-template.nunjucks -i example.raml -o example.html
	
