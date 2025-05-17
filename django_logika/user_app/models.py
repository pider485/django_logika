from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    ROLES = (
        ('admin',"Адміністратор"),
        ('user',"Користувач"),
    )


    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLES, default='user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)