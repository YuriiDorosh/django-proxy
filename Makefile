setup:
	python3 -m venv env
	source env/bin/activate
	pip3 install -r req.txt

run:
	python3 manage.py makemigrations
	python3 manage.py runserver

