from django.db import models


class Vehicle(models.Model):
    VEHICLE_STATUS = [
        ("available", "Available"),
        ("on-hire", "On hire"),
        ("off-fleet", "Off Fleet"),
        ("in-repair", "In Repair"),
        ("in-for-service", "In for Service"),
    ]

    VEHICLE_CATEGORY = [
        ("saloon", "Saloon"),
        ("purpose-built", "Purpose Built"),
        ("mpv", "MPV"),
        ("minibus", "Minibus"),
        ("executive-e-class", "Executive E Class"),
        ("executive-s-class", "Executive S Class"),
        ("dual-control", "Dual Control"),
    ]

    VEHICLE_DEPOT = [
        ("all-depots", "All depots"),
        ("depot-1", "Depot 1"),
        ("depot-2", "Depot 2")
    ]

    FUEL_TYPE = [
        ("diesel", "Diesel"),
        ("lpg", "LPG"),
        ("petrol", "Petrol"),
    ]

    cross_hire = models.BooleanField()
    vehicle_status = models.CharField(max_length=50, choices=VEHICLE_STATUS)
    currently_reserved = models.BooleanField(verbose_name="Is vehicle currently reserved?")
    opened_by = models.CharField(max_length=255)
    last_recorded_mileage = models.FloatField()
    as_at = models.DateTimeField(verbose_name="as at")

    category = models.CharField(max_length=50, blank=True, null=True, choices=VEHICLE_CATEGORY, verbose_name="Vehicle category")
    depot = models.CharField(max_length=25, choices=VEHICLE_DEPOT, verbose_name="Depot/Branch", help_text="eg. DE51 BBY")
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255, verbose_name="Colour")
    cc = models.CharField(max_length=255, verbose_name="CC")
    radio_code = models.CharField(max_length=255)
    callibration_no = models.CharField(max_length=255)
    number_of_doors = models.IntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE)
    first_registration = models.DateTimeField()
    tax_date = models.DateTimeField()
    insurance_group = models.CharField(max_length=255)
