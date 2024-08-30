from django.urls import path
from .views import HealthMetricsListCreate,create_health_metrics, create_health_goal, health_metric_list, health_goal_list, health_progress_report

urlpatterns = [
    path('metrics/', HealthMetricsListCreate.as_view(), name='healthmetric-list-create'),
    # path('metrics/<int:pk/', HealthMetriDetail.as_view(), name='healthmetric-detail'),
    path('create-health-metric/',create_health_metrics, name='create-health-metric'),
    path('create-health-goal/',create_health_goal, name='create-health-goal'),
    path('health-metrics/',health_goal_list, name='health-metrics-list'),
    path('health-goals/',health_goal_list, name='health-goals'),
    path('health-progress-report/',health_progress_report, name='health-progress-report'),
]