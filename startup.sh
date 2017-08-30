cd supersurvey
python manage.py makemigrations
python manage.py migrate
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python2 manage.py shell 1>/dev/null 2>&1
# /usr/bin/supervisord
python manage.py runserver 0.0.0.0:8000