import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logika_django.settings")

django.setup()

from user_app.models import User, Group

# new_group = Group(name='Вчителі')
# new_group.save()

user = User.objects.create(username='sanur',
                           email='arterf@gmail.com',
                           role='user',)