from django.urls import path
from .views import HealthMetricsListCreate,HealthMetriDetail

urlpatterns = [
    path('metrics/', HealthMetricsListCreate.as_view(), name='healthmetric-list-create'),
    path('metrics/<int:pk/', HealthMetriDetail.as_view(), name='healthmetric-detail'),
]