from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100)
    available_time = models.FloatField()  # Available time in minutes
    unplanned_downtime = models.FloatField()  # Unplanned downtime in minutes
    ideal_cycle_time = models.FloatField()  # Ideal cycle time in seconds
    available_operating_time = models.FloatField()  # Available operating time in minutes
    # Add other machine-related fields

class ProductionLog(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    cycle_id = models.IntegerField()
    log_date = models.DateTimeField()
    units_produced = models.IntegerField()
    # Add other production log related fields
