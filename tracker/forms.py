from django import forms
from .models import *

class HealtMetricsForm(forms.ModelForm):
    class Meta:
        model = HealMetrics
        fields = ['date','weight','hight','exercise_min','calories_consumed','water_intake']

    class HealthGoalForm(forms.ModelForm):
        class Meta:
            model = HealthGoal
            fields = ['goal_type','target_value','current_value','start_date','end_time']