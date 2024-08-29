from django.db import models
from django.contrib.auth.models import User


class HealMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models. FloatField(help_text="Weight in kg",null = True, blank = True)
    height = models.FloatField(help_text="Height in cm",null = True, blank = True)
    exercise_min  = models.PositiveIntegerField(default=0)
    calories_consumed  = models.PositiveIntegerField(default=0)
    water_intake  =models.FloatField(default=0.0,help_text="wate intake in litres")
    
    def __str__(self):
            return f"{self.user.username} - {self.date}"
    

class HealthGoal(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      goal_type = models.CharField(max_length=50,choices=[('weight', 'Weight'), ('calories', 'Calories'), ('exercise', 'Exercise')])
      target_value = models.FloatField()
      current_value = models.FloatField(default = 0)
      start_date = models.DateField()
      end_time  = models.DateField()

      def __str__(self):
            return f"{self.user.username} - {self.goal_type} goal"