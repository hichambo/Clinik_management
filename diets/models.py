from django.db import models

# Create your models here.
from django.db import models
from User.models import User

class DietPlan(models.Model):
    patient = models.ForeignKey(User, related_name='diet_plans', on_delete=models.CASCADE)
    description = models.TextField()
    recommendations = models.TextField()

    def __str__(self):
        return f"Diet Plan for {self.patient.username}"
