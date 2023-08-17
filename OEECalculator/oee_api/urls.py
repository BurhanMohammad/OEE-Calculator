from django.urls import path
from .views import MachineList, ProductionLogList, OEECalculation

urlpatterns = [
    path('machines/', MachineList.as_view(), name='machine-list'),
    path('production-logs/', ProductionLogList.as_view(), name='production-log-list'),
    path('oee-calculation/', OEECalculation.as_view(), name='oee-calculation'),
]
