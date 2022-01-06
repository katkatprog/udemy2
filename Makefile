default_project=proj
default_app=app

project:
	docker-compose run --rm backend django-admin startproject $(default_project) .

app:
	docker-compose run --rm backend python manage.py startapp $(default_app)