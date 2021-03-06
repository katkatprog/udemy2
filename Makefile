include .env
app_name=app #アプリケーション名(デフォルトでapp)

django-app:
	docker-compose run --rm backend sh -c "cd $(BACK_PROJECT_NAME) && python manage.py startapp $(app_name)"

django-shell:
	docker-compose exec backend sh -c "cd $(BACK_PROJECT_NAME) && python manage.py shell_plus"

# front_node_modulesボリュームにnodeのモジュールをインストールする。
next-install:
	docker-compose run --rm frontend sh -c "cd $(FRONT_PROJECT_NAME) && npm install"

build:
	docker-compose build --no-cache
	@make next-install

db-login:
	docker-compose exec db sh -c 'mysql -u ${MYSQL_USER} -p${MYSQL_PASSWORD}'

rm-volumes:
	docker volume rm next_django_db_store
	docker volume rm next_django_front_node_modules

#イメージ全削除する場合。
rm-all-images:
	docker ps -aq | xargs docker rm
	docker images -aq | xargs docker rmi
