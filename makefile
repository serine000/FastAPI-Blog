install:
	pip install -r backend/requirements.txt

activateEnv:
	source venv/bin/activate

freeze:
	pip freeze > backend/requirements.txt

