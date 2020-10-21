# Summary  

- Goal - Review extending demo web app to allow uploading of test cdb and vocab models on a virtual machine

- Steps
	- Run instance locally [DONE - but outside of docker container setup]
	- Review options to store models (e.g. save in database, update environment variables) [DONE]
	- Created basic upload form for CDB model [DONE]
	- Review loading models from database (issue with FileField path) and adding to annotation
	- Review adding multiple forms in one page (e.g. Vocab and CDB) OR (preference) create an update models view
	- Review adding model selection list on annotation page 
	- Tidy views
	- Discuss how setup on Docker and virtual machine

- Notes
	- Issue with docker-compose launch version, db not synced so get "no such table" error when try and post new annotation
		- tried editing docker file to add python manage.py migrate --run-syncdb
		- fixed when run locally (only need python manage.py migrate) and when move model loading logic to apps.py (wasn't running the try: except: code in views)
	- Issue with FileField.path, Suspicious File Operation - The joined path (/models/vocab.dat) is located outside of the base path component (/Users/alexanderhandy/Documents/code/MedCAT-AH-fork/webapp/webapp)