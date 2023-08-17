from datetime import timedelta

def calculate_oee(availability, performance):
    return availability * performance * 100

def calculate_availability(available_time, unplanned_downtime):
    return (available_time - unplanned_downtime) / available_time

def calculate_performance(ideal_cycle_time, actual_output, available_operating_time):
    return (ideal_cycle_time * actual_output) / available_operating_time
