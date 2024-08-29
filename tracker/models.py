from django.db import models
from django.contrib.auth.models import User


class HealMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    
    steps = models.PositiveIntegerField(default=0)
    calorise = models.PositiveIntegerField(default=0)
    water_intake  =models.FloatField(default=0)
    
    def __str__(self):
            return f"{self.user.username} - {self.date}"
    


