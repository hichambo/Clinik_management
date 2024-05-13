from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('provider', 'Healthcare Provider')
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    mobile = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
