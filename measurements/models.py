from django.db import models

# Create your models here.
from django.db import models
from User.models import User

class Measurement(models.Model):
    MEASUREMENT_TYPE_CHOICES = (
        ('blood_sugar', 'Blood Sugar'),
        ('weight', 'Weight'),
        ('other', 'Other')
    )
    CONDITION_TYPE_CHOICES = (
        ('fasting', 'Fasting'),
        ('postprandial', 'Postprandial'),
        ('random', 'Random')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    measurement_type = models.CharField(max_length=20, choices=MEASUREMENT_TYPE_CHOICES)
    condition_type = models.CharField(max_length=20, choices=CONDITION_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s Measurement on {self.date_time}"
