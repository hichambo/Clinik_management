from django.db import models

# Create your models here.
from django.db import models
from User.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    diabetes_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username + "'s Profile"
