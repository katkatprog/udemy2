app_name=app #プロジェクト名(デフォルトでapp)

app:
	docker-compose run --rm backend python manage.py startapp $(app_name)