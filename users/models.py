from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    img = models.ImageField(upload_to='users/')


    def __str__(self):
        return self.username