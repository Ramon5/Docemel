clean:
	find . -name "*.pyc" -exec rm -rf {} \;
runssl:
	python manage.py runserver 127.0.0.1:8000
run:
	python manage.py runserver 127.0.0.1:8002
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
user:
	python manage.py createsuperuser

shell:
	python manage.py shell
statics:
	python manage.py collectstatic
test:
	python manage.py test
