from rest_framework import generics
from rest_framework.response import Response
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer, OEESerializer
from .utils import calculate_oee, calculate_availability, calculate_performance
from rest_framework import status


class MachineList(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ProductionLogList(generics.ListCreateAPIView):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer

class OEECalculation(generics.ListAPIView):
    serializer_class = OEESerializer

    def get_queryset(self):
        camera_name = self.request.query_params.get('camera_name', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        oee_threshold = float(self.request.query_params.get('oee_threshold', 0.0))

        queryset = ProductionLog.objects.all()

        if camera_name:
            queryset = queryset.filter(machine__name=camera_name)

        if start_date and end_date:
            queryset = queryset.filter(log_date__range=[start_date, end_date])

        oee_data = []
        for log in queryset:
            availability = calculate_availability(log.machine.available_time, log.machine.unplanned_downtime)
            performance = calculate_performance(log.machine.ideal_cycle_time, log.units_produced, log.machine.available_operating_time)
            oee = calculate_oee(availability, performance)  # Define 'oee' here
            
            if oee >= oee_threshold:
                oee_data.append({
                    'machine_name': log.machine.name,
                    'log_date': log.log_date,
                    'availability': availability,
                    'performance': performance,
                    'oee': oee,
                })

        return oee_data


    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)