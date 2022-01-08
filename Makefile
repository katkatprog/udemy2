include .env
app_name=app #プロジェクト名(デフォルトでapp)

django-app:
	docker-compose run --rm backend sh -c "cd $(BACK_PROJECT_NAME) && python manage.py startapp $(app_name)"

django-project:
	docker-compose run --rm backend sh -c "django-admin startproject $(BACK_PROJECT_NAME)"

# front_node_modulesボリュームにnodeのモジュールをインストールする。
next-install:
	docker-compose run --rm frontend sh -c "cd $(FRONT_PROJECT_NAME) && npm install"

rm-volumes:
	docker volume rm next_django_db_store
	docker volume rm next_django_front_node_modules