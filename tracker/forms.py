from django import forms
from .models import HealMetrics,HealthGoal

class HealtMetricsForm(forms.ModelForm):
    class Meta:
        model = HealMetrics
        fields = ['user','date','weight','height','exercise_min','calories_consumed','water_intake']

class HealthGoalForm(forms.ModelForm):
        class Meta:
            model = HealthGoal
            fields = ['goal_type','target_value','current_value','start_date','end_time']