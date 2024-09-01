from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    roles = models.CharField(max_length=100, choices=[
        ("admin", "admin"), 
        ("user", "user")
    ])

    def __str__(self):
        return self.name
