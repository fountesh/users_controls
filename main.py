import sys
import os
import django



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from myapp.models import User

user1 = User(
    name= "Ivan",
    email="hungry_dog@gmail.com",
    roles = "user"
)

user1.save()