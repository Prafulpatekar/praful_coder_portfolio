# .PHONY is used to tell make the these are commands not files to bypass the checking file logic and imporve the performance speed
.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit install;

.PHONY: migrations
migrations:
	poetry run python -m myportfolio.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m myportfolio.manage migrate

.PHONY: run-server
run-server:
	poetry run python -m myportfolio.manage runserver 0.0.0.0:8080

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

.PHONY: docker-down
docker-down:
	docker-compose -f docker-compose.dev.yml down

# PROD
.PHONY: docker-prod-up
docker-prod-up:
	docker-compose -f docker-compose.yml up --force-recreate prod-db app -d

.PHONY: docker-prod-down
docker-prod-down:
	docker-compose -f docker-compose.yml down

.PHONY: shell
shell:
	poetry run python -m myportfolio.manage shell

.PHONY: test
test:
	poetry run pytest -v
