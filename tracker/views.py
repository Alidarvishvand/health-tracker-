from django.shortcuts import render
from rest_framework import generics
from .models import HealMetrics
from .serializers import HealthMetricSrializer
from rest_framework.permissions import IsAuthenticated
class HealthMetricsListCreate(generics.ListCreateAPIView):
    queryset = HealMetrics.objects.all()
    serializer_class = HealthMetricSrializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealMetrics.objects.filter(user=self.request.user)
    
    def perform_creat(self,serializer):
        serializer.save(user = self.request.user)

class HealthMetriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealMetrics.objects.all()
    serializer_class = HealthMetricSrializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HealMetrics.objects.filter(user = self.request.user)