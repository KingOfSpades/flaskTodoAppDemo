activate_venv:
	source .venv/bin/activate

run_app:
	FLASK_APP=flaskr/app.py \
	flask run --debug

seed_database:
	python3 flaskr/initDB.py
