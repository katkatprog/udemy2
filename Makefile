project_name=proj #プロジェクト名(デフォルトでproj)
app_name=app #プロジェクト名(デフォルトでapp)

project:
	docker-compose run --rm backend django-admin startproject $(project_name) .

app:
	docker-compose run --rm backend python manage.py startapp $(app_name)