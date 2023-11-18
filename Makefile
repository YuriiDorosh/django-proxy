setup:
	python3 -m venv env && \
	. env/bin/activate && \
	pip3 install -r req.txt

run:
	. env/bin/activate && \
	python3 manage.py runserver

