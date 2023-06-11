run:
	FLASK_APP=flaskr/app.py \
	flask run --debug

database:
	python3 flaskr/initDB.py

clean_database:
	rm flaskr/instance/myDB.db