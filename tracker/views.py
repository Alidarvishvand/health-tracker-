from django.shortcuts import render,redirect
from .forms import HealtMetricsForm,HealthGoalForm
from rest_framework import generics
from .models import HealMetrics,HealthGoal
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum
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

@login_required
def create_health_metrics(request):
    if request.method == 'POST':
        form = HealtMetricsForm(request.POST)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.user = request.user
            metric.save()
            return redirect('health-metrics-list')
        
    else:
        form = HealtMetricsForm()
    return render(request, '../templates/health_metrics_form.html', {'form': form})

@login_required
def create_health_goal(request):
    if request.method == 'POST':
        form = HealthGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit= False) 
            goal.user = request.user
            goal.save()
            return redirect('health-goal-list')
    else :
        form = HealthGoalForm()
    return render(request, '../templates/health_goal_form.html',{'form': form})

@login_required
def health_metric_list(request):
    metrics = HealMetrics.objects.filter(user=request.user)
    return render(request, '../templates/health_metric_list.html',{'metrics': metrics})


@login_required
def health_goal_list(request):
    goals = HealthGoal.objects.filter(user=request.user)
    return render(request, '../templates/health_goal_list.html',{'goals': goals})
    

@login_required
def health_progress_report(request):
    metrics = HealMetrics.objects.filter(user=request.user)
    weight_progress = metrics.aggregate(Avg('weight'))['weight__avg']
    total_exercise = metrics.aggregate(Sum('exercise_min'))['exercise_min__sum']
    total_calories_consumed = metrics.aggregate(Sum('calories_consumed'))['calories_consumed__sum']
    # total_calorise_burned = metrics.aggregate(Sum('calorise_burned'))['calorise_burned__sum']

    goals = HealthGoal.objects.filter(user=request.user)

    context = {
        'weight_progress' :  weight_progress,
        'total_exercise'  : total_exercise,
        'total_calories_consumed' : total_calories_consumed,
        # 'total_calorise_burned' : total_calorise_burned,
        'goals' : goals,

    }

    return render(request,'../templates/health_progress_report.html',context)










