from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    national_id = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.username



