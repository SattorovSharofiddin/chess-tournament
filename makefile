mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
install:
	pip install -r requirements.txt

admin:
	python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='admin@example.com', full_name='Admin adminov', is_teacher=True, is_active=True, password='1')"

req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
