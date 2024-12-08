# .PHONY is used to tell make the these are commands not files to bypass the checking file logic and imporve the performance speed
.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit clean;
	poetry run pre-commit autoupdate;
	poetry run pre-commit uninstall;
	poetry run pre-commit install;

.PHONY: migrations
migrations:
	poetry run python -m myportfolio.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m myportfolio.manage migrate

.PHONY: run-server
run-server:
	poetry run python -m myportfolio.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m myportfolio.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: docker-up
docker-up:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db -d
