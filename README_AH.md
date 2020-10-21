# Summary  

- Goal - Review extending demo web app to allow uploading of test cdb and vocab models on a virtual machine

- Steps
	- Run instance locally
	- Review options to store models (e.g. save in database, update environment variables)
	- Implement test
	- Add upload flow to views
	- Tidy views
	- Discuss how setup on virtual machine

- Notes
	- Issue with docker-compose launch version, db not synced so get "no such table" error when try and post new annotation
		- tried editing docker file to add python manage.py migrate --run-syncdb
		- fixed when run locally (only need python manage.py migrate) and when move model loading logic to apps.py