from django.db import models

# Create your models here.
from django.db import models
from User.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.CASCADE)
    provider = models.ForeignKey(User, related_name='provider_appointments', on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"Appointment with {self.provider.username} on {self.date_time}"
