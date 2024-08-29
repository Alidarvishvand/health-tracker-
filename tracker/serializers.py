from rest_framework import serializers
from .models import HealMetrics

class HealthMetricSrializer(serializers.ModelSerializer):
    class Meta:
        model = HealMetrics
        fields  = '__all__'