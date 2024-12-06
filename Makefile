# .PHONY is used to tell make the these are commands not files to bypass the checking file logic and imporve the performance speed
.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	poetry run python src/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python src/manage.py migrate

.PHONY: run-server
run-server:
	poetry run python src/manage.py runserver

.PHONY: superuser
superuser:
	poetry run python src/manage.py createsuperuser

.PHONY: update
update: install migrate ;
