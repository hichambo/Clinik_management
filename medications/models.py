from django.db import models

# Create your models here.
from django.db import models
from User.models import User

class Medication(models.Model):
    patient = models.ForeignKey(User, related_name='medications', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.name
